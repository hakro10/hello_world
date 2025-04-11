#!/usr/bin/env python3

print('Hello World!')

    

class Employee:
    
    bonus = 1.05
    
    def __init__(self,name, last_name, age, is_employed,salary=0):
        self.name = name
        self.last_name = last_name
        self.age = age 
        self.is_employed = is_employed
        self.email = f'{self.name}.{self.last_name}@gmail.com'.lower()
        self.salary = salary
    
    def full_name(self):
        return f'{self.name} {self.last_name}'
    
    def rase_amount(self):
        return self.bonus * self.salary

emp_1 = Employee('Auris', 'Aleks',38, True)
emp_2 = Employee('Zydre', 'Aleks', 46, True)
emp_3 = Employee(age=23, name='Deimante', is_employed= False, last_name= 'Aleksandrike')
 
# fullname = emp_1.full_name()

# print(emp_1.age)
# print(emp_2.is_employed) 
# print(emp_1.email)
# print(fullname)

# print('---------------')
# print(emp_3.name)
# print(emp_3.full_name())


print(emp_1.name)
print(emp_1.salary)
emp_1.salary = 45000
print(emp_1.salary)

print(emp_1.bonus)

print(emp_1.rase_amount())

print('-'*30)
print(f'{emp_1.name} bonus rates are {emp_1.bonus}')
print(f'{emp_2.name} bonus rates are {emp_2.bonus}')

emp_1.bonus = 1.08

print(f'{emp_1.name} bonus rates are {emp_1.bonus}')
print(f'{emp_2.name} bonus rates are {emp_2.bonus}')

print('-'*30)

emp_2.bonus = 1.15
print(f'New bonus rates for {emp_2.name} are {emp_2.bonus}')

emp_2.salary = 51000
print(f'{emp_1.name} salary is {emp_1.salary}$')
print(f'{emp_2.name} salary is {emp_2.salary}$')


print(f'{emp_1.name} new salary is {emp_1.rase_amount()}')

print(f'{emp_2.name} new salary is {emp_2.rase_amount()}')

print('-'* 40)
# salary_bonus = int(emp_1.rase_amount())
# print(type(emp_1.salary))
# print(type(salary_bonus))
print(f'{emp_1.name} bonus is {int(emp_1.rase_amount()) - emp_1.salary}')
print(f'{emp_2.name} bonus is { int(emp_2.rase_amount()) - emp_2.salary}')

