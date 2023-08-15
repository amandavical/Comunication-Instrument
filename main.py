"""
Comunication-Instrument Main Module.

This module serves as the entry point for the Comunication-Instrument project. It collects temperatures using the
temperature_collection module and checks if they are within permissible limits using the temperature_check module.
"""

from data_collection.current_collection import collect_currents
from data_collection.temperature_collection import collect_temperatures
from utilities.current_check import check_current_threshold
from utilities.temperature_check import (TemperatureTooHighError,
                                         check_temperatures)


def main():
    """
    Entry point for Communication Instrument design.

    Collects and verifies that data (such as temperature, voltage,current) are within allowable limits.
    """
    try:
        temperature_list = collect_temperatures()
        print("Collected Temperatures:", temperature_list)
        check_temperatures(temperature_list)
        print("All temperatures are within limits.")
    except TemperatureTooHighError as e:
        print("Error:", e)

    print("---------------------------------------------------")

    currents = collect_currents()
    print("Collected Current values:", currents)

    for value in currents:
        check_current_threshold(value)

if _name_ == "_main_":
    main()
