import math
from datetime import date, timedelta
from typing import Dict


def easter_sunday(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return month, day


def my_day_of_year(month, day, year) -> int:
    return (date(year, month, day) - date(year, 1, 1)).days + 1


# print("19 days before Christmas:", xmas)
# print("19 days before Easter:", easter)
# print("19 days before Thanksgiving:", thanksgiving)
# print("19 days before New Year's Day:", new_years)
# print("19 days before Valentine's Day:", valentines)

def day_value(day_of_year, start_day, end_day, rise_duration=10):
    total_days = 365

    # Adjust for periods wrapping over the end of the year
    if end_day < start_day:
        if day_of_year < start_day:
            day_of_year += total_days
        end_day += total_days

    if start_day <= day_of_year < start_day + rise_duration:
        x = (day_of_year - start_day) / rise_duration
        return 1 / (1 + math.exp(-12 * (x - 0.5)))
    elif start_day + rise_duration <= day_of_year <= end_day:
        return 1
    else:
        return 0


# Example usage
start_day = 350  # Starting day of the 20-day period
end_day = (start_day + 19) % 365  # Ending day of the 20-day period

for day_of_year in range(1, 366):
    value = day_value(day_of_year, start_day, end_day)


class EventScores():
    thanksgiving_weight: list[float]
    xmas_weight: list[float]
    easter_weight: list[float]
    valentines_weight: list[float]
    halloween_weight: list[float]
    new_year_weight: list[float]
    pass


def make_my_event_scores() -> Dict[str, EventScores]:
    event_scores = EventScores()
    year = 2023
    easter_month, easter_day = easter_sunday(2023)
    xmas = my_day_of_year(12, 25, 2023)
    easter = my_day_of_year(easter_month, easter_day, year) - 19
    thanksgiving = my_day_of_year(11, 3, year)  # This assumes Thanksgiving is always on November 22nd
    new_years = my_day_of_year(12, 31 - 18, year - 1)  # Subtracting 18 to account for wrapping around the year
    valentines = my_day_of_year(1, 25, year)

    event_scores.thanksgiving_weight = [day_value(day, thanksgiving, thanksgiving + 19) for day in range(1, 366)]
    event_scores.xmas_weight = [day_value(day, xmas, xmas + 19) for day in range(1, 366)]
    event_scores.easter_weight = [day_value(day, easter, easter + 19) for day in range(1, 366)]
    event_scores.valentines_weight = [day_value(day, valentines, valentines + 19) for day in range(1, 366)]
    event_scores.halloween_weight = [day_value(day, 304, 304 + 19) for day in range(1, 366)]
    event_scores.new_year_weight = [day_value(day, new_years, new_years + 19) for day in range(1, 366)]
    return event_scores



