'''
for given age, categorize age as 
   child   <= 12
   teenager <= 19
   adult    <= 40
   middle-aged <= 60
   senior citizen <= 80
   super senior citizen > 80
'''

age = int(input('Age:'))
if age <= 12:
    category = 'Child'
elif age <= 19:
    category = 'Teenager'
elif age <= 40:
    category = 'Adult'   
elif age <= 60:
    category = 'Middle Aged' 
elif age <= 80:
    category = 'Senior Citizen' 
else:
    category = 'Super Senior Citizen' 

print(f'Age:{age}')
print(f'Category:{category}')