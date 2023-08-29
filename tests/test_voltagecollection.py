"""
Voltage Test Module.

This module is responsible for testing the voltage_collection.
Through functions with already expected answers,
it analyzes whether they are all correct according to the check_voltage function

"""

import random
import unittest
from unittest.mock import MagicMock, patch

from data_collection.voltage_collection import collect_voltages


class TestVoltageCollector(unittest.TestCase):
    """
    Test class.

    In this class are added the test methods
    """
    @patch("modules.comunication_client.Client")
    @patch("modules.simulated_instrument.Instrument")
    def test_collect_voltage_above_limit(self, mock_instrument, mock_client):
        """
        Test collection of 20 random voltages between 0 and 220.

        Returns:
        list[int]: List containing voltages values (0, 220).
        """
        mock_client_instance = MagicMock()
        mock_instrument_instance = MagicMock()

        mock_client.return_value = mock_client_instance
        mock_instrument.return_value = mock_instrument_instance

        mock_client_instance.read_response.side_effect = [int(random.randint(0, 220)) for _ in range(1, 21)]

        result = collect_voltages()

        for voltage in result:
            self.assertGreaterEqual(voltage, 0)
            self.assertLessEqual(voltage, 220)
            print(f"Collected voltages: {voltage}")


if __name__ == "__main__":
    unittest.main()
