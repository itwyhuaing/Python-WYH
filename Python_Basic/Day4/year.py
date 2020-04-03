def is_leap_year(year):
    rlt = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
    return rlt

def which_day(year,month,day):
    days_month = [[31,28,31,30,31,30,31,31,30,31,30,31],
                  [31,29,31,30,31,30,31,31,30,31,30,31]][is_leap_year(year)]
    total = 0
    for index in range(month-1):
        total += days_month[index]
    rlt = total + day
    return rlt

if __name__ == '__main__':
    print(which_day(1990,12,11))
    print(which_day(2018,6,18))
    print(which_day(2018,8,18))
    print(which_day(2019,12,31))
    print(which_day(2020,3,30))
