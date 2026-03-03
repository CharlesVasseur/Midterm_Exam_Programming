birthday = input("What is your birthday? ")

def ndays(birthday):
    birth_year = int(birthday[6:10])
    current_year = 2026
    full_years = current_year - birth_year - 1

    if full_years < 0:
        return 0
    days = full_years * 365
    return days

print(ndays(birthday), "days has passed since you were born")