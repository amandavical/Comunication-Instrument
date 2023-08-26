import unittest
import random
from unittest.mock import MagicMock, patch
from data_collection.current_collection import collect_currents
from modules.comunication_client import Client
from modules.simulated_instrument import Instrument
from utilities.current_check import check_current_threshold

class TestCurrentCollector(unittest.TestCase):
    @patch("modules.comunication_client.Client")
    @patch("modules.simulated_instrument.Instrument")
    @patch("data_collection.current_collection.check_current_threshold")
    def test_collect_currents_above_limit(self, mock_check_current_threshold, mock_instrument, mock_client):
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
        mock_client_instance = MagicMock()
        mock_instrument_instance = MagicMock()

        mock_client.return_value = mock_client_instance
        mock_instrument.return_value = mock_instrument_instance

        mock_client_instance.read_response.side_effect = [int(random.randint(0, 24)) for _ in range(1, 31)]

        result = collect_currents()

        with unittest.mock.patch('builtins.print') as mock_print:
            check_current_threshold(24)
            mock_print.assert_called_once_with("Threshold alert!")

            for current in result:
                if current < 25:
                    print(f"Threshold alert!")


if __name__ == "__main__":
    unittest.main()