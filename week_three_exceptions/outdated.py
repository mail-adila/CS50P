# Implement a program that prompts the user for a date,
# anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
# wherein the month in the latter might be any of the values in the list below:
# [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]
# Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in
# either format, prompt the user again. Assume that every month has no more than 31 days;
# no need to validate whether a month has 28, 29, 30, or 31 days.

months = ["January","February","March","April","May","June","July",
          "August","September","October","November","December"]

def get_date():
    while True:
        date = input("Enter date in month-day-year order: ").strip()
        if '/' in date: #10/31/1991
            try:
                month, day, year = map(int, date.split('/'))
                if 1 <= month <= 12 and 1 <= day <= 31:
                    return month, day, year
            except ValueError:
                pass
        elif ',' in date: #August 29, 2025
            parts = date.replace(',', '').split()
            if len(parts) == 3:
                month_str, day_str, year_str = parts
                try:
                    day = int(day_str)
                    year = int(year_str)
                    month = month_str.title()
                    if month in months and 1 <= day <= 31:
                        return months.index(month) + 1, day, year
                except ValueError:
                    pass
        else:
            pass


def main():
    month, day, year = get_date()
    print(f"{year}-{month:02}-{day:02}")

if __name__ == "__main__":
    main()