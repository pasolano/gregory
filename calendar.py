class Calendar(object):
    def _is_leap_year(self, year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        else:
            return False

    def _valid_date_day_year(self, day, year):
        if (type(year) is not int):
            raise RuntimeError('Year is not an interger')
        if (type(day) is not str):
            raise RuntimeError('Day is not a string / Missing month input')
        if self._is_leap_year(year) == True:
            true_special_days = self.leap_special_days
        else:
            true_special_days = self.special_days
        result = False
        for key,val in true_special_days.items():
            if day == key:
                result = True
        if result != True:
            raise RuntimeError('Invalid special day')
        return result
        
    def _valid_date_month_day_year(self, month, day, year):
        if (type(year) is not int):
            raise RuntimeError("Value 'year' is not an integer")
        if self._is_leap_year(year) == True:
            true_days_in_month = self.leap_no_special_days
        else:
            true_days_in_month = self.no_special_days
        for key,val in true_days_in_month.items():
            tester = None
            if month == key:
                tester = val
                if day <= 0 or day > val:
                    raise RuntimeError("Integer 'day' invalid")
                break
        if tester == None:
            raise RuntimeError('Invalid month')
        else:
            return True

    def _valid_date_year_doy(self, year, doy):
        if (type(year) is not int):
            raise RuntimeError("'year' is not an integer")
        elif (type(doy) is not int):
            raise RuntimeError("'doy' is not an integer")
        if self._is_leap_year(year) == True:
            if doy > 366 or doy <= 0:
                raise RuntimeError('Invalid day of year')
            else:
                return True
        else:
            if doy > 365 or doy <= 0:
                raise RuntimeError('Invalid day of year')
            else:
                return True

    def date_to_day_of_year(self, *args):
        length = len(args)
        if length == 2:
            day = args[0]
            year = args[1]
            if self._valid_date_day_year(day,year) == True:
                leap_year = self._is_leap_year(year)
                if leap_year == True:
                    true_special_days = self.leap_special_days
                else:
                    true_special_days = self.special_days
                for key,val in true_special_days.items():
                    if day == key:
                        total_days = val
                return total_days
        elif length == 3:
            month = args[0]
            day = args[1]
            year = args[2]
            if self._valid_date_month_day_year(month,day,year) == True:
                leap_year = self._is_leap_year(year)
                if leap_year == True:
                    true_no_special_days = self.leap_no_special_days
                    true_special_days = self.leap_special_days
                else:
                    true_no_special_days = self.no_special_days
                    true_special_days = self.special_days
                doy = 0
                for key,val in true_no_special_days.items():
                    if month == key:
                        break
                    doy += val
                doy += day
                for key,val in true_special_days.items():
                    if doy >= val:
                        doy += 1
                return doy

    def day_of_year_to_date(self, year, doy):
        if self._valid_date_year_doy(year,doy) == True:
            leap_year = self._is_leap_year(year)
            if leap_year == True:
                true_special_days = self.leap_special_days
                true_no_special_days = self.leap_no_special_days
            elif leap_year == False:
                true_special_days = self.special_days
                true_no_special_days = self.no_special_days
            doy2 = 0
            for key,val in true_special_days.items():
                if doy == val:
                    day = key
                    return (day, year)
                if doy >= val:
                    doy2 = doy2 + 1
            doy = doy - doy2
            total_days = 0
            sum_of_previous_months = 0
            for key,val in true_no_special_days.items():
                total_days += val
                if doy <= total_days:
                    month = key
                    break
                sum_of_previous_months += val
            day = doy - sum_of_previous_months
            return (month,day,year)
    
    def date_to_day_of_week(self, *args):
        if len(args) == 3:
            month = args[0]
            day = args[1]
            year = args[2]
            doy = self.date_to_day_of_year(month,day,year)
            return self.day_of_year_to_day_of_week(year,doy)
        elif len(args) == 2:
            day = args[0]
            year = args[1]
            doy = self.date_to_day_of_year(day,year)
            return self.day_of_year_to_day_of_week(year,doy)

class Gregorian_Calendar(Calendar):
    def __init__(self):
        self.days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
        self.months = {'Jan': 0, 'Feb': 31, 'Mar': 59, 'Apr': 90, 'May': 120, 'Jun': 151, 'Jul': 181, 'Aug': 212, 'Sep': 243, 'Oct': 273, 'Nov': 304, 'Dec': 334}
        self.leap_months = {'Jan': 0, 'Feb': 31, 'Mar': 60, 'Apr': 91, 'May': 121, 'Jun': 152, 'Jul': 182, 'Aug': 213, 'Sep': 244, 'Oct': 274, 'Nov': 305, 'Dec': 335}
        self.special_days = {}
        self.leap_special_days = self.special_days
        self.days_in_month = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
        self.leap_days_in_month = {'Jan': 31, 'Feb': 29, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
        self.no_special_days =  {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
        self.leap_no_special_days = {'Jan': 31, 'Feb': 29, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
    
    def day_of_year_to_day_of_week(self, year, doy):
        if self._valid_date_year_doy(year, doy) == True:
            days = 0
            if self._is_leap_year(year) == True:
                days_in_year_tested = 366
            else:
                days_in_year_tested = 365
            if year >= 2001:
                for i in range(2001, year):
                    if self._is_leap_year(i) == True:
                        days += 366
                    else:
                        days += 365
                days += doy
            else:
                for i in range(year + 1, 2001):
                    if self._is_leap_year(i) == True:
                        days += 366
                    else:
                        days += 365
                days += days_in_year_tested - doy
            weeks = days // 7
            days = days - (weeks * 7)
            if year >= 2001:
                day_of_week = self.days[days - 1]
            else:
                day_of_week = self.days[6 - days]
            return day_of_week
    
class Shire_Calendar(Calendar):
    def __init__(self):
        self.months = {'Afteryule': 1, 'Solmath': 31, 'Rethe': 61, 'Astron': 91, 'Thrimidge': 121, 'Forelithe': 151, 'Afterlithe': 184, 'Wedmath': 214, 'Halimath': 244, 'Winterfilth': 274, 'Blotmath': 304, 'Foreyule': 334}
        self.leap_months = {'Afteryule': 0, 'Solmath': 31, 'Rethe': 61, 'Astron': 91, 'Thrimidge': 121, 'Forelithe': 151, 'Afterlithe': 184, 'Wedmath': 215, 'Halimath': 245, 'Winterfilth': 275, 'Blotmath': 305, 'Foreyule': 335}
        self.special_days = {'2 Yule': 1, '1 Lithe': 182, 'Midyear\'s Day': 183, '2 Lithe': 184, '1 Yule': 365}
        self.leap_special_days = {'2 Yule': 1, '1 Lithe': 182, 'Midyear\'s Day': 183, 'Overlithe': 184, '2 Lithe': 185, '1 Yule': 366}
        self.days = ('Sterday', 'Sunday', 'Monday', 'Trewsday', 'Hensday', 'Mersday', 'Highday')
        self.days_in_month = {'Afteryule': 31, 'Solmath': 30, 'Rethe': 30, 'Astron': 30, 'Thrimidge': 30, 'Forelithe': 31, 'Afterlithe': 31, 'Wedmath': 30, 'Halimath': 30, 'Winterfilth': 30, 'Blotmath': 30, 'Foreyule': 31}
        self.leap_days_in_month = self.days_in_month
        self.no_special_days = {'Afteryule': 30, 'Solmath': 30, 'Rethe': 30, 'Astron': 30, 'Thrimidge': 30, 'Forelithe': 30, 'Afterlithe': 30, 'Wedmath': 30, 'Halimath': 30, 'Winterfilth': 30, 'Blotmath': 30, 'Foreyule': 30}
        self.leap_no_special_days = self.no_special_days

    def _is_leap_year(self, year):
        if year % 4 == 0 and year % 100 != 0:
            return True
        else:
            return False
    
    def day_of_year_to_day_of_week(self, year, doy):
        if self._valid_date_year_doy(year,doy) == True:
            if self._is_leap_year(year) == True and doy >= 185:
                doy = doy - 2
                counter = 0
                list_counter = (doy - 1) % 7
                for day_of_week in self.days:
                    if list_counter == counter:
                        return day_of_week
                    counter += 1
            elif self._is_leap_year(year) == False and doy >= 184:
                doy = doy - 1
                counter = 0
                list_counter = (doy - 1) % 7
                for day_of_week in self.days:
                    if list_counter == counter:
                        return day_of_week
                    counter += 1
            else:
                counter = 0
                list_counter = (doy - 1) % 7
                for day_of_week in self.days:
                    if list_counter == counter:
                        return day_of_week
                    counter += 1

class Calendrier_Républicain(Calendar):
    def __init__(self):
        self.months = {'Vendémiaire': 0, 'Brumaire': 30, 'Frimaire': 60, 'Nivôse': 90, 'Pluviôse': 120, 'Ventôse': 150, 'Germinal': 180, 'Floréal': 210, 'Prairial': 240, 'Messidor': 270, 'Thermidor': 300, 'Fructidor': 330}
        self.leap_months = self.months
        self.special_days = {'Jour de la vertu': 361, 'Jour du génie': 362, 'Jour du travail': 363, 'Jour de l\'opinion': 364, 'Jour des récompenses': 365}
        self.leap_special_days = {'Jour de la vertu': 361, 'Jour du génie': 362, 'Jour du travail': 363, 'Jour de l\'opinion': 364, 'Jour des récompenses': 365, 'Jour de la Révolution': 366}
        self.days = ('primidi', 'duodi', 'tridi', 'quartidi', 'quintidi', 'sextidi', 'septidi', 'octidi', 'nonidi', 'décadi')
        self.days_in_month = {'Vendémiaire': 30, 'Brumaire': 30, 'Frimaire': 30, 'Nivôse': 30, 'Pluviôse': 30, 'Ventôse': 30, 'Germinal': 30, 'Floréal': 30, 'Prairial': 30, 'Messidor': 30, 'Thermidor': 30, 'Fructidor': 30}
        self.leap_days_in_month = self.days_in_month
        self.no_special_days = self.days_in_month
        self.leap_no_special_days = self.days_in_month

    def day_of_year_to_day_of_week(self, year, doy):
        if self._valid_date_year_doy(year,doy) == True:
            if self._is_leap_year(year) == True:
                true_special_days = self.leap_special_days
            else:
                true_special_days = self.special_days
            for key,val in true_special_days.items():
                if doy == val:
                    return key
            counter = 0
            list_counter = (doy - 1) % 10
            for day_of_week in self.days:
                if list_counter == counter:
                    return day_of_week
                counter += 1
