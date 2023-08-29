"""
Voltage Check Test Module.

This module unit tests the voltage check function,
checks if the levels are above or below the threshold.

"""

import random
import unittest

from utilities.voltage_check import VoltageTooHighError, check_voltages


class TestVoltageCheck(unittest.TestCase):
    """
       Test class.

       In this class are added the test methods
       """
    def test_check_voltage_below_limit(self):
        """
        Test checking voltages below the limit.
        """
        voltages_below_limit = [random.randint(0, 190) for _ in range(10)]

        try:
            check_voltages(voltages_below_limit)
        except VoltageTooHighError:
            self.fail("VoltageTooHighError raised unexpectedly.")

    def test_check_voltages_above_limit(self):
        """
        Test checking voltages above the limit.
        """
        voltages_above_limit = [random.randint(191, 220) for _ in range(10)]

        with self.assertRaises(VoltageTooHighError):
            check_voltages(voltages_above_limit)


if __name__ == "__main__":
    unittest.main()
