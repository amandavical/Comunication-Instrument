"""
Temperature Check Module.

This module contains a custom exception class and a function to check if temperatures are within limits.
The TemperatureTooHighError exception is raised if a temperature exceeds 80 degrees.

"""


class TemperatureTooHighError(Exception):
    """Custom exception for temperatures exceeding 80 degrees."""

    pass


def check_temperatures(temperatures):
    """
    Check if any temperature in the list is higher than 80 degrees.

    If found, raises TemperatureTooHighError exception.

    Parameters:
        temperatures (list[int]): List of temperatures.
    """
    for temperature in temperatures:
        if temperature > 80:
            raise TemperatureTooHighError(
                "Temperature is too high: {} degrees".format(temperature)
            )
