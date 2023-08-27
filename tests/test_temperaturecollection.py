"""
Unit Test for Temperature Collection Module.

This module contains a unit test case for the temperature collection module.
It simulates the collection of 20 random temperatures between 0 and 85 degrees.
The test ensures that the collected temperatures fall within the specified range.

"""

import random
import unittest
from unittest.mock import MagicMock, patch

from data_collection.temperature_collection import collect_temperatures


class TestTemperatureCollector(unittest.TestCase):
    """
       Test class.

       In this class are added the test methods
       """
    @patch("modules.comunication_client.Client")
    @patch("modules.simulated_instrument.Instrument")
    def test_collect_temperatures_above_limit(self, mock_instrument, mock_client):
        """
        Test the collection of 20 random temperatures between 0 and 85.

        This test validates the behavior of collecting a set of temperatures within the range of 0 to 85 degrees.
        It uses mock objects to simulate the client and instrument

       Returns:
          list[int]: List containing temperature values (0, 85).
        """

        mock_client_instance = MagicMock()
        mock_instrument_instance = MagicMock()

        # Set up the mock objects with return values for the read_response method
        mock_client.return_value = mock_client_instance
        mock_instrument.return_value = mock_instrument_instance
        mock_client_instance.read_response.side_effect = [int(random.randint(0, 85)) for _ in range(1, 21)]

        # Call the collect_temperatures function
        result = collect_temperatures()

        # Validate that collected temperatures are within the specified range
        for temperature in result:
            self.assertTrue(0 <= temperature <= 85)
            print(f"Collected temperature: {temperature}")


if __name__ == "__main__":
    unittest.main()
