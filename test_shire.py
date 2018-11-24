import calendar
import random
import unittest

class Shire_Test(unittest.TestCase):
    # The following method is called before every test.  It creates a calendar.
    def setUp(self):
        self.cal = calendar.Shire_Calendar()

    # Test month/day/year date to day of year.
    def test_date_to_day_of_year_Sol_01_1418(self):
        self.assertEqual(32, self.cal.date_to_day_of_year('Solmath', 1, 1418))
    def test_date_to_day_of_year_Sol_01_1420(self):
        self.assertEqual(32, self.cal.date_to_day_of_year('Solmath', 1, 1420))
    def test_date_to_day_of_year_2Yule_1901(self):
        self.assertEqual(1, self.cal.date_to_day_of_year('2 Yule', 1901))
    def test_date_to_day_of_year_1Lithe_1420(self):
        self.assertEqual(182, self.cal.date_to_day_of_year('1 Lithe', 1420))
    def test_date_to_day_of_year_midyear_1418(self):
        self.assertEqual(183, self.cal.date_to_day_of_year("Midyear's Day", 1418))
    def test_date_to_day_of_year_midyear_1420(self):
        self.assertEqual(183, self.cal.date_to_day_of_year("Midyear's Day", 1420))
    def test_date_to_day_of_year_overlithe_1420(self):
        self.assertEqual(184, self.cal.date_to_day_of_year("Overlithe", 1420))
    def test_date_to_day_of_year_2Lithe_1418(self):
        self.assertEqual(184, self.cal.date_to_day_of_year('2 Lithe', 1418))        
    def test_date_to_day_of_year_2Lithe_1420(self):
        self.assertEqual(185, self.cal.date_to_day_of_year('2 Lithe', 1420))
    def test_date_to_day_of_year_1Yule_1420(self):
        self.assertEqual(366, self.cal.date_to_day_of_year('1 Yule', 1420))
    def test_date_to_day_of_year_1Yule_1901(self):
        self.assertEqual(365, self.cal.date_to_day_of_year('1 Yule', 1901))        

    # Test day of year to month/day/year date.
    def test_day_of_year_to_date_1420_183(self):
        self.assertEqual(("Midyear's Day", 1420), self.cal.day_of_year_to_date(1420, 183))
    def test_day_of_year_to_date_1420_184(self):
        self.assertEqual(("Overlithe", 1420), self.cal.day_of_year_to_date(1420, 184))
    def test_day_of_year_to_date_1600_01(self):
        self.assertEqual(('2 Yule', 1600), self.cal.day_of_year_to_date(1600, 1))
    def test_day_of_year_to_date_1600_365(self):
        self.assertEqual(('1 Yule', 1600), self.cal.day_of_year_to_date(1600, 365))
    def test_day_of_year_to_date_1601_365(self):
        self.assertEqual(('1 Yule', 1601), self.cal.day_of_year_to_date(1601, 365))
    def test_day_of_year_to_date_1601_01(self):
        self.assertEqual(('2 Yule', 1601), self.cal.day_of_year_to_date(1601, 1))

    # Test inverse property.
    def test_inverse(self):
        for d in range(1, 366):
            with self.subTest(i=d):
                ndoy = d
                result = self.cal.day_of_year_to_date(1693, d)
                doy  = self.cal.date_to_day_of_year(*result)
                self.assertEqual(ndoy, doy)

    # Test bogus dates.
    def test_bogus_day_of_year_2018_366(self):
        with self.assertRaises(RuntimeError):
            self.cal.day_of_year_to_date(2000, 366)
    def test_bogus_day_of_year_2000_366(self):
        with self.assertRaises(RuntimeError):
            self.cal.day_of_year_to_date(2000, 366)
    def test_bogus_day_of_year_1900_0(self):
        with self.assertRaises(RuntimeError):
            self.cal.day_of_year_to_date(1900, 0)
    def test_bogus_month_jan(self):
        with self.assertRaises(RuntimeError):
            self.cal.date_to_day_of_year('Jan', 23, 1999)
    def test_bogus_day_of_month_2Yule_2(self):
        with self.assertRaises(RuntimeError):
            self.cal.date_to_day_of_year('2 Yule', 2, 1999)
    def test_bogus_day_of_Afteryule(self):
        with self.assertRaises(RuntimeError):
            self.cal.date_to_day_of_year('Afteryule', 31, 1999)
    def test_date_to_day_of_year_overlithe_1418(self):
        with self.assertRaises(RuntimeError):
            self.cal.date_to_day_of_year("Overlithe", 1418)

    # Test day of year to day of week.
    def test_day_of_year_1800_01(self):
        self.assertEqual('Sterday', self.cal.day_of_year_to_day_of_week(1800, 1))
    def test_day_of_year_1420_01(self):
        self.assertEqual('Sterday', self.cal.day_of_year_to_day_of_week(1420, 1))
    def test_day_of_year_1400_01(self):
        self.assertEqual('Sterday', self.cal.day_of_year_to_day_of_week(1400, 1))
    def test_day_of_year_1400_07(self):
        self.assertEqual('Highday', self.cal.day_of_year_to_day_of_week(1400, 7))
    def test_day_of_year_1400_08(self):
        self.assertEqual('Sterday', self.cal.day_of_year_to_day_of_week(1400, 8))
    def test_day_of_year_1400_365(self):
        self.assertEqual('Highday', self.cal.day_of_year_to_day_of_week(1400, 365))
    def test_day_of_year_1401_01(self):
        self.assertEqual('Sterday', self.cal.day_of_year_to_day_of_week(1401, 1))

    # Test date to day of week.
    def test_date_to_day_of_week_01_02_1419(self):
        self.assertEqual('Monday', self.cal.date_to_day_of_week('Afteryule', 2, 1419))
    def test_date_to_day_of_week_01_02_2020(self):
        self.assertEqual('Monday', self.cal.date_to_day_of_week('Afteryule', 2, 2020))
    def test_date_to_day_of_week_07_02_1419(self):
        self.assertEqual('Monday', self.cal.date_to_day_of_week('Afterlithe', 2, 1419))
    def test_date_to_day_of_week_07_02_2020(self):
        self.assertEqual('Monday', self.cal.date_to_day_of_week('Afterlithe', 2, 2020))
    def test_date_to_day_of_week_1Lithe_2020(self):
        self.assertEqual('Highday', self.cal.date_to_day_of_week('1 Lithe', 2020))
        
if (__name__ == '__main__'):
    print('Testing Shire_Calendar...')
    shire_test = Shire_Test()
    unittest.main()
