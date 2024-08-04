year = 1900

mounths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# so it loops thru only "the" amount of time because it starts on zero
for n in range(len(mounths)):
    mounths[n] -= 1
mounth = 0

dayInMounth = 0

day = 0
# 0 = man, 1 = tis, 2 = ons, 3 = tor, 4 = fre, 5 = lor, 6 = son

sundays = 0

while True:
    if year == 2001 and dayInMounth == 0 and mounth == 0:
        if day == 6:
            sundays -= 1
        print(sundays)
        break
    if dayInMounth >= mounths[mounth]:
        if mounth == 1:
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        # leap year
                        if dayInMounth >= mounths[mounth] + 1:
                            dayInMounth = -1
                            mounth += 1
                            if day == 5:
                                if year > 1900:
                                    sundays += 1
                    else:
                        dayInMounth = -1
                        mounth += 1
                        if day == 5:
                            if year > 1900:
                                sundays += 1
                else:
                    # leap year
                    if dayInMounth >= mounths[mounth] + 1:
                        dayInMounth = -1
                        mounth += 1
                        if day == 5:
                            if year > 1900:
                                sundays += 1
            else:
                dayInMounth = -1
                mounth += 1
                if day == 5:
                    if year > 1900:
                        sundays += 1
        else:
            dayInMounth = -1
            mounth += 1
            if day == 5:
                if year > 1900:
                    sundays += 1
    if day > 6:
        day = 0
    if mounth >= len(mounths):
        mounth = 0
        year += 1

    dayInMounth += 1
    day += 1
