''' 
    ** Pay Roll Processing **
    for given base salary
    hra in percentage (house rent allowance) +
    da in percentage (daily allowance) +
    ta in percentage (travel allowance) +   ==> gross salary
    pf in percentage (provident fund) - ==> net salary 
'''
base_salary = float(input('Base Salary:'))
hra_per = float(input('HRA%:'))
da_per = float(input('DA%:'))
ta_per = float(input('TA%:'))
pf_per = float(input('PF%:'))

hra = (base_salary / 100) * hra_per
da = (base_salary / 100) * da_per
ta = (base_salary / 100) * ta_per

gross_salary = base_salary + hra + da + ta 
pf = (gross_salary / 100) * pf_per

net_salary = gross_salary - pf 

print(f'Base Salary: {base_salary:.2f}')
print(f'HRA {hra_per:.2f}%: {hra:.2f}')
print(f'DA {da_per:.2f}%: {da:.2f}')
print(f'TA {ta_per:.2f}%: {ta:.2f}')
print(f'Gross Salary: {gross_salary:.2f}')
print(f'PF {pf_per:.2f}%: {pf:.2f}')
print(f'Net Salary: {net_salary:.2f}')