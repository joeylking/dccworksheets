
regular_rate = float(input('Enter your hourly pay rate: '))
hours_worked = float(input('Enter the number of hours you worked this week: '))
hours_overtime = hours_worked - 40.0
hours_regular = hours_worked - hours_overtime
overtime_rate = regular_rate * 1.5
regular_pay = regular_rate * hours_regular
overtime_pay = hours_overtime * overtime_rate
total_pay = regular_pay + overtime_pay
print(f'Your pay this week is ${total_pay}. Overtime hours: {hours_overtime} Overtime rate: {overtime_rate} Overtime pay: {overtime_pay}')