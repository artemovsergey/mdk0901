# Лекция 18. Применение темы Material Design с помощью Jetpack Compose

Material Design - это система дизайна, созданная и поддерживаемая дизайнерами и разработчиками Google для создания высококачественного цифрового опыта для Android, а также других мобильных и веб-платформ. Она содержит рекомендации по созданию читаемого, привлекательного и последовательного пользовательского интерфейса приложений.

В этом уроке вы узнаете о Material Theming, который позволяет использовать Material Design в вашем приложении, с руководством по настройке цветов, типографики и форм. Вы можете настроить для своего приложения как можно меньше или больше. Вы также узнаете, как добавить верхнюю панель приложения для отображения его названия и значка.

### Необходимые условия

- Знакомство с языком Kotlin, включая синтаксис, функции и переменные.
- Уметь создавать макеты в Compose, включая строки и столбцы с подложкой.
- Уметь создавать простые списки в Compose.

### Что вы узнаете

- Как применить Material Theming к приложению Compose.
- Как добавить в приложение пользовательскую цветовую палитру.
- Как добавлять пользовательские шрифты в приложение.
- Как добавлять пользовательские формы к элементам приложения.
- Как добавить в приложение верхнюю панель приложений.

### Что вы создадите

- Вы создадите красивое приложение, в котором будут использованы лучшие практики Material Design.

### Что вам понадобится

- Последняя версия Android Studio.
- Подключение к gogc для загрузки начального кода и шрифтов.


### Обзор приложения

В этом уроке вы создадите ```Woof```, приложение, которое отображает список собак и использует Material Design для создания красивого интерфейса приложения.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/92eca92f64b029cf_856.png" width="400px"/>
</center>

В этом уроке мы покажем вам некоторые возможности использования Material Theming. Используйте этот коделаб для поиска идей о том, как использовать Material Theming для улучшения внешнего вида и ощущения приложений, которые вы создаете в будущем.

### Цветовая палитра

Ниже приведены цветовые палитры для светлой и темной тем, которые мы создадим.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/d6b2e7b613386dfe_856.png)

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/5087303587b44563_856.png)

Вот финальная версия приложения в светлой и темной темах.

<div style="display:flex">
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/92eca92f64b029cf_856.png"/>
    </div>
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/883428064ccbc9_856.png"/>
    </div>
</div>

### Типографика

Ниже приведены стили шрифтов, которые вы будете использовать в приложении.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/8ea685b3871d5ffc_856.png)

### Файл темы

Файл ```Theme.kt``` - это файл, содержащий всю информацию о теме приложения, которая определяется с помощью цвета, типографики и формы. Это важный файл, который вы должны знать. Внутри файла находится составная функция ```WoofTheme()```, которая задает цвета, типографику и формы приложения.

```kt
@Composable
fun WoofTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    // Dynamic color is available on Android 12+
    dynamicColor: Boolean = false,
    content: @Composable () -> Unit
) {
    val colorScheme = when {
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> {
            val context = LocalContext.current
            if (darkTheme) dynamicDarkColorScheme(context) else dynamicLightColorScheme(context)
        }

        darkTheme -> DarkColors
        else -> LightColors
    }
    val view = LocalView.current
    if (!view.isInEditMode) {
        SideEffect {
            setUpEdgeToEdge(view, darkTheme)
        }
    }

    MaterialTheme(
        colorScheme = colorScheme,
        shapes = Shapes,
        typography = Typography,
        content = content
    )
}

/**
 * Устанавливает от края до края для окна этого [вида]. Цвета системных значков устанавливаются либо
 * светлыми или темными в зависимости от того, включена ли тема [darkTheme] или нет.
 */
private fun setUpEdgeToEdge(view: View, darkTheme: Boolean) {
    val window = (view.context as Activity).window
    WindowCompat.setDecorFitsSystemWindows(window, false)
    window.statusBarColor = Color.Transparent.toArgb()
    val navigationBarColor = when {
        Build.VERSION.SDK_INT >= 29 -> Color.Transparent.toArgb()
        Build.VERSION.SDK_INT >= 26 -> Color(0xFF, 0xFF, 0xFF, 0x63).toArgb()
        // Min sdk version for this app is 24, this block is for SDK versions 24 and 25
        else -> Color(0x00, 0x00, 0x00, 0x50).toArgb()
    }
    window.navigationBarColor = navigationBarColor
    val controller = WindowCompat.getInsetsController(window, view)
    controller.isAppearanceLightStatusBars = !darkTheme
    controller.isAppearanceLightNavigationBars = !darkTheme
}
```

В файле MainActivity.kt добавляется функция WoofTheme(), которая обеспечивает материальную тематику для всего приложения.

```kt
class MainActivity : ComponentActivity() {
   override fun onCreate(savedInstanceState: Bundle?) {
       super.onCreate(savedInstanceState)
       setContent {
           WoofTheme {
               Surface(
                   modifier = Modifier.fillMaxSize()
               ) {
                   WoofApp()
               }
           }
       }
   }
}
```

- Взгляните на WoofPreview(). Функция WoofTheme() добавлена, чтобы обеспечить оформление материала, которое вы видите в WoofPreview().

```kt
@Preview
@Composable
fun WoofPreview() {
    WoofTheme(darkTheme = false) {
        WoofApp()
    }
}
```

### Получите стартовый код

Чтобы начать работу, загрузите стартовый код:

```
$ git clone https://github.com/google-developer-training/basic-android-kotlin-compose-training-woof.git
$ cd basic-android-kotlin-compose-training-woof
$ git checkout starter
```

> Настройка: для работы измените параметры в проекте

AGP: 7.4.1
Gradle version: 7.5

build.gradle.kts (project) 

plugins {
    id("com.android.application") version "7.4.1" apply false
    id("com.android.library") version "7.4.1" apply false
    id("org.jetbrains.kotlin.android") version "2.0.0" apply false
    id("org.jetbrains.kotlin.plugin.compose") version "2.0.0" apply false
}

- версия core зависимости

```
implementation("androidx.core:core-ktx:1.12.0")
```



### Изучите стартовый код

- Откройте стартовый код в Android Studio.
- Откройте ```com.example.woof > data > Dog.kt```. Здесь содержится класс данных Dog, который будет использоваться для представления фотографии, имени, возраста и увлечений собаки. Здесь также содержится список собак и информация, которую вы будете использовать в качестве данных в своем приложении.
- Откройте ```res > drawable```. Здесь содержатся все изображения, необходимые для этого проекта, включая значок приложения, изображения собак и иконки.
- Откройте res > values > strings.xml. Здесь содержатся строки, которые вы используете в этом приложении, включая название приложения, клички собак, их описания и многое другое.

- Откройте файл MainActivity.kt. В нем содержится код для создания простого списка, в котором отображается фотография собаки, ее имя и возраст.

WoofApp() содержит LazyColumn, который отображает DogItems.
DogItem() содержит строку, в которой отображается фотография собаки и информация о ней.
DogIcon() отображает фотографию собаки.
DogInformation() отображает кличку и возраст собаки.
Функция WoofPreview() позволяет увидеть предварительный просмотр приложения в панели Design.

> Примечание: Вы можете заметить, что в каждом методе @Composable в качестве параметра добавлен модификатор. В Compose наилучшей практикой является передача параметра модификатора в композитные функции. Это позволяет родительской композитной функции передавать контекстную информацию дочерней композитной функции.

Например, если речь идет о кнопке, то один родитель может захотеть, чтобы его дочерняя кнопка использовала весь доступный размер, а другой родитель может захотеть, чтобы она обернула содержимое. Это делает код более многоразовым. Этот параметр обычно называется «modifier» и должен быть первым необязательным параметром в списке параметров функции. **Этот модификатор применяется к первому дочернему методу**. Подробнее об этом читайте в руководстве по API для Jetpack Compose.

- Убедитесь, что на вашем эмуляторе/устройстве установлена светлая тема

В этом уроке вы будете работать как со светлой, так и с темной темой, однако большая часть урока будет посвящена светлой теме. Прежде чем приступить к работе, убедитесь, что ваше устройство/эмулятор находится в светлой теме.

Чтобы просмотреть ваше приложение в светлой теме, на эмуляторе или физическом устройстве:

- Зайдите в приложение «Настройки» на устройстве.
- Найдите пункт «Темная тема» и нажмите на него.
- Если темная тема включена, отключите ее.
- Запустите код запуска и посмотрите, с чего вы начнете: это список, в котором отображаются собаки с их фотографиями, именами и возрастом. Он функционален, но выглядит не очень, поэтому мы собираемся это исправить.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/6d253ae50c63014d_856.png" width="400px"/>
</center>

### Добавьте цвет

Первое, что вам предстоит изменить в приложении Woof, - это цветовая схема.

Цветовая схема - это сочетание цветов, которые использует ваше приложение. Различные сочетания цветов вызывают разное настроение, что влияет на то, как люди чувствуют себя при использовании вашего приложения.

В системе Android цвет представлен шестнадцатеричным (hex) цветовым значением. Шестнадцатеричный код цвета начинается с символа фунта (#), за которым следуют шесть букв и/или цифр, обозначающих красный, зеленый и синий (RGB) компоненты этого цвета. Первые две буквы/цифры относятся к красному цвету, следующие две - к зеленому, а последние две - к синему.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/e0349c33dd6fbafe_856.png)

Цвет также может включать альфа-значение - буквы и/или цифры - которое отражает прозрачность цвета (#00 - 0% непрозрачности (полностью прозрачный), #FF - 100% непрозрачности (полностью непрозрачный)). Если альфа-значение включено, оно представляет собой первые два символа шестнадцатеричного кода цвета после знака фунта (#). Если альфа-значение не включено, считается, что оно равно #FF, то есть 100% непрозрачности (полностью непрозрачный).

Ниже приведены примеры цветов и их шестнадцатеричные значения.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/2753d8cdd396c449_856.png" width="400px"/>
</center>


### Используйте Material Theme Builder для создания цветовой схемы

Чтобы создать пользовательскую цветовую схему для нашего приложения, мы воспользуемся конструктором тем Material Theme Builder.

По адресу 

https://m3.material.io/theme-builder#/custom

можно перейти в Material Theme Builder.

> Только для ознакомления. В колледже не работает

На левой панели вы увидите основные цвета, нажмите на Primary:

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/c58fc807f4378d4d_856.png" width="400px"/>
</center>

Откроется окно выбора цвета HCT.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/62c87ab4b476cf92_856.png" width="400px"/>
</center>

- Чтобы создать цветовую схему, показанную на скриншотах приложения, вы измените основной цвет в этом цветовом редакторе. В текстовом поле замените текущий текст на #006C4C. В результате основной цвет приложения станет зеленым.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/ead81a6bf86d2170_856.png" width="400px"/>
</center>


- Обратите внимание, как при этом приложения на экране приобретают зеленую цветовую гамму.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/1e3f080002e0174_856.png" width="400px"/>
</center>

- Прокрутите страницу вниз, и вы увидите полную цветовую схему для светлой и темной темы, созданную на основе введенного вами цвета.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/d6b2e7b613386dfe_856.png" width="400px"/>
</center>

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/5087303587b44563_856.png" width="400px"/>
</center>


Вам может быть интересно, что это за роли и как они используются, вот несколько основных из них:

- Основные цвета используются для ключевых компонентов пользовательского интерфейса.
- Вторичные цвета используются для менее заметных компонентов пользовательского интерфейса.
- Третичные цвета используются для контрастных акцентов, которые могут быть использованы для балансировки основного и вторичного цветов или привлечения повышенного внимания к элементу, например, к полю ввода.

Цветовые элементы появляются поверх других цветов в палитре и применяются в основном для текста, иконографии и штрихов. В нашей палитре цветов есть onSurface color, который появляется поверх цвета поверхности, и onPrimary color, который появляется поверх основного цвета.

Наличие этих слотов приводит к созданию целостной системы дизайна, в которой связанные компоненты окрашиваются одинаково.

Хватит теории о цветах, пора добавить эту красивую цветовую палитру в приложение!

### Добавление цветовой палитры в тему

На странице Material Theme Builder есть возможность нажать кнопку ```Export```, чтобы загрузить файл ```Color.kt``` и файл ```Theme.kt``` с пользовательской темой, созданной в Theme Builder.

- Это позволит добавить созданную нами пользовательскую тему в ваше приложение. Однако, поскольку сгенерированный файл ```Theme.kt``` не включает код для динамического цвета, который мы рассмотрим позже в уроке, скопируйте эти файлы.

> Примечание: Если вы решите использовать файлы, сгенерированные в Material Theme Builder, для другого проекта, вам нужно будет обновить имя пакета до имени пакета вашего проекта.

Откройте файл ```Color.kt``` и замените его содержимое приведенным ниже кодом, чтобы скопировать новую цветовую схему.

```kt
package com.example.woof.ui.theme

import androidx.compose.ui.graphics.Color

val md_theme_light_primary = Color(0xFF006C4C)
val md_theme_light_onPrimary = Color(0xFFFFFFFF)
val md_theme_light_primaryContainer = Color(0xFF89F8C7)
val md_theme_light_onPrimaryContainer = Color(0xFF002114)
val md_theme_light_secondary = Color(0xFF4D6357)
val md_theme_light_onSecondary = Color(0xFFFFFFFF)
val md_theme_light_secondaryContainer = Color(0xFFCFE9D9)
val md_theme_light_onSecondaryContainer = Color(0xFF092016)
val md_theme_light_tertiary = Color(0xFF3D6373)
val md_theme_light_onTertiary = Color(0xFFFFFFFF)
val md_theme_light_tertiaryContainer = Color(0xFFC1E8FB)
val md_theme_light_onTertiaryContainer = Color(0xFF001F29)
val md_theme_light_error = Color(0xFFBA1A1A)
val md_theme_light_errorContainer = Color(0xFFFFDAD6)
val md_theme_light_onError = Color(0xFFFFFFFF)
val md_theme_light_onErrorContainer = Color(0xFF410002)
val md_theme_light_background = Color(0xFFFBFDF9)
val md_theme_light_onBackground = Color(0xFF191C1A)
val md_theme_light_surface = Color(0xFFFBFDF9)
val md_theme_light_onSurface = Color(0xFF191C1A)
val md_theme_light_surfaceVariant = Color(0xFFDBE5DD)
val md_theme_light_onSurfaceVariant = Color(0xFF404943)
val md_theme_light_outline = Color(0xFF707973)
val md_theme_light_inverseOnSurface = Color(0xFFEFF1ED)
val md_theme_light_inverseSurface = Color(0xFF2E312F)
val md_theme_light_inversePrimary = Color(0xFF6CDBAC)
val md_theme_light_shadow = Color(0xFF000000)
val md_theme_light_surfaceTint = Color(0xFF006C4C)
val md_theme_light_outlineVariant = Color(0xFFBFC9C2)
val md_theme_light_scrim = Color(0xFF000000)

val md_theme_dark_primary = Color(0xFF6CDBAC)
val md_theme_dark_onPrimary = Color(0xFF003826)
val md_theme_dark_primaryContainer = Color(0xFF005138)
val md_theme_dark_onPrimaryContainer = Color(0xFF89F8C7)
val md_theme_dark_secondary = Color(0xFFB3CCBE)
val md_theme_dark_onSecondary = Color(0xFF1F352A)
val md_theme_dark_secondaryContainer = Color(0xFF354B40)
val md_theme_dark_onSecondaryContainer = Color(0xFFCFE9D9)
val md_theme_dark_tertiary = Color(0xFFA5CCDF)
val md_theme_dark_onTertiary = Color(0xFF073543)
val md_theme_dark_tertiaryContainer = Color(0xFF244C5B)
val md_theme_dark_onTertiaryContainer = Color(0xFFC1E8FB)
val md_theme_dark_error = Color(0xFFFFB4AB)
val md_theme_dark_errorContainer = Color(0xFF93000A)
val md_theme_dark_onError = Color(0xFF690005)
val md_theme_dark_onErrorContainer = Color(0xFFFFDAD6)
val md_theme_dark_background = Color(0xFF191C1A)
val md_theme_dark_onBackground = Color(0xFFE1E3DF)
val md_theme_dark_surface = Color(0xFF191C1A)
val md_theme_dark_onSurface = Color(0xFFE1E3DF)
val md_theme_dark_surfaceVariant = Color(0xFF404943)
val md_theme_dark_onSurfaceVariant = Color(0xFFBFC9C2)
val md_theme_dark_outline = Color(0xFF8A938C)
val md_theme_dark_inverseOnSurface = Color(0xFF191C1A)
val md_theme_dark_inverseSurface = Color(0xFFE1E3DF)
val md_theme_dark_inversePrimary = Color(0xFF006C4C)
val md_theme_dark_shadow = Color(0xFF000000)
val md_theme_dark_surfaceTint = Color(0xFF6CDBAC)
val md_theme_dark_outlineVariant = Color(0xFF404943)
val md_theme_dark_scrim = Color(0xFF000000)
```

- Откройте файл ```Theme.kt``` и замените его содержимое на приведенный ниже код, чтобы добавить новые цвета в тему.

```kt
package com.example.woof.ui.theme

import android.app.Activity
import android.os.Build
import android.view.View
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.dynamicDarkColorScheme
import androidx.compose.material3.dynamicLightColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.SideEffect
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.toArgb
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalView
import androidx.core.view.WindowCompat

private val LightColors = lightColorScheme(
    primary = md_theme_light_primary,
    onPrimary = md_theme_light_onPrimary,
    primaryContainer = md_theme_light_primaryContainer,
    onPrimaryContainer = md_theme_light_onPrimaryContainer,
    secondary = md_theme_light_secondary,
    onSecondary = md_theme_light_onSecondary,
    secondaryContainer = md_theme_light_secondaryContainer,
    onSecondaryContainer = md_theme_light_onSecondaryContainer,
    tertiary = md_theme_light_tertiary,
    onTertiary = md_theme_light_onTertiary,
    tertiaryContainer = md_theme_light_tertiaryContainer,
    onTertiaryContainer = md_theme_light_onTertiaryContainer,
    error = md_theme_light_error,
    errorContainer = md_theme_light_errorContainer,
    onError = md_theme_light_onError,
    onErrorContainer = md_theme_light_onErrorContainer,
    background = md_theme_light_background,
    onBackground = md_theme_light_onBackground,
    surface = md_theme_light_surface,
    onSurface = md_theme_light_onSurface,
    surfaceVariant = md_theme_light_surfaceVariant,
    onSurfaceVariant = md_theme_light_onSurfaceVariant,
    outline = md_theme_light_outline,
    inverseOnSurface = md_theme_light_inverseOnSurface,
    inverseSurface = md_theme_light_inverseSurface,
    inversePrimary = md_theme_light_inversePrimary,
    surfaceTint = md_theme_light_surfaceTint,
    outlineVariant = md_theme_light_outlineVariant,
    scrim = md_theme_light_scrim,
)


private val DarkColors = darkColorScheme(
    primary = md_theme_dark_primary,
    onPrimary = md_theme_dark_onPrimary,
    primaryContainer = md_theme_dark_primaryContainer,
    onPrimaryContainer = md_theme_dark_onPrimaryContainer,
    secondary = md_theme_dark_secondary,
    onSecondary = md_theme_dark_onSecondary,
    secondaryContainer = md_theme_dark_secondaryContainer,
    onSecondaryContainer = md_theme_dark_onSecondaryContainer,
    tertiary = md_theme_dark_tertiary,
    onTertiary = md_theme_dark_onTertiary,
    tertiaryContainer = md_theme_dark_tertiaryContainer,
    onTertiaryContainer = md_theme_dark_onTertiaryContainer,
    error = md_theme_dark_error,
    errorContainer = md_theme_dark_errorContainer,
    onError = md_theme_dark_onError,
    onErrorContainer = md_theme_dark_onErrorContainer,
    background = md_theme_dark_background,
    onBackground = md_theme_dark_onBackground,
    surface = md_theme_dark_surface,
    onSurface = md_theme_dark_onSurface,
    surfaceVariant = md_theme_dark_surfaceVariant,
    onSurfaceVariant = md_theme_dark_onSurfaceVariant,
    outline = md_theme_dark_outline,
    inverseOnSurface = md_theme_dark_inverseOnSurface,
    inverseSurface = md_theme_dark_inverseSurface,
    inversePrimary = md_theme_dark_inversePrimary,
    surfaceTint = md_theme_dark_surfaceTint,
    outlineVariant = md_theme_dark_outlineVariant,
    scrim = md_theme_dark_scrim,
)

@Composable
fun WoofTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    // Dynamic color is available on Android 12+
    dynamicColor: Boolean = false,
    content: @Composable () -> Unit
) {
    val colorScheme = when {
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> {
            val context = LocalContext.current
            if (darkTheme) dynamicDarkColorScheme(context) else dynamicLightColorScheme(context)
        }

        darkTheme -> DarkColors
        else -> LightColors
    }
    val view = LocalView.current
    if (!view.isInEditMode) {
        SideEffect {
            setUpEdgeToEdge(view, darkTheme)
        }
    }

    MaterialTheme(
        colorScheme = colorScheme,
        shapes = Shapes,
        typography = Typography,
        content = content
    )
}

/**
 * Устанавливает от края до края для окна этого [вида]. Цвета системных значков устанавливаются либо
 * светлыми или темными в зависимости от того, включена ли тема [darkTheme] или нет.
 */
private fun setUpEdgeToEdge(view: View, darkTheme: Boolean) {
    val window = (view.context as Activity).window
    WindowCompat.setDecorFitsSystemWindows(window, false)
    window.statusBarColor = Color.Transparent.toArgb()
    val navigationBarColor = when {
        Build.VERSION.SDK_INT >= 29 -> Color.Transparent.toArgb()
        Build.VERSION.SDK_INT >= 26 -> Color(0xFF, 0xFF, 0xFF, 0x63).toArgb()
        // Min sdk version for this app is 24, this block is for SDK versions 24 and 25
        else -> Color(0x00, 0x00, 0x00, 0x50).toArgb()
    }
    window.navigationBarColor = navigationBarColor
    val controller = WindowCompat.getInsetsController(window, view)
    controller.isAppearanceLightStatusBars = !darkTheme
    controller.isAppearanceLightNavigationBars = !darkTheme
}
```

В WoofTheme() в val colorScheme используется оператор ```when```.

Если dynamicColor равен true и версия сборки S или выше, проверяется, находится ли устройство в темной теме или нет.
Если оно находится в темной теме, colorScheme будет установлен в dynamicDarkColorScheme.
Если темной темы нет, будет установлено значение dynamicLightColorScheme.

Если приложение не использует dynamicColorScheme, проверяется, находится ли ваше приложение в темной теме. Если да, то для colorScheme будет установлено значение DarkColors.
Если ни то, ни другое не верно, то colorScheme будет установлен в LightColors.
В скопированном в файл ```Theme.kt``` файле dynamicColor установлено значение false, а устройства, с которыми мы работаем, находятся в светлом режиме, поэтому colorScheme будет установлен в LightColors.

```kt
val colorScheme = when {
       dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> {
           val context = LocalContext.current
           if (darkTheme) dynamicDarkColorScheme(context) else dynamicLightColorScheme(context)
       }

       darkTheme -> DarkColors
       else -> LightColors
   }
```

- Запустите приложение снова, обратите внимание, что панель приложений автоматически изменила цвет.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/b48b3fa2ecec9b86_856.png" width="400px"/>
</center>

### Сопоставление цветов

Компоненты материалов автоматически привязываются к цветовым слотам. Другие ключевые компоненты пользовательского интерфейса, такие как плавающие кнопки действий, также по умолчанию используют основной цвет. Это означает, что вам не нужно явно назначать цвет компоненту; он автоматически сопоставляется с цветовым слотом, когда вы устанавливаете цветовую тему в приложении. Вы можете отменить это, явно задав цвет в коде.

В этом разделе мы обернем строку, содержащую DogIcon() и DogInformation(), карточкой, чтобы отличить цвет элементов списка от фона.

В композитной функции DogItem() оберните Row() с помощью Card().

```kt
Card() {
   Row(
       modifier = modifier
           .fillMaxWidth()
           .padding(dimensionResource(id = R.dimen.padding_small))
   ) {
       DogIcon(dog.imageResourceId)
       DogInformation(dog.name, dog.age)
   }
}
```

Поскольку Card теперь является первым дочерним объектом, компонуемым в DogItem(), передайте модификатор из DogItem() в Card и обновите модификатор Row на новый экземпляр Modifier.

```kt
Card(modifier = modifier) {
   Row(
       modifier = Modifier
           .fillMaxWidth()
           .padding(dimensionResource(id = R.dimen.padding_small))
   ) {
       DogIcon(dog.imageResourceId)
       DogInformation(dog.name, dog.age)
   }
}
```

Взгляните на функцию WoofPreview(). Теперь элементы списка автоматически меняют цвет благодаря Card Composables. Цвета выглядят отлично, но между элементами списка нет интервала.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/6d49372a1ef49bc7_856.png" width="400px"/>
</center>

**Файл dimens**
Точно так же, как вы используете файл ```strings.xml``` для хранения строк в вашем приложении, рекомендуется использовать файл ```dimens.xml``` для хранения значений размеров. Это полезно для того, чтобы не кодировать значения жестко, и чтобы в случае необходимости их можно было изменить в одном месте.

Перейдите в ```app > res > values > dimens.xml``` и посмотрите на файл. В нем хранятся значения размеров padding_small, padding_medium и image_size. Эти размеры будут использоваться во всем приложении.

```xml
<resources>
   <dimen name="padding_small">8dp</dimen>
   <dimen name="padding_medium">16dp</dimen>
   <dimen name="image_size">64dp</dimen>
</resources>
```

- Чтобы добавить значение из файла dimens.xml, воспользуйтесь этим правильным форматом:

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/550d49d70146013b_856.png" width="400px"/>
</center>

Например, чтобы добавить padding_small, вы передадите dimensionResource(id = R.dimen.padding_small).

В WoofApp() добавьте модификатор с padding_small в вызов DogItem().

```kt
@Composable
fun WoofApp() {
    Scaffold { it ->
        LazyColumn(contentPadding = it) {
            items(dogs) {
                DogItem(
                    dog = it,
                    modifier = Modifier.padding(dimensionResource(R.dimen.padding_small))
                )
            }
        }
    }
}
```

В функции WoofPreview() теперь больше расстояния между элементами списка.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/c54f870f121fe02_856.png" width="400px"/>
</center>

### Темная тема

В системе Android есть возможность переключить устройство на темную тему. В темной теме используются более темные и приглушенные цвета:

- Может значительно снизить энергопотребление (в зависимости от технологии экрана устройства).
- Улучшает видимость для пользователей со слабым зрением и тех, кто чувствителен к яркому свету.
- Упрощает использование устройства в условиях недостаточной освещенности.

Ваше приложение может выбрать Force Dark, что означает, что система будет реализовывать темную тему для вас. Однако для пользователей будет лучше, если вы сами внедрите темную тему, чтобы сохранить полный контроль над темой приложения.

При выборе темной темы важно учитывать, что цвета для темной темы должны соответствовать стандартам контрастности. В темных темах используется темный цвет поверхности с ограниченным количеством цветовых акцентов.

### Просмотр темной темы в предварительном просмотре

Вы уже добавили цвета для темной темы в предыдущем шаге. Чтобы увидеть темную тему в действии, вы добавите еще один компонент Preview Composable в MainActivity.kt. Таким образом, когда вы измените макет пользовательского интерфейса в коде, вы сможете увидеть, как одновременно выглядят превью светлой и темной тем.

- В разделе WoofPreview() создайте новую функцию WoofDarkThemePreview() и аннотируйте ее с помощью @Preview и @Composable.

```kt
@Preview
@Composable
fun WoofDarkThemePreview() {

}
```

- Внутри DarkThemePreview() добавьте WoofTheme(). Без добавления WoofTheme() вы не увидите ни одного из стилей, которые мы добавили в приложение. Установите для параметра darkTheme значение true.

```kt
@Preview
@Composable
fun WoofDarkThemePreview() {
   WoofTheme(darkTheme = true) {

   }
}
```

- Вызовите WoofApp() внутри WoofTheme().

```kt
@Preview
@Composable
fun WoofDarkThemePreview() {
   WoofTheme(darkTheme = true) {
       WoofApp()
   }
}
```

Теперь прокрутите панель «Дизайн» вниз, чтобы увидеть приложение в темной теме, включая более темный фон приложения/элемента списка и более светлый текст. Сравните различия между темной и светлой темами.

<div style="display:flex;">
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/92e2efb9dfd4ca6d_856.png"/>
    </div>
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/b444fd0900815b2a_856.png"/>
    </div>
</div>

### Просмотр темной темы на устройстве или эмуляторе

Чтобы просмотреть свое приложение в темной теме на эмуляторе или физическом устройстве:

- Зайдите в приложение «Настройки» на устройстве.
- Найдите пункт «Темная тема» и нажмите на него.
- Включите темную тему.
- Снова откройте приложение Woof, и оно перейдет в темную тему.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/bc31a94207265b08_856.png" width="400px"/>
</center>

Этот урко больше сосредоточен на светлой теме, поэтому перед тем, как приступить к работе с приложением, отключите темную тему.

- Перейдите в приложение «Настройки» на устройстве.
- Выберите Дисплей.
- Отключите темную тему.
- Сравните, как выглядело приложение в начале раздела и сейчас. Элементы списка и текст стали более четкими, а цветовая схема - более привлекательной.


<div style="display:flex">
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/6d253ae50c63014d_856.png"/>
    </div>
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/3d3d99c8b3643cf7_856.png"/>
    </div>
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/bc31a94207265b08_856.png"/>
    </div>
</div>


### Динамический цвет

В Material 3 большое внимание уделяется персонализации пользователей - новая функция в Material 3 - Dynamic Color, которая создает тему для вашего приложения на основе обоев пользователя. Таким образом, если пользователь любит зеленый цвет и имеет синий фон телефона, его приложение Woof также будет синим, чтобы отразить это. Динамическая тема работает только на некоторых устройствах под управлением Android 12 и выше.

Пользовательская тема может быть использована для приложений, которые имеют сильные брендинговые цвета, а также должна быть реализована для устройств, которые не поддерживают динамическую тематику, чтобы ваше приложение оставалось тематическим.

Чтобы включить динамический цвет, откройте ```Theme.kt```, перейдите к композиту WoofTheme() и установите параметр ```dynamicColor``` в true.

```kt
@Composable
fun WoofTheme(
   darkTheme: Boolean = isSystemInDarkTheme(),
   dynamicColor: Boolean = true,
   content: @Composable () -> Unit
)
```

- Чтобы изменить фон устройства или эмулятора, зайдите в «Настройки», затем найдите «Обои».

- Измените обои на цвет или набор цветов.
- Перезапустите приложение, чтобы увидеть динамическую тему (обратите внимание, что ваше устройство или эмулятор должны быть на Android 12+, чтобы увидеть динамический цвет)

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/710bd13f6b189dc5_856.png" width="400px"/>
</center>

В этом уроке рассматриваются пользовательские темы, поэтому отключите dynamicColor, прежде чем двигаться дальше.

```kt
@Composable
fun WoofTheme(
   darkTheme: Boolean = isSystemInDarkTheme(),
   dynamicColor: Boolean = false,
   content: @Composable () -> Unit
)
```

### Добавьте форму

Применение формы может изменить очень многое во внешнем виде и восприятии композита. Формы направляют внимание, идентифицируют компоненты, передают состояние и выражают бренд.

Многие формы определяются с помощью ```RoundedCornerShape```, которая описывает прямоугольник с закругленными углами. Передаваемое число определяет, насколько закруглены углы. Если используется ```RoundedCornerShape(0.dp)```, прямоугольник не имеет закругленных углов; если используется ```RoundedCornerShape(50.dp)```, углы будут полностью круглыми.

<div style="display:flex">
    <div>
    <p> 0.dp </p>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/7aa47654fba1869a_856.png"/>
    </div>
    <div>
    <p> 25.dp </p>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/d0661b773c703f57_856.png"/>
    </div>
    <div>
    <p> 50.dp </p>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/78bbef6f504eff53_856.png"/>
    </div>
</div>


Вы также можете изменять формы, добавляя различные проценты округления на каждом углу.


<div style="display:flex">
    <div>
        <p> Top left: 50.dp </p>
        <p> Bottom left: 25.dp </p>
        <p> Top right: 0.dp </p>
        <p> Bottom right: 15.dp </p>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/35e7aa917b0b6d4_856.png"/>
    </div>
    <div>
        <p> Top left: 15.dp </p>
        <p> Bottom left: 50.dp </p>
        <p> Top right: 50.dp </p>
        <p> Bottom right: 15.dp </p>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/5c030ab0f4557b21_856.png"/>
    </div>
    <div>
        <p> Top left: 0.dp </p>
        <p> Bottom left: 50.dp </p>
        <p> Top right: 0.dp </p>
        <p> Bottom right: 50.dp </p>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/56a7b7b62313ef89_856.png"/>
    </div>
</div>


Файл ```Shape.kt``` используется для определения форм компонентов в Compose. Существует три типа компонентов: маленькие, средние и большие. В этом разделе вы измените компонент Card, который определен как средний. Компоненты группируются в категории форм в зависимости от их размера.

В этом разделе вы придадите изображению собаки форму круга и измените форму элемента списка.

**Придайте изображению собаки форму круга**

- Откройте файл ```Shape.kt``` и обратите внимание, что для параметра small установлено значение ```RoundedCornerShape(50.dp)```. Этот параметр будет использоваться для придания изображению формы круга.
```kt
val Shapes = Shapes(
   small = RoundedCornerShape(50.dp),
)
```

- Откройте файл MainActivity.kt. В функции DogIcon() добавьте атрибут clip к модификатору Image; это позволит закрепить изображение в форме. 
- Передайте материал MaterialTheme.shapes.small.

```kt
import androidx.compose.ui.draw.clip

@Composable
fun DogIcon(
   @DrawableRes dogIcon: Int,
   modifier: Modifier = Modifier
) {
   Image(
       modifier = modifier
           .size(dimensionResource(id = R.dimen.image_size))
           .padding(dimensionResource(id = R.dimen.padding_small))
           .clip(MaterialTheme.shapes.small),
```

- Когда вы посмотрите на WoofPreview(), вы заметите, что иконки собак круглые! Однако некоторые фотографии обрезаны по бокам и не отображаются полностью.
cular.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/1d4d1e5eaaddf71e_856.png" width="400px"/>
</center>

Чтобы сделать все фотографии круглыми, добавьте ```ContentScale``` и атрибут Crop; это обрезает изображение по размеру. Обратите внимание, что contentScale - это атрибут Image, а не часть модификатора.

```kt
import androidx.compose.ui.layout.ContentScale

@Composable
fun DogIcon(
   @DrawableRes dogIcon: Int,
   modifier: Modifier = Modifier
) {
   Image(
       modifier = modifier
           .size(dimensionResource(id = R.dimen.image_size))
           .padding(dimensionResource(id = R.dimen.padding_small))
           .clip(MaterialTheme.shapes.small),
       contentScale = ContentScale.Crop,
```

Это полная версия ```DogIcon()``` Composable.


```kt
@Composable
fun DogIcon(
    @DrawableRes dogIcon: Int,
    modifier: Modifier = Modifier
) {
    Image(
        modifier = modifier
            .size(dimensionResource(R.dimen.image_size))
            .padding(dimensionResource(R.dimen.padding_small))
            .clip(MaterialTheme.shapes.small),
        contentScale = ContentScale.Crop,
        painter = painterResource(dogIcon),

        // Content Description is not needed here - image is decorative, and setting a null content
        // description allows accessibility services to skip this element during navigation.

        contentDescription = null
    )
}
```

Теперь в WoofPreview() иконки стали круглыми.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/fc93106990f5e161_856.png" width="400px"/>
</center>


**Добавление фигуры к элементу списка**

В этом разделе вы добавите форму к элементу списка. Элемент списка уже отображается через карточку. Карточка - это поверхность, которая может содержать один составной элемент и содержит опции для украшения. Украшение можно добавить с помощью границы, формы и других элементов. В этом разделе вы будете использовать карточку для добавления формы к элементу списка.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/244cf8727b603de9_856.png)

- Откройте файл ```Shape.kt```. Card - это средний компонент, поэтому вы добавляете параметр medium объекта Shapes. В этом приложении верхний правый и нижний левый углы элемента списка нужно сделать полностью круглыми, но не полностью. Чтобы добиться этого, передайте в атрибут medium значение 16.dp.

```kt
medium = RoundedCornerShape(bottomStart = 16.dp, topEnd = 16.dp)
```

Поскольку открытка по умолчанию уже использует среднюю форму, вам не нужно явно устанавливать ее на среднюю форму. Посмотрите предварительный просмотр, чтобы увидеть новую форму карточки!

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/ff657577b77964ae_856.png" width="400px"/>
</center>

Если вы вернетесь к файлу ```Theme.kt``` в WoofTheme() и посмотрите на MaterialTheme(), вы увидите, что атрибут shapes установлен на значение Shapes, которое вы только что обновили.


```kt
MaterialTheme(
   colors = colors,
   typography = Typography,
   shapes = Shapes,
   content = content
)
```

Ниже показаны элементы списка до и после шейпинга. Обратите внимание, насколько визуально привлекательнее стало приложение с добавлением шейпинга.

<div style="display:flex">
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/618b091614c6bc5b_856.png"/>
    </div>
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/87d476f7a7f786dd_856.png"/>
    </div>
</div>

### Добавьте типографику

#### Шкала типов Material Design

**Шкала типов** - это набор стилей шрифтов, которые можно использовать во всех приложениях, обеспечивая гибкий, но последовательный стиль. Шкала типов Material Design включает пятнадцать стилей шрифтов, поддерживаемых системой типов. Названия и группировки были упрощены до следующих: display, headline, title, body и label, с большим, средним и маленьким размером для каждого. Эти варианты нужно использовать только в том случае, если вы хотите настроить свое приложение. Если вы не знаете, что установить для каждой категории шкалы, знайте, что есть шкала по умолчанию, которую можно использовать.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/999a161dcd9b0ec4_856.png)

Шкала типов содержит многократно используемые категории текста, каждая из которых имеет свое назначение и значение.

**Дисплей**
Как самый крупный текст на экране, дисплейные стили предназначены для короткого, важного текста или цифр. Они лучше всего работают на больших экранах.

**Заголовок**
Заголовки лучше всего подходят для короткого текста с высоким выделением на небольших экранах. Эти стили могут быть полезны для выделения основных отрывков текста или важных областей контента.

**Заголовок**
Заголовки меньше по размеру, чем стили заголовков, и их следует использовать для текста со средним выделением, который остается относительно коротким.

**Тело**
Стили body используются для более длинных отрывков текста в вашем приложении.

**Label**
Стили Label - это более мелкие, утилитарные стили, которые используются для текста внутри компонентов или для очень мелкого текста в теле контента, например, для подписей.

**Шрифты**
Платформа Android предоставляет множество шрифтов, но вы можете захотеть настроить свое приложение, используя шрифт, не предусмотренный по умолчанию. Пользовательские шрифты могут придать индивидуальность и использоваться для брендинга.

В этом разделе вы добавите пользовательские шрифты ```Abril Fatface```, ```Montserrat Bold``` и ```Montserrat Regular```. Вы будете использовать заголовки displayLarge и displayMedium, а также текст bodyLarge из системы Material Type и добавите их в текст вашего приложения.

**Создайте каталог ресурсов шрифта Android.**

Прежде чем добавлять шрифты в приложение, необходимо добавить каталог шрифтов.

- В представлении проекта в Android Studio щелкните правой кнопкой мыши папку res.
Выберите ```New > Android Resource Directory```.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/8ea7753261102f61_856.png)

- Назовите шрифт Directory, установите тип ресурса как font и нажмите OK.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/d8b11c1535ac8372_856.png)

- Откройте каталог ресурсов нового шрифта, расположенный по адресу ```res > font```.
- Загрузите пользовательские шрифты

Поскольку вы используете шрифты, не предусмотренные платформой Android, вам необходимо загрузить пользовательские шрифты.

- Перейдите на сайт https://fonts.google.com/.

- Найдите Montserrat и нажмите кнопку Загрузить семью.
Распакуйте zip-файл.

> Примечание: шрифт находится в ресурсах репозитория на gogc

- Откройте скачанную папку ```Montserrat```. В папке static найдите Montserrat-Bold.ttf и Montserrat-Regular.ttf (ttf означает TrueType Font и является форматом для файлов шрифтов). Выберите оба шрифта и перетащите их в каталог ресурсов шрифтов в вашем проекте в Android Studio.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/195ecec4cb8bd27e_856.png)

- В папке со шрифтами переименуйте Montserrat-Bold.ttf в montserrat_bold.ttf и Montserrat-Regular.ttf в montserrat_regular.ttf.

- Найдите Abril Fatface и нажмите кнопку Загрузить семью.

- Откройте загруженную папку Abril_Fatface. Выберите AbrilFatface-Regular.ttf и перетащите его в каталог ресурсов шрифта.
- В папке со шрифтами переименуйте Abril_Fatface_Regular.ttf в abril_fatface_regular.ttf.

Вот как должен выглядеть каталог ресурсов шрифтов в вашем проекте с тремя пользовательскими файлами шрифтов:

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/90bc5dc3a03699c8_856.png)

**Инициализация шрифтов**

В окне проекта откройте ```ui.theme > Type.kt```. Инициализируйте загруженные шрифты ниже операторов импорта и выше Typography val. Сначала инициализируйте Abril Fatface, установив его равным FontFamily и передав Font с файлом шрифта abril_fatface_regular.

```kt
​​import androidx.compose.ui.text.font.Font
import androidx.compose.ui.text.font.FontFamily
import com.example.woof.R

val AbrilFatface = FontFamily(
   Font(R.font.abril_fatface_regular)
)
```

- Инициализируйте Montserrat, под Abril Fatface, установив его равным FontFamily и передав Font с файлом шрифта montserrat_regular. Для montserrat_bold также включите FontWeight.Bold. Даже если вы передаете жирную версию файла шрифта, Compose не знает, что файл является жирным, поэтому вам нужно явно связать файл с FontWeight.Bold.

```kt
import androidx.compose.ui.text.font.FontWeight

val AbrilFatface = FontFamily(
   Font(R.font.abril_fatface_regular)
)

val Montserrat = FontFamily(
   Font(R.font.montserrat_regular),
   Font(R.font.montserrat_bold, FontWeight.Bold)
)
```

- Затем установите различные типы заголовков для шрифтов, которые вы только что добавили. Объект Typography имеет параметры для 13 различных шрифтов, о которых говорилось выше. Вы можете задать столько параметров, сколько вам нужно. В этом приложении мы зададим displayLarge, displayMedium и bodyLarge. В следующей части этого приложения вы будете использовать labelSmall, поэтому добавьте его сюда.

Ниже приведена таблица, в которой указаны шрифт, вес и размер каждого добавляемого заголовка.


![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/8ea685b3871d5ffc_856.png)

- Для атрибута displayLarge установите значение TextStyle и заполните fontFamily, fontWeight и fontSize информацией из таблицы выше. Это означает, что весь текст, установленный в displayLarge, будет иметь шрифт Abril Fatface, нормальный вес шрифта и размер шрифта 36.sp.
Повторите этот процесс для displayMedium, labelSmall и bodyLarge.


```kt
import androidx.compose.ui.text.TextStyle
import androidx.compose.ui.unit.sp


val Typography = Typography(
   displayLarge = TextStyle(
       fontFamily = AbrilFatface,
       fontWeight = FontWeight.Normal,
       fontSize = 36.sp
   ),
   displayMedium = TextStyle(
       fontFamily = Montserrat,
       fontWeight = FontWeight.Bold,
       fontSize = 20.sp
   ),
   labelSmall = TextStyle(
       fontFamily = Montserrat,
       fontWeight = FontWeight.Bold,
       fontSize = 14.sp
   ),
   bodyLarge = TextStyle(
       fontFamily = Montserrat,
       fontWeight = FontWeight.Normal,
       fontSize = 14.sp
   )
)
```

- Если вы перейдете в файл ```Theme.kt``` в WoofTheme() и посмотрите на MaterialTheme(), параметр typography будет равен параметру Typography val, который вы только что обновили.

```kt
MaterialTheme(
   colors = colors,
   typography = Typography,
   shapes = Shapes,
   content = content
)
```

- Добавьте типографику в текст приложения

Теперь вы добавите типы заголовков к каждому экземпляру текста в приложении.

- Добавьте displayMedium в качестве стиля для имени собаки, потому что это короткий и важный фрагмент информации. Добавьте bodyLarge в качестве стиля для dogAge, потому что он хорошо работает с меньшими размерами текста.

```kt
@Composable
fun DogInformation(
   @StringRes dogName: Int,
   dogAge: Int,
   modifier: Modifier = Modifier
) {
   Column(modifier = modifier) {
       Text(
           text = stringResource(dogName),
           style = MaterialTheme.typography.displayMedium,
           modifier = Modifier.padding(top = dimensionResource(id = R.dimen.padding_small))
       )
       Text(
           text = stringResource(R.string.years_old, dogAge),
           style = MaterialTheme.typography.bodyLarge
       )
   }
}
```

Теперь в WoofPreview() имя собаки отображается жирным шрифтом Montserrat размером 20.sp, а возраст собаки - обычным шрифтом Montserrat размером 14.sp.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/c26c588948ec3253_856.png" width="400px"/>
</center>

Ниже показаны элементы списка до и после добавления типографики. Обратите внимание на разницу в шрифте между кличкой собаки и ее возрастом.


<div style="display:flex">
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/be21970ae4c0e847_856.png"/>
    </div>
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/165489157cee3532_856.png"/>
    </div>
</div>

### Добавьте верхнюю панель

**Scaffold** - это макет, который предоставляет **слоты** для различных компонентов и элементов экрана, таких как изображение, строка или столбец. В макете Scaffold также есть слот для **TopAppBar**, который вы будете использовать в этом разделе.

**TopAppBar** может использоваться для многих целей, но в данном случае вы будете использовать его для брендинга и придания индивидуальности вашему приложению. Существует четыре различных типа **TopAppBar**: центральный, маленький, средний и большой. В этом уроке вы реализуете центральную верхнюю панель приложений. Вы создадите композит, который будет выглядеть как на скриншоте ниже, и вставите его в секцию topBar скаффолда.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/172417c7b64372f7_856.png" width="400px"/>
</center>

Для этого приложения наша верхняя панель состоит из строки с изображением логотипа и текста названия приложения. На логотипе изображена милая градиентная лапа и название приложения!

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/736f411f5067e0b5_856.png" width="400px"/>
</center>

- Добавьте изображение и текст в верхнюю панель
В файле MainActivity.kt создайте компонент WoofTopAppBar() с дополнительным модификатором.


```kt
@Composable
fun WoofTopAppBar(modifier: Modifier = Modifier) {
  
}
```

**Scaffold** поддерживает параметр contentWindowInsets, с помощью которого можно указать вставки для содержимого скаффолда. **WindowInsets** - это части экрана, где ваше приложение может пересекаться с системным пользовательским интерфейсом, которые должны быть переданы в слот контента через параметры PaddingValues.

Значение contentWindowInsets передается в LazyColumn в качестве contentPadding.


```kt
@Composable
fun WoofApp() {
    Scaffold { it ->
        LazyColumn(contentPadding = it) {
            items(dogs) {
                DogItem(
                    dog = it,
                    modifier = Modifier.padding(dimensionResource(R.dimen.padding_small))
                )
            }
        }
    }
}
```

Внутри Scaffold добавьте атрибут topBar и задайте ему значение WoofTopAppBar().


```kt
Scaffold(
   topBar = {
       WoofTopAppBar()
   }
)
```

Ниже показано, как будет выглядеть композит WoofApp():

```kt
@Composable
fun WoofApp() {
    Scaffold(
        topBar = {
            WoofTopAppBar()
        }
    ) { it ->
        LazyColumn(contentPadding = it) {
            items(dogs) {
                DogItem(
                    dog = it,
                    modifier = Modifier.padding(dimensionResource(R.dimen.padding_small))
                )
            }
        }
    }
}
```

В WoofPreview() ничего не изменилось, потому что ничего нет в WoofTopAppBar(). Давайте изменим это!

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/b15d5423bc726a5e_856.png" width="400px"/>
</center>

- В составной части WoofTopAppBar() добавьте CenterAlignedTopAppBar() и установите параметр модификатора на модификатор, переданный в WoofTopAppBar().


```kt
import androidx.compose.material3.CenterAlignedTopAppBar

@Composable
fun WoofTopAppBar(modifier: Modifier = Modifier) {
   CenterAlignedTopAppBar(
       modifier = modifier
   )
}
```

- Для параметра title передайте строку Row, которая будет содержать изображение и текст CenterAlignedTopAppBar.

```kt
@Composable
fun WoofTopAppBar(modifier: Modifier = Modifier){
   CenterAlignedTopAppBar(
       title = {
           Row() {
              
           }
       },
       modifier = modifier
   )
}
```

**Добавьте изображение логотипа в строку.**

- Установите размер изображения в модификаторе как image_size в файле dimens.xml и padding как padding_small из файла dimens.xml.
С помощью painter установите изображение как ```ic_woof_logo``` из папки drawable.

- Установите contentDescription как null. В данной ситуации логотип приложения не добавляет никакой семантической информации для пользователей с ослабленным зрением, поэтому нам не нужно добавлять описание содержимого.

```kt
Row() {
   Image(
       modifier = Modifier
           .size(dimensionResource(id = R.dimen.image_size))
           .padding(dimensionResource(id = R.dimen.padding_small)),
       painter = painterResource(R.drawable.ic_woof_logo),
       contentDescription = null
   )
}
```

- Затем добавьте текстовый компонент в строку после изображения.
С помощью функции stringResource() установите для него значение ```app_name```. Это установит текст на название приложения, которое хранится в файле strings.xml.

- Установите стиль текста на displayLarge, поскольку название приложения - это короткий и важный текст.

```kt
Text(
   text = stringResource(R.string.app_name),
   style = MaterialTheme.typography.displayLarge
)
```
<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/85b82dfc6c8fc964_856.png" width="400px"/>
</center>

Вот что отображается в WoofPreview(), это выглядит немного не так, потому что иконка и текст не выровнены по вертикали.

- Чтобы исправить это, добавьте в Row значение-параметр verticalAlignment и установите его равным Alignment.CenterVertically.

```kt
import androidx.compose.ui.Alignment

Row(
   verticalAlignment = Alignment.CenterVertically
)
```

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/9cbc3aa6a315c938_856.png)

Это выглядит намного лучше!

Это полная композиция WoofTopAppBar():

```kt
@Composable
fun WoofTopAppBar(modifier: Modifier = Modifier) {
   CenterAlignedTopAppBar(
       title = {
           Row(
               verticalAlignment = Alignment.CenterVertically
           ) {
               Image(
                   modifier = Modifier
                       .size(dimensionResource(id = R.dimen.image_size))
                       .padding(dimensionResource(id = R.dimen.padding_small)),
                   painter = painterResource(R.drawable.ic_woof_logo),

                   contentDescription = null
               )
               Text(
                   text = stringResource(R.string.app_name),
                   style = MaterialTheme.typography.displayLarge
               )
           }
       },
       modifier = modifier
   )
}
```

- Запустите приложение и полюбуйтесь, как красиво TopAppBar связывает приложение воедино.

<div style="display:flex">
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/70225afc97adee46_856.png"/>
    </div>
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/8de41607e8ff2c79_856.png"/>
    </div>
</div>

А теперь посмотрите на готовое приложение в темной теме!

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-material-theming/img/2776e6a45cf3434a_856.png" width="400px"/>
</center>

### Заключение

Вы только что создали свое первое приложение Material! Вы создали пользовательскую цветовую палитру для светлой и темной тем, создали формы для различных компонентов, загрузили шрифты и добавили их в приложение, а также создали красивую верхнюю панель, чтобы связать все вместе.

### Резюме

- ```Material Theming``` позволяет вам использовать Material Design в вашем приложении, с руководством по настройке цветов, типографики и форм.
- Файл ```Theme.kt``` - это место, где задается тема, через композитную функцию [название вашего приложения]+Theme()- WoofTheme() в случае с этим приложением. В этой функции объект MaterialTheme задает цвет, типографику, формы и содержание приложения.
- В файле Color.kt перечисляются цвета, используемые в приложении. Затем в Theme.kt вы назначаете цвета в LightColorPalette и DarkColorPalette на определенные слоты. Не все слоты должны быть назначены.
- Ваше приложение может выбрать Force Dark, что означает, что система будет реализовывать темную тему для вас. Однако для пользователей будет лучше, если вы внедрите темную тему, чтобы сохранить полный контроль над темой приложения.
- Shape.kt - это место, где вы определяете формы вашего приложения. Есть три размера форм (маленькая, средняя, большая), и вы можете указать, как будут скруглены углы.
- Формы направляют внимание, идентифицируют компоненты, передают состояние и выражают бренд.
- Type.kt - это место, где вы инициализируете свои шрифты и назначаете fontFamily, fontWeight и fontSize для шкалы типов Material Design.
- Шкала типов Material Design включает в себя ряд контрастных стилей, которые соответствуют потребностям вашего приложения и его содержимого. Шкала типов представляет собой комбинацию из 15 стилей, поддерживаемых системой типов.

