# Лекция 11. Введение в Jetpack Compose.

В этом уроке вы используете ```Jetpack Compose``` для создания простого приложения для Android, которое выводит на экран сообщение о дне рождения.

### Предварительные условия

**Что вы узнаете**

- Как писать композитные функции, такие как композитные функции ```Text```, ```Column``` и ```Row```.
- Как отображать текст в приложении в виде макета.
- Как форматировать текст, например, изменять его размер.

**Что вы создадите**

Приложение для Android, отображающее поздравление с днем рождения в текстовом формате, которое в готовом виде выглядит как на этом скриншоте:

<center>
<img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/2ff181d48325023c_856.png" style="width:200px"/>
</center>


### Создание приложения "С днем рождения"

В этом уроке вы создадите проект в Android Studio с шаблоном ```Empty Compose Activity``` и измените текстовое сообщение на персонализированное поздравление с днем рождения.

- Создайте проект ```Empty Compose Activity```
- В диалоговом окне Welcome to Android Studio выберите New Project.
- В диалоговом окне Новый проект выберите Empty Compose Activity и нажмите кнопку Далее.
- В поле ```Name``` введите Happy Birthday, затем выберите минимальный уровень **API 35** в поле Minimum SDK и нажмите Finish.

- Дождитесь, пока Android Studio создаст файлы проекта и соберет его.
- Нажмите предварительный просмотр
- Приложение должно выглядеть как на этом скриншоте (при запуске на эмуляторе):

<center>
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/d8299bfc1a82cd57_856.png
    " style="width:400px;margin:50px;"/>
</center>

Когда вы создали это приложение Happy Birthday с помощью шаблона Empty Compose Activity, Android Studio настроила ресурсы для базового приложения Android, включая сообщение Hello Android! на экране. В этом уроке вы узнаете, как это сообщение появилось, как изменить его текст на поздравление с днем рождения, а также как добавить и отформатировать дополнительные сообщения.

**Что такое пользовательский интерфейс (UI)?**

Пользовательский интерфейс (UI) приложения - это то, что вы видите на экране: текст, изображения, кнопки и многие другие элементы, а также то, как они расположены на экране. Это то, как приложение показывает все пользователю и как пользователь взаимодействует с приложением.

На этом изображении есть кнопка, на которую можно нажать, текстовое сообщение и поле ввода, в которое пользователь может ввести данные.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/9a2df39af4122803_856.png)
Кнопка

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/50a9b402fd9037c0_856.png)
Текстовое сообщение внутри открытки

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/17794ea52cfb5473_856.png)
Поле ввода текста

Каждый из этих элементов называется **компонентом** пользовательского интерфейса. Почти все, что вы видите на экране вашего приложения, является элементом пользовательского интерфейса (также известным как компонент пользовательского интерфейса). Они могут быть интерактивными, например, кликабельными кнопками или редактируемыми полями ввода, а могут быть декоративными изображениями.

В следующих приложениях постарайтесь найти как можно больше компонентов пользовательского интерфейса.

<center>
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/dcb5e11ef39aa76d_856.png
    " style="width:400px;margin:50px;"/>
</center>

В этом уроке вы работаете с элементом пользовательского интерфейса, который отображает текст, называемым элементом ```Text```.

# Что такое Jetpack Compose?

**Jetpack Compose** - это современный набор инструментов для создания пользовательских интерфейсов для Android. Compose упрощает и ускоряет разработку пользовательских интерфейсов на Android благодаря меньшему количеству кода, мощным инструментам и интуитивно понятным возможностям Kotlin. С помощью Compose вы можете создавать пользовательский интерфейс, определяя набор функций, называемых композитными функциями, которые принимают данные и описывают элементы пользовательского интерфейса.

**Compose function** - это основной строительный блок пользовательского интерфейса в Compose. Составная функция:

- Описывает некоторую часть вашего пользовательского интерфейса.
- Ничего не возвращает.
- Принимает некоторые входные данные и генерирует то, что отображается на экране.

**Аннотации** - это средства прикрепления дополнительной информации к коду. Эта информация помогает таким инструментам, как компилятор Jetpack Compose, и другим разработчикам понять код приложения.

Аннотация применяется путем префиксации ее имени (аннотации) с символом @ в начале объявления, которое вы аннотируете. Аннотировать можно различные элементы кода, включая свойства, функции и классы.

На следующей диаграмме приведен пример аннотированной функции:

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/87fe1e19ff89ee9c_856.png)

В следующем фрагменте кода приведены примеры аннотированных свойств.

```kt
@Json
val imgSrcUrl: String

@Volatile
private var INSTANCE: AppDatabase? = null
```

**Аннотации с параметрами**

Аннотации могут принимать параметры. Параметры предоставляют дополнительную информацию инструментам, обрабатывающим их. Ниже приведены примеры аннотации ```@Preview``` с параметрами и без них.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/c7165115f8a9e40b_856.png)
Аннотация без параметров

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/e3845e0f058aede9_856.png)
Фон для предварительного просмотра аннотаций

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/28a8df85bf4e80e6_856.png)
Аннотация с заголовком предварительного просмотра

Вы можете передать аннотации несколько аргументов, как показано здесь

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/895f8d3a229c287a_856.png)
Снимок экрана Android Studio с кодом и предварительным просмотром

**Аннотация с заголовком превью и системным пользовательским интерфейсом (экран телефона)**

Jetpack Compose включает в себя широкий спектр встроенных аннотаций, вы уже познакомились с аннотациями ```@Composable``` и ```@Preview```.

**Пример композитной функции**

Функция Composable аннотирована аннотацией ```@Composable```. Все композитные функции должны иметь эту аннотацию. Эта аннотация сообщает компилятору Compose, что данная функция предназначена для преобразования данных в пользовательский интерфейс. Напомним, что **компилятор** - это специальная программа, которая берет написанный вами код, просматривает его построчно и переводит в понятный компьютеру язык (машинный язык).

Этот фрагмент кода - пример простой композитной функции, которой передаются данные (параметр функции name) и которая использует их для вывода текстового элемента на экран.

```kt
@Composable
fun Greeting(name: String) {
    Text(text = "Hello $name!")
}
```

Несколько замечаний о композитной функции:

- Jetpack Compose построен на основе композитных функций. Эти функции позволяют вам программно определять пользовательский интерфейс вашего приложения, описывая, как он должен выглядеть, а не сосредотачиваясь на процессе создания пользовательского интерфейса. Чтобы создать композитную функцию, просто добавьте аннотацию ```@Composable``` к имени функции.
- Композитные функции могут принимать аргументы, которые позволяют логике приложения описывать или изменять пользовательский интерфейс. В данном случае ваш элемент пользовательского интерфейса принимает строку String, чтобы поприветствовать пользователя по имени.

Обратите внимание на составные функции в коде
В Android Studio откройте файл ```MainActivity.kt```.
Прокрутите его до функции ```GreetingPreview()```. Эта составная функция помогает выполнить предварительный просмотр функции Greeting(). Как правило, функции всегда следует называть или переименовывать, чтобы описать их функциональность. Измените название этой функции на ```BirthdayCardPreview()```.

```kt
@Preview(showBackground = true)
@Composable
fun BirthdayCardPreview() {
    HappyBirthdayTheme {
        Greeting("Android")
    }
}
```

Композитные функции могут вызывать другие композитные функции. В этом фрагменте кода функция предварительного просмотра вызывает композитную функцию `Greeting()`.

Обратите внимание, что предыдущая функция также имеет другую аннотацию, аннотацию @Preview, с параметром перед аннотацией @Composable.

**Имена компонуемых функций**

Функция-композитор, которая ничего не возвращает и имеет аннотацию @Composable, ДОЛЖНА быть названа с использованием регистра Паскаля. Падеж Pascal означает соглашение об именовании, в котором первая буква каждого слова в составном слове пишется с заглавной буквы. Разница между регистром Паскаля и верблюжьим регистром заключается в том, что все слова в регистре Паскаля пишутся с заглавной буквы. В верблюжьем регистре первое слово может быть в любом регистре.

Функция Compose:

- ДОЛЖНА быть существительным: DoneButton()
- НЕ глагол или глагольная фраза: DrawTextField()
- НЕ существительное с предлогом: TextFieldWithLink()
- НЕ прилагательное: Bright()
- НЕ наречие: Outside()

К существительным МОЖНО добавлять описательные прилагательные: RoundIcon()

```kt
// Эта функция представляет собой описательное существительное в паскале в виде визуального элемента пользовательского интерфейса
@Composable
fun FancyButton(text: String) {}


// Эта функция представляет собой описательное существительное в паскале как невизуальный элемент.
// с присутствием в композиции
@Composable
fun BackButtonHandler() {}


// Не надо: эта функция является существительным, но не имеет PascalCased!
@Composable
fun fancyButton(text: String) {}


// Не надо: эта функция имеет PascalCased, но не является существительным!
@Composable
fun RenderFancyButton(text: String) {}


// Не надо: эта функция не является ни PascalCased, ни существительным!
@Composable
fun drawProfileImage(image: ImageAsset) {}
```

### Панель дизайна в Android Studio

Android Studio позволяет просматривать композитные функции в IDE, а не устанавливать приложение на Android-устройство или эмулятор. Как вы узнали в предыдущем разделе, вы можете просмотреть, как выглядит ваше приложение, в панели Design в Android Studio.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/2bb27291fa8c8ecc_856.png)

Композитная функция должна предоставлять значения по умолчанию для любых параметров для предварительного просмотра. По этой причине не рекомендуется выполнять предварительный просмотр функции Greeting() напрямую. Вместо этого необходимо добавить другую функцию, в данном случае BirthdayCardPreview(), которая вызывает функцию Greeting() с соответствующим параметром.

```kt
@Preview(showBackground = true)
@Composable
fun BirthdayCardPreview() {
    HappyBirthdayTheme {
        Greeting("Android")
    }
}
```

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/86a1dd28a40dea11_856.png)

Чтобы просмотреть предварительный просмотр:

В функции BirthdayCardPreview() измените аргумент «Android» в функции Greeting() на свое имя.

```kt
@Preview(showBackground = true)
@Composable
fun BirthdayCardPreview() {
    HappyBirthdayTheme {
        Greeting("James")
    }
}
```

Предварительный просмотр автоматически обновится.
Вы должны увидеть обновленный предварительный просмотр.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/907e7542c84daf9f_856.png)


<div style="border-left:0.5rem solid green; padding-left: 1rem ">
Важно: Код, который вы добавили в функцию BirthdayCardPreview() с аннотацией @Preview, предназначен только для предварительного просмотра в панели Design в Android Studio. Эти изменения не отражаются в приложении.
</div>

# Добавление нового текстового элемента

В этом задании вы удалите приветствие ```Hello $name!``` и добавите поздравление с днем рождения.

Добавьте новую составную функцию
В файле ```MainActivity.kt``` удалите определение функции Greeting(). Позже вы добавите собственную функцию для отображения приветствия в codelab.

Удалите следующий код:
```kt
@Composable
fun Greeting(name: String, modifier: Modifier = Modifier) {
    Text(
        text = "Hello $name!",
        modifier = modifier
    )
}
```

Внутри функции ```onCreate()``` обратите внимание, что вызов функции Greeting() теперь окрашен в красный цвет. Этот красный цвет указывает на ошибку. Наведите курсор на этот вызов функции, и Android Studio отобразит информацию об ошибке.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/9634619e59248532_856.png)

Удалите вызов функции Greeting() вместе с ее аргументами из функций onCreate() и BirthdayCardPreview(). Ваш файл MainActivity.kt будет выглядеть примерно так:

```kt
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            HappyBirthdayTheme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                }
            }
        }
    }
}

@Preview(showBackground = true)
@Composable
fun BirthdayCardPreview() {
    HappyBirthdayTheme {
    }
}
```

Перед функцией BirthdayCardPreview() добавьте новую функцию GreetingText(). Не забудьте добавить аннотацию @Composable перед функцией, потому что это будет композитная функция, описывающая композитный текст.

```kt
@Composable
    fun GreetingText() {
}
```

Лучше всего, если ваш Composable будет принимать параметр ```Modifier``` и передавать этот модификатор своему первому дочернему элементу. Подробнее о ```Modifier``` и дочерних элементах вы узнаете в последующих заданиях. А пока добавьте параметр ```Modifier``` в функцию GreetingText().

```kt
@Composable
fun GreetingText(modifier: Modifier = Modifier) {
}
```

Добавьте параметр сообщения типа String в составную функцию GreetingText().

```kt
@Composable
fun GreetingText(message: String, modifier: Modifier = Modifier) {
}
```

В функцию GreetingText() добавьте составной элемент Text, передающий текстовое сообщение в качестве именованного аргумента.

```kt
@Composable
fun GreetingText(message: String, modifier: Modifier = Modifier) {
    Text(
        text = message
    )
}
```

Эта функция GreetingText() отображает текст в пользовательском интерфейсе. Она делает это, вызывая композитную функцию Text().

### Предварительный просмотр функции

В этом задании вы сделаете предварительный просмотр функции GreetingText() в панели Design.

Вызовите функцию GreetingText() внутри функции BirthdayCardPreview().
Передайте функции GreetingText() аргумент String - поздравление с днем рождения для вашего друга. При желании вы можете добавить в него его имя, например «Happy Birthday Sam!».

```kt
@Preview(showBackground = true)
@Composable
fun BirthdayCardPreview() {
    HappyBirthdayTheme {
        GreetingText(message = "Happy Birthday Sam!")
    }
}
```

В панели Design обновляется автоматически. Просмотрите изменения.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/334688e2e89fb19e_856.png)

# Изменение размера шрифта

Вы добавили текст в пользовательский интерфейс, но он еще не выглядит как готовое приложение. В этом задании вы узнаете, как изменить размер, цвет текста и другие атрибуты, влияющие на внешний вид текстового элемента. Вы также сможете поэкспериментировать с различными размерами и цветами шрифта.

**Масштабируемые пиксели**
Масштабируемые пиксели (SP) - это единица измерения размера шрифта. Элементы пользовательского интерфейса в приложениях Android используют две разные единицы измерения: пиксели, не зависящие от плотности (DP), которые вы используете позже для макета, и масштабируемые пиксели (SP). По умолчанию единица SP имеет тот же размер, что и DP, но ее размер изменяется в зависимости от предпочитаемого пользователем размера текста в настройках телефона.

- В файле MainActivity.kt прокрутите страницу до композита Text() в функции GreetingText().
- Передайте функции Text() аргумент fontSize в качестве второго именованного аргумента и установите для него значение 100.sp.

```kt
Text(
    text = message,
    fontSize = 100.sp
)
```

Android Studio выделяет код ```.sp```, потому что для компиляции приложения необходимо импортировать некоторые классы или свойства.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/ba6c753d4eefd1d5_856.png)

- Щелкните ```.sp```, который выделяется Android Studio.
- Нажмите Import во всплывающем окне, чтобы импортировать ```androidx.compose.ui.unit.sp``` для использования свойства расширения ```.sp```.

<div style="border-left:0.5rem solid green;padding-left: 1rem;margin:1rem">
Примечание: Библиотека AndroidX (Android Extension) содержит набор библиотек и классов, которые помогают ускорить разработку приложений, предоставляя вам основную функциональность. Вы можете получить доступ к классам, свойствам и другим артефактам с помощью пакета androidx.
</div>


Прокрутите верхнюю часть файла и обратите внимание на операторы импорта, где вы должны увидеть оператор ```import androidx.compose.ui.unit.sp```, который означает, что Android Studio добавляет пакет в ваш файл.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/e073e9d3465e080c_856.png)

> Примечание: Если у вас возникнут проблемы с импортом с помощью Android Studio, вы можете вручную добавить импорт в верхней части файла.

Обратите внимание на обновленный предварительный просмотр размера шрифта. Причина перекрытия сообщений заключается в том, что вам нужно указать высоту строки.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/3bf48548c10f4ea_856.png)

> Примечание: ```sp``` - это свойство расширения для Int, которое создает единицу sp. Аналогично можно использовать свойство расширения .sp в других типах данных, таких как Float и Double.

Обновите составной элемент Text, чтобы включить в него высоту строки.

```kt
@Composable
fun GreetingText(message: String, modifier: Modifier = Modifier) {
    Text(
        text = message,
        fontSize = 100.sp,
        lineHeight = 116.sp,
    )
}
```

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/ef457e9b19d4d495_856.png)

Теперь вы можете поэкспериментировать с разными размерами шрифта.

# Добавьте еще один текстовый элемент

В предыдущих заданиях вы добавили поздравление с днем рождения своему другу. В этом задании вы подписываете открытку своим именем.

В файле MainActivity.kt прокрутите страницу до функции GreetingText().
Передайте функции параметр from типа String для вашей подписи.

```kt
fun GreetingText(message: String, from: String, modifier: Modifier = Modifier)
```

> Примечание: Порядок параметров функции не имеет значения, если вы используете именованные аргументы в вызове функции.

После текстового композита «Поздравление с днем рождения» добавьте еще один текстовый композит, который принимает текстовый аргумент, установленный в значение from.

```kt
@Composable
fun GreetingText(message: String, from: String, modifier: Modifier = Modifier) {
    Text(
        // ...
    )
    Text(
        text = from
    )
}
```

Добавьте именованный аргумент fontSize, установленный на значение 36.sp.

```kt
Text(
    text = from,
    fontSize = 36.sp
)
```

Перейдите к функции BirthdayCardPreview().
Добавьте еще один аргумент String для подписи вашей открытки, например «From Emma».

```kt
GreetingText(message = "Happy Birthday Sam!", from = "From Emma")
```

Обратите внимание на предварительный просмотр.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/8d148222c669dcad_856.png)

Композитная функция может описывать несколько элементов пользовательского интерфейса. Однако если вы не дадите указаний, как их расположить, Compose может расположить элементы так, как вам не понравится. Например, предыдущий код генерирует два текстовых элемента, которые накладываются друг на друга, потому что в нем нет указаний, как расположить два составных элемента.

В следующем задании вы узнаете, как расположить составные элементы в строке и в столбце.

# Расположите текстовые элементы в строку и колонку

**Иерархия пользовательского интерфейса**
Иерархия пользовательского интерфейса основана на содержании, то есть один компонент может содержать один или несколько компонентов, и иногда используются термины «родитель» и «ребенок». В данном случае речь идет о том, что родительские элементы пользовательского интерфейса содержат дочерние элементы пользовательского интерфейса, которые, в свою очередь, могут содержать дочерние элементы пользовательского интерфейса. В этом разделе вы узнаете о композитных элементах ```Column```, ```Row``` и ```Box```, которые могут выступать в качестве родительских элементов пользовательского интерфейса.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/9270b7e10f954dcb_856.png)

Три основных стандартных элемента макета в Compose - это композиты ```Column```, ```Row``` и ```Box```.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/d7df7c362f507d6b_856.png)

```Column```, ``Row`` и ```Box``` - это составные функции, которые принимают в качестве аргументов составное содержимое, поэтому вы можете размещать элементы внутри этих элементов макета. Например, каждый дочерний элемент внутри композитного элемента ```Row``` размещается горизонтально рядом друг с другом в строке.

```kt
// Don't copy.
Row {
    Text("First Column")
    Text("Second Column")
}
```

Эти текстовые элементы отображаются рядом друг с другом на экране, как показано на этом изображении.

Синие границы используются только в демонстрационных целях и не отображаются.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/7117f9998760a828_856.png)

**Синтаксис лямбды в конце строки**

> Обратите внимание, что в предыдущем фрагменте кода вместо круглых скобок в функции Row composable используются фигурные скобки. Это называется синтаксисом прицепных лямбд. Подробно о лямбдах и синтаксисе спускающихся лямбд вы узнаете позже в курсе. Пока же ознакомьтесь с этим часто используемым синтаксисом Compose.

Kotlin предлагает специальный синтаксис для передачи функций в качестве параметров функций, когда последний параметр является функцией.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/6373d65802273065_856.png)

Когда в качестве параметра передается функция, можно использовать синтаксис лямбды. Вместо того чтобы помещать функцию внутри круглых скобок, вы можете поместить ее вне круглых скобок в фигурных скобках. Это рекомендуемая и распространенная практика в Compose, поэтому вам нужно знать, как выглядит код.

Например, последним параметром в функции Row() composable является параметр ```content``` - функция, описывающая дочерние элементы пользовательского интерфейса. Предположим, вы хотите создать строку, содержащую три текстовых элемента. Этот код будет работать, но использование именованного параметра для последующей лямбды очень громоздко:

```kt
Row(
    content = {
        Text("Some text")
        Text("Some more text")
        Text("Last text")
    }
)
```

Поскольку параметр ```content``` является последним в сигнатуре функции, и вы передаете его значение в виде лямбда-выражения (ничего страшного, если вы не знаете, что такое лямбда, просто ознакомьтесь с синтаксисом), вы можете удалить параметр content и круглые скобки следующим образом:

```kt
Row {
    Text("Some text")
    Text("Some more text")
    Text("Last text")
}
```

###  Расположите текстовые элементы в ряд
В этом задании вы расположите текстовые элементы в вашем приложении в ряд, чтобы избежать наложения.

В файле MainActivity.kt прокрутите страницу до функции GreetingText().
Добавьте композит ```Row``` вокруг текстовых элементов так, чтобы он показывал строку с двумя текстовыми элементами. Выберите два текстовых элемента, щелкните на лампочке. Выберите ```Surround with widget > Surround with Row```.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/7ca98d82742d60b9_856.png)

Теперь функция должна выглядеть так, как показано в этом фрагменте кода:

```kt
@Composable
fun GreetingText(message: String, from: String, modifier: Modifier = Modifier) {
    Row {
        Text(
            text = message,
            fontSize = 100.sp,
            lineHeight = 116.sp,
        )
        Text(
            text = from,
            fontSize = 36.sp
        )
    }
}
```

Android Studio автоматически импортирует функцию ```Row```. Прокрутите страницу вверх и обратите внимание на раздел импорта. Импорт ```androidx.compose.foundation.layout.Row``` должен был быть добавлен.

Обратите внимание на обновленный предварительный просмотр в панели Design. Временно измените размер шрифта для сообщения о дне рождения на 30.sp.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/665aa2f1cc85c29_856.png)

Теперь предварительный просмотр выглядит гораздо лучше, так как нет перекрытия. Однако это не то, что вы хотите, потому что не хватает места для подписи. В следующем задании вы расположите текстовые элементы в столбце, чтобы решить эту проблему.

### Расположите текстовые элементы в столбце
В этом задании вам предстоит изменить функцию GreetingText(), чтобы расположить текстовые элементы в столбце. Предварительный просмотр должен выглядеть как на этом скриншоте:

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/d80295e73578e75d_856.png)

Теперь, когда вы попробовали сделать это самостоятельно, не стесняйтесь сверять свой код с кодом решения в этом фрагменте:

```kt
@Composable
fun GreetingText(message: String, from: String, modifier: Modifier = Modifier) {
    Column {
        Text(
            text = message,
            fontSize = 100.sp,
            lineHeight = 116.sp,
        )
        Text(
            text = from,
            fontSize = 36.sp
        )
    }
}
```

Обратите внимание на автоматически импортируемый Android Studio пакет:

```kt
import androidx.compose.foundation.layout.Column
```

> Вспомните, что в составных элементах нужно передавать параметр модификатора дочернему элементу. Это означает, что вам нужно передать параметр модификатора композитному элементу ```Column```.

```kt
@Composable
fun GreetingText(message: String, from: String, modifier: Modifier = Modifier) {
    Column(modifier = modifier) {
        Text(
            text = message,
            fontSize = 100.sp,
            lineHeight = 116.sp,
        )
        Text(
            text = from,
            fontSize = 36.sp
        )
    }
}
```

# Добавьте приветствие в приложение

Когда вы будете довольны предварительным просмотром, настанет время добавить композицию в ваше приложение на устройстве или эмуляторе.

В файле MainActivity.kt прокрутите страницу до функции ```onCreate()```.
Вызовите функцию GreetingText() из блока Surface.
Передайте функции GreetingText() свое поздравление с днем рождения и подпись.

Завершенная функция onCreate() должна выглядеть так, как показано в этом фрагменте кода:

```kt
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            HappyBirthdayTheme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    GreetingText(message = "Happy Birthday Sam!", from = "From Emma")
                }
            }
        }
    }
}
```

Создайте и запустите свое приложение в эмуляторе.

<center>
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/59e9c0c6e19748ff_856.png" style="width:400px;margin:50px;"/>
</center>

### Выравнивание приветствия по центру

Чтобы выровнять приветствие по центру экрана, добавьте параметр ```verticalArrangement``` и установите его в ```Arrangement.Center```.

```kt
@Composable
fun GreetingText(message: String, from: String, modifier: Modifier = Modifier) {
    Column(
        verticalArrangement = Arrangement.Center,
        modifier = modifier
    ) {
        // ...
    }
}
```

Добавьте 8.dp подкладки вокруг колонки. 

> Хорошей практикой является использование отступов с шагом 4.dp.

```kt
@Composable
fun GreetingText(message: String, from: String, modifier: Modifier = Modifier) {
    Column(
        verticalArrangement = Arrangement.Center,
        modifier = modifier.padding(8.dp)
    ) {
        // ...
    }
}
```

Чтобы еще больше украсить ваше приложение, выровняйте текст приветствия по центру с помощью ```textAlign```.

```kt
Text(
    text = message,
    fontSize = 100.sp,
    lineHeight = 116.sp,
    textAlign = TextAlign.Center
)
```

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/28c8e62f86323ba4_856.png)

На скриншоте выше только приветствие выровнено по центру благодаря параметру ```textAlign```. Подпись «From Emma» имеет выравнивание по умолчанию - по левому краю.

Добавьте ```padding``` к подписи и выровняйте ее по правому краю.

```kt
Text(
    text = from,
    fontSize = 36.sp,
    modifier = Modifier
        .padding(16.dp)
        .align(alignment = Alignment.End)
)
```

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/82b858f2f79ca9c4_856.png)

### Применяйте передовую практику

> Хорошей практикой является передача атрибута(ов) модификатора вместе с модификатором из родительского композита. Обновите параметр модификатора в GreetingText() следующим образом:

onCreate()

```kt
Surface(
    //...
) {
    GreetingText(
        message = "Happy Birthday Sam!",
        from = "From Emma",
        modifier = Modifier.padding(8.dp)
    )
}
```

GreetingText()

```kt
@Composable
fun GreetingText(message: String, from: String, modifier: Modifier = Modifier) {
    Column(
        verticalArrangement = Arrangement.Center,
        modifier = modifier
    ) {
        // ...
    }
}
```

Создайте и запустите свое приложение в эмуляторе, чтобы увидеть конечный результат.

<center>
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-text-composables/img/2ff181d48325023c_856.png" style="width:400px;margin:50px;"/>
</center>

# Получите код решения

Завершенный файл MainActivity.kt:

```kt
package com.example.happybirthday

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.example.happybirthday.ui.theme.HappyBirthdayTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            HappyBirthdayTheme {
                // A surface container using the 'background' color from the theme
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    GreetingText(
                        message = "Happy Birthday Sam!",
                        from = "From Emma",
                        modifier = Modifier.padding(8.dp)
                    )
                }
            }
        }
    }
}

@Composable
fun GreetingText(message: String, from: String, modifier: Modifier = Modifier) {
    Column(
        verticalArrangement = Arrangement.Center,
        modifier = modifier
    ) {
        Text(
            text = message,
            fontSize = 100.sp,
            lineHeight = 116.sp,
            textAlign = TextAlign.Center
        )
        Text(
            text = from,
            fontSize = 36.sp,
            modifier = Modifier
                .padding(16.dp)
                .align(alignment = Alignment.End)
        )
    }
}

@Preview(showBackground = true)
@Composable
fun BirthdayCardPreview() {
    HappyBirthdayTheme {
        GreetingText(message = "Happy Birthday Sam!", from = "From Emma")
    }
}
```

# Резюме

- Jetpack Compose - это современный набор инструментов для создания пользовательского интерфейса Android. Jetpack Compose упрощает и ускоряет разработку пользовательского интерфейса на Android благодаря меньшему количеству кода, мощным инструментам и интуитивно понятным API на языке Kotlin.

- Пользовательский интерфейс (UI) приложения - это то, что вы видите на экране: текст, изображения, кнопки и многие другие типы элементов.

- Композитные функции - это основной строительный блок Compose. Композитная функция - это функция, которая описывает некоторую часть вашего пользовательского интерфейса.

- Функция Composable аннотируется аннотацией ```@Composable```; эта аннотация сообщает компилятору Compose, что данная функция предназначена для преобразования данных в пользовательский интерфейс.

- Три основных стандартных элемента макета в Compose - это ```Column```, ```Row``` и ```Box```. Они представляют собой функции Composable, которые принимают содержимое Composable, поэтому вы можете размещать внутри них элементы. Например, каждый дочерний элемент в ```Row``` будет располагаться горизонтально рядом друг с другом.
