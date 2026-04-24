def categorize_age():
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

print('Start of age categorization app...')
times = int(input('Number of times:')) # 5
for I in range(times): #0 1 2 3 4 [5 exclue]
    categorize_age()
print('End of app. Thank you for using app!')