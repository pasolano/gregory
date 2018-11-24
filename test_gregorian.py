import calendar
import random
import unittest

class Gregorian_Test(unittest.TestCase):
    # The following method is called before every test.  It creates a Gregorian calendar.
    def setUp(self):
        self.cal = calendar.Gregorian_Calendar()

    # Test month/day/year date to day of year.
    def test_date_to_day_of_year_03_01_1900(self):
        self.assertEqual(60, self.cal.date_to_day_of_year('Mar', 1, 1900))

    def test_date_to_day_of_year_12_31_1968(self):
        self.assertEqual(366, self.cal.date_to_day_of_year('Dec', 31, 1968))

    def test_date_to_day_of_year_01_01_2019(self):
        self.assertEqual(1, self.cal.date_to_day_of_year('Jan', 1, 2019))

    # Test day of year to month/day/year date.
    def test_day_of_year_to_date_1900_60(self):
        self.assertEqual(('Mar', 1, 1900), self.cal.day_of_year_to_date(1900, 60))

    def test_day_of_year_to_date_1969_364(self):
        self.assertEqual(('Dec', 30, 1969), self.cal.day_of_year_to_date(1969, 364))

    def test_day_of_year_to_date_2019_01(self):
        self.assertEqual(('Jan', 1, 2019), self.cal.day_of_year_to_date(2019, 1))

    # Test inverse property.
    def test_inverse(self):
        for d in range(1, 366):
            with self.subTest(i=d):
                ndoy = d
                result = self.cal.day_of_year_to_date(1693, d)
                doy  = self.cal.date_to_day_of_year(*result)
                self.assertEqual(ndoy, doy)
        for d in range(1, 367):
            with self.subTest(i=d):
                ndoy = d
                result = self.cal.day_of_year_to_date(2400, d)
                doy  = self.cal.date_to_day_of_year(*result)
                self.assertEqual(ndoy, doy)                

    # Test bogus dates.
    def test_bogus_day_of_year_2018_366(self):
        with self.assertRaises(RuntimeError):
            self.cal.day_of_year_to_date(2018, 366)

    def test_bogus_day_of_year_1900_0(self):
        with self.assertRaises(RuntimeError):
            self.cal.day_of_year_to_date(1900, 0)

    def test_bogus_date_01_32_1999(self):
        with self.assertRaises(RuntimeError):
            self.cal.date_to_day_of_year('Jan', 32, 1999)

    def test_bogus_date_02_29_1999(self):
        with self.assertRaises(RuntimeError):
            self.cal.date_to_day_of_year('Feb', 29, 1999)
        
    def test_bogus_date_06_37_2019(self):
        with self.assertRaises(RuntimeError):
            self.cal.date_to_day_of_year('Jun', 37, 2019)

    # Test day of year to day of week.
    def test_day_of_year_to_day_of_week_01_01_1800(self):
        self.assertEqual('Wed', self.cal.day_of_year_to_day_of_week(1800, 1))

    def test_day_of_year_to_day_of_week_12_31_1990(self):
        self.assertEqual('Mon', self.cal.day_of_year_to_day_of_week(1990, 365))

    def test_day_of_year_to_day_of_week_12_31_2000(self):
        self.assertEqual('Sun', self.cal.day_of_year_to_day_of_week(2000, 366))

    def test_day_of_year_to_day_of_week_01_01_2001(self):
        self.assertEqual('Mon', self.cal.day_of_year_to_day_of_week(2001, 1))

    def test_day_of_year_to_day_of_week_01_02_2001(self):
        self.assertEqual('Tue', self.cal.day_of_year_to_day_of_week(2001, 2))

    def test_day_of_year_to_day_of_week_03_01_2100(self):
        self.assertEqual('Mon', self.cal.day_of_year_to_day_of_week(2100, 60))

    def test_day_of_year_to_day_of_week_03_01_2101(self):
        self.assertEqual('Tue', self.cal.day_of_year_to_day_of_week(2101, 60))

    # Test date to day of week.
    def test_date_to_day_of_week_01_01_1800(self):
        self.assertEqual('Wed', self.cal.date_to_day_of_week('Jan', 1, 1800))

    def test_date_to_day_of_week_07_20_1969(self):
        self.assertEqual('Sun', self.cal.date_to_day_of_week('Jul', 20, 1969))

    def test_date_to_day_of_week_12_31_1990(self):
        self.assertEqual('Mon', self.cal.date_to_day_of_week('Dec', 31, 1990))

    def test_date_to_day_of_week_12_31_2000(self):
        self.assertEqual('Sun', self.cal.date_to_day_of_week('Dec', 31, 2000))

    def test_date_to_day_of_week_01_01_2001(self):
        self.assertEqual('Mon', self.cal.date_to_day_of_week('Jan', 1, 2001))

    def test_date_to_day_of_week_01_02_2001(self):
        self.assertEqual('Tue', self.cal.date_to_day_of_week('Jan', 2, 2001))

    def test_date_to_day_of_week_12_31_2001(self):
        self.assertEqual('Mon', self.cal.date_to_day_of_week('Dec', 31, 2001))

    def test_date_to_day_of_week_10_18_2018(self):
        self.assertEqual('Thu', self.cal.date_to_day_of_week('Oct', 18, 2018))

    def test_date_to_day_of_week_03_01_2100(self):
        self.assertEqual('Mon', self.cal.date_to_day_of_week('Mar', 1, 2100))

    def test_date_to_day_of_week_03_01_2101(self):
        self.assertEqual('Tue', self.cal.date_to_day_of_week('Mar', 1, 2101))

    # Test Validity Tests
    def test_type_year_is_int_1(self):
        with self.assertRaises(RuntimeError):
            self.cal.day_of_year_to_date('foo', 366)
    def test_type_doy_is_int_1(self):
        with self.assertRaises(RuntimeError):
            self.cal.day_of_year_to_date(2018, 'foo')
    def test_doy_in_range_1(self):
        with self.assertRaises(RuntimeError):
            self.cal.day_of_year_to_date(2018, 367)
    def test_doy_in_range_2(self):
        with self.assertRaises(RuntimeError):
            self.cal.day_of_year_to_date(2018, -1)
    def test_type_year_is_int_2(self):
        with self.assertRaises(RuntimeError):
            self.cal.date_to_day_of_year('bar', 366)
    def test_type_year_is_int_3(self):
        with self.assertRaises(RuntimeError):
            self.cal.date_to_day_of_year('spam', 366)
    def test_type_day_is_str_1(self):
        with self.assertRaises(RuntimeError):
            self.cal.date_to_day_of_year(2018, 'foo')
    def test_doy_in_range_3(self):
        with self.assertRaises(RuntimeError):
            self.cal.day_of_year_to_day_of_week(2020, 367)
    def test_type_day_is_str_2(self):
        with self.assertRaises(RuntimeError):
            self.cal.date_to_day_of_year(13, 2018)
    def test_type_year_is_int_4(self):
        with self.assertRaises(RuntimeError):
            self.cal.date_to_day_of_year('Jan', 13, 'wombat')
if (__name__ == '__main__'):
    print('Testing Gregorian_Calendar...')
    greg_test  = Gregorian_Test()
    unittest.main()
