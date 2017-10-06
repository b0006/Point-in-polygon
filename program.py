#библиотека математических функций
import math

#класс точки
class Point:
    #конструктор класса
    def __init__(self, x, y): 
        self.x = x
        self.y = y

#функция определения принадлежности точки полигону
#параметры функции:
    #polygon - полигон
    #number_of_vertices - кол-во вершин у полигона
    #x - x-координата точки
    #y - y-координата точки
def IsPointInsidePolygon(polygon, number_of_vertices, x, y):
    count = 0 #кол-во False'ов ("костыль")
    #цикл
    for n in range(number_of_vertices):
        #значение, которое хранит ответ на принадлежность точки полигону (изначально задан false)
        flag = False
        
        if (n < number_of_vertices - 1):
            i1 = n + 1
        else:
            i1 = 0
        
        #цикл c постусловием
        while flag == False:
            i2 = i1 + 1

            if (i2 >= number_of_vertices):
                i2 = 0
            
            #общая площадь
                #abs - модуль числа
            S = math.fabs (polygon.x[i1] * (polygon.y[i2] - polygon.y[n]) + polygon.x[i2] * (polygon.y[n] - polygon.y[i1]) + polygon.x[n] * (polygon.y[i1] - polygon.y[i2]))
            #первая площадь
            S1 = math.fabs (polygon.x[i1] * (polygon.y[i2] - y) + polygon.x[i2] * (y - polygon.y[i1]) + x * (polygon.y[i1] - polygon.y[i2]))
            #вторая площадь
            S2 = math.fabs (polygon.x[n] * (polygon.y[i2] - y) + polygon.x[i2] * (y - polygon.y[n]) + x * (polygon.y[n] - polygon.y[i2]))
            #третья площадь
            S3 = math.fabs (polygon.x[i1] * (polygon.y[n] - y) + polygon.x[n] * (y - polygon.y[i1]) + x * (polygon.y[i1] - polygon.y[n]))

            #сравнение трех площадей с общей (если истино - точка принадлежит)
            if(S == S1 + S2 + S3):
                flag = True
                break

            i1 = i1 + 1

            if (i1 >= number_of_vertices):
                i1 = 0

            count += 1
            if(count >= 3):
                break

    #вывод на печать
    print("Принадлежит ли точка полигону?")
    #возвращает значение
    return flag

#объект класса Point
#точка имеет координаты вида [x1,x2,x3...], [y1,y2,y3...]
poly = Point([10, 10, -10, -10], [10, -10, -10, 10])

#кол-во вершин
poly_size = len(poly.x)

#вывод на печать
print(">>>> Проверка принадлежности точки полигону <<<<")
print("------------------------------------------------")
print("Введите координаты точки:")

#ввод координат с клавиатуры с проверкой на корректный ввод цифр
x_input = 0
y_input = 0
check = 0 #переменная проверки

while check != 1:
    try:
        x_input = float(input("X >>> "))
        check = 1
    except (TypeError, ValueError):
        print ('Ошибка! X-координата введена не верна. Повторите ввод')
while check != 0:
    try: 
        y_input = float(input("Y >>> "))
        check = 0
    except (TypeError, ValueError):
        print ('Ошибка! Y-координата введена не верна. Повторите ввод')

#вывод на печать и вызов функции
print(IsPointInsidePolygon(poly, poly_size, x_input, y_input))

