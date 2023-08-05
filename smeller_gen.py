import random
import csv

# Define the ranges for each field
barometric_pressure_range = (1, 30)
moon_phases = ['FM', 'WG', 'LQ', 'WC', 'NM', 'WC', 'FQ', 'WG']
tide_phases = ['High', 'Low']
time_of_day = ['Daytime', 'Night']
weather_conditions = ['Clear', 'Cloudy', 'Rain']
wind_directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
wind_scale_range = (1, 8)

# Create a list to store the generated data
data = []

# Generate 1000 random samples
for _ in range(1000):
    barometric_pressure = round(random.uniform(
        barometric_pressure_range[0], barometric_pressure_range[1]), 2)
    moon_phase = random.choice(moon_phases)
    tide_phase = random.choice(tide_phases)
    time_of_day_value = random.choice(time_of_day)
    weather = random.choice(weather_conditions)
    wind_direction = random.choice(wind_directions)
    wind_scale = random.randint(wind_scale_range[0], wind_scale_range[1])
    success = random.randint(0, 1)

    # Append the data to the list
    data.append([barometric_pressure, moon_phase, tide_phase,
                time_of_day_value, weather, wind_direction, wind_scale, success])

# Write the data to a CSV file
with open('conditions.csv', 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['barometric_pressure', 'moon_phase', 'tide_phase',
                        'time_of_day', 'weather', 'wind_direction', 'wind_scale', 'success'])
    csv_writer.writerows(data)

print("Random data generation and writing to CSV completed.")
