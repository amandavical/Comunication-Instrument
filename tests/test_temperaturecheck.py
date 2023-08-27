"""
Temperature Check Unit Tests.

This module contains unit tests for the temperature check functionality,
including checking temperatures below and above the limit.

"""

import random
import unittest

from utilities.temperature_check import (TemperatureTooHighError,
                                         check_temperatures)


class TestTemperatureCheck(unittest.TestCase):
    """
       Test class.

       In this class are added the test methods
       """
    def test_check_temperatures_below_limit(self):
        """
        Test checking temperatures below the limit.
        """
        # Generate a list of 10 random temperatures below the limit (0-80)
        temperatures_below_limit = [random.randint(0, 80) for _ in range(10)]

        try:
            # Check if the TemperatureTooHighError exception is raised unexpectedly
            check_temperatures(temperatures_below_limit)
        except TemperatureTooHighError:
            self.fail("TemperatureTooHighError raised unexpectedly.")

    def test_check_temperatures_above_limit(self):
        """
        Test checking temperatures above the limit.
        """
        # Generate a list of 10 random temperatures above the limit (81-85)
        temperatures_above_limit = [random.randint(81, 85) for _ in range(10)]

        # Check if the TemperatureTooHighError exception is raised as expected
        with self.assertRaises(TemperatureTooHighError):
            check_temperatures(temperatures_above_limit)


if __name__ == "__main__":
    unittest.main()
