# Лекция 19. Простая анимация с помощью Jetpack Compose

В уроке вы узнаете, как добавить простую анимацию в приложение для Android. Анимация может сделать ваше приложение более интерактивным, интересным и легким для восприятия пользователями. Анимация отдельных обновлений на экране, заполненном информацией, поможет пользователю увидеть, что изменилось.

Существует множество типов анимации, которые можно использовать в пользовательском интерфейсе приложения. Элементы могут появляться и исчезать, перемещаться по экрану или за его пределы, а также интересно трансформироваться. Это помогает сделать пользовательский интерфейс приложения выразительным и удобным в использовании.

Анимация также может придать вашему приложению полированный вид, что делает его элегантным и одновременно помогает пользователю.

### Необходимые условия

- Знание Kotlin, включая функции, лямбды и stateless composables.
- Базовые знания о том, как создавать макеты в Jetpack Compose.
- Базовые знания о том, как создавать списки в Jetpack Compose.
- Базовые знания о Material Design.

### Что вы узнаете

- Как создать простую анимацию с помощью Jetpack Compose.

### Что вы будете создавать

- Вы создадите приложение ```Woof``` из практической работы по Material Theming with Jetpack Compose и добавите простую анимацию, подтверждающую действие пользователя.

### Что вам понадобится

- Последняя стабильная версия Android Studio.
- Подключение к локальному серверу ```gogc``` для загрузки стартового кода.

### Обзор приложения

В практической работе Material Theming with Jetpack Compose вы создали приложение `Woof` с использованием Material Design, которое отображает список собак и информацию о них.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/36c6cabd93421a92_856.png" width=""/>
</center>

В этом уроке вы добавите анимацию в приложение Woof. Вы добавите информацию о хобби, которая будет отображаться при раскрытии элемента списка. Вы также добавите весеннюю анимацию, чтобы анимировать разворачивающийся элемент списка.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/c0d0a52463332875.gif" width="400px"/>
</center>

### Добавьте иконку Expand More

В этом разделе вы добавите иконки ```Expand More``` и ```Expand Less``` в ваше приложение.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/def59d71015c0fbe_856.png" width="400px"/>
</center>

### Иконки

Значки - это символы, которые помогают пользователям понять интерфейс, визуально передавая его назначение. Они часто черпают вдохновение в объектах физического мира, с которыми, как ожидается, сталкивался пользователь. При разработке иконок уровень детализации часто снижается до минимума, необходимого для того, чтобы быть знакомым пользователю. Например, карандаш в физическом мире используется для письма, поэтому его иконка обычно обозначает «создать» или «редактировать».


<div style="display:flex;">
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/1c71e91aa04d3837_856.jpeg"/>
    </div>
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/b718af58f961d2b4_856.png"/>
    </div>
</div>

Material Design предлагает множество иконок, распределенных по общим категориям, для большинства ваших нужд.

<center style="margin:50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/254688426772346f_856.png" width="400px"/>
</center>

## Добавьте зависимость Gradle

Добавьте зависимость библиотеки ```material-icons-extended``` в ваш проект. Вы будете использовать иконки ```Icons.Filled.ExpandLess``` и ```Icons.Filled.ExpandMore``` из этой библиотеки.

> Примечание о зависимостях Gradle: Чтобы добавить зависимость в свой проект, укажите конфигурацию зависимости, такую как implementation, в блоке dependencies файла ```build.gradle.kts``` вашего модуля. Когда вы собираете свое приложение, система сборки компилирует библиотечный модуль и упаковывает полученное скомпилированное содержимое в приложение.

На панели ```Project``` откройте ```Gradle Scripts > build.gradle.kts (Module :app)```.

Прокрутите до конца файл ```build.gradle.kts``` (Модуль :app). В блоке dependencies{} добавьте следующую строку:

```
implementation("androidx.compose.material:material-icons-extended")
```

> Совет: Когда вы изменяете файлы Gradle, Android Studio может потребоваться импортировать или обновить библиотеки и запустить некоторые фоновые задачи. Android Studio отображает всплывающее окно с предложением синхронизировать проект. Нажмите ```Sync Now```.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/772f8f274e7d3f44_856.png)

### Добавьте композитную иконку

Добавьте функцию для отображения иконки ```Expand More``` из библиотеки иконок Material и используйте ее в качестве кнопки.

- В файле ```MainActivity.kt``` после функции DogItem() создайте новую композитную функцию DogItemButton().
Передайте в нее булево значение для расширенного состояния, лямбда-выражение для обработчика кнопки onClick и необязательный модификатор следующим образом:


```kt
@Composable
private fun DogItemButton(
   expanded: Boolean,
   onClick: () -> Unit,
   modifier: Modifier = Modifier
) {
 

}
```

- Внутри функции DogItemButton() добавьте составную IconButton(), которая принимает именованный параметр onClick, лямбду с использованием синтаксиса trailing lambda, которая вызывается при нажатии на эту иконку, и необязательный модификатор. Установите значения параметров IconButton onClick и модификатора равными тем, которые были переданы в DogItemButton.


```kt
@Composable
private fun DogItemButton(
   expanded: Boolean,
   onClick: () -> Unit,
   modifier: Modifier = Modifier
){
   IconButton(
       onClick = onClick,
       modifier = modifier
   ) {

   }
}
```

- Внутри лямбда-блока IconButton() добавьте композитный Icon и установите значение-параметр imageVector в Icons.Filled.ExpandMore. Android Studio выдает предупреждение о параметрах составного Icon(), которое вы исправите в следующем шаге.

```kt
import androidx.compose.material.icons.filled.ExpandMore
import androidx.compose.material.icons.Icons
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton

IconButton(
   onClick = onClick,
   modifier = modifier
) {
   Icon(
       imageVector = Icons.Filled.ExpandMore
   )
}
```

- Добавьте параметр значения tint и установите цвет иконки на MaterialTheme.colorScheme.secondary. - Добавьте именованный параметр contentDescription и установите его в строковый ресурс R.string.expand_button_content_description.


```kt
IconButton(
   onClick = onClick,
   modifier = modifier
){
   Icon(
       imageVector = Icons.Filled.ExpandMore,
       contentDescription = stringResource(R.string.expand_button_content_description),
       tint = MaterialTheme.colorScheme.secondary
   )
}
```

### Отображение иконки

- Отобразите композит DogItemButton(), добавив его в макет.

- В начале функции DogItem() добавьте переменную для сохранения развернутого состояния элемента списка.
- Установите начальное значение false.

```kt
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue

var expanded by remember { mutableStateOf(false) }
```

> Освежите в памяти функции ```remember()``` и ```mutableStateOf()```:
Используйте функцию mutableStateOf(), чтобы Compose наблюдал за любыми изменениями значения состояния и запускал рекомпозицию для обновления пользовательского интерфейса. 

- Оберните вызов функции mutableStateOf() функцией remember(), чтобы сохранить значение в Composition при начальной композиции, а сохраненное значение вернуть при рекомпозиции.

### Отображение кнопки с иконкой внутри элемента списка.

- В композиции DogItem() в конце блока Row, после вызова DogInformation(), добавьте DogItemButton(). 

- Передайте в нее расширенное состояние и пустую лямбду для обратного вызова. Вы определите действие onClick на следующем шаге.

```kt
Row(
   modifier = Modifier
       .fillMaxWidth()
       .padding(dimensionResource(R.dimen.padding_small))
) {
   DogIcon(dog.imageResourceId)
   DogInformation(dog.name, dog.age)
   DogItemButton(
       expanded = expanded,
       onClick = { /*TODO*/ }
   )
}
```

- Проверьте функцию WoofPreview() в панели Design.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/5bbf09cd2828b6_856.png" width="400"/>
</center>

- Обратите внимание, что кнопка «Развернуть еще» не выровнена по концу элемента списка. Вы исправите это в следующем шаге.

### Выравнивание кнопки «Развернуть

Чтобы выровнять кнопку «Развернуть» по концу элемента списка, нужно добавить в макет разделитель с атрибутом Modifier.weight().

> Примечание: ```Modifier.weight()``` устанавливает ширину/высоту элемента пользовательского интерфейса пропорционально его весу, относительно его взвешенных братьев и сестер (других дочерних элементов в строке или столбце).

> Пример: Рассмотрим три дочерних элемента в строке с весами 1f, 1f и 2f. В этом случае все дочерние элементы имеют назначенные веса. Свободное место в строке распределяется пропорционально указанному значению веса, при этом больше свободного места достается дочерним элементам с большим значением веса. Дочерние элементы распределят вес, как показано ниже:
![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/197842fd06abf239_856.png)
В приведенном выше ряду первый дочерний компонуемый элемент имеет ¼ ширины ряда, второй также имеет ¼ ширины ряда, а третий - ½ ширины ряда.
Если у дочерних элементов нет назначенных весов (weight - необязательный параметр), то высота/ширина дочернего композитного элемента по умолчанию будет соответствовать параметру wrap content (обертывание содержимого того, что находится внутри элемента пользовательского интерфейса).

> Примечание о float значениях: float значения в Kotlin - это десятичные числа, обозначаемые буквой f или F в конце числа.

В приложении ```Woof``` каждая строка списка содержит изображение собаки, информацию о ней и кнопку «Развернуть». Чтобы правильно выровнять значок кнопки, перед кнопкой «Развернуть еще» добавляется композит Spacer с весом ```1f```. Поскольку padding является единственным взвешенным дочерним элементом в строке, она заполнит пространство, оставшееся в строке после измерения ширины других невзвешенных дочерних элементов.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/733f6d9ef2939ab5_856.png)

- Добавьте разделитель в строку элемента списка
В DogItem(), между DogInformation() и DogItemButton(), добавьте спейсер. Передайте модификатор с весом(1f). Модификатор.weight() заставляет спейсер заполнить пространство, оставшееся в строке.

```kt
import androidx.compose.foundation.layout.Spacer

Row(
   modifier = Modifier
       .fillMaxWidth()
       .padding(dimensionResource(R.dimen.padding_small))
) {
   DogIcon(dog.imageResourceId)
   DogInformation(dog.name, dog.age)
   Spacer(modifier = Modifier.weight(1f))
   DogItemButton(
       expanded = expanded,
       onClick = { /*TODO*/ }
   )
}
```

- Проверьте функцию ```WoofPreview()``` в панели Design. Обратите внимание, что кнопка «Развернуть еще» теперь выровнена по концу элемента списка.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/8df42b9d85a5dbaa_856.png" width="400"/>
</center>

### Добавьте композит для отображения хобби

В этом задании вы добавите Text composables для отображения информации о хобби собаки.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/bba8146c6332cc37_856.png)

- Создайте новую составную функцию DogHobby(), которая принимает строковый идентификатор ресурса «Хобби» собаки и необязательный модификатор.

```kt
@Composable
fun DogHobby(
   @StringRes dogHobby: Int,
   modifier: Modifier = Modifier
) {
}
```

- Внутри функции DogHobby() создайте столбец и передайте в него модификатор, переданный в DogHobby().

```kt
@Composable
fun DogHobby(
   @StringRes dogHobby: Int,
   modifier: Modifier = Modifier
){
   Column(
       modifier = modifier
   ) { 

   }
}
```

- Внутри блока Column добавьте два составных элемента Text - один для отображения текста About над информацией о хобби, а другой - для отображения информации о хобби.

- Установите для первого из них текст about из файла strings.xml и задайте стиль labelSmall. Для второго установите текст dogHobby, который передается в файл, и установите стиль bodyLarge.

```kt
Column(
   modifier = modifier
) {
   Text(
       text = stringResource(R.string.about),
       style = MaterialTheme.typography.labelSmall
   )
   Text(
       text = stringResource(dogHobby),
       style = MaterialTheme.typography.bodyLarge
   )
}
```

- В DogItem() составной элемент DogHobby() будет располагаться ниже строки, содержащей DogIcon(), DogInformation(), Spacer() и DogItemButton(). Для этого оберните Строку столбцом, чтобы хобби можно было добавить под Строкой.


```kt
Column() {
   Row(
       modifier = Modifier
           .fillMaxWidth()
           .padding(dimensionResource(R.dimen.padding_small))
   ) {
       DogIcon(dog.imageResourceId)
       DogInformation(dog.name, dog.age)
       Spacer(modifier = Modifier.weight(1f))
       DogItemButton(
           expanded = expanded,
           onClick = { /*TODO*/ }
       )
   }
}
```

- Добавьте DogHobby() после Row в качестве второго дочернего элемента Column. Передайте dog.hobbies, который содержит уникальное хобби переданной собаки и модификатор с паддингом для композита DogHobby().

```kt
Column() {
   Row() {
      ...
   }
   DogHobby(
       dog.hobbies,
       modifier = Modifier.padding(
           start = dimensionResource(R.dimen.padding_medium),
           top = dimensionResource(R.dimen.padding_small),
           end = dimensionResource(R.dimen.padding_medium),
           bottom = dimensionResource(R.dimen.padding_medium)
       )
   )
}
```

<div style="    
    margin-bottom: 1rem;
    padding: 1rem;
    border-left: 5px solid green;
    width: auto;
    background-color: white;">

<strong style="color:green">Заметка: </strong> о собачьих увлечениях: Информация о собачьих увлечениях для всех собак уже предоставлена вам как часть стартового кода. Чтобы увидеть это в своем коде, откройте файл data/Dog.kt, обратите внимание на список собак, предварительно заполненный информацией о них.
</div>

Полная функция DogItem() должна выглядеть следующим образом:

```kt
@Composable
fun DogItem(
   dog: Dog,
   modifier: Modifier = Modifier
) {
   var expanded by remember { mutableStateOf(false) }
   Card(
       modifier = modifier
   ) {
       Column() {
           Row(
               modifier = Modifier
                   .fillMaxWidth()
                   .padding(dimensionResource(R.dimen.padding_small))
           ) {
               DogIcon(dog.imageResourceId)
               DogInformation(dog.name, dog.age)
               Spacer(Modifier.weight(1f))
               DogItemButton(
                   expanded = expanded,
                   onClick = { /*TODO*/ },
               )
           }
           DogHobby(
               dog.hobbies, 
               modifier = Modifier.padding(
                   start = dimensionResource(R.dimen.padding_medium),
                   top = dimensionResource(R.dimen.padding_small),
                   end = dimensionResource(R.dimen.padding_medium),
                   bottom = dimensionResource(R.dimen.padding_medium)
               )
           )
       }
   }
}
```

- Посмотрите на функцию WoofPreview() в панели Design. Обратите внимание на отображение хобби собаки.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/2704a4ef191ef458_856.png" width=""/>
</center>

### Показывать или скрывать хобби по нажатию кнопки

В вашем приложении есть кнопка «Развернуть больше» для каждого элемента списка, но она еще ничего не делает! В этом разделе вы добавите возможность скрывать или раскрывать информацию о хобби, когда пользователь нажимает на кнопку «Развернуть больше».

- В составной функции DogItem(), в вызове функции DogItemButton(), определите лямбда-выражение onClick(), измените значение состояния expanded boolean на true, когда кнопка нажата, и измените его обратно на false, если кнопка нажата снова.

```kt
DogItemButton(
   expanded = expanded,
   onClick = { expanded = !expanded }
)
```

> Примечание: Логический оператор NOT ( ! ) возвращает отрицаемое значение булева выражения.
Например, если expanded равно true, то !expanded будет равно false.

- В функции DogItem() оберните вызов функции DogHobby() проверкой if для расширенного булева выражения.

```kt
@Composable
fun DogItem(
   dog: Dog,
   modifier: Modifier = Modifier
) {
   var expanded by remember { mutableStateOf(false) }
   Card(
       ...
   ) {
       Column(
           ...
       ) {
           Row(
               ...
           ) {
               ...
           }
           if (expanded) {
               DogHobby(
                   dog.hobbies, modifier = Modifier.padding(
                       start = dimensionResource(R.dimen.padding_medium),
                       top = dimensionResource(R.dimen.padding_small),
                       end = dimensionResource(R.dimen.padding_medium),
                       bottom = dimensionResource(R.dimen.padding_medium)
                   )
               )
           }
       }
   }
}
```

- Теперь информация о хобби собаки отображается только в том случае, если значение параметра expanded равно true.

Предварительный просмотр может показать вам, как выглядит пользовательский интерфейс, но вы также можете взаимодействовать с ним. Чтобы взаимодействовать с предварительным просмотром пользовательского интерфейса, наведите курсор на текст ```WoofPreview``` в панели дизайна, а затем нажмите кнопку Интерактивный режим в правом верхнем углу панели дизайна. Это запустит предварительный просмотр в интерактивном режиме.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/74e1624d68fb4131_856.png)

Взаимодействуйте с предварительным просмотром, нажав кнопку «Развернуть еще». Обратите внимание, что информация о хобби собаки скрывается и раскрывается, когда вы нажимаете кнопку «Развернуть».

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/e4c793196993a9ae.gif)

> Примечание: Чтобы остановить интерактивный режим, нажмите кнопку Остановить интерактивный режим в левом верхнем углу панели предварительного просмотра.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/60829fbffe4d8302_856.png)

Обратите внимание, что значок кнопки «Развернуть больше» остается неизменным, когда элемент списка развернут. Для улучшения пользовательского опыта вы измените значок так, чтобы ```ExpandMore``` отображала стрелку вниз, а ExpandLess - стрелку вверх.

- В функции DogItemButton() добавьте оператор if, который обновляет значение imageVector на основе расширенного состояния следующим образом:

```kt
import androidx.compose.material.icons.filled.ExpandLess

@Composable
private fun DogItemButton(
   ...
) {
   IconButton(onClick = onClick) {
       Icon(
           imageVector = if (expanded) Icons.Filled.ExpandLess else Icons.Filled.ExpandMore,
           ...
       )
   }
}
```

Обратите внимание, как вы написали if-else в предыдущем фрагменте кода.

```kt
if (expanded) Icons.Filled.ExpandLess else Icons.Filled.ExpandMore
```

Это то же самое, что и использование фигурных скобок { } в следующем коде:

```kt
if (expanded) {
`Icons.Filled.ExpandLess`
} else {
`Icons.Filled.ExpandMore`
}
```

Фигурные скобки необязательны, если оператор if-else состоит из одной строки кода.

- Запустите приложение на устройстве или в эмуляторе, или снова используйте интерактивный режим в предварительном просмотре. Обратите внимание, что значок чередуется между значками ```ExpandMore``` и ```ExpandLess```.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/de5dc4a953f11e65.gif" width="400"/>
</center>

> Примечание об интерактивном режиме: Интерактивный режим позволяет вам взаимодействовать с предварительным просмотром так же, как вы взаимодействовали бы на устройстве. Однако режим предварительного просмотра не заменяет запуск приложения на устройстве для тестирования.

Когда вы развернули элемент списка, заметили ли вы резкое изменение высоты? Резкое изменение высоты не похоже на отполированное приложение. Чтобы решить эту проблему, вы добавите в приложение анимацию.

### Добавьте анимацию

Анимации могут добавлять визуальные подсказки, которые уведомляют пользователей о том, что происходит в вашем приложении. Они особенно полезны, когда пользовательский интерфейс меняет состояние, например, когда загружается новый контент или становятся доступны новые действия. Анимации также могут придать приложению полированный вид.

В этом разделе вы добавите анимацию для изменения высоты элемента списка.

### Пружинная анимация

Пружинная анимация - это анимация, основанная на физике, которая управляется силой пружины. При пружинной анимации величина и скорость движения рассчитываются в зависимости от приложенной силы пружины.

Например, если вы перетащите значок приложения по экрану, а затем отпустите его, подняв палец, значок под действием невидимой силы переместится в исходное положение.

Следующая анимация демонстрирует эффект пружины. Как только палец отпускается от значка, значок отпрыгивает назад, имитируя пружину.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/af35a9d327d1cab0.gif" width="400"/>
</center>

### Spring effect

Сила пружины определяется двумя следующими свойствами:

- Коэффициент демпфирования: Отказоустойчивость пружины.
- Уровень жесткости: Жесткость пружины, то есть то, насколько быстро пружина движется к концу.

Ниже приведено несколько примеров анимации
 <a href="https://developer.android.com/reference/kotlin/androidx/compose/animation/core/Spring">
 различные коэффициенты демпфирования и уровни жесткости
</a>.

<div style="dispay:flex">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/d8e850d6eeec30a5.gif"/>
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/32eac117de778099.gif"/>
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/7ba20cf822ecb900.gif"/>
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/710c9cad92e2d7ad.gif"/>
</div>

- Посмотрите на вызов функции DogHobby() в композитной функции DogItem(). Информация о хобби собаки включается в композицию, основываясь на расширенном булевом значении. Высота элемента списка меняется в зависимости от того, видна или скрыта информация о хобби. В настоящее время переход осуществляется нечетко. В этом разделе вы воспользуетесь модификатором animateContentSize, чтобы добавить более плавный переход между расширенным и нерасширенным состояниями.


```kt
// No need to copy over
@Composable
fun DogItem(...) {
  ...
    if (expanded) {
       DogHobby(
          dog.hobbies, 
          modifier = Modifier.padding(
              start = dimensionResource(R.dimen.padding_medium),
              top = dimensionResource(R.dimen.padding_small),
              end = dimensionResource(R.dimen.padding_medium),
              bottom = dimensionResource(R.dimen.padding_medium)
          )
      )
   }
}
```

В файле MainActivity.kt в функции DogItem() добавьте параметр-модификатор для макета Column.

```kt
@Composable
fun DogItem(
   dog: Dog, 
   modifier: Modifier = Modifier
) {
   ...
   Card(
       ...
   ) {
       Column(
          modifier = Modifier
       ){
           ...
       }
   }
}
```

- Cцепите этот модификатор с модификатором animateContentSize, чтобы анимировать изменение размера (высоты элемента списка).


```kt
import androidx.compose.animation.animateContentSize

Column(
   modifier = Modifier
       .animateContentSize()
)
```

В текущей реализации вы анимируете высоту элементов списка в своем приложении. Но анимация настолько тонкая, что ее трудно заметить при запуске приложения. Чтобы решить эту проблему, используйте дополнительный параметр animationSpec, который позволит вам настроить анимацию.

- Для ```Woof``` анимация плавно приближается и удаляется без скачков. Чтобы добиться этого, добавьте параметр animationSpec в вызов функции animateContentSize(). Установите для анимации пружину с параметром DampingRatioNoBouncy, чтобы не было отскока, и параметр StiffnessMedium, чтобы сделать пружину немного жестче.


```kt
import androidx.compose.animation.core.Spring
import androidx.compose.animation.core.spring

Column(
   modifier = Modifier
       .animateContentSize(
           animationSpec = spring(
               dampingRatio = Spring.DampingRatioNoBouncy,
               stiffness = Spring.StiffnessMedium
           )
       )
)
```

- Проверьте функцию WoofPreview() в панели Design и воспользуйтесь интерактивным режимом или запустите приложение на эмуляторе или устройстве, чтобы увидеть  анимацию в действии.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/c0d0a52463332875.gif" width="400"/>
</center>

# 7. (Необязательно) Поэкспериментируйте с другими анимациями

### animate*AsState

- Функции animate*AsState() - это один из самых простых API анимации в Compose для анимации одного значения. Вы указываете только конечное значение (или целевое значение), и API запускает анимацию от текущего значения до указанного конечного значения.

Compose предоставляет функции animate*AsState() для Float, Color, Dp, Size, Offset и Int, и это лишь некоторые из них. Вы можете легко добавить поддержку других типов данных с помощью функции animateValueAsState(), которая принимает общий тип.

Попробуйте использовать функцию animateColorAsState() для изменения цвета при раскрытии элемента списка.

В функции DogItem() объявите цвет и делегируйте его инициализацию функции animateColorAsState().

```kt
import androidx.compose.animation.animateColorAsState

@Composable
fun DogItem(
   dog: Dog,
   modifier: Modifier = Modifier
) {
   var expanded by remember { mutableStateOf(false) }
   val color by animateColorAsState()
   ...
}
```

- Установите именованный параметр targetValue в зависимости от расширенного булевого значения. Если элемент списка расширен, установите для него третичный цветContainer. В противном случае установите для него цвет primaryContainer.

```kt
import androidx.compose.animation.animateColorAsState

@Composable
fun DogItem(
   dog: Dog,
   modifier: Modifier = Modifier
) {
   var expanded by remember { mutableStateOf(false) }
   val color by animateColorAsState(
       targetValue = if (expanded) MaterialTheme.colorScheme.tertiaryContainer
       else MaterialTheme.colorScheme.primaryContainer,
   )
   ...
}
```

- Установите цвет в качестве модификатора фона для столбца.

```kt
@Composable
fun DogItem(
   dog: Dog, 
   modifier: Modifier = Modifier
) {
   ...
   Card(
       ...
   ) {
       Column(
           modifier = Modifier
               .animateContentSize(
                   ...
                   )
               )
               .background(color = color)
       ) {...}
}
```

- Посмотрите, как меняется цвет при расширении элемента списка. Элементы списка без расширения имеют цвет primaryContainer, а элементы списка с расширением - цвет tertiaryContainer.

<center style="margin: 50px">
    <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-woof-animation/img/b45e86eb53fd7d88_856.png" width="400"/>
</center>

### Заключение

Вы добавили кнопку для скрытия и раскрытия информации о собаке. Вы улучшили пользовательский опыт с помощью анимации. Вы также узнали, как использовать интерактивный режим в панели дизайна.
Вы также можете попробовать другой тип анимации Jetpack Compose.

