"""
Type Collection Module.

This module contains a function to simulate connecting to an instrument and collecting 5 Types.

"""
import serial

from modules.comunication_client import Client
from modules.simulated_instrument import Instrument


def collect_types():
    """
    Simulate connecting to an instrument and collecting 5 types.

    Returns:
         list[str]: List containing types.
    """
    client = Client(serial.Serial("COM1", 9600, timeout=2))
    instrument = Instrument(serial.Serial("COM2", 9600, timeout=2))

    types = []

    for _ in range(1, 6):
        client.write_request("TYP")
        instrument.read_message()
        type = str(client.read_response())
        types.append(type)

    return types
