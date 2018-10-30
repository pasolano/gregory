class Gregorian_Calendar(object):
    def __init__(self):
        self.__leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.__reg = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.__week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __leap_test(self, test_year):
        if (test_year % 100 == 0 and test_year % 400 == 0) or (test_year % 4 == 0 and test_year % 100 != 0):
            return True
        else:
            return False

    def __days_in_year(self, test_year):
        if self.__leap_test(test_year) == True:
            return 366
        else:
            return 365

    def __days_list(self, test_year):
        if self.__leap_test(test_year) == True:
            return self.__leap
        else:
            return self.__reg
        
    def __year_test(self, year):
        if year > 1752:
            return True
        else:
            return False
    
    def __validity_test_one(self, year, day_of_year):
        if self.__year_test(year) == True:
            if self.__leap_test(year) and self.__year_test(year) == True:
                if day_of_year <= 366:
                    return True
                else:
                    return False
            else:
                if day_of_year <= 365:
                    return True
                else:
                    return False
        else:
            return False

    def __validity_test_two(self, month, day, year):
        days_list = self.__days_list(year)
        if all( [self.__year_test(year) == True, month > 0, month <= 12, day > 0] ):
            if day <= days_list[month - 1]:
                return True
            else:
                return False
        else:
            return False

    def day_of_year_to_date(self, year, day_of_year):
        if self.__validity_test_one(year, day_of_year) == True:
            days_list = self.__days_list(year)
            month = 0
            month_sum = 0
            while day_of_year > month_sum:
                month_sum += days_list[month]
                month += 1
                day = day_of_year - (month_sum - days_list[month - 1])
            return (month, day, year)
        else:
            return None

    def date_to_day_of_year(self, month, day, year):
        if self.__validity_test_two(month, day, year) == True:
            days_list = self.__days_list(year)
            day_of_year = 0
            for i in range(0, month - 1):
                day_of_year += days_list[i]
            day_of_year += day
            return (day_of_year)
        else:
            return None

    def day_of_year_to_day_of_week(self, year, day_of_year):
        if self.__validity_test_one(year, day_of_year) == True:
            days = 0
            if year >= 2001:
                for i in range(2001, year):
                    days += self.__days_in_year(i)
                days += day_of_year
            else:
                for i in range(year + 1, 2001):
                    days += self.__days_in_year(i)
                days += self.__days_in_year(year) - day_of_year
            weeks = days // 7
            days = days - (weeks * 7)
            if year >= 2001:
                day_of_week = self.__week[days - 1]
            else:
                day_of_week = self.__week[6 - days]
            return day_of_week
        else:
            return None

    def date_to_day_of_week(self, month, day, year):
        if self.__validity_test_two(month, day, year) == True:
            day_of_year = 0
            days_list = self.__days_list(year)
            for i in range(0, month - 1):
                day_of_year += days_list[i]
            day_of_year += day
            return self.day_of_year_to_day_of_week(year, day_of_year)
        else:
            return None
