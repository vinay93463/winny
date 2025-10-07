import calendar

def show_month_calendar():
    year = int(input("Enter year (e.g. 2025): "))
    month = int(input("Enter month (1-12): "))

    # Create a plain text calendar
    cal = calendar.TextCalendar(calendar.SUNDAY)
    month_calendar = cal.formatmonth(year, month)
    print("\n" + month_calendar)

if __name__ == "__main__":
    show_month_calendar()
