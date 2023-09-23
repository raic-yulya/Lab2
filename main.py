#задание3
a = 3
print (type(a))
a = 3.5
print(type(a))
a = 'qwerty'
print(type(a))
a = True
print(type(a))
a = '123'
print(type(a))
#int - целочисленный тип, float - вещественный с запятой, bool - логический либо try or false
#string - строчный, если сюда добавить число будет ошибка, так как нельзя складывать строку с числом

#задание4
x = int(5.7)
print(x)

x = int(-5.7)
print(x)

x = 3**39 - int(float(3*39))
print(x)

#задание5
name = input("Введите ваше имя: ")
print("Привет, " + name + "!")

#задание6
x = int(input("Доктор Иванов в дороге (в часах): "))
y = int(input("Доктор Иванов на работе (в минутах): "))
total_time = x * 60 + y
print("Доктор Иванов проводит в дороге", total_time, "минут.")

#задание7
a = False
b = True
c = False

result = ((not a or b) and c)
print(result)

#задание8
def check_birthday(year):
    if year < 1900 or year > 3000:
        print("Год не входит в выборку")
    elif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print("С днём рождения!")
    else:
        print("Год обычный")

year = int(input("Введите год: "))
check_birthday(year)

#задание9
num = 2
while num <= 20:
    print(num, end=' ')
    num += 2

#задание10
# Инициализируем переменную для накопления суммы
s = 0

# Считываем первое число
n = int(input())

# Цикл для считывания чисел и накопления суммы
while n != 0:
    s += n
    n = int(input())

# Выводим сумму на экран
print(s)

#задание11
x = int(input("Коллеги в клинике: "))
y = int(input("Коллеги в поликлинике: "))

# Находим наибольший общий делитель
while y != 0:
    x, y = y, x % y

# Выводим количество кусочков
print("Необходимое количество кусочков пиццы:", x)

#задание12
for i in range(2, 21, 2):
    print(i, end=' ')


#задание13
a = int(input("Начало первого: "))
b = int(input("Конец первого: "))
c = int(input("Начало второго: "))
d = int(input("Конец второго: "))

for i in range(a, b+1):
    for j in range(c, d+1):
        print(i*j, end='\t')
    print()

#задание14
n = int(input("Введите размер ковра: "))
matrix = [[0] * n for i in range(n)]
x, y = 0, 0
dx, dy = 0, 1
for i in range(n ** 2):
    matrix[x][y] = i + 1
    if matrix[(x + dx) % n][(y + dy) % n]:
        dx, dy = dy, -dx
    x, y = x + dx, y + dy
for row in matrix:
    print(" ".join([str(elem) for elem in row]))

#задание15
import tkinter as tk

def show_reminder():
    reminder_window = tk.Toplevel(root)
    reminder_window.title("Напоминание об отдыхе")
    reminder_window.geometry("300x100")
    reminder_label = tk.Label(reminder_window, text="Время для перерыва!")
    reminder_label.pack(pady=20)
    close_button = tk.Button(reminder_window, text="Закрыть", command=reminder_window.destroy)
    close_button.pack(pady=10)
    reminder_window.after(10000, show_reminder)

def quit_program():
    root.destroy()

root = tk.Tk()
root.title("Напоминание об отдыхе")
root.geometry("300x100")
reminder_label = tk.Label(root, text="Время для перерыва!")
reminder_label.pack(pady=20)
show_button = tk.Button(root, text="Показать", command=show_reminder)
show_button.pack(side=tk.LEFT, padx=10)
quit_button = tk.Button(root, text="Выход", command=quit_program)
quit_button.pack(side=tk.RIGHT, padx=10)
root.mainloop()






