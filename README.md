# Program Capli
## Описание
Данная программа реализует детекцию капель, расположенных на стекле, и вычисляет общую площадь, занимаемую каплями.  

## Установка
Проект собран в один файл запуска. Для работы вам нужно:  
>Скачать файл "capli.exe"  
>Запустить файл "capli.exe"  
## Инструкция
Для загрузки изображения:  
  >В строке меню выбрать "Файл" и выбрать "Открыть"  

При открытии изображения к нему применяются филтры и выводится изображение вы выделенными на нам обьектами.  
Используется 3 последовательных фильтра:  
  >Пороговый метод  
  >Удаление шума  
  >Увеличение площади  

 Можно вручную подбирать параметры фильтра и применять их.  
 Автоматически фильтр используется к результату предыдущего.   
 При включении "Применить к текущему" применяется к тому же фильтру.  
 Пример: 
   >Автоматически "Увеличение площади" применяется к результату после "удаление шума"  
   >При включении "Применить к текущему" "Увеличение площади" применяется к предыдущему использованию фильтра "Увеличение площади".  

Кнопка "Сбросить" сбрасывает настройки фильтра к начальным и удаляет результат применения фильтра.  
Кнопка "Сбросить все настройки" сбрасывает все настройки фильтров к начальным и заново использует все фильтры.  

"Выделение границ" выводит загруженное изображение с выделенными границами и посчитанной площадью занимаемой выделенными обьектами.  
Для коректного подсчёта площади нужно указать нужный DPI.
 
