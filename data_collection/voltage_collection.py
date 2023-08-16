"""
Voltage Collection Module.

This module contains a function to simulate connecting to an instrument and collecting 20 random voltages.

"""
import serial

from modules.comunication_client import Client
from modules.simulated_instrument import Instrument


def collect_voltages():
    """
    Simulate connecting to an instrument and collect 20 random voltages.

    Returns:
         list[int]: List containing voltages.
    """
    client = Client(serial.Serial("COM1", 9600, timeout=2))
    instrument = Instrument(serial.Serial("COM2", 9600, timeout=2))

    voltages = []

    for _ in range(1, 21):
        client.write_request("VOL")
        instrument.read_message()
        voltage = int(client.read_response())
        voltages.append(voltage)

    return voltages
