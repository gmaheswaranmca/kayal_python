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
choice = 'y'
while choice == 'y':
    categorize_age()
    choice = input('Are you sure to continue (y/n):')
print('End of app. Thank you for using app!')