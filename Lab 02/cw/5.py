#5
def time(days):
    year = days // 365
    month = (days % 365) // 30
    day = (days % 365) % 30
    print(f"{year} Years, {month} months, {day} days")

time(4320)