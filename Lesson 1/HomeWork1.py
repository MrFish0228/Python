#Найдите сумму цифр трехзначного числа.
'''
num = input("Введите число: ")

if len(num) == 3:
    a = int(num[0])
    b = int(num[1])
    c = int(num[2])
    print(f"{a + b + c} ({a} + {b} + {c})")
else:
    print("Вы ввели неверное число")
'''
#Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
#Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
#а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
'''
s = int(input("Количество журавликов: "))

print(f"Петя и Серёжа сделали по {int(s/6)} штук, а Катя {int(s/6*4)}")
'''
#Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
#Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
#Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
'''
ticket = input("Введите номер билета: ")

if len(ticket) == 6:
    sum1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    sum2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
    if sum1 == sum2:
        print("Вам повезло!")
    else:
        print("Увы, у Вас несчатливый билет. Повезёт в следующий раз!")
else:
    print("Вы ввели неверный номер")
'''
#Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
#если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n,m,k = int(input("Введите длину: ")), int(input("Ведите ширину: ")), int(input("Количество долек: "))

if k%n == 0 or k%m == 0:
    print("Можно")
else:
    print("Нельзя")