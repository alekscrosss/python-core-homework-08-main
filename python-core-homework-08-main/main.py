from datetime import datetime, date, timedelta

def get_birthdays_per_week(users):
    current_date = date.today()
    result = {"Monday": [], "Tuesday": [], "Wednesday": [], "Thursday": [], "Friday": []}

    for user in users:
        birthday_this_year = user["birthday"].replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year += timedelta(days=365)

        delta = birthday_this_year - current_date

        if timedelta(0) <= delta <= timedelta(6):
            if birthday_this_year.weekday() in [5, 6]:
                result["Monday"].append(user["name"])
            else:
                day_name = birthday_this_year.strftime("%A")
                result[day_name].append(user["name"])

    result = {day: names for day, names in result.items() if names}

    return result


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
