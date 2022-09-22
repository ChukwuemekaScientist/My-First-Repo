# Chukwuemeka Agu
# 1871765

print("Birthday Calculator")

print("Current Day")
current_month = int(input("Month: "))
current_day = int(input("Day: "))
current_year = int(input("Year: "))

print("Birthday")
birthday_month = int(input("Month: "))
birthday_day = int(input("Day: "))
birthday_year = int(input("Year: "))

is_birthday = False
if current_month > birthday_month:
    age_years = current_year - birthday_year
elif (current_month == birthday_month) and (current_day > birthday_day):
    age_years = current_year - birthday_year
elif (current_month == birthday_month) and (current_day == birthday_day):
    age_years = current_year - birthday_year
    is_birthday = True
else:
    age_years = current_year - birthday_year - 1

print ("You are", age_years, "years old.")
if is_birthday == True:
    print("Happy Birthday")



