"""
Current Test Module.


This module contains functions to simulate the collection of 6 random statuses and the correct storage.
"""

import random
import unittest
from unittest.mock import MagicMock, patch

from data_collection.status_collection import collect_statuses


class TestStatusCollector(unittest.TestCase):
    """
    Test class.

    In this class are added the test methods
    """
    @patch("modules.comunication_client.Client")
    @patch("modules.simulated_instrument.Instrument")
    def test_collect_status(self, mock_instrument, mock_client):
        """
        Test collection of 5 random status.

        Returns:
        list[int]: List containing status values (0, 0xFFFFFFFF).
        """
        mock_client_instance = MagicMock()
        mock_instrument_instance = MagicMock()

        mock_client.return_value = mock_client_instance
        mock_instrument.return_value = mock_instrument_instance

        mock_client_instance.read_response.side_effect = [random.randint(0, 0xFFFFFFFF) for _ in range(1, 6)]

        result = collect_statuses()

        for status in result:
            self.assertTrue(0 < status < 0xFFFFFFFF)
            print(f"Collected status: {status}")


if __name__ == "__main__":
    unittest.main()
