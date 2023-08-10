from dataclasses import dataclass


@dataclass
class WindDirection:
    North = 0
    NorthEast = 1
    East = 2
    SouthEast = 3
    South = 4
    SouthWest = 5
    West = 6
    NorthWest = 7

    def of(data):
        if int(data) == WindDirection.North:
            return WindDirection.North
        elif int(data) == WindDirection.NorthEast:
            return WindDirection.NorthEast
        elif int(data) == WindDirection.East:
            return WindDirection.East
        elif int(data) == WindDirection.SouthEast:
            return WindDirection.SouthEast
        elif int(data) == WindDirection.South:
            return WindDirection.South
        elif int(data) == WindDirection.SouthWest:
            return WindDirection.SouthWest
        elif int(data) == WindDirection.West:
            return WindDirection.West
        elif int(data) == WindDirection.NorthWest:
            return WindDirection.NorthWest
        else:
            raise ValueError(f'Unknown wind direction: {data}')
    def ofWord(wind_direction: str):
        wind_direction = wind_direction.upper()
        if wind_direction == 'N':
            return WindDirection.North
        elif wind_direction == 'NE':
            return WindDirection.NorthEast
        elif wind_direction == 'E':
            return WindDirection.East
        elif wind_direction == 'SE':
            return WindDirection.SouthEast
        elif wind_direction == 'S':
            return WindDirection.South
        elif wind_direction == 'SW':
            return WindDirection.SouthWest
        elif wind_direction == 'W':
            return WindDirection.West
        elif wind_direction == 'NW':
            return WindDirection.NorthWest
        else:
            raise Exception('Invalid wind direction')


@dataclass
class WindSpeed:
    Calm = 0
    LightAir = 1
    LightBreeze = 2
    GentleBreeze = 3
    ModerateBreeze = 4
    FreshBreeze = 5
    StrongBreeze = 6
    NearGale = 7
    Gale = 8
    StrongGale = 9
    Storm = 10
    ViolentStorm = 11
    Hurricane = 12

    def of(data):
        if int(data) == WindSpeed.Calm:
            return WindSpeed.Calm
        elif int(data) == WindSpeed.LightAir:
            return WindSpeed.LightAir
        elif int(data) == WindSpeed.LightBreeze:
            return WindSpeed.LightBreeze
        elif int(data) == WindSpeed.GentleBreeze:
            return WindSpeed.GentleBreeze
        elif int(data) == WindSpeed.ModerateBreeze:
            return WindSpeed.ModerateBreeze
        elif int(data) == WindSpeed.FreshBreeze:
            return WindSpeed.FreshBreeze
        elif int(data) == WindSpeed.StrongBreeze:
            return WindSpeed.StrongBreeze
        elif int(data) == WindSpeed.NearGale:
            return WindSpeed.NearGale
        elif int(data) == WindSpeed.Gale:
            return WindSpeed.Gale
        elif int(data) == WindSpeed.StrongGale:
            return WindSpeed.StrongGale
        elif int(data) == WindSpeed.Storm:
            return WindSpeed.Storm
        elif int(data) == WindSpeed.ViolentStorm:
            return WindSpeed.ViolentStorm
        elif int(data) == WindSpeed.Hurricane:
            return WindSpeed.Hurricane
        else:
            raise ValueError(f'Unknown wind speed: {data}')

    def ofWord(wind_speed: str):
        wind_speed = wind_speed.upper()

        if wind_speed == 'CALM':
            return WindSpeed.Calm
        elif wind_speed == 'LIGHTAIR':
            return WindSpeed.LightAir
        elif wind_speed == 'LIGHTBREEZE':
            return WindSpeed.LightBreeze
        elif wind_speed == 'GENTLEBREEZE':
            return WindSpeed.GentleBreeze
        elif wind_speed == 'MODERATEBREEZE':
            return WindSpeed.ModerateBreeze
        elif wind_speed == 'FRESHBREEZE':
            return WindSpeed.FreshBreeze
        elif wind_speed == 'STRONGBREEZE':
            return WindSpeed.StrongBreeze
        elif wind_speed == 'NEARGALE':
            return WindSpeed.NearGale
        elif wind_speed == 'GALE':
            return WindSpeed.Gale
        elif wind_speed == 'STRONGGALE':
            return WindSpeed.StrongGale
        elif wind_speed == 'STORM':
            return WindSpeed.Storm
        elif wind_speed == 'CIOLENTSTORM':
            return WindSpeed.ViolentStorm
        elif wind_speed == 'HURRICANE':
            return WindSpeed.Hurricane
        else:
            raise Exception('Invalid wind speed')

@dataclass
class MoonPhase:
    FullMoon = 0
    WaxingGibbous = 1
    FirstQuarter = 2
    WaxingCrescent = 3
    NewMoon = 4
    WaningCrescent = 5
    LastQuarter = 6
    WaningGibbous = 7

    def of(data):
        if int(data) == MoonPhase.FullMoon:
            return MoonPhase.FullMoon
        elif int(data) == MoonPhase.WaxingGibbous:
            return MoonPhase.WaxingGibbous
        elif int(data) == MoonPhase.FirstQuarter:
            return MoonPhase.FirstQuarter
        elif int(data) == MoonPhase.WaxingCrescent:
            return MoonPhase.WaxingCrescent
        elif int(data) == MoonPhase.NewMoon:
            return MoonPhase.NewMoon
        elif int(data) == MoonPhase.WaningCrescent:
            return MoonPhase.WaningCrescent
        elif int(data) == MoonPhase.LastQuarter:
            return MoonPhase.LastQuarter
        elif int(data) == MoonPhase.WaningGibbous:
            return MoonPhase.WaningGibbous
        else:
            raise ValueError(f'Unknown moon phase: {data}')

    def ofWord(moon_phase: str):
        moon_phase = moon_phase.upper()
        if moon_phase == 'FULLMOON':
            return MoonPhase.FullMoon
        elif moon_phase == 'WAXINGGIBBOUS':
            return MoonPhase.WaxingGibbous
        elif moon_phase == 'FIRSTQUARTER':
            return MoonPhase.FirstQuarter
        elif moon_phase == 'WAXINGCRESCENT':
            return MoonPhase.WaxingCrescent
        elif moon_phase == 'NEWMOON':
            return MoonPhase.NewMoon
        elif moon_phase == 'WANINGCRESCENT':
            return MoonPhase.WaningCrescent
        elif moon_phase == 'LASTQUARTER':
            return MoonPhase.LastQuarter
        elif moon_phase == 'WANINGGIBBOUS':
            return MoonPhase.WaningGibbous
        else:
            raise Exception('Invalid moon phase')

@dataclass
class Tide:
    HighRaising = 0
    HighFalling = 1
    LowRaising = 2
    LowFalling = 3

    def of(data):
        if int(data) == Tide.HighRaising:
            return Tide.HighRaising
        elif int(data) == Tide.HighFalling:
            return Tide.HighFalling
        elif int(data) == Tide.LowRaising:
            return Tide.LowRaising
        elif int(data) == Tide.LowFalling:
            return Tide.LowFalling
        else:
            raise ValueError(f'Unknown tide: {data}')

    def ofWord(tide: str):
        tide = tide.upper()

        if tide == 'HIGHRAISING':
            return Tide.HighRaising
        elif tide == 'HIGHFALLING':
            return Tide.HighFalling
        elif tide == 'LOWRAISING':
            return Tide.LowRaising
        elif tide == 'LOWFALLING':
            return Tide.LowFalling
        else:
            raise Exception('Invalid tide')

@dataclass
class Barometer:
    Rising = 0
    Falling = 1
    Steady = 2

    def of(data):
        if int(data) == Barometer.Rising:
            return Barometer.Rising
        elif int(data) == Barometer.Falling:
            return Barometer.Falling
        elif int(data) == Barometer.Steady:
            return Barometer.Steady
        else:
            raise ValueError(f'Unknown barometer: {data}')
        
    def ofWord(barometer: str):
        barometer = barometer.upper()

        if barometer == 'RISING':
            return Barometer.Rising
        elif barometer == 'FALLING':
            return Barometer.Falling
        elif barometer == 'STEADY':
            return Barometer.Steady
        else:
            raise Exception('Invalid barometer')


@dataclass
class Data:
    windDirection: WindDirection
    windSpeed: WindSpeed
    moonPhase: MoonPhase
    tide: Tide
    barometer: Barometer
    success: bool
