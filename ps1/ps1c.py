# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 18:00:03 2020

@author: Sharon G
"""
# Solution for Problem Set 1: Question C.
# Although not specified in the homework, it is assumed that the user
# would like to know the MINIMUM percent of their monthly salary required
# if they wish to reach the portion_down_payment by the number_of_months.

print("Welcome to PS1C")
menu_cycle = 1
# The following values are given explicitly in the problem set 1C definition:
rate = 0.04 
portion_down_payment = 250000.00 
number_of_months = 37
semi_annual_raise = 0.07

while menu_cycle != 0:
    starting_salary = float(input("Enter the starting salary: "))
    monthly_salary = starting_salary/12.0

# Initial test to see whether salary is great enough to save the required 
# portion_down_payment. This is NOT ideal, and assumes that the entire 
# montly salary is put into savings, but must be performed this way. 

    current_savings = monthly_salary 
    for j in range(1, number_of_months, 1):
        current_savings += monthly_salary *(1 + rate)
        if j % 6 == 0:
            monthly_salary *= (1 + semi_annual_raise) 
        
    if current_savings < portion_down_payment:
        print("It is not possible to pay the down payment in 3 years.")
    else:
    # Salary is enough to perform bisection search
        high = 10000 
        low = 0
        current_savings = 0.0
        steps_in_search = 0
        while abs(current_savings - portion_down_payment) > 100: 
            monthly_salary = round(starting_salary/12.0, 2)
            guess = (high + low)/2
            current_savings = round(monthly_salary * guess * .001, 2) 
            steps_in_search += 1
            for i in range(1, number_of_months, 1):
                current_savings += round(monthly_salary * guess * .001 * (1 + rate), 2)
                if i % 6 == 0:
                    monthly_salary = round(monthly_salary * (1 + semi_annual_raise), 2)          
            if current_savings < portion_down_payment:
                low = guess
            else:
                high = guess       
    print("Best savings rate " + str(round(guess*.001, 4)) + ".")
    print("Steps in bisection search: " + str(steps_in_search) + ".")
    print("Current savings is " + str(round(current_savings, 2)) + ".")
    menu_cycle = input("Press 0 and enter to exit or any other key to continue: ")
    


        
        
        
        
        

        
        
            