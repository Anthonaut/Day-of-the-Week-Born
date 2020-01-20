
from math import floor


def is_leap_year(year):
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        else:
            return True
    else:
        return False


def is_gregorian_date(year, month, date):
    if year < 1752:
        return False
    if year == 1752:
        if month < 9:
            return False
        if month == 9:
            if date > 13:
                return True
            else:
                return False
        if month > 9:
            if date > 0:
                return True
    if year > 1752:
        if month > 0:
            if date > 0:
                return True


def is_valid_date(year, month, date):
    if is_gregorian_date(year, month, date):
        if 1752 <= year <= 1755:
            if month == 2:
                if 1 <= date <= 28:
                    return True
                else:
                    return False
            if month == 4 or month == 6 or month == 9 or month == 11:
                if 1 <= date <= 30:
                    return True
                else:
                    return False
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if 1 <= date <= 31:
                    return True
                else:
                    return False
        if year > 1755:
            if is_leap_year(year):
                if 1 <= month <= 12:
                    if month == 2:
                        if 1 <= date <= 29:
                            return True
                        else:
                            return False
                    if month == 4 or month == 6 or month == 9 or month == 11:
                        if 1 <= date <= 30:
                            return True
                        else:
                            return False
                    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                        if 1 <= date <= 31:
                            return True
                        else:
                            return False
                else:
                    return False
            if not is_leap_year(year):
                if 1 <= month <= 12:
                    if month == 2:
                        if 1 <= date <= 28:
                            return True
                        else:
                            return False
                    if month == 4 or month == 6 or month == 9 or month == 11:
                        if 1 <= date <= 30:
                            return True
                        else:
                            return False
                    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                        if 1 <= date <= 31:
                            return True
                        else:
                            return False
                else:
                    return False
    else:
        return False


def weekday_of(year, month, date):
    if is_valid_date(year, month, date):
        D = date

        century = str(year)
        C = int(century[0: 2])

        year_no_cent = str(year)
        Y = int(year_no_cent[2: 4])

        M = month
        if M == 1 or month == 2:
            if M == 1:
                M = 13
                prev_year = str(year - 1)
                century = prev_year[0: 2]
                year_no_cent = prev_year[2: 4]
                C = int(century)
                Y = int(year_no_cent)
                zeller = (D + floor((13 * M + 13) / 5) + Y + floor(Y / 4) + floor(C / 4) + (C * 5)) % 7
                return zeller
            if M == 2:
                M = 14
                prev_year = str(year - 1)
                century = prev_year[0: 2]
                year_no_cent = prev_year[2: 4]
                C = int(century)
                Y = int(year_no_cent)
                zeller = (D + floor((13 * M + 13) / 5) + Y + floor(Y / 4) + floor(C / 4) + (C * 5)) % 7
                return zeller
        else:
            zeller = (D + floor((13 * M + 13) / 5) + Y + floor(Y / 4) + floor(C / 4) + (C * 5)) % 7
            return zeller
    else:
        return False


def weekday_name(weekday):
    if weekday == 0:
        return 'Saturday'
    if weekday == 1:
        return 'Sunday'
    if weekday == 2:
        return 'Monday'
    if weekday == 3:
        return 'Tuesday'
    if weekday == 4:
        return 'Wednesday'
    if weekday == 5:
        return 'Thursday'
    if weekday == 6:
        return 'Friday'
    else:
        return False


def main():
    '''birth_cal = input('Enter your birthday in YYYY-MM-DD format: ')

    YYYY = birth_cal[: 4]
    MM = birth_cal[5: 7]
    DD = birth_cal[8:]

    year = int(YYYY)
    month = int(MM)
    date = int(DD)
'''
    while True:
        birth_cal = input('Enter your birthday in YYYY-MM-DD format: ')
        YYYY = birth_cal[: 4]
        MM = birth_cal[5: 7]
        DD = birth_cal[8:]

        year = int(YYYY)
        month = int(MM)
        date = int(DD)
        if is_valid_date(year, month, date):
            weekday_of(year, month, date)
            weekday = weekday_of(year, month, date)
            weekday_name(weekday)
            print('You were born on a ' + str(weekday_name(weekday)) + '!')
            break
        if not is_valid_date(year, month, date):
            print("You entered an invalid date.")
    input("Press enter to exit")




    '''if is_valid_date(year, month, date):
        weekday_of(year, month, date)
        weekday = weekday_of(year, month, date)
        weekday_name(weekday)
        print('You were born on a ' + str(weekday_name(weekday)) + '!')
        input("Press enter to exit")
    else:
        while not is_valid_date(year, month, date):
            print('The date you entered is invalid.')
            input('Enter your birthday in YYYY-MM-DD format: ')
    '''


if __name__ == '__main__':
    main()
