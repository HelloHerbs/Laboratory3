name = input("Employee Name: ")
num = input("Employee Number: ")
work_hours = float(input ("Number of Total Work Hours: "))
print("")
salary = 60 * work_hours
print("Gross Salary: Php " + format(salary, ",.2f"))
if salary >= 50000:
    tax = 0.20 * salary
    net = salary - tax
    
elif salary >= 30000 and salary <= 49999:
    tax = 0.15 * salary
    net = salary - tax
    
elif salary >= 20000 and salary <= 29999:
    tax = 0.10 * salary
    net = salary - tax
    
elif salary >= 10000 and salary <= 19999:
    tax = 0.05 * salary
    net = salary - tax
    
elif salary < 10000:
    net = salary
    tax = 0.00

print("Income Tax Payable: Php " + format(tax, ",.2f"))
print("") 
print("Total Net Salary: Php " + format(net, ",.2f"))