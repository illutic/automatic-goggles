import csv
from dataclasses import dataclass
from data import WindDirection, WindSpeed, MoonPhase, Tide, Barometer, Data


def read_csv_to_data():
    with open('historical_data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            data = Data(
                windDirection=WindDirection.of(row[0]),
                windSpeed=WindSpeed.of(row[1]),
                moonPhase=MoonPhase.of(row[2]),
                tide=Tide.of(row[3]),
                barometer=Barometer.of(row[4]),
                success=bool(row[5])
            )
            yield data

def write_data_to_csv(data: Data):
    with open('historical_data.csv', 'a+', errors='ignore', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            data.windDirection,
            data.windSpeed,
            data.moonPhase,
            data.tide,
            data.barometer,
            data.success
        ])