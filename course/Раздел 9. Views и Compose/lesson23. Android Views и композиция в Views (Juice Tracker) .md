# Лекция 23. Android Views и композиция в Views

В этом уроке вы узнаете, как использовать представления и создавать пользовательский интерфейс Android-приложения с помощью XML. Вы также узнаете, как использовать навигацию с помощью представлений и перемещаться между различными фрагментами, которые соответствуют разным экранам.

# Создание приложения для Android с помощью Views

К настоящему времени вы узнали все о создании приложений для Android с помощью Compose. 

Compose - это очень мощный инструмент, который может упростить процесс разработки. Однако приложения для Android не всегда создавались с декларативными пользовательскими интерфейсами. Compose - это очень недавний инструмент в истории приложений для Android. Изначально пользовательские интерфейсы Android создавались с помощью представлений. Поэтому вполне вероятно, что вы столкнетесь с представлениями, когда будете продолжать свой путь разработчика Android. В этом уроке вы узнаете основы того, как создавались приложения для Android до появления Compose - с помощью XML, представлений, привязок представлений и фрагментов.

### Предварительные требования:

- Пройдите курс «Основы Android с Compose» до Главы 7.

### Что вам понадобится

- Компьютер с доступом в Интернет и Android Studio
- Устройство или эмулятор
- Стартовый код для приложения `Juice Tracker`.

### Что вы будете создавать

В этой кодовой лаборатории вы завершите работу над приложением `Juice Tracker`. Это приложение позволяет отслеживать интересные соки, создавая список, состоящий из подробных элементов. Вы добавляете и изменяете фрагменты и XML, чтобы завершить пользовательский интерфейс и начальный код. В частности, вы создаете форму ввода для создания нового вида сока, включая пользовательский интерфейс и любую связанную с ним логику или навигацию. В результате вы получаете приложение с пустым списком, в который можно добавлять собственные соки.

<div style="display:flex">
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-app-with-views/img/d6dc43171ae62047_856.png"/>
    </div>
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-app-with-views/img/87b2ca7b49e814cb_856.png"/>
    </div>
    <div>
        <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-app-with-views/img/2d630489477e216e_856.png"/>
    </div>
</div>


### Получите стартовый код

https://github.com/google-developer-training/basic-android-kotlin-compose-training-juice-tracker

Название ветки со стартовым кодом: ```views-starter```

- В Android Studio откройте папку ```basic-android-kotlin-compose-training-juice-tracker```.
- Откройте код приложения ```Juice Tracker``` в Android Studio.


### Создание макета

При создании приложения с помощью представлений вы создаете пользовательский интерфейс внутри макета. Макеты обычно объявляются с помощью XML. Эти XML-файлы макетов находятся в каталоге ресурсов в разделе ```res > layout```. Макеты содержат компоненты, из которых состоит пользовательский интерфейс; эти компоненты называются ```представлениями```. Синтаксис XML состоит из тегов, элементов и атрибутов.

В этом разделе вы создадите XML-макет для диалогового окна ввода «Тип сока», изображенного на рисунке.

<center style="margin:50px">
   <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-app-with-views/img/87b2ca7b49e814cb_856.png" width="400px">
</center>

- Создайте новый файл ресурсов макета в директории `main > res > layout` под названием `fragment_entry_dialog.`

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-app-with-views/img/331927b84e9d1a27_856.png)

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-app-with-views/img/6adb279d6e74ab13_856.png)

Макет `fragment_entry_dialog.xml` содержит компоненты пользовательского интерфейса, которые приложение отображает пользователю.

Обратите внимание, что корневой элемент - это ```ConstraintLayout```. Этот тип макета представляет собой ViewGroup, который позволяет гибко позиционировать и изменять размеры представлений с помощью ограничений. ViewGroup - это тип представления, который содержит другие представления, называемые дочерними или дочерними представлениями. Более подробно эта тема рассматривается в следующих шагах, но подробнее о ConstraintLayout вы можете узнать в разделе Построение отзывчивого пользовательского интерфейса с помощью ConstraintLayout.

После создания файла определите пространство имен приложения в ConstraintLayout.

fragment_entry_dialog.xml
```xml
<androidx.constraintlayout.widget.ConstraintLayout
   xmlns:android="http://schemas.android.com/apk/res/android"
   xmlns:app="http://schemas.android.com/apk/res-auto"
   android:layout_width="match_parent"
   android:layout_height="match_parent">
</androidx.constraintlayout.widget.ConstraintLayout>
```

- Добавьте следующие указания в `ConstraintLayout`.

fragment_entry_dialog.xml
```xml
<androidx.constraintlayout.widget.Guideline
   android:id="@+id/guideline_left"
   android:layout_width="wrap_content"
   android:layout_height="wrap_content"
   android:orientation="vertical"
   app:layout_constraintGuide_begin="16dp" />
<androidx.constraintlayout.widget.Guideline
   android:id="@+id/guideline_middle"
   android:layout_width="wrap_content"
   android:layout_height="wrap_content"
   android:orientation="vertical"
   app:layout_constraintGuide_percent="0.5" />
<androidx.constraintlayout.widget.Guideline
   android:id="@+id/guideline_top"
   android:layout_width="wrap_content"
   android:layout_height="wrap_content"
   android:orientation="horizontal"
   app:layout_constraintGuide_begin="16dp" />
```

Эти рекомендации служат в качестве дополнения к другим видам. Рекомендации ограничивают текст заголовка «Тип сока».

Создайте элемент `TextView`. Этот `TextView` представляет заголовок фрагмента детали.

<center style="margin:50px">
   <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-app-with-views/img/110cad4ae809e600_856.png" width="400px">
</center>

Задайте TextView идентификатор header_title.
Установите layout_width на 0dp. Ограничения макета в конечном итоге определяют ширину этого TextView. Поэтому определение ширины только добавляет ненужные вычисления во время отрисовки пользовательского интерфейса; определение ширины 0dp позволяет избежать лишних вычислений.
Установите для атрибута TextView text значение @string/juice_type.
Установите textAppearance на @style/TextAppearance.MaterialComponents.Headline5.

fragment_entry_dialog.xml
```xml
<TextView
   android:id="@+id/header_title"
   android:layout_width="0dp"
   android:layout_height="wrap_content"
   android:text="@string/juice_type"
   android:textAppearance="@style/TextAppearance.MaterialComponents.Headline5" />
```

Наконец, необходимо определить ограничения. В отличие от руководящих принципов, которые используют размеры в качестве ограничений, сами руководящие принципы ограничивают этот TextView. Чтобы достичь этого результата, вы можете сослаться на id руководства, по которому вы хотите ограничить представление.

Ограничьте верхнюю часть заголовка нижней частью guideline_top.

fragment_entry_dialog.xml
```xml
<TextView
   android:id="@+id/header_title"
   android:layout_width="0dp"
   android:layout_height="wrap_content"
   android:text="@string/juice_type"
   android:textAppearance="@style/TextAppearance.MaterialComponents.Headline5"
   app:layout_constraintTop_toBottomOf="@+id/guideline_top" />
```

Ограничьте конец до начала guideline_middle и начало до начала guideline_left, чтобы завершить размещение TextView. Имейте в виду, что то, как вы ограничиваете тот или иной вид, полностью зависит от того, как вы хотите, чтобы выглядел ваш пользовательский интерфейс.

fragment_entry_dialog.xml
```xml
<TextView
   android:id="@+id/header_title"
   android:layout_width="0dp"
   android:layout_height="wrap_content"
   android:text="@string/juice_type"
   android:textAppearance="@style/TextAppearance.MaterialComponents.Headline5"
   app:layout_constraintTop_toBottomOf="@+id/guideline_top"
   app:layout_constraintEnd_toStartOf="@+id/guideline_middle"
   app:layout_constraintStart_toStartOf="@+id/guideline_left" />
```

Try to build the rest of the UI based on the screenshots. You can find the completed fragment_entry_dialog.xml file in the <a href=«https://github.com/google-developer-training/basic-android-kotlin-compose-training-juice-tracker/tree/views»>solution</a>.

# 4. Create a Fragment with Views
In Compose, you build layouts declaratively using Kotlin or Java. You can access different «screens» by navigating to different Composables, typically within the same activity. When building an app with Views, a Fragment that hosts the XML layout replaces the concept of a Composable «screen.»

In this section, you create a Fragment to host the fragment_entry_dialog layout and provide data to the UI.

In the juicetracker package, create a new class called EntryDialogFragment.
Make the EntryDialogFragment extend the BottomSheetDialogFragment.

EntryDialogFragment.kt
```kt
import com.google.android.material.bottomsheet.BottomSheetDialogFragment


class EntryDialogFragment : BottomSheetDialogFragment() {
}
```

DialogFragment - это фрагмент, который отображает плавающий диалог. BottomSheetDialogFragment наследует класс DialogFragment, но отображает лист шириной с экран, прикрепленный к нижней части экрана. Такой подход соответствует дизайну, изображенному ранее.

Пересоберите проект, в результате чего будут автоматически сгенерированы файлы привязки представлений, основанные на макете fragment_entry_dialog. Привязки представлений позволяют вам получать доступ и взаимодействовать с представлениями, объявленными в XML, подробнее о них вы можете прочитать в документации по привязкам представлений.
В классе EntryDialogFragment реализуйте функцию onCreateView(). Как следует из названия, эта функция создает представление для данного фрагмента.

> Примечание: Как и активность, фрагмент также имеет различные состояния жизненного цикла и соответствующие методы жизненного цикла.

EntryDialogFragment.kt
```kt
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup

override fun onCreateView(
   inflater: LayoutInflater,
   container: ViewGroup?,
   savedInstanceState: Bundle?
): View? {
   return super.onCreateView(inflater, container, savedInstanceState)
}
```

Функция onCreateView() возвращает представление, но сейчас она не возвращает полезное представление.

Вместо возврата функции super.onCreateView() верните представление, созданное при раздувании FragmentEntryDialogViewBinding.

EntryDialogFragment.kt
```kt
import com.example.juicetracker.databinding.FragmentEntryDialogBinding


override fun onCreateView(
   inflater: LayoutInflater,
   container: ViewGroup?,
   savedInstanceState: Bundle?
): View? {
   return FragmentEntryDialogBinding.inflate(inflater, container, false).root
}
```

Вне функции onCreateView(), но внутри класса EntryDialogFragment, создайте экземпляр EntryViewModel.
Реализуйте функцию onViewCreated().
После раздувания привязки представлений вы можете получать доступ к представлениям в макете и изменять их. Метод onViewCreated() вызывается после onCreateView() в жизненном цикле. Метод onViewCreated() - это рекомендуемое место для доступа и изменения представлений в макете.

Создайте экземпляр привязки представления, вызвав метод bind() на FragmentEntryDialogBinding.
На этом этапе ваш код должен выглядеть так, как показано в следующем примере:

EntryDialogFragment.kt
```kt
import androidx.fragment.app.viewModels
import com.example.juicetracker.ui.AppViewModelProvider
import com.example.juicetracker.ui.EntryViewModel

class EntryDialogFragment : BottomSheetDialogFragment() {

   private val entryViewModel by viewModels<EntryViewModel> { AppViewModelProvider.Factory }

   override fun onCreateView(
       inflater: LayoutInflater,
       container: ViewGroup?,
       savedInstanceState: Bundle?
   ): View {
       return FragmentEntryDialogBinding.inflate(inflater, container, false).root
   }

   override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val binding = FragmentEntryDialogBinding.bind(view)
    }
}
```

Вы можете получать доступ к представлениям и устанавливать их через привязку. Например, вы можете установить TextView с помощью метода setText().

```kt
binding.name.setText("Apple juice")
```

> Примечание: Использование жестко закодированной строки «Apple juice» в приведенном выше примере было сделано для простоты. В производстве следует использовать строковые ресурсы.

Диалоговый пользовательский интерфейс служит местом, где пользователь может создать новый элемент, но его также можно использовать для изменения существующего элемента. Поэтому фрагмент должен получать нажатый элемент. Навигационный компонент облегчает переход к фрагменту EntryDialogFragment и получение щелкнутого элемента.

Фрагмент EntryDialogFragment еще не завершен, но не волнуйтесь! А пока переходите к следующему разделу, чтобы узнать больше об использовании компонента навигации в приложении с Views.

> 5. Модификация компонента навигации
В этом разделе вы используете компонент навигации для запуска диалога ввода и извлечения элемента, если это необходимо.

Compose дает возможность визуализировать различные компоненты, просто вызывая их. Однако фрагменты работают по-другому. Навигационный компонент координирует «пункты назначения» фрагментов, обеспечивая простой способ перемещения между различными фрагментами и содержащимися в них представлениями.

Используйте компонент Navigation, чтобы скоординировать навигацию к фрагменту EntryDialogFragment.

Откройте файл nav_graph.xml и убедитесь, что выбрана вкладка Design.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-app-with-views/img/783cb5d7ff0ba127_856.png){style="width:400px"}

Нажмите на значок 93401bf098936c15.png, чтобы добавить новый пункт назначения.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-app-with-views/img/d5410c90e408b973_856.png){style="width:400px"}

Выберите пункт назначения EntryDialogFragment. Это действие объявляет фрагмент EntryDialogFragment в навигационном графе, делая его доступным для действий навигации.

<center style="margin:50px">
   <img src="https://developer.android.com/static/codelabs/basic-android-kotlin-compose-app-with-views/img/418feed425072ea4_856.png" width="400px">
</center>

> Примечание: Экран entryDialogFragment может появиться в случайном месте на экране nav_graph.xml. Вы можете перетаскивать места назначения, чтобы сделать отображение более организованным.

Необходимо запустить фрагмент EntryDialogFragment из фрагмента TrackerFragment. Поэтому для выполнения этой задачи необходимо выполнить навигационное действие.

Перетащите курсор на фрагмент TrackerFragment. Выберите серую точку и перетащите линию к фрагменту EntryDialogFragment.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-app-with-views/img/85decb6fcddec713_856.png){style="width:400px"}


В представлении дизайна nav_graph можно объявить аргументы для пункта назначения, выбрав его и щелкнув значок a0d73140a20e4348.png рядом с выпадающим списком Arguments. Используйте эту функцию, чтобы добавить аргумент itemId типа Long к фрагменту entryDialogFragment; значение по умолчанию должно быть 0L.

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-app-with-views/img/555cf791f64f62b8_856.png){style=«width:400px»}

![](https://developer.android.com/static/codelabs/basic-android-kotlin-compose-app-with-views/img/840105bd52f300f7_856.png){style=«width:400px»}

Обратите внимание, что фрагмент TrackerFragment содержит список элементов Juice - при нажатии на один из этих элементов запускается фрагмент EntryDialogFragment.

Пересоберите проект. Аргумент itemId теперь доступен в EntryDialogFragment.


# 6. Завершите фрагмент
Используя данные из аргументов навигации, завершите диалог ввода.

Получите navArgs() в методе onViewCreated() фрагмента EntryDialogFragment.
Извлеките itemId из navArgs().
Реализуйте кнопку saveButton для сохранения нового/измененного сока с помощью ViewModel.
Вспомните из пользовательского интерфейса диалога ввода, что значение цвета по умолчанию - красный. Пока передайте это значение в качестве держателя.

При вызове saveJuice() передайте id элемента из args.

EntryDialogFragment.kt
```kt
import androidx.navigation.fragment.navArgs
import com.example.juicetracker.data.JuiceColor


class EntryDialogFragment : BottomSheetDialogFragment() {

   //...
   var selectedColor: JuiceColor = JuiceColor.Red

   override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val binding = FragmentEntryDialogBinding.bind(view)
        val args: EntryDialogFragmentArgs by navArgs()
        val juiceId = args.itemId

        binding.saveButton.setOnClickListener {
           entryViewModel.saveJuice(
               juiceId,
               binding.name.text.toString(),
               binding.description.text.toString(),
               selectedColor.name,
               binding.ratingBar.rating.toInt()
           )
        }
    }
}
```

После сохранения данных завершите диалог методом dismiss().
EntryDialogFragment.kt
```kt
class EntryDialogFragment : BottomSheetDialogFragment() {

    //...
    var selectedColor: JuiceColor = JuiceColor.Red
    //...

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val binding = FragmentEntryDialogBinding.bind(view)
        val args: EntryDialogFragmentArgs by navArgs()
        binding.saveButton.setOnClickListener {
           entryViewModel.saveJuice(
               juiceId,
               binding.name.text.toString(),
               binding.description.text.toString(),
               selectedColor.name,
               binding.ratingBar.rating.toInt()
           )
           dismiss()
        }
    }
}
```

Помните, что приведенный выше код не завершает фрагмент EntryDialogFragment. Вам еще нужно реализовать ряд вещей, таких как заполнение полей существующими данными Juice (если применимо), выбор цвета из colorSpinner, реализация кнопки отмены и многое другое. Однако этот код не является уникальным для Fragments, и вы можете реализовать его самостоятельно. Попробуйте реализовать остальную функциональность. В крайнем случае, вы можете обратиться к коду решения для этого коделаба.


# 7. Запуск диалога ввода
Последняя задача - запустить диалог входа с помощью компонента навигации. Диалог входа должен запускаться, когда пользователь нажимает плавающую кнопку действия (FAB). Он также должен запускаться и передавать соответствующий id, когда пользователь нажимает на элемент.

В onClickListener() для FAB вызовите navigate() на контроллере nav.

TrackerFragment.kt
```kt
import androidx.navigation.findNavController


//...

binding.fab.setOnClickListener { fabView ->
   fabView.findNavController().navigate(
   )
}

//...
```

В функции navigate передайте действие для перехода от трекера к диалогу входа.
TrackerFragment.kt

```kt
//...

binding.fab.setOnClickListener { fabView ->
   fabView.findNavController().navigate(
TrackerFragmentDirections.actionTrackerFragmentToEntryDialogFragment()
   )
}

//...
```

Повторите это действие в теле лямбды для метода onEdit() в JuiceListAdapter, но на этот раз передайте id сока.
TrackerFragment.kt

```kt
//...

onEdit = { drink ->
   findNavController().navigate(
       TrackerFragmentDirections.actionTrackerFragmentToEntryDialogFragment(drink.id)
   )
},

//...
```

# Получение кода решения
Чтобы загрузить код готового урока, вы можете воспользоваться этими командами git:

```
$ git clone https://github.com/google-developer-training/basic-android-kotlin-compose-training-juice-tracker.git
$ cd basic-android-kotlin-compose-training-juice-tracker
$ git checkout views
```