"""
Voltage Check Module.

This module contains a custom exception class and a function to check if voltage are within limits.
The VoltageTooHighError exception is raised if a voltage exceeds 190 volts.

"""


class VoltageTooHighError(Exception):
    """Custom exception for voltage exceeding 190 volts."""

    pass


def check_voltages(voltages):
    """
    Check if any voltage in the list is greater than 190 volts or equal to 0 volts.

    If it is greater than 190 volts, it raises the VoltageTooHighError exception.

    otherwise, it prints "voltage equal to 0, check your equipment".

    Parameters:
        voltages (list[int]): List of voltages.
    """
    for voltage in voltages:
        if voltage > 190:
            raise VoltageTooHighError(
                "Voltage is too high: {} volts".format(voltage)
            )
        elif voltage == 0:
            print("voltage equal to 0, check your equipment")
