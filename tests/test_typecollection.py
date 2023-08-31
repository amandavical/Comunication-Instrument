"""
Type Test Module.


This module contains functions to simulate the collection of 6 random types and the correct storage.
"""

import random
import unittest
from unittest.mock import MagicMock, patch

from data_collection.type_collection import collect_types


class TestTypeCollector(unittest.TestCase):
    """
    Test class.

    In this class are added the test methods
    """
    @patch("modules.comunication_client.Client")
    @patch("modules.simulated_instrument.Instrument")
    def test_collect_currents_at_limit(self, mock_instrument, mock_client):
        """
        Test collection of 5 random types.

        Returns:
        list[int]: List containing typ values.
        """
        mock_client_instance = MagicMock()
        mock_instrument_instance = MagicMock()

        mock_client.return_value = mock_client_instance
        mock_instrument.return_value = mock_instrument_instance

        mock_client_instance.read_response.side_effect = [random.choice(["a", "b", "c", "abc"]) for _ in range(1, 6)]

        result = collect_types()

        for typ in result:
            self.assertTrue(typ in ["a", "b", "c", "abc"])
            print(f"Collected types: {typ}")


if __name__ == "__main__":
    unittest.main()
