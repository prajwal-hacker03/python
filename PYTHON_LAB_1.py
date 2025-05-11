import datetime

# Prompt the user for their name
name = input("Enter your name: ")

# Prompt the user for their year of birth
year_of_birth = int(input("Enter your year of birth: "))

# Get the current year
current_year = datetime.datetime.now().year

# Calculate the age
age = current_year - year_of_birth

# Determine if the person is a senior citizen
if age >= 60:
    print(f"{name}, you are a senior citizen.")
else:
    print(f"{name}, you are not a senior citizen.")
