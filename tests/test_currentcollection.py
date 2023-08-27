"""
Current Test Module.


This module contains functions to simulate the collection of 30 random electric currents and the correct use of the
values defined in the collect_currents and check_current_threshold functions.
"""

import random
import unittest
from unittest.mock import MagicMock, patch

from data_collection.current_collection import collect_currents


class TestCurrentCollector(unittest.TestCase):
    """
    Test class.

    In this class are added the test methods
    """
    @patch("modules.comunication_client.Client")
    @patch("modules.simulated_instrument.Instrument")
    def test_collect_currents_at_limit(self, mock_instrument, mock_client):
        """
        Test collection of 30 random electrical currents between 0 and 2000.
        Returns:
        list[int]: List containing electric currents values (0, 2000).
        """
        mock_client_instance = MagicMock()
        mock_instrument_instance = MagicMock()

        mock_client.return_value = mock_client_instance
        mock_instrument.return_value = mock_instrument_instance

        mock_client_instance.read_response.side_effect = [int(random.randint(0, 2000)) for _ in range(1, 31)]

        result = collect_currents()

        for current in result:
            self.assertTrue(25 < current < 2000)
            print(f"Collected currents: {current}")

    @patch("modules.comunication_client.Client")
    @patch("modules.simulated_instrument.Instrument")
    @patch("data_collection.current_collection.check_current_threshold")
    def test_collect_currents_below_limit(self, mock_check_current_threshold, mock_instrument, mock_client):
        """
        Test collection of 30 random electrical currents between 0 and 24 for error message verification.

        Returns:
        list[int]: List containing electric currents values (0, 24).
        """
        mock_client_instance = MagicMock()
        mock_instrument_instance = MagicMock()

        mock_client.return_value = mock_client_instance
        mock_instrument.return_value = mock_instrument_instance

        mock_client_instance.read_response.side_effect = [int(random.randint(0, 24)) for _ in range(1, 31)]

        result = collect_currents()

        with unittest.mock.patch('builtins.print') as mock_print:
            for current in result:
                if current < 25:
                    mock_check_current_threshold(current)
                    mock_print.assert_called_once_with("Threshold alert!")
                else:
                    mock_check_current_threshold(current)
                    mock_print.assert_not_called()


if __name__ == "__main__":
    unittest.main()
