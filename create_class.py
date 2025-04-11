#!/usr/bin/env pyhon3

class Family:
    
    is_family = ''
    
    def __init__(self, name, gender= '', age=0):
        self.name = name 
        self.gender = gender
        self.age = age
        
    def test(self):
        return self.is_family
    
    
victor = Family('Victor', 'Male')

dagmara = Family('Dagmara','Female',30)
dagmara.is_family = False

print('')
# print(victor.name, victor.gender)
# print(victor.gender)
print('')

victor.is_family = True


# print(victor.is_family)
# print(dagmara.is_family)
# Family.is_family =  True
# print(Family.is_family)
# print(victor.test())

result_1 = victor.name  # should print victor
result_2 = victor.test()
result_3 = victor.age

print(result_1)
print(result_2)
print(result_3)