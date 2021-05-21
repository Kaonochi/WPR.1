# import random
import sys


# # zad 1
# names = (
#     "Lukasz",
#     "Marek",
#     "Zbyszek",
#     "Asia",
#     "Basia",
#     "Kasia",
# )
# # zad 2
# surnames = {
#     "Lukasz",
#     "Banach",
#     "Curie",
#     "Kowalski",
#     "Nowak",
#     "Studencki"
# }
#
# print(names)
# print(surnames)
#
# #zad 3
# for x in names:
#     if x[-1] == "a":
#         print(x)
#
# #zad 4
# def llps(s):
#     polski_sufix = ('ski', 'cki')
#     for each in polski_sufix:
#         if s.endswith(each):
#             return True
#     return False
#
# #zad 5
# for each in surnames:
#     if llps(each):
#         print (each)
#
# def filtracjaPolaczkow(zastNazw):
#     listaPolaczkow = []
#     for each in surnames:
#         if llps(each):
#             listaPolaczkow.append(each)
#     return listaPolaczkow
# print(filtracjaPolaczkow(surnames))
#
# people = []
#
# for i in names:
#     for j in surnames:
#         if i[-1] == 'a' and llps(j):
#             j = j[:-1] + 'a'
#             people.append((i,j))
#             print (i,j)
#
#
# def create_a_persone(names, surnames):
#     x = random.randint(0,len(names)-1)
#     random_name = names[x]
#     x = random.randint(0, len(surnames)-1)
#     random_surname = list(surnames)[x]
#     if random_name[-1] == 'a' and llps(random_surname):
#         random_surname=random_surname[:1]+'a'
#     return f"{random_name} {random_surname}"
# print(create_a_persone(names,surnames))

# x = random.randint(0,100)
#
#
#
# while True:
#     n = int(input("Podaj liczbe"))
#     if x > n:
#         print("Za malo")
#     elif x < n:
#         print("Za duzo")
#     else:
#         print("W sam raz")
#         break
#

# def trojkat(rozmiar):
#     gwiazdka = "*"
#     i = 1
#     while i <= rozmiar:
#         print(gwiazdka * i)
#         i += 1
#
#
# trojkat(2)
# trojkat(3)
# trojkat(4)
#
# def trojkatRysowanko(rozmiar):
#     for i in range (rozmiar,0, -1):
#         print('*'*i)
#
# trojkatRysowanko(2)
# trojkatRysowanko(3)
# trojkatRysowanko(4)

# def trojkat(h):
#     i=1
#     while i<=h:
#         print ("*"*i)
#         i += 1
# def od_trojkat(h):
#     i=h
#     while i > 0:
#         print("*"*i)
#         i -=1
# def piramida(h):
#     s=h-1
#     spacje = range(h-1,-1,-1)
#     for i in range(len(spacje)):
#         print(" "*spacje[i]+"*"*(1+i*2))
# h=5
# piramida(h)

# n = 0
#
# for i in range(1,n+1):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i, "FizzBuzz")
#     elif i % 3 == 0:
#         print(i, "Fizz")
#     elif i % 5 == 0:
#         print(i, "Buzz")
#     fizz_buzz=[]
#     if i % 3 == 0:
#         fizz_buzz.append("Fizz")
#     if i % 5 == 0:
#         fizz_buzz.append("Buzz")
#     if fizz_buzz:
#         print(i,"".join(fizz_buzz))
#
# lista=["Ala","ma","kata."]
# print ("?".join(lista))

# n = 3
# for i in range(n, 1, -1):
#     if i <= 0:
#         print(i, " bottles of beer on the wall, 99 bottles of beer.")
#         print("Take one down, pass it around, {n} bottles of beer on the wall...")
#     else:
#         print(n, " bottles of beer on the wall,", n, "bottles of beer.")
#         print("Take one down, pass it around, ", i-1, "bottles of beer on the wall...")

# terminator = "\n"
# rev = False
# upp = False
# line = " "
#
# for i, each in enumerate(sys.argv[1:]):
#     if each == "-n":
#         terminator = ""
#     elif each == "-r":
#         rev = True
#     elif each == "-u":
#         upp = True
#     elif each == "-l":
#         line = "\n"
#     else:
#         break
#
# args = sys.argv[i+1:]
# if rev:
#     args = list(reversed(args))
#
# if upp:
#     for i, arg in enumerate(args):
#         args[i] = arg.lower()
#     args[0] = args[0].capitalize()
#
#
# print(line.join(args), end=terminator)


# def evaluate_plus(stack):
#     a = stack.pop()
#     b = stack.pop()
#     stack.append(a + b)
#
#
# def evaluate_minus(stack):
#     a = stack.pop()
#     b = stack.pop()
#     stack.append(b - a)
#
#
# def evaluate_multiply(stack):
#     a = stack.pop()
#     b = stack.pop()
#     stack.append(b * a)
#
#
# def evaluate_divide(stack):
#     a = stack.pop()
#     b = stack.pop()
#     stack.append(b / a)
#
#
# def evaluate_integer(stack, expr):
#     stack.append(int(e))
#
#
#
# def evaluate_expression(expr, stack):
#     for e in expr:
#         if e.isdigit():
#             stack.append(int(e))
#         elif e == "+":
#             a = stack.pop()
#             b = stack.pop()
#             stack.append(a + b)
#         elif e == "-":
#             a = stack.pop()
#             b = stack.pop()
#             stack.append(b - a)
#         elif e == "/":
#             a = stack.pop()
#             b = stack.pop()
#             stack.append(b / a)
#         elif e == "*":
#             a = stack.pop()
#             b = stack.pop()
#             stack.append(b * a)
#         elif e == "p":
#             print(stack[-1])
#
#
#
# stack = []
#
# while True:
#     expr = input()
#     expr = expr.split()
#     done = evaluate_expression(expr, stack)
#     if done:
#         break




# zjazd 10

#kassy i objekty

# class Basic:
#     def __init__(self, field):  #pass to pusta instrukcja
#         self.field = field
#
#     def __str__(self):
#         return "basic " + str(self.field)
#
#     def print_field(self):
#         return print(self.field)
#
#     def __gt__(self, other):
#         return self.field > other.field
#
# class x:
#     def __init__(self, field):  #pass to pusta instrukcja
#         self.field = field
#
#
# def print_field(x):
#     return print(x.field)
#
# c = Basic(-5)
# b = Basic(5)
# x = x(10)
#
# print(b)
# b.print_field()
# print_field(b)
# Basic.print_field(b)
# print_field(x)
# Basic.print_field(x)
# print(c < b)
# print(c > b)
# print(c == b)


# zadanie class Hello

# class Hello:
#     def __init__(self, greeating):
#         self.greeating=greeating
#     def great(self, person):
#         return print("{} {}".format(self.greeating, person))
#
# def hello(person, greeating):
#
#     return print("{} {}".format(greeating, person))
#
# hello("Text", "Hi")
# new = Hello("Hi")
# new.great("Bartek")
# new.greeating="hello"
# new.great("xyz")

# Klasy `Shape`, `Triangle` i `Square`

# class Shape:
#     def __init__(self, n = None):
#         self.n = n
#
#     def make_n(self, n):
#         if n is None:
#             n = self.n
#         return n
#
#
#     def draw(self, n = None):
#         n = self.make_n(n)
#         for i in range(1, n + 1):
#             self.draw_line(i,n)
#
#     def scale(self, f):
#         self.n *= f
#
#
# class Triangle(Shape):
#     def draw_line(self, i, n):
#         print("*" * i)
#
#
#
# class Square(Shape):
#     def draw_line(self, i , n):
#         print("*" * n)
#
# s = Shape()
# # s.draw(4)
# t = Triangle(2)
# t.draw()
# t.draw(4)
# q = Square(2)
# q.draw()
# q.draw(4)
#
# q = Square(2)
# q.draw()
# q.scale(3)
# q.draw()


# Kalkulator RPN (3)
# class Expresion:
#     def __init__(self, expr):
#         self.expr = expr
#
#
#     def evaluate(self, stack):
#         pass
#
#
# class Add(Expresion):
#     def evaluate(self, stack):
#         a = stack.pop()
#         b = stack.pop()
#         stack.append(a + b)
#
#
# class Sub(Expresion):
#     def evaluate(self, stack):
#         a = stack.pop()
#         b = stack.pop()
#         stack.append(a - b)
#
#
# class Inreger(Expresion):
#     def evaluate(self, stack):
#         stack.append(int(self.expr))
#
#
# class Print(Expresion):
#     def evaluate(self, stack):
#         print(stack[-1])
#
#
# def evaluate(ops, stack):
#     for each in ops:
#         each.evaluate(stack)
# stack = []
#
# while True:
#     ops = []
#     expr = input()
#
#     for each in expr.split():
#         if each.isdigit():
#             ops.append(Inreger(each))
#         elif each == '+':
#             ops.append(Add(each))
#         elif each == '-':
#             ops.append(Sub(each))
#         elif each == 'p':
#             ops.append(Print(each))
#         else:
#             exit(1)
#     evaluate(ops, stack)

# didiczenie po welu classuw
class Swimmer():
    def swim(self):
        print("{} swims".format(self))


class Quaker():
    def quak(self):
        print("{} quaks".format(self))


class Duck(Swimmer,Quaker):
    pass


s = Swimmer()
q = Quaker()
s.swim()
q.quak()
d = Duck()
d.swim()
d.quak()
