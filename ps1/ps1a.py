# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:17:02 2020

@author: Sharon G
"""
#Solution for Problem Set 1: Question A. 

menu_cycle = 1

print("Welcome to PS1A\n")
while menu_cycle !=0 :
    annual_salary = float(input("Enter your annual salary:"))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
    total_cost = float(input("Enter the cost of your dream home: "))

    current_savings = 0.0
    rate = 0.04
    monthly_salary = annual_salary/12.0
    portion_down_payment = 0.25 * total_cost
    number_of_months = 0
        
    while current_savings <= portion_down_payment:
        current_savings += (monthly_salary * portion_saved) + current_savings*rate/12.0
        number_of_months +=1


    print("Number of months:",number_of_months)
    menu_cycle = input("Press 0 and enter to exit, or any other key to continue: ")
        





