import calendar
import unittest

class French_Test(unittest.TestCase):
    # The following method is called before every test.  It creates a French Revolutionary calendar.
    def setUp(self):
        self.cal = calendar.Calendrier_Républicain()

    # Test date to day of week.
    def test_date_to_day_of_week_03_01_1900(self):
        self.assertEqual('primidi', self.cal.date_to_day_of_week('Frimaire', 1, 1900))

    # Test month/day/year date to day of year.
    def test_date_to_day_of_year_03_01_1900(self):
        self.assertEqual(60, self.cal.date_to_day_of_year('Brumaire', 30, 1900))
    def test_date_to_day_of_year_vertue_1968(self):
        self.assertEqual(361, self.cal.date_to_day_of_year('Jour de la vertu', 1968))
    def test_date_to_day_of_year_genie_1968(self):
        self.assertEqual(362, self.cal.date_to_day_of_year('Jour du génie', 1968))
    def test_date_to_day_of_year_travail_1968(self):
        self.assertEqual(363, self.cal.date_to_day_of_year('Jour du travail', 1968))                             
    def test_date_to_day_of_year_opinion_1968(self):
        self.assertEqual(364, self.cal.date_to_day_of_year("Jour de l'opinion", 1968))
    def test_date_to_day_of_year_recompenses_1968(self):
        self.assertEqual(365, self.cal.date_to_day_of_year('Jour des récompenses', 1968))
    def test_date_to_day_of_year_revolution_1968(self):
        self.assertEqual(366, self.cal.date_to_day_of_year('Jour de la Révolution', 1968))

    # Test day of year to month/day/year date.
    def test_day_of_year_to_date_1900_60(self):
        self.assertEqual(('Frimaire', 1, 1900), self.cal.day_of_year_to_date(1900, 61))

    def test_day_of_year_to_date_1969_364(self):
        self.assertEqual(("Jour de l'opinion", 1969), self.cal.day_of_year_to_date(1969, 364))

    def test_day_of_year_to_date_2019_01(self):
        self.assertEqual(('Vendémiaire', 1, 2019), self.cal.day_of_year_to_date(2019, 1))

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
            self.cal.day_of_year_to_date(2018, 366)

    def test_bogus_day_of_year_1900_0(self):
        with self.assertRaises(RuntimeError):        
            self.cal.day_of_year_to_date(1900, 0)

    def test_bogus_date_01_32_1999(self):
        with self.assertRaises(RuntimeError):        
            self.cal.date_to_day_of_year('Vendémiaire', 32, 1999)

    def test_bogus_date_02_29_1999(self):
        with self.assertRaises(RuntimeError):        
            self.cal.date_to_day_of_year('Jour de la vertu', 2, 1999)

    def test_bogus_date_06_37_2019(self):
        with self.assertRaises(RuntimeError):
            self.cal.date_to_day_of_year('Brumaire', -2, 2019)

    # Test day of year to day of week.
    def test_day_of_year_to_day_of_week_01_01_1800(self):
        self.assertEqual('primidi', self.cal.day_of_year_to_day_of_week(1800, 1))

    def test_day_of_year_to_day_of_week_12_31_1990(self):
        self.assertEqual('Jour des récompenses', self.cal.day_of_year_to_day_of_week(1990, 365))

    def test_day_of_year_to_day_of_week_12_31_2000(self):
        self.assertEqual('Jour de la Révolution', self.cal.day_of_year_to_day_of_week(2000, 366))

    def test_day_of_year_to_day_of_week_01_01_2001(self):
        self.assertEqual('primidi', self.cal.day_of_year_to_day_of_week(2001, 1))

    def test_day_of_year_to_day_of_week_01_02_2001(self):
        self.assertEqual('duodi', self.cal.day_of_year_to_day_of_week(2001, 2))

    def test_day_of_year_to_day_of_week_02_30_2100(self):
        self.assertEqual('décadi', self.cal.day_of_year_to_day_of_week(2100, 60))

    def test_day_of_year_to_day_of_week_03_01_2101(self):
        self.assertEqual('primidi', self.cal.day_of_year_to_day_of_week(2101, 61))
        
if (__name__ == '__main__'):
    print('Testing Calendrier_Républicain...')
    french_test = French_Test()
    unittest.main()
