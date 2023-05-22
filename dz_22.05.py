#!
class PrimeGenerator:
    def __init__(self, data):
        self.data = data
    def generate(self, data):
        for i in data:
            yield i

l = [1, 2, 3, 5, 7, 11, 13, 17, 19]
p = PrimeGenerator(l)
for num in p.generate(l):
    print(num)

#2
l = [1, 2, 3, 4]
class average_closure:
    def __init__(self, lst):
        self.lst = lst
    def add_number(self, number):
        self.number = number
        self.lst.append(number)
        return self.lst
    def get_average(self):
        result = sum(self.lst) / len(self.lst)
        if len(l) != 0:
            return result
        else:
            raise ValueError('Неможливо поділити на нуль!')
a = average_closure(l)

print(a.add_number(7))
print(a.get_average())

#or
def average_closure(l):
    def add_number(number):
        l.append(number)
        return l
    def get_average():
        if len(l) != 0:
            return sum(l) / len(l)
        else:
            raise ValueError('Неможливо поділити на нуль!')
    return add_number, get_average
add, get = average_closure(l)
print(add(5))
print(get())


#3
import random
class PasswordGenerator:
    def __init__(self, length, characters):
        self.legth = length
        self.characters = characters
    def generate_password(self):
        password = ''
        for i in range(self.legth):
            c = random.choice(self.characters)
            password += c
        if 'Деякі погані слова' in password:
            raise ValueError('У паролі наявні заборонені слова!')
        yield password
c1 = ['1', '2', 't','L', 'F', '_', 'D', 'g', 'b', 'X']
p1 = PasswordGenerator(7, c1)
for password in p1.generate_password():
    print(password)
c2 = ['1', '2', '3', '4', '5', 'a', 'b', 'c', 'd', 'e', 'A', 'B', 'C', 'D', 'E', 'F', '_', '$' ]
p2 = PasswordGenerator(int(input('Введіть кількість символів в другому паролі: ')), c2)
for password in p2.generate_password():
    print(password)
