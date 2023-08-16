"""This module contains a function to simulate connecting to an instrument and collecting 30 random electric currents."""
import serial

from modules.comunication_client import Client
from modules.simulated_instrument import Instrument
from utilities.current_check import check_current_threshold


def collect_currents():
    """
    Simulate connecting to an instrument and collect 30 random current values.

    Returns:
         list[int]: List containing current values.
    """
    client = Client(serial.Serial("COM1", 9600, timeout=2))
    instrument = Instrument(serial.Serial("COM2", 9600, timeout=2))

    currents = []

    for _ in range(1, 31):
        client.write_request("CUR")
        instrument.read_message()
        current = int(client.read_response())
        if 25 < current < 800:
            currents.append(current)

    # Check each individual value within the loop
    check_current_threshold(current)

    return currents
