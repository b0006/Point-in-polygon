# Принадлежность произвольной точки полигону
<h1>Содержание</h1>
  <ul>
    <li><a href="#square">Метод сравнения площадей</a></li>
    <li><a href="#theory">Теоретическая часть</a></li>
    <li><a href="#task">Задача модуля</a></li>
    <li><a href="#test">Тестирование модуля</a></li>
    <li><a href="#exp">Полученный мною опыт</a></li>
  </ul>

<h5 align="center">Определение принадлежности точки произвольному полигону по координатам </h5>
<h2 id="theory">Теоретическая часть</h2>

<p align="justify">
  В вычислительной геометрии известна задача об определении принадлежности точки полигону. На плоскости даны полигон и точка. Требуется решить вопрос о принадлежности точки полигону.
</p>
<br>
<p align="justify">
  Полигон может быть, как <b>выпуклым</b>, так и <b>невыпуклым</b>. Обычно предполагается, что полигон простой, т.е. без самопересечений, но задачу рассматривают и для непростых полигонов. В последнем случае разные способы определения принадлежности точки полигону могут привести к разным результатам. Различают алгоритмы без предварительной обработки и алгоритмы с предварительной обработкой, в ходе которой создаются некоторые структуры данных, позволяющие в дальнейшем быстрее отвечать на множество запросов о принадлежности точек одному и тому же полигону.
</p>

<h2 id="square">Метод сравнения площадей</h2>
<p align="justify">
  Вычисления и сравнения площадей треугольников заменяются вычислениями и сравнениями их удвоенных площадей. Тем самым исключается погрешность округления при программной реализации всего алгоритма, в целом.
</p>
<br>
<p align="justify">
  В данном методе сначала находятся площади трёх треугольников, которые образует произвольная точка с каждой стороной треугольника. 
</p>
<br>
<p align="justify">
  Затем находится площадь самого полигона. Найденные площади сравниваются — если сумма трёх площадей равна площади всего полигона, то значит точка принадлежит полигону.
</p>

<h2 id="task">Задачи модуля</h2>
<ul>
  <li>ввод координат точки в виде кортежей вида (x, y);</li>
  <li>определить принадлежности точки полигону;</li>
</ul>
<h2 id="test">Тестирование модуля</h2>
<table>
    <tr>
        <td>Входные данные</td>
        <td>Выходные данные</td>
    </tr>
    <tr>
        <td><pre>X >>> 0 
Y >>> 0</pre></td>
        <td>True</td>
    </tr>
    <tr>
        <td><pre>X >>> 10 
Y >>> 10</pre></td>
        <td>True</td>
    </tr>
    <tr>
        <td><pre>X >>> 11 
Y >>> -10</pre></td>
        <td>False</td>
    </tr>
    <tr>
        <td><pre>X >>> 5 
Y >>> 2</pre></td>
        <td>True</td>
    </tr>
    <tr>
        <td><pre>X >>> 5 
Y >>> -2</pre></td>
        <td>True</td>
    </tr>
    <tr>
        <td><pre>X >>> -0 
Y >>> 1</pre></td>
        <td>True</td>
    </tr>
    <tr>
        <td><pre>X >>> 02 
Y >>> 3</pre></td>
        <td>True</td>
    </tr>
    <tr>
        <td><pre>X >>> dff 
Y >>> 10
X >>> 3</pre></td>
        <td><pre>'Ошибка! X-координата введена не верна. Повторите ввод.'
True</pre>
</td>
    </tr>
    <tr>
        <td><pre>X >>> 10 
Y >>> gdd
X >>> 3</pre></td>
        <td><pre>'Ошибка! Y-координата введена не верна. Повторите ввод.'
True</pre>
</td>
    </tr>
    <tr>
        <td><pre>X >>> -10 
Y >>> -12</pre></td>
        <td>False</td>
    </tr>
    <tr>
        <td><pre>X >>> 10 
Y >>> -11</pre></td>
        <td>False</td>
    </tr>
    <tr>
        <td><pre>X >>> -11 
Y >>> 9</pre></td>
        <td>False</td>
    </tr>
    <tr>
        <td><pre>X >>> 10 
Y >>> -10</pre></td>
        <td>True</td>
    </tr>
    <tr>
        <td><pre>X >>> -10 
Y >>> 10</pre></td>
        <td>True</td>
    </tr>
</table>
<h2 id="exp">Полученный мною опыт</h2>
  <ul>
    <li>Опыт работы с языком Python 3;</li>
    <li>Обработка исключений при неправильном вводе входных параметров;</li>
    <li>Вспомнил школьный курс геометрии.</li>   
  </ul>
  </ul>
