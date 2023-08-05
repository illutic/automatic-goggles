import csv
import os.path

# Define global constants
MOON_PHASE_NAMES = {
    "FM": "Full Moon",
    "WG": "Waning Gibbous",
    "LQ": "Last Quarter",
    "WC": "Waning Crescent",
    "NM": "New Moon",
    "WC": "Waxing Crescent",
    "FQ": "First Quarter",
    "WG": "Waxing Gibbous"
}

WIND_DIRECTION_NAMES = {
    "N": "North",
    "NE": "Northeast",
    "E": "East",
    "SE": "Southeast",
    "S": "South",
    "SW": "Southwest",
    "W": "West",
    "NW": "Northwest"
}

WIND_SCALE_NAMES = {
    1: "Calm",
    2: "Light Air",
    3: "Light Breeze",
    4: "Gentle Breeze",
    5: "Moderate Breeze",
    6: "Fresh Breeze",
    7: "Strong Breeze",
    8: "Near Gale"
}


def anyIsNone(list):
    for i in list:
        if i is None:
            return True
    return False

# Prints the average conditions where the user has caught fish


def printSuccessRates(conditions):
    filtered_conditions = list(
        filter(lambda x: x["success"] == '1', conditions))
    print("Prominent conditions when fish were caught:")
    print("--------------")
    print("Average Barometric Pressure: " +
          str(sum([float(x["barometric_pressure"]) for x in filtered_conditions]) / len(filtered_conditions)))
    prominent_moon_phase = max(set([x["moon_phase"] for x in filtered_conditions]), key=[
                               x["moon_phase"] for x in filtered_conditions].count)
    print("Prominent Moon Phase: ", MOON_PHASE_NAMES[prominent_moon_phase])
    prominent_tide_phase = max(set([x["tide_phase"] for x in filtered_conditions]), key=[
                               x["tide_phase"] for x in filtered_conditions].count)
    print("Prominent Tide Phase: ", prominent_tide_phase)
    prominent_time_of_day = max(set([x["time_of_day"] for x in filtered_conditions]), key=[
                                x["time_of_day"] for x in filtered_conditions].count)
    print("Prominent Time of Day: ", prominent_time_of_day)
    prominent_weather = max(set([x["weather"] for x in filtered_conditions]), key=[
                            x["weather"] for x in filtered_conditions].count)
    print("Prominent Weather: ", prominent_weather)
    prominent_wind_direction = max(set([x["wind_direction"] for x in filtered_conditions]), key=[
                                   x["wind_direction"] for x in filtered_conditions].count)
    print("Prominent Wind Direction: ",
          WIND_DIRECTION_NAMES[prominent_wind_direction])
    prominent_wind_scale = max(set([x["wind_scale"] for x in filtered_conditions]), key=[
                               x["wind_scale"] for x in filtered_conditions].count)
    print("Prominent Wind Scale: ",
          WIND_SCALE_NAMES[int(prominent_wind_scale)])

# Reads conditions from a file
# File format is:
# barometric_pressure,moon_phase,tide_phase,time_of_day,weather,wind_direction,wind_scale,success
# 29.92,FM,High,Daytime,Clear,N,1,1


def get_conditions_from_file():
    if os.path.isfile("conditions.csv"):
        with open("conditions.csv", "r") as file:
            reader = csv.DictReader(file)
            conditions = []
            for row in reader:
                conditions.append(row)
            return conditions
    else:
        return []


def write_conditions_to_file(conditions):
    with open("conditions_out.csv", "w") as file:
        fieldnames = ["barometric_pressure", "moon_phase", "tide_phase",
                      "time_of_day", "weather", "wind_direction", "wind_scale", "success"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for condition in conditions:
            writer.writerow(condition)


def get_conditions():
    print("Enter the conditions for your fishing session:")

    barometric_pressure = input("Barometric Pressure (inHg): ")
    moon_phase = input("Moon Phase (FM, WG, LQ, WC, NM, WC, FQ, WG): ").upper()
    while moon_phase not in MOON_PHASE_NAMES.keys():
        print("Invalid Moon Phase")
        moon_phase = input(
            "Moon Phase (FM, WG, LQ, WC, NM, WC, FQ, WG): ").upper()
    tide_phase = input("Tide Phase (High, Low): ").lower()
    while tide_phase not in ["high", "low"]:
        print("Invalid Tide Phase")
        tide_phase = input("Tide Phase (High, Low): ").lower()
    time_of_day = input("Time of Day (Daytime, Night): ").lower()
    while time_of_day not in ["daytime", "night"]:
        print("Invalid Time of Day")
        time_of_day = input("Time of Day (Daytime, Night): ").lower()
    weather = input("Weather (Clear, Cloudy, Rain): ").lower()
    while weather not in ["clear", "cloudy", "rain"]:
        print("Invalid Weather")
        weather = input("Weather (Clear, Cloudy, Rain): ").lower()
    wind_direction = input(
        "Wind Direction (N, NE, E, SE, S, SW, W, NW): ").upper()
    while wind_direction not in WIND_DIRECTION_NAMES.keys():
        print("Invalid Wind Direction")
        wind_direction = input(
            "Wind Direction (N, NE, E, SE, S, SW, W, NW): ").upper()
    wind_scale = int(input("Wind Scale (1-8): "))
    while wind_scale not in WIND_SCALE_NAMES.keys():
        print("Invalid Wind Scale")
        wind_scale = int(input("Wind Scale (1-8): "))

    success = input("Did you succeed in catching fish? (0/1): ")
    while success not in ["0", "1"]:
        print("Invalid Success")
        success = input("Did you succeed in catching fish? (0/1): ")

    print()
    return {
        "barometric_pressure": barometric_pressure,
        "moon_phase": moon_phase,
        "tide_phase": tide_phase,
        "time_of_day": time_of_day,
        "weather": weather,
        "wind_direction": wind_direction,
        "wind_scale": wind_scale,
        "success": success
    }


def print_summary(fishing_logs):
    for log in fishing_logs:
        print("Conditions:")
        print("-----------")
        print(
            f"Barometric Pressure: {log['conditions']['barometric_pressure']}")
        print(
            f"Moon Phase: {MOON_PHASE_NAMES[log['conditions']['moon_phase']]}")
        print(f"Tide Phase: {log['conditions']['tide_phase']}")
        print(f"Time of Day: {log['conditions']['time_of_day']}")
        print(f"Weather: {log['conditions']['weather']}")
        print(
            f"Wind Direction: {WIND_DIRECTION_NAMES[log['conditions']['wind_direction']]}")
        print(
            f"Wind Scale: {WIND_SCALE_NAMES[log['conditions']['wind_scale']]}")
        print(f"Success: {log['success']}")

# Calculates the deviation between the historical conditions and the current conditions


def calculate_deviation(historical_conditions, conditions):
    deviation = 0
    for key in conditions.keys():
        if key == "barometric_pressure":
            deviation += abs(
                float(historical_conditions[key]) - float(conditions[key]))
        elif key == "wind_scale":
            deviation += abs(int(historical_conditions[key]
                                 ) - int(conditions[key]))
        else:
            deviation += 1 if historical_conditions[key] == conditions[key] else 0
    return deviation


def main():
    fishing_logs = []

    print("Welcome to the Fishing Smeller!")
    print("-------------------------------")

    fishing_logs = get_conditions_from_file()

    if len(fishing_logs) <= 0:
        print("No historical data found. Please enter your fishing sessions.")

        while True:
            conditions = get_conditions()
            if anyIsNone(conditions) is True:
                break
            print("Would you like to enter another fishing session?")
            print("Enter 'no' to exit the Fishing Smeller\n")
            another_session = input("Enter your choice (y/n): ").lower()
            while another_session not in ["y", "n"]:
                print("Invalid choice")
                another_session = input("Enter your choice (y/n): ").lower()
            if another_session == "n":
                write_conditions_to_file(fishing_logs)
                break

    print("Please enter the conditions for your current fishing session.")
    current_conditions = get_conditions()
    print("-----------------")
    printSuccessRates(fishing_logs)
    print("-----------------")
    print("Deviation from historical conditions: ")
    for log in fishing_logs:
        print("Deviation from historial condtions" + str(log) + ": ")
        print(calculate_deviation(log, current_conditions))
    print("-----------------")
    print("Average deviation from historical conditions: ")
    print(sum([calculate_deviation(log, current_conditions)
          for log in fishing_logs]) / len(fishing_logs))


if __name__ == "__main__":
    main()
