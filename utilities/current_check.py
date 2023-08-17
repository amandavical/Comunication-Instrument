"""Utilities for checking electric current values."""


def check_current_threshold(value):
    """
    Contains a method that filters currents, leaving only those above 25mA.

    parameter:
        currents (int): List of currents.
    """
    if value < 25:
        print("Threshold alert!")
