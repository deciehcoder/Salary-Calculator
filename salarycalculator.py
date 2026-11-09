# Decie Hall
# 10/24/2026
# P4HW2 - Salary Calculator
# Calculates each employee's gross pay and totals pay for multiple employees.
# Get employee's name
name = input('Enter employee\'s name or "Done" to terminate: ')
# Initialize totals
overtime_total = 0.0
regular_total = 0.0
gross_total = 0.0
employee_count = 0
while name != "Done":
hours_worked = float(input(f"How many hours did {name} work? "))
rate = float(input(f"What is {name}'s pay rate? "))
if hours_worked > 40:
overtime_hours = hours_worked - 40
regular_hours = 40
else:
overtime_hours = 0
regular_hours = hours_worked
overtime_pay = overtime_hours * rate * 1.5
regular_pay = regular_hours * rate
gross_pay = regular_pay + overtime_pay
overtime_total += overtime_pay
regular_total += regular_pay
gross_total += gross_pay
employee_count += 1
print(f"\nEmployee name: {name}\n")
print(f"{'Hours Worked':<16}{'Pay Rate':<13}{'OverTime':<12}{'OverTime
Pay':<24}{'RegHour Pay':<24}{'Gross Pay':<12}")
print("-" * 126)
print(f"{hours_worked:<16.1f}{rate:<13.2f}{overtime_hours:<12.1f}
{overtime_pay:<24.2f}${regular_pay:<23.2f}${gross_pay:<12.2f}")
print()
name = input('Enter employee\'s name or "Done" to terminate: ')
print("Total number of employees entered:", employee_count)
print(f"Total amount paid for overtime: ${overtime_total:.2f}")
print(f"Total amount paid for regular hours: ${regular_total:.2f}")
print(f"Total amount paid in gross: ${gross_total:.2f}")
