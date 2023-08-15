"""
Temperature Collection Module.

This module contains a function to simulate connecting to an instrument and collecting 20 random temperatures.

"""
import serial

from modules.comunication_client import Client
from modules.simulated_instrument import Instrument


def collect_temperatures():
    """
    Simulate connecting to an instrument and collect 20 random temperatures.

    Returns:
         list[int]: List containing temperatures.
    """
    client = Client(serial.Serial("COM1", 9600, timeout=2))
    instrument = Instrument(serial.Serial("COM2", 9600, timeout=2))

    temperatures = []

    for _ in range(1, 21):
        client.write_request("TMP")
        instrument.read_message()
        temperature = int(client.read_response())
        temperatures.append(temperature)

    return temperatures
