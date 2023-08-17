"""
Status Collection Module.

This module contains a function to simulate connecting to an instrument and collecting 5 statuses.

"""
import serial

from modules.comunication_client import Client
from modules.simulated_instrument import Instrument


def collect_statuses():
    """
    Simulate connecting to an instrument and collecting 5 statuses.

    Returns:
         list[int]: List containing statuses.
    """
    client = Client(serial.Serial("COM1", 9600, timeout=2))
    instrument = Instrument(serial.Serial("COM2", 9600, timeout=2))

    statuses = []

    for _ in range(1, 6):
        client.write_request("STA")
        instrument.read_message()
        status = int(client.read_response())
        statuses.append(status)

    return statuses
