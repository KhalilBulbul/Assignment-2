# Variables

current_age= int(input ("Enter Current Age In Years: "))
current_years_service= int(input("Enter Current Years Of Service: "))
largest_expected_income= int(input("Enter The Largest Expected Annual Income: "))
second_largest_income= int(input("Enter The Second-Largest Expected Annual Income: "))
third_largest_income= int(input("Enter The Third-Largest Expected Annual Income: "))

# Calculations

average_income= float((largest_expected_income+second_largest_income+third_largest_income)/3)
rate= float(0.014)
pension_income= (average_income*rate*current_years_service)

# Seperating calculations

service_years_at_55 = current_years_service + int(55 - current_age)
service_years_at_60 = current_years_service + int(60 - current_age)
service_years_at_65 = current_years_service + int(65 - current_age)

# Seperating pension

pension_income_55 = average_income * rate * service_years_at_55
pension_income_60 = average_income * rate * service_years_at_60
pension_income_65 = average_income * rate * service_years_at_65

# Displays

print(f"\n{'Retirement Age':<17}{'Retirement Income'}")
print(f"{55:<17}${pension_income_55:,.2f}")
print(f"{60:<17}${pension_income_60:,.2f}")
print(f"{65:<17}${pension_income_65:,.2f}")