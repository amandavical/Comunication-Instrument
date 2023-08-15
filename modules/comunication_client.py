"""
Communication Client Module.

This module contains a simulated client class that communicates with an instrument over a serial port.
"""

import serial


class Client:
    """
    Simulated client class that communicates with an instrument over a serial port.

    This class simulates a client that communicates with an instrument through a serial port.
    It can send requests to the instrument and read responses from the instrument.

    Args:
        ser (serial.Serial): An instance of the `serial.Serial` class representing the serial port.
    """

    def __init__(self, ser: serial.Serial) -> None:
        """
        Initialize the Client with a serial port.

        Args:
            ser (serial.Serial): An instance of the `serial.Serial` class representing the serial port.
        """
        self.ser = ser

    def write_request(self, command: str) -> None:
        """
        Write a request command to the serial port.

        This method writes a request command to the serial port. The command is sent as bytes
        using the UTF-8 encoding.

        Args:
            command (str): The request command to be sent.

        Example:
            client1 = Client(ser)
            client1.write_request("TMP")
        """
        self.ser.write(bytearray(command + "\r\n", "utf-8"))

    def read_response(self) -> str:
        """
        Read a response from the serial port.

        This method reads a response from the serial port and returns it as a string.

        Returns:
            str: The response received from the serial port.

        Example:
            client1 = Client(ser)
            response = client1.read_response()
        """
        response = self.ser.readline().decode().strip()
        return response
