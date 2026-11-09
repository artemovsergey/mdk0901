#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Универсальный генератор презентаций по лекциям МДК 09.01.

Поддерживает разные форматы лекций:
- `### **1. ...**` (разделы 1-4);
- `#### **1. ...**` (раздел 6);
- `## План` + `### 1. ...` (разделы 8-9);
- `**Цель:**`, `### **Цель лекции:**`, `## Цель`.

Примеры:
    python tools/generate_all_pptx.py --dry-run
    python tools/generate_all_pptx.py --lecture 1
    python tools/generate_all_pptx.py --section "Раздел 6. .NET"
    python tools/generate_all_pptx.py --all
"""

import argparse
import re
import sys
from pathlib import Path

from generate_lecture_pptx import build_lecture_pptx

ROOT = Path(__file__).resolve().parents[1]
COURSE = ROOT / "course"

HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
BULLET = re.compile(r"^(\s*)[*+-]\s+(.*)$")
NUMBERED = re.compile(r"^(\s*)\d+[.)]\s+(.*)$")
IMAGE = re.compile(r"^!\[([^\]]*)\]\([^)]+\)\s*$")
TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")
SPECIAL = re.compile(r"(план|резюме|контрольные вопросы|вопросы для самопроверки|материалы|тема|цель|аудитория)", re.I)


def clean(text: str) -> str:
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"\1", text)
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = text.replace("**", "")
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("&nbsp;", " ")
    return re.sub(r"\s+", " ", text).strip(" \t-—–")


def mask_code(lines):
    """True для строк внутри fenced code block."""
    mask = [False] * len(lines)
    fence = None
    for i, line in enumerate(lines):
        m = FENCE.match(line)
        if fence is None:
            if m:
                fence = m.group(1)
                mask[i] = True
            continue
        mask[i] = True
        if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
            fence = None
    return mask


def headings(lines, mask):
    out = []
    for i, line in enumerate(lines):
        if mask[i]:
            continue
        m = HEADING.match(line)
        if m:
            out.append((i, len(m.group(1)), m.group(2).strip()))
    return out


def next_heading(heads, idx, max_level=None):
    for pos, (line_i, level, _text) in enumerate(heads):
        if line_i <= idx:
            continue
        if max_level is None or level <= max_level:
            return pos
    return len(heads)


def heading_text(text: str) -> str:
    text = re.sub(r"^\**\s*\d+[.)]\s*", "", text)
    return text.strip("* ").strip()


def find_heading(heads, pattern):
    for pos, (line_i, level, text) in enumerate(heads):
        if re.search(pattern, heading_text(text), re.I):
            return pos
    return None


def collect_text_after(lines, start, end, max_items=20):
    items = []
    i = start
    while i < end:
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            i += 1
            continue
        m = BULLET.match(line) or NUMBERED.match(line)
        if m:
            items.append(clean(m.group(2)))
        elif stripped.startswith("|") and stripped.endswith("|"):
            pass
        elif stripped.startswith("#"):
            pass
        elif IMAGE.match(stripped):
            pass
        else:
            items.append(clean(stripped.lstrip(">")))
        i += 1
    return [x for x in items if x][:max_items]


def extract_field(lines, mask, names):
    """Ищет поле вида **Цель:**, ## Цель или ### **Цель лекции:**."""
    patterns = [
        re.compile(rf"^\s*#{{2,4}}\s*\*\*{names}(?:\s+\w+)?:?\*\*\s*(.*)$", re.I),
        re.compile(rf"^\s*#{{2,4}}\s*{names}(?:\s+\w+)?:?\s*(.*)$", re.I),
        re.compile(rf"^\s*\*\*{names}(?:\s+\w+)?:?\*\*\s*(.*)$", re.I),
        re.compile(rf"^\s*{names}(?:\s+\w+)?:\s*(.*)$", re.I),
    ]
    for i, line in enumerate(lines):
        if mask[i]:
            continue
        for pat in patterns:
            m = pat.match(line)
            if not m:
                continue
            value = clean(m.group(1))
            if value:
                return value
            # значение на следующих строках до заголовка/пустой строки
            j = i + 1
            buf = []
            while j < len(lines):
                s = lines[j].strip()
                if not s:
                    if buf:
                        break
                    j += 1
                    continue
                if s.startswith("#") or s.startswith("---"):
                    break
                buf.append(clean(s))
                j += 1
                if len(" ".join(buf)) > 600:
                    break
            if buf:
                return " ".join(buf)
    return ""


def parse_blocks(lines, start, end, mask):
    blocks = []
    i = start
    while i < end:
        line = lines[i]
        if mask[i]:
            # fenced code
            fence = FENCE.match(line).group(1)
            j = i + 1
            code = []
            while j < end:
                if FENCE.match(lines[j]) and FENCE.match(lines[j]).group(1)[0] == fence[0] and len(FENCE.match(lines[j]).group(1)) >= len(fence):
                    j += 1
                    break
                code.append(lines[j])
                j += 1
            if code:
                blocks.append(("code", code))
            i = j
            continue

        stripped = line.strip()
        if not stripped:
            i += 1
            continue

        if TABLE_ROW.match(line):
            rows = []
            while i < end and TABLE_ROW.match(lines[i]):
                rows.append(lines[i].strip())
                i += 1
            blocks.append(("table", rows))
            continue

        bm = BULLET.match(line)
        nm = NUMBERED.match(line) if not bm else None
        if bm or nm:
            items = []
            while i < end:
                raw = lines[i]
                if not raw.strip():
                    break
                b2 = BULLET.match(raw)
                n2 = NUMBERED.match(raw) if not b2 else None
                m2 = b2 or n2
                if not m2:
                    break
                indent = len(m2.group(1))
                prefix = "  " if indent >= 2 else ""
                items.append(prefix + clean(m2.group(2)))
                i += 1
            if items:
                blocks.append(("bullets", items))
            continue

        hm = HEADING.match(line)
        if hm:
            blocks.append(("subhead", [clean(hm.group(2))]))
            i += 1
            continue

        bold_only = re.match(r"^\*\*([^*]+)\*\*:?\s*$", stripped)
        if bold_only:
            blocks.append(("subhead", [clean(bold_only.group(1))]))
            i += 1
            continue

        im = IMAGE.match(stripped)
        if im:
            i += 1
            continue

        # paragraph until blank / block start
        paras = []
        while i < end:
            raw = lines[i]
            s = raw.strip()
            if not s:
                break
            if TABLE_ROW.match(raw) or BULLET.match(raw) or NUMBERED.match(raw) or HEADING.match(raw) or IMAGE.match(s) or mask[i]:
                break
            if re.match(r"^\*\*([^*]+)\*\*:?\s*$", s):
                break
            paras.append(clean(s.lstrip(">")))
            i += 1
        text = " ".join(x for x in paras if x)
        if text:
            blocks.append(("para", [text]))
    return blocks


def split_summary(text_lines):
    items = []
    for line in text_lines:
        s = line.strip()
        if not s:
            continue
        m = BULLET.match(s) or NUMBERED.match(s)
        if m:
            items.append(clean(m.group(2)))
        elif not s.startswith("#") and not s.startswith("---") and not s.startswith("|"):
            # длинный абзац делим по предложениям
            for part in re.split(r"(?<=[.!?])\s+", clean(s.lstrip(">"))):
                if len(part) > 2:
                    items.append(part)
    return [x for x in items if x]


def parse_lecture(md_path: Path):
    text = md_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    mask = mask_code(lines)
    heads = headings(lines, mask)

    title = ""
    for i, level, h in heads:
        if level == 1:
            title = h
            break
    if not title:
        title = md_path.stem

    m = re.match(r"Лекция\s+(\d+)\.\s*(.*)", title)
    num = int(m.group(1)) if m else None
    if m:
        title = m.group(2).strip()
    if num is None:
        m2 = re.match(r"Лекция\s+(\d+)\.", md_path.stem)
        num = int(m2.group(1)) if m2 else 0

    section_label = md_path.parent.name

    goal = extract_field(lines, mask, "Цель")
    if not goal:
        goal = extract_field(lines, mask, "Тема")
    if not goal:
        goal = f"Изучить тему «{title}» и закрепить её практическими примерами."

    audience = extract_field(lines, mask, "Аудитория") or f"Студенты, изучающие {section_label}."

    # ---------- план ----------
    plan = []
    plan_pos = find_heading(heads, r"^План\b")
    if plan_pos is not None:
        plan_i, plan_level, _ = heads[plan_pos]
        plan_end = heads[plan_pos + 1][0] if plan_pos + 1 < len(heads) else len(lines)
        i = plan_i + 1
        while i < plan_end:
            s = lines[i].strip()
            pm = re.match(r"^\d+[.)]\s+(.*)$", s)
            if pm:
                t = clean(pm.group(1))
                t = re.sub(r"\s*\(\d+\s*мин.*?\)\s*$", "", t, flags=re.I)
                plan.append((len(plan) + 1, t, []))
            elif plan and (BULLET.match(lines[i]) or re.match(r"^\s{2,}\d+[.)]\s+", lines[i])):
                b = BULLET.match(lines[i])
                sub = clean(b.group(2)) if b else clean(re.sub(r"^\s*\d+[.)]\s+", "", lines[i]))
                plan[-1][2].append(sub)
            i += 1

    # ---------- область содержания ----------
    detail_pos = find_heading(heads, r"(Детальное|Подробное)\s+рассмотрение")
    special_positions = [
        p for p in (
            find_heading(heads, r"^Резюме"),
            find_heading(heads, r"^Контрольные вопросы"),
            find_heading(heads, r"^Вопросы для самопроверки"),
            find_heading(heads, r"^Материалы"),
        ) if p is not None
    ]
    if detail_pos is not None:
        content_start = heads[detail_pos][0] + 1
        detail_level = heads[detail_pos][1]
        content_end = len(lines)
        for pos in range(detail_pos + 1, len(heads)):
            if heads[pos][1] <= detail_level:
                content_end = heads[pos][0]
                break
    else:
        content_start = (heads[plan_pos][0] + 1) if plan_pos is not None else 0
        content_end = len(lines)

    if special_positions:
        all_content_heads = [
            (line_i, level, h) for (line_i, level, h) in heads
            if content_start <= line_i < content_end and level >= 2
        ]
        numbered_lines = [
            line_i for (line_i, level, h) in all_content_heads
            if re.match(r"^\**\s*\d+[.)]\s+", h)
        ]
        cut_from = min(numbered_lines) if numbered_lines else content_start
        specials_after = [heads[p][0] for p in special_positions if heads[p][0] >= cut_from]
        if specials_after:
            content_end = min(content_end, min(specials_after))

    content_heads = [
        (pos, line_i, level, h) for pos, (line_i, level, h) in enumerate(heads)
        if content_start <= line_i < content_end and level >= 2
    ]

    # исключаем служебные заголовки
    content_heads = [x for x in content_heads if not SPECIAL.search(x[3])]

    numbered = [(pos, li, lvl, h) for pos, li, lvl, h in content_heads
                if re.match(r"^\**\s*\d+[.)]\s+", h)]
    if numbered:
        section_level = min(x[2] for x in numbered)
        selected = [x for x in numbered if x[2] == section_level]
    else:
        if content_heads:
            from collections import Counter
            section_level = Counter(x[2] for x in content_heads).most_common(1)[0][0]
            selected = [x for x in content_heads if x[2] == section_level]
        else:
            selected = []

    sections = []
    for idx, (pos, line_i, level, h) in enumerate(selected):
        end = selected[idx + 1][1] if idx + 1 < len(selected) else content_end
        sec_title = clean(re.sub(r"^\**\s*\d+[.)]\s+", "", h))
        blocks = parse_blocks(lines, line_i + 1, end, mask)
        if sec_title and blocks:
            sections.append({"title": sec_title, "blocks": blocks})

    if not sections:
        # fallback: весь текст после плана как один раздел
        blocks = parse_blocks(lines, content_start, content_end, mask)
        if blocks:
            sections.append({"title": title, "blocks": blocks})

    if not plan:
        plan = [(i + 1, s["title"], []) for i, s in enumerate(sections)]

    # ---------- резюме ----------
    summary = []
    s_pos = find_heading(heads, r"^Резюме")
    if s_pos is not None:
        s_i, s_level, _ = heads[s_pos]
        s_end = len(lines)
        for pos in range(s_pos + 1, len(heads)):
            if heads[pos][1] <= s_level:
                s_end = heads[pos][0]
                break
        summary = split_summary(lines[s_i + 1:s_end])

    # ---------- вопросы ----------
    questions = []
    q_pos = find_heading(heads, r"^(Контрольные вопросы|Вопросы для самопроверки)")
    if q_pos is not None:
        q_i, q_level, _ = heads[q_pos]
        q_end = len(lines)
        for pos in range(q_pos + 1, len(heads)):
            if heads[pos][1] <= q_level:
                q_end = heads[pos][0]
                break
        top_level = []
        nested = []
        plain = []
        for line in lines[q_i + 1:q_end]:
            s = line.strip()
            if not s or s.startswith("#") or s.startswith("---") or s.startswith("|"):
                continue
            m = NUMBERED.match(s) or BULLET.match(s)
            if m:
                (nested if line[:1].isspace() else top_level).append(clean(m.group(2)))
            else:
                plain.append(clean(s))
        questions = top_level or nested or plain
        questions = [q for q in questions if q]

    # ---------- материалы ----------
    materials = []
    m_pos = find_heading(heads, r"^Материалы")
    if m_pos is not None:
        m_i, m_level, _ = heads[m_pos]
        m_end = len(lines)
        for pos in range(m_pos + 1, len(heads)):
            if heads[pos][1] <= m_level:
                m_end = heads[pos][0]
                break
        for line in lines[m_i + 1:m_end]:
            s = line.strip()
            m = BULLET.match(s) or NUMBERED.match(s)
            if m:
                materials.append(clean(m.group(2)))
            elif s and not s.startswith("#") and not s.startswith("---") and not s.startswith("|"):
                materials.append(clean(s))
        materials = [x for x in materials if x]

    if not summary:
        summary = [f"Основные понятия темы «{title}» — в блоках «ЧТО ЗАКОНСПЕКТИРОВАТЬ»."]

    meta = f"{section_label} · 2 академических часа (90 мин)"
    if "React" in section_label:
        meta = "ИП 242 / ИП 245 / ИП 246 · Раздел 5. React · 2 академических часа (90 мин)"

    return {
        "number": num,
        "title": title,
        "section_label": section_label,
        "meta_line": meta,
        "goal": goal,
        "audience": audience,
        "plan": plan,
        "sections": sections,
        "summary": summary,
        "questions": questions,
        "materials": materials,
    }


def is_practical(text: str) -> bool:
    return bool(re.search(r"^\s*#\s*Практическая работа", text, re.M))


def main():
    ap = argparse.ArgumentParser(description="Генерация PPTX по лекциям МДК 09.01")
    ap.add_argument("--lecture", type=int, help="номер лекции")
    ap.add_argument("--section", help="подстрока названия раздела")
    ap.add_argument("--all", action="store_true", help="все лекции; существующие PPTX пропускаются без --force")
    ap.add_argument("--force", action="store_true", help="перезаписать существующие PPTX")
    ap.add_argument("--include-practical", action="store_true", help="обрабатывать файлы, помеченные как практическая работа")
    ap.add_argument("--dry-run", action="store_true", help="только показать план")
    args = ap.parse_args()

    files = sorted(COURSE.rglob("Лекция *.md"))
    if args.lecture is not None:
        files = [p for p in files if re.match(rf"Лекция\s+{args.lecture}\.", p.name)]
    if args.section:
        files = [p for p in files if args.section.lower() in str(p.parent).lower()]

    total = 0
    generated = 0
    skipped = 0
    for p in files:
        text = p.read_text(encoding="utf-8", errors="replace")
        if is_practical(text) and not args.include_practical:
            print(f"SKIP practical: {p.relative_to(ROOT)}")
            skipped += 1
            continue
        data = parse_lecture(p)
        num = data["number"]
        title = data["title"]
        out_dir = p.parent / f"Презентация {num}. {title}"
        out_path = out_dir / f"Лекция {num}. {title}.pptx"
        total += 1
        if out_path.exists() and not args.force:
            print(f"SKIP exists: {out_path.relative_to(ROOT)}")
            skipped += 1
            continue
        print(f"PLAN: {p.relative_to(ROOT)} -> {out_path.relative_to(ROOT)}")
        print(f"      sections={len(data['sections'])} plan={len(data['plan'])} "
              f"summary={len(data['summary'])} questions={len(data['questions'])}")
        if args.dry_run:
            continue
        out_dir.mkdir(parents=True, exist_ok=True)
        build_lecture_pptx(data, str(out_path))
        generated += 1

    print(f"\nВсего: {total}, сгенерировано: {generated}, пропущено: {skipped}")
    if args.dry_run:
        print("Режим dry-run: файлы не создавались.")


if __name__ == "__main__":
    main()
