from datetime import date, timedelta

def getDay(n):
    days = []
    for i in range(n):
        day = date.today() + timedelta(days=i+1)
        days.append((day.weekday(), day.day, day.month))
    return days

if __name__ == "__main__":
    n = int(input("Enter number of days: "))
    days = getDay(n)
    for day in days:
        print(day[0], day[1], day[2])
