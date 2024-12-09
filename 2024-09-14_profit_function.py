# This code has functions for basic arithmetic operations: add, subtract, multiply, and divide.
# Added new functions as needed.

# Function to add two numbers
def addTwoNumbers(n1, n2):
    ans = n1 + n2
    return ans

# Function to subtract two numbers
def subtractAfromB(a, b):
    ans = b - a
    return ans

# Function to multiply two numbers
def multiplyTwoNumbers(n1, n2):
    ans = n1 * n2
    return ans

# Function to divide two numbers, handling division by zero
def divideAbyB(a, b):
    ans=a/b
    return ans

def total(list1):
    total=0
    for i in list1:
        total=addTwoNumbers(total,i)
    return total
# Main code

# We have sales data for a week.
costOfCoffee, costOfTea, costOfVadai = 25, 20, 25
employeeSalary=500

coffeeSales = [56, 78, 56, 45, 90, 103, 120]
teaSales = [100, 123, 456, 123, 222, 400, 346]
vadaiSales = [23, 45, 67, 12, 89, 90, 120]

# Find total sales for the week.
totalCoffeeSales =total(coffeeSales)
totalTeaSales = total(teaSales)
totalVadaiSales = total(vadaiSales)

# Total revenue calculation
totalCoffeeRevenue = multiplyTwoNumbers(totalCoffeeSales, costOfCoffee)
totalTeaRevenue = multiplyTwoNumbers(totalTeaSales, costOfTea)
totalVadaiRevenue = multiplyTwoNumbers(totalVadaiSales, costOfVadai)

totalRevenue = total([totalCoffeeRevenue, totalTeaRevenue, totalVadaiRevenue])

# Calculate average sales for a week
avgCoffeeSales = divideAbyB(totalCoffeeSales, len(coffeeSales))
avgTeaSales = divideAbyB(totalTeaSales, len(teaSales))
avgVadaiSales = divideAbyB(totalVadaiSales, len(vadaiSales))

# Employee salary for the week
employeeSalaryPerWeek = multiplyTwoNumbers(employeeSalary, 7)

# Calculate profit for the week (Total Revenue - Employee Salaries)
profitForTheWeek = subtractAfromB(employeeSalaryPerWeek, totalRevenue)

# Calculate sales and profit for the month (assuming 4 weeks in a month)
salesPerMonth = multiplyTwoNumbers(totalRevenue, 4)
salaryPerMonth = multiplyTwoNumbers(employeeSalaryPerWeek, 4)
profitPerMonth = subtractAfromB(salaryPerMonth, salesPerMonth)

# Output results
print(f"Total revenue for the week: {totalRevenue} Rs")
print(f"Average coffee sales: {avgCoffeeSales} cups/day")
print(f"Average tea sales: {avgTeaSales} cups/day")
print(f"Average vadai sales: {avgVadaiSales} pieces/day")
print(f"Profit for the week: {profitForTheWeek} Rs")
print(f"Total sales for the month: {salesPerMonth} Rs")
print(f"Profit for the month: {profitPerMonth} Rs")
