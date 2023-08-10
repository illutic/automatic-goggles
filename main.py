from typing import Iterable
from percent import calculate_percentages
from utils import read_csv_to_data, write_data_to_csv
from data import WindDirection, WindSpeed, MoonPhase, Tide, Barometer, Data


def ask_wind_direction():
    wind_direction = input(
        'What is the wind direction? (N, NE, E, SE, S, SW, W, NW)\n').upper()
    while wind_direction not in ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']:
        wind_direction = input(
            'What is the wind direction? (N, NE, E, SE, S, SW, W, NW)\n').upper()
    return WindDirection.ofWord(wind_direction)


def ask_wind_speed():
    wind_speed = input(
        'What is the wind speed? (Calm, LightAir, LightBreeze, GentleBreeze, ModerateBreeze, FreshBreeze, StrongBreeze, NearGale, Gale, StrongGale, Storm, ViolentStorm, Hurricane)\n').upper()
    while wind_speed not in ['CALM', 'LIGHTAIR', 'LIGHTBREEZE', 'GENTLEBREEZE', 'MODERATEBREEZE', 'FRESHBREEZE', 'STRONGBREEZE', 'NEARGALE', 'GALE', 'STRONGGALE', 'STORM', 'VIOLENTSTORM', 'HURRICANE']:
        wind_speed = input(
            'What is the wind speed? (Calm, LightAir, LightBreeze, GentleBreeze, ModerateBreeze, FreshBreeze, StrongBreeze, NearGale, Gale, StrongGale, Storm, ViolentStorm, Hurricane)\n').upper()
    return WindSpeed.ofWord(wind_speed)


def ask_moon_phase():
    moon_phase = input(
        'What is the moon phase? (FullMoon, WaxingGibbous, FirstQuarter, WaxingCrescent, NewMoon, WaningCrescent, LastQuarter, WaningGibbous)\n').upper()
    while moon_phase not in ['FULLMOON', 'WAXINGGIBBOUS', 'FIRSTQUARTER', 'WAXINGCRESCENT', 'NEWMOON', 'WANINGCRESCENT', 'LASTQUARTER', 'WANINGGIBBOUS']:
        moon_phase = input('What is the moon phase?\n').upper()
    return MoonPhase.ofWord(moon_phase)


def ask_tide():
    tide = input(
        'What is the tide? (HighRaising, HighFalling, LowRaising, LowFalling)\n').upper()
    while tide not in ['HIGHRAISING', 'HIGHFALLING', 'LOWRAISING', 'LOWFALLING']:
        tide = input(
            'What is the tide? (HighRaising, HighFalling, LowRaising, LowFalling)\n').upper()
    return Tide.ofWord(tide)


def ask_barometer():
    barometer = input(
        'What is the barometer?(Rising, Falling, Steady)\n').upper()
    while barometer not in ['RISING', 'FALLING', 'STEADY']:
        barometer = input(
            'What is the barometer?(Rising, Falling, Steady)\n').upper()

    return Barometer.ofWord(barometer)


def ask_success():
    success = input('Was the fishing trip successful? (True, False)\n').upper()
    while success not in ['TRUE', 'FALSE']:
        success = input(
            'Was the fishing trip successful? (True, False)\n').upper()

    if success == 'TRUE':
        return True
    elif success == 'FALSE':
        return False
    else:
        raise Exception('Invalid input')


def get_data_from_user():
    wind_direction = ask_wind_direction()
    wind_speed = ask_wind_speed()
    moon_phase = ask_moon_phase()
    tide = ask_tide()
    barometer = ask_barometer()
    success = ask_success()
    return Data(
        windDirection=wind_direction,
        windSpeed=wind_speed,
        moonPhase=moon_phase,
        tide=tide,
        barometer=barometer,
        success=success
    )

def main():
    historical_data = read_csv_to_data()
    historical_data = list(historical_data)

    while (True):
        print("Welcome to the Fishing Success Predictor")
        print("Please enter the current weather conditions")
        user_data = get_data_from_user()

        print("Calculating Success Rate...")

        write_data_to_csv(user_data)

        see_data = input(
            "Would you like to see the success rates per attribute? (y/n) \n")
        if see_data.upper() == 'Y':
            historical_data.append(user_data)
            calculate_percentages(historical_data)

        cont = input("Would you like to enter more data? (y/n) \n")
        if cont.upper() == 'N':
            print("Goodbye!")
            break


main()
