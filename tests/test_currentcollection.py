"""
Current Test Module.


This module contains functions to simulate the collection of 30 random electric currents and the correct use of the
values defined in the collect_currents function.
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
        list[int]: List containing electric currents values (26, 800).
        """
        mock_client_instance = MagicMock()
        mock_instrument_instance = MagicMock()

        mock_client.return_value = mock_client_instance
        mock_instrument.return_value = mock_instrument_instance

        mock_client_instance.read_response.side_effect = [int(random.randint(0, 2000)) for _ in range(1, 31)]

        result = collect_currents()

        for current in result:
            self.assertTrue(25 < current < 800)
            print(f"Collected currents: {current}")


if __name__ == "__main__":
    unittest.main()
