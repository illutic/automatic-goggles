
from data import Data, WindDirection, WindSpeed, MoonPhase, Tide, Barometer
from typing import Iterable


def calculate_percentages(historical_data: Iterable[Data]):
    success_data = list(filter(lambda x: x.success == True, historical_data))

    n_success_wind_dir = list(filter(
        lambda x: x.windDirection == WindDirection.North, success_data))
    n_success_wind_dir_rate = len(n_success_wind_dir) / len(success_data)

    ne_success_wind_dir = list(filter(
        lambda x: x.windDirection == WindDirection.NorthEast, success_data))
    ne_success_wind_dir_rate = len(ne_success_wind_dir) / len(success_data)

    e_success_wind_dir = list(filter(
        lambda x: x.windDirection == WindDirection.East, success_data))
    e_success_wind_dir_rate = len(e_success_wind_dir) / len(success_data)

    se_success_wind_dir = list(filter(
        lambda x: x.windDirection == WindDirection.SouthEast, success_data))
    se_success_wind_dir_rate = len(se_success_wind_dir) / len(success_data)

    s_success_wind_dir = list(filter(
        lambda x: x.windDirection == WindDirection.South, success_data))
    s_success_wind_dir_rate = len(s_success_wind_dir) / len(success_data)

    sw_success_wind_dir = list(filter(
        lambda x: x.windDirection == WindDirection.SouthWest, success_data))
    sw_success_wind_dir_rate = len(sw_success_wind_dir) / len(success_data)

    w_success_wind_dir = list(filter(
        lambda x: x.windDirection == WindDirection.West, success_data))
    w_success_wind_dir_rate = len(w_success_wind_dir) / len(success_data)

    nw_success_wind_dir = list(filter(
        lambda x: x.windDirection == WindDirection.NorthWest, success_data))
    nw_success_wind_dir_rate = len(nw_success_wind_dir) / len(success_data)

    calm_success_wind_spd = list(filter(
        lambda x: x.windSpeed == WindSpeed.Calm, success_data))
    calm_success_wind_spd_rate = len(calm_success_wind_spd) / len(success_data)

    light_air_success_wind_spd = list(filter(
        lambda x: x.windSpeed == WindSpeed.LightAir, success_data))
    light_air_success_rate = len(
        light_air_success_wind_spd) / len(success_data)

    light_breeze_success_wind_spd = list(filter(
        lambda x: x.windSpeed == WindSpeed.LightBreeze, success_data))
    light_breeze_success_rate = len(
        light_breeze_success_wind_spd) / len(success_data)

    gentle_breeze_success_wind_spd = list(filter(
        lambda x: x.windSpeed == WindSpeed.GentleBreeze, success_data))
    gentle_breeze_success_rate = len(
        gentle_breeze_success_wind_spd) / len(success_data)

    moderate_breeze_success_wind_spd = list(filter(
        lambda x: x.windSpeed == WindSpeed.ModerateBreeze, success_data))
    moderate_breeze_success_rate = len(
        moderate_breeze_success_wind_spd) / len(success_data)

    fresh_breeze_success_wind_spd = list(filter(
        lambda x: x.windSpeed == WindSpeed.FreshBreeze, success_data))
    fresh_breeze_success_rate = len(
        fresh_breeze_success_wind_spd) / len(success_data)

    strong_breeze_success_wind_spd = list(filter(
        lambda x: x.windSpeed == WindSpeed.StrongBreeze, success_data))
    strong_breeze_success_rate = len(
        strong_breeze_success_wind_spd) / len(success_data)

    near_gale_success_wind_spd = list(filter(
        lambda x: x.windSpeed == WindSpeed.NearGale, success_data))
    high_wind_success_rate = len(
        near_gale_success_wind_spd) / len(success_data)

    gale_success_wind_spd = list(filter(
        lambda x: x.windSpeed == WindSpeed.Gale, success_data))
    gale_success_rate = len(gale_success_wind_spd) / len(success_data)

    strong_gale_success_wind_spd = list(filter(
        lambda x: x.windSpeed == WindSpeed.StrongGale, success_data))
    strong_gale_success_rate = len(
        strong_gale_success_wind_spd) / len(success_data)

    storm_success_wind_spd = list(filter(
        lambda x: x.windSpeed == WindSpeed.Storm, success_data))
    storm_success_rate = len(storm_success_wind_spd) / len(success_data)

    hurricane_success_wind_spd = list(filter(
        lambda x: x.windSpeed == WindSpeed.Hurricane, success_data))
    hurricane_success_rate = len(
        hurricane_success_wind_spd) / len(success_data)

    waxing_crescent_success_moon_phase = list(filter(
        lambda x: x.moonPhase == MoonPhase.WaxingCrescent, success_data))
    waxing_crescent_success_moon_phase_rate = len(
        waxing_crescent_success_moon_phase) / len(success_data)

    first_quarter_success_moon_phase = list(filter(
        lambda x: x.moonPhase == MoonPhase.FirstQuarter, success_data))
    first_quarter_success_moon_phase_rate = len(
        first_quarter_success_moon_phase) / len(success_data)

    waxing_gibbous_success_moon_phase = list(filter(
        lambda x: x.moonPhase == MoonPhase.WaxingGibbous, success_data))
    waxing_gibbous_success_moon_phase_rate = len(
        waxing_gibbous_success_moon_phase) / len(success_data)

    new_moon_success_moon_phase = list(filter(
        lambda x: x.moonPhase == MoonPhase.NewMoon, success_data))
    new_moon_success_moon_phase_rate = len(
        new_moon_success_moon_phase) / len(success_data)

    full_moon_success_moon_phase = list(filter(
        lambda x: x.moonPhase == MoonPhase.FullMoon, success_data))
    full_moon_success_moon_phase_rate = len(
        full_moon_success_moon_phase) / len(success_data)

    waning_gibbous_success_moon_phase = list(filter(
        lambda x: x.moonPhase == MoonPhase.WaningGibbous, success_data))
    waning_gibbous_success_moon_phase_rate = len(
        waning_gibbous_success_moon_phase) / len(success_data)

    last_quarter_success_moon_phase = list(filter(
        lambda x: x.moonPhase == MoonPhase.LastQuarter, success_data))
    last_quarter_success_moon_phase_rate = len(
        last_quarter_success_moon_phase) / len(success_data)

    waning_crescent_success_moon_phase = list(filter(
        lambda x: x.moonPhase == MoonPhase.WaningCrescent, success_data))
    waning_crescent_success_moon_phase_rate = len(
        waning_crescent_success_moon_phase) / len(success_data)

    high_raing_rate_success = list(filter(
        lambda x: x.tide == Tide.HighRaising, success_data))
    high_raing_rate_success_rate = len(
        high_raing_rate_success) / len(success_data)

    high_falling_rate_success = list(filter(
        lambda x: x.tide == Tide.HighFalling, success_data))
    high_falling_rate_success_rate = len(
        high_falling_rate_success) / len(success_data)

    low_raising_rate_success = list(filter(
        lambda x: x.tide == Tide.LowRaising, success_data))
    low_raising_rate_success_rate = len(
        low_raising_rate_success) / len(success_data)

    low_falling_rate_success = list(filter(
        lambda x: x.tide == Tide.LowFalling, success_data))
    low_falling_rate_success_rate = len(
        low_falling_rate_success) / len(success_data)

    barometer_rising_success = list(filter(
        lambda x: x.barometer == Barometer.Rising, success_data))
    barometer_rising_success_rate = len(
        barometer_rising_success) / len(success_data)

    barometer_falling_success = list(filter(
        lambda x: x.barometer == Barometer.Falling, success_data))
    barometer_falling_success_rate = len(
        barometer_falling_success) / len(success_data)

    barometer_steady_success = list(filter(
        lambda x: x.barometer == Barometer.Steady, success_data))
    barometer_steady_success_rate = len(
        barometer_steady_success) / len(success_data)

    print("Success Rates per Attribute")
    print("Wind Direction")
    print("North: " + str(n_success_wind_dir_rate * 100) + ' %')
    print("North East: " + str(ne_success_wind_dir_rate * 100) + ' %')
    print("East: " + str(e_success_wind_dir_rate * 100) + ' %')
    print("South East: " + str(se_success_wind_dir_rate * 100) + ' %')
    print("South: " + str(s_success_wind_dir_rate * 100) + ' %')
    print("South West: " + str(sw_success_wind_dir_rate * 100) + ' %')
    print("West: " + str(w_success_wind_dir_rate * 100) + ' %')
    print("North West: " + str(nw_success_wind_dir_rate * 100) + ' %')

    print("Wind Speed")
    print("Calm: " + str(calm_success_wind_spd_rate * 100) + ' %')
    print("Light Air: " + str(light_air_success_rate * 100) + ' %')
    print("Light Breeze: " + str(light_breeze_success_rate * 100) + ' %')
    print("Gentle Breeze: " + str(gentle_breeze_success_rate * 100) + ' %')
    print("Moderate Breeze: " + str(moderate_breeze_success_rate * 100) + ' %')
    print("Fresh Breeze: " + str(fresh_breeze_success_rate * 100) + ' %')
    print("Strong Breeze: " + str(strong_breeze_success_rate * 100) + ' %')
    print("High Wind: " + str(high_wind_success_rate * 100) + ' %')
    print("Gale: " + str(gale_success_rate * 100) + ' %')
    print("Strong Gale: " + str(strong_gale_success_rate * 100) + ' %')
    print("Storm: " + str(storm_success_rate * 100) + ' %')
    print("Hurricane: " + str(hurricane_success_rate * 100) + ' %')

    print("Moon Phase")
    print("New Moon: " + str(new_moon_success_moon_phase_rate * 100) + ' %')
    print("Waxing Crescent: " +
          str(waxing_crescent_success_moon_phase_rate * 100) + ' %')
    print("First Quarter: " + str(first_quarter_success_moon_phase_rate * 100) + ' %')
    print("Waxing Gibbous: " +
          str(waxing_gibbous_success_moon_phase_rate * 100) + ' %')
    print("Full Moon: " + str(full_moon_success_moon_phase_rate * 100) + ' %')
    print("Waning Gibbous: " +
          str(waning_gibbous_success_moon_phase_rate * 100) + ' %')
    print("Last Quarter: " + str(last_quarter_success_moon_phase_rate * 100) + ' %')
    print("Waning Crescent: " +
          str(waning_crescent_success_moon_phase_rate * 100) + ' %')

    print("Tide")
    print("High Raising: " + str(high_raing_rate_success_rate * 100) + ' %')
    print("High Falling: " + str(high_falling_rate_success_rate * 100) + ' %')
    print("Low Raising: " + str(low_raising_rate_success_rate * 100) + ' %')
    print("Low Falling: " + str(low_falling_rate_success_rate * 100) + ' %')

    print("Barometer")
    print("Rising: " + str(barometer_rising_success_rate * 100) + ' %')
    print("Falling: " + str(barometer_falling_success_rate * 100) + ' %')
    print("Steady: " + str(barometer_steady_success_rate * 100) + ' %')
