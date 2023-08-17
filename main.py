"""
Comunication-Instrument Main Module.

This module serves as the entry point for the Communication-Instrument project. It collects temperatures using the
temperature_collection module and checks if they are within permissible limits using the temperature_check module.
It also collects current values, voltage values, and status information
from other modules and performs necessary checks.

"""

from data_collection.current_collection import collect_currents
from data_collection.type_collection import collect_types
from data_collection.status_collection import collect_statuses
from data_collection.temperature_collection import collect_temperatures
from data_collection.voltage_collection import collect_voltages
from utilities.current_check import check_current_threshold
from utilities.temperature_check import (TemperatureTooHighError,
                                         check_temperatures)
from utilities.voltage_check import VoltageTooHighError, check_voltages


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

    print("---------------------------------------------------")

    try:
        voltages_list = collect_voltages()
        print("Collected Voltages:", voltages_list)
        check_voltages(voltages_list)
        print("All voltages are within limits.")
    except VoltageTooHighError as e:
        print("Error:", e)

    print("---------------------------------------------------")

    try:
        statuses_list = collect_statuses()
        print("Collected Statuses:", statuses_list)
    except:
        print("An error occurred while colleting the statuses")

    print("---------------------------------------------------")

    try:
        types_list = collect_types()
        print("Collected Types:", types_list)
    except:
        print("An error occurred while colleting the types")

    print("---------------------------------------------------")

    data = {
        "temperature": temperature_list,
        "voltage": voltages_list,
        "current": currents,
        "status": statuses_list,
        "type": types_list
    }

    print("All the data is available in the dictionary data:")

    for key in data.keys():
        print(key + ":", data[key])


if __name__ == "__main__":
    main()
