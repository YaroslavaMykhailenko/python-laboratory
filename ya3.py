print("Михайленко Ярослава Євгенівна \nЛабораторна робота №1 \nВаріант 10 \nОбчислення виразу в залежності від значення \n")


def myfunc():
    x = float(input('x='))
    if x>=8 :
        print('F(x)=%d'%(-x**2+x-9))
        p = input("Продолжить тестирование программы? +/-")
        if p == "+":
            myfunc()
        else:
            return
    else:
        c = 1/(x**4-6)
        print(c)
        p = input("Продолжить тестирование программы? +/-")
        if p == "+":
            myfunc()
        else:
            return
myfunc()