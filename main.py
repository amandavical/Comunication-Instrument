"""
Comunication-Instrument Main Module.

This module serves as the entry point for the Comunication-Instrument project. It collects temperatures using the
temperature_collection module and checks if they are within permissible limits using the temperature_check module.
"""

from data_collection.temperature_collection import collect_temperatures
from utilities.temperature_check import (TemperatureTooHighError,
                                         check_temperatures)

if __name__ == "__main__":
    try:
        temperature_list = collect_temperatures()
        print("Collected Temperatures:", temperature_list)
        check_temperatures(temperature_list)
        print("All temperatures are within limits.")
    except TemperatureTooHighError as e:
        print("Error:", e)
