from typing import Dict, List

import numpy as np
from numpy.core.records import ndarray

# temperature data
NewYorkCity = [32, 35, 42, 52, 62, 72, 77, 75, 68, 57, 48, 38]
LosAngeles = [58, 60, 62, 65, 68, 72, 75, 76, 74, 70, 65, 59]
Chicago = [22, 27, 37, 49, 60, 70, 75, 73, 66, 54, 40, 28]
Houston = [53, 56, 62, 70, 78, 84, 87, 87, 82, 72, 62, 54]
Phoenix = [56, 60, 65, 73, 83, 93, 99, 97, 91, 81, 68, 57]
Philadelphia = [32, 35, 43, 54, 64, 74, 79, 77, 70, 59, 48, 38]
SanAntonio = [50, 54, 60, 68, 75, 81, 84, 84, 79, 70, 60, 52]
SanDiego = [57, 58, 60, 63, 66, 70, 73, 74, 72, 68, 63, 58]
Dallas = [46, 50, 58, 67, 76, 84, 89, 89, 82, 71, 57, 48]
SanJose = [49, 53, 56, 61, 65, 69, 72, 72, 70, 64, 57, 50]

# population data
NewYorkCityPop = 8.623
LosAngelesPop = 3.999
ChicagoPop = 2.716
HoustonPop = 2.312
PhoenixPop = 1.626
PhiladelphiaPop = 1.580
SanAntonioPop = 1.511
SanDiegoPop = 1.419
DallasPop = 1.341
SanJosePop = 1.035

# GDP data
NewYorkCityGDP = 1.82
LosAngelesGDP = 0.94
ChicagoGDP = 0.59
HoustonGDP = 0.44
PhoenixGDP = 0.33
PhiladelphiaGDP = 0.32
SanAntonioGDP = 0.30
SanDiegoGDP = 0.27
DallasGDP = 0.26
SanJoseGDP = 0.19






def extrapolate_daily_temperatures(monthly_averages):
    daily_temperatures = []
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    for i in range(len(monthly_averages) - 1):
        start_temp = monthly_averages[i]
        end_temp = monthly_averages[i + 1]
        delta_temp = end_temp - start_temp
        daily_delta = delta_temp / days_in_month[i]

        for day in range(days_in_month[i]):
            daily_temp = start_temp + daily_delta * day
            daily_temperatures.append(daily_temp)

    # Add temperatures for the last month
    daily_temperatures.extend([monthly_averages[-1]] * days_in_month[-1])

    return daily_temperatures


# daily_temperatures = extrapolate_daily_temperatures(monthly_averages)


class CityInfo():
    name: str
    population: float
    GDP: float
    temp_per_day: List[float]
    noise_values: ndarray
    thanksgiving_weight: float
    xmas_weight: float
    easter_weight: float
    valentines_weight: float
    halloween_weight: float
    new_year_weight: float
    pass


def make_my_cities() -> Dict[str, CityInfo]:
    MyCityDict = {}

    MyCityDict["New York City"] = CityInfo()
    MyCityDict["New York City"].name = "New York City"
    MyCityDict["New York City"].population = NewYorkCityPop
    MyCityDict["New York City"].GDP = NewYorkCityGDP
    MyCityDict["New York City"].temp_per_day = extrapolate_daily_temperatures(NewYorkCity)
    MyCityDict["New York City"].thanksgiving_weight = 1.0
    MyCityDict["New York City"].xmas_weight = 1.0
    MyCityDict["New York City"].easter_weight = 1.0
    MyCityDict["New York City"].valentines_weight = 1.0
    MyCityDict["New York City"].halloween_weight = 1.0
    MyCityDict["New York City"].new_year_weight = 1.0

    MyCityDict["Los Angeles"] = CityInfo()
    MyCityDict["Los Angeles"].name = "Los Angeles"
    MyCityDict["Los Angeles"].population = LosAngelesPop
    MyCityDict["Los Angeles"].GDP = LosAngelesGDP
    MyCityDict["Los Angeles"].temp_per_day = extrapolate_daily_temperatures(LosAngeles)
    MyCityDict["Los Angeles"].thanksgiving_weight = 1.0
    MyCityDict["Los Angeles"].xmas_weight = 1.0
    MyCityDict["Los Angeles"].easter_weight = 1.0
    MyCityDict["Los Angeles"].valentines_weight = 1.0
    MyCityDict["Los Angeles"].halloween_weight = 1.0
    MyCityDict["Los Angeles"].new_year_weight = 1.0

    MyCityDict["Chicago"] = CityInfo()
    MyCityDict["Chicago"].name = "Chicago"
    MyCityDict["Chicago"].population = ChicagoPop
    MyCityDict["Chicago"].GDP = ChicagoGDP
    MyCityDict["Chicago"].temp_per_day = extrapolate_daily_temperatures(Chicago)
    MyCityDict["Chicago"].thanksgiving_weight = 1.0
    MyCityDict["Chicago"].xmas_weight = 1.0
    MyCityDict["Chicago"].easter_weight = 1.0
    MyCityDict["Chicago"].valentines_weight = 1.0
    MyCityDict["Chicago"].halloween_weight = 1.0
    MyCityDict["Chicago"].new_year_weight = 1.0

    MyCityDict["Houston"] = CityInfo()
    MyCityDict["Houston"].name = "Houston"
    MyCityDict["Houston"].population = HoustonPop
    MyCityDict["Houston"].GDP = HoustonGDP
    MyCityDict["Houston"].temp_per_day = extrapolate_daily_temperatures(Houston)
    MyCityDict["Houston"].thanksgiving_weight = 1.0
    MyCityDict["Houston"].xmas_weight = 1.0
    MyCityDict["Houston"].easter_weight = 1.0
    MyCityDict["Houston"].valentines_weight = 1.0
    MyCityDict["Houston"].halloween_weight = 1.0
    MyCityDict["Houston"].new_year_weight = 1.0

    MyCityDict["Phoenix"] = CityInfo()
    MyCityDict["Phoenix"].name = "Phoenix"
    MyCityDict["Phoenix"].population = PhoenixPop
    MyCityDict["Phoenix"].GDP = PhoenixGDP
    MyCityDict["Phoenix"].temp_per_day = extrapolate_daily_temperatures(Phoenix)
    MyCityDict["Phoenix"].thanksgiving_weight = 1.0
    MyCityDict["Phoenix"].xmas_weight = 1.0
    MyCityDict["Phoenix"].easter_weight = 1.0
    MyCityDict["Phoenix"].valentines_weight = 1.0
    MyCityDict["Phoenix"].halloween_weight = 1.0
    MyCityDict["Phoenix"].new_year_weight = 1.0

    MyCityDict["Philadelphia"] = CityInfo()
    MyCityDict["Philadelphia"].name = "Philadelphia"
    MyCityDict["Philadelphia"].population = PhiladelphiaPop
    MyCityDict["Philadelphia"].GDP = PhiladelphiaGDP
    MyCityDict["Philadelphia"].temp_per_day = extrapolate_daily_temperatures(Philadelphia)
    MyCityDict["Philadelphia"].thanksgiving_weight = 1.0
    MyCityDict["Philadelphia"].xmas_weight = 1.0
    MyCityDict["Philadelphia"].easter_weight = 1.0
    MyCityDict["Philadelphia"].valentines_weight = 1.0
    MyCityDict["Philadelphia"].halloween_weight = 1.0
    MyCityDict["Philadelphia"].new_year_weight = 1.0

    MyCityDict["San Antonio"] = CityInfo()
    MyCityDict["San Antonio"].name = "San Antonio"
    MyCityDict["San Antonio"].population = SanAntonioPop
    MyCityDict["San Antonio"].GDP = SanAntonioGDP
    MyCityDict["San Antonio"].temp_per_day = extrapolate_daily_temperatures(SanAntonio)
    MyCityDict["San Antonio"].thanksgiving_weight = 1.0
    MyCityDict["San Antonio"].xmas_weight = 1.0
    MyCityDict["San Antonio"].easter_weight = 1.0
    MyCityDict["San Antonio"].valentines_weight = 1.0
    MyCityDict["San Antonio"].halloween_weight = 1.0
    MyCityDict["San Antonio"].new_year_weight = 1.0

    MyCityDict["San Diego"] = CityInfo()
    MyCityDict["San Diego"].name = "San Diego"
    MyCityDict["San Diego"].population = SanDiegoPop
    MyCityDict["San Diego"].GDP = SanDiegoGDP
    MyCityDict["San Diego"].temp_per_day = extrapolate_daily_temperatures(SanDiego)
    MyCityDict["San Diego"].thanksgiving_weight = 1.0
    MyCityDict["San Diego"].xmas_weight = 1.0
    MyCityDict["San Diego"].easter_weight = 1.0
    MyCityDict["San Diego"].valentines_weight = 1.0
    MyCityDict["San Diego"].halloween_weight = 1.0
    MyCityDict["San Diego"].new_year_weight = 1.0

    MyCityDict["Dallas"] = CityInfo()
    MyCityDict["Dallas"].name = "Dallas"
    MyCityDict["Dallas"].population = DallasPop
    MyCityDict["Dallas"].GDP = DallasGDP
    MyCityDict["Dallas"].temp_per_day = extrapolate_daily_temperatures(Dallas)
    MyCityDict["Dallas"].thanksgiving_weight = 1.0
    MyCityDict["Dallas"].xmas_weight = 1.0
    MyCityDict["Dallas"].easter_weight = 1.0
    MyCityDict["Dallas"].valentines_weight = 1.0
    MyCityDict["Dallas"].halloween_weight = 1.0
    MyCityDict["Dallas"].new_year_weight = 1.0

    MyCityDict["San Jose"] = CityInfo()
    MyCityDict["San Jose"].name = "San Jose"
    MyCityDict["San Jose"].population = SanJosePop
    MyCityDict["San Jose"].GDP = SanJoseGDP
    MyCityDict["San Jose"].temp_per_day = extrapolate_daily_temperatures(SanJose)
    MyCityDict["San Jose"].thanksgiving_weight = 1.0
    MyCityDict["San Jose"].xmas_weight = 1.0
    MyCityDict["San Jose"].easter_weight = 1.0
    MyCityDict["San Jose"].valentines_weight = 1.0
    MyCityDict["San Jose"].halloween_weight = 1.0
    MyCityDict["San Jose"].new_year_weight = 1.0
    return MyCityDict
