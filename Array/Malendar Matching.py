'''
calendar1 = [["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]]
dailyBounds1 = ["9:00", "20:00"]
calendar2 = [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]]
dailyBounds2 = ["10:00", "18:30"]
meetingDuration = 30
To find free time slot to create your meeting with person 2.
expected = [["11:30", "12:00"], ["15:00", "16:00"], ["18:00", "18:30"]]
'''

def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):
    # step 1
    calendar1 = timeToInt(calendar1)
    calendar2 = timeToInt(calendar2)
    offset = 40  # 100 - 60

    # step 2
    merged_list = []
    merged_list.append(checkMorning(dailyBounds1[0], dailyBounds2[0]))
    merged_list = mergeList(calendar1, calendar2, merged_list)
    merged_list.append(checkEvening(dailyBounds1[1], dailyBounds2[1]))

    # step 3: search free periods
    free_periods = []
    for i in range(1, len(merged_list)):
        start_next = merged_list[i][0]
        end_before = merged_list[i - 1][1]
        if end_before < start_next:
            duration = start_next - end_before
            if duration % 100 >= (100 - offset):
                duration -= offset
            if duration >= meetingDuration:
                free_periods.append([intToTime(end_before), intToTime(start_next)])
    return free_periods


def mergeList(l1, l2, merged_list):
    if not l1:
        for i in range(len(l2)):
            merged_list.append(l2[i])
        return merged_list
    if not l2:
        for i in range(len(l1)):
            merged_list.append(l2[i])
        return merged_list

    i = 0
    j = 0

	while i < len(l1) and j < len(l2):
        current_l1 = l1[i]
        current_l2 = l2[j]

        if current_l1 <= current_l2:
            if not merged_list or merged_list[-1][1] < current_l1[0]:
                merged_list.append(current_l1)
            else:
                merged_list[-1][1] = max(current_l1[1], merged_list[-1][1])
            i += 1
        else:
            if not merged_list or merged_list[-1][1] < current_l2[0]:
                merged_list.append(current_l2)
            else:
                merged_list[-1][1] = max(current_l2[1], merged_list[-1][1])
            j += 1

    while i < len(l1):
        if not merged_list or merged_list[-1][1] < l1[i][0]:
            merged_list.append(l1[i])
        else:
            merged_list[-1][1] = max(l1[i][1], merged_list[-1][1])
        i += 1

    while j < len(l2):
        if not merged_list or merged_list[-1][1] < l2[j][0]:
            merged_list.append(l2[j])
        else:
            merged_list[-1][1] = max(l2[j][1], merged_list[-1][1])
        j += 1

    return merged_list


def timeToInt(calendar):
    for i in range(len(calendar)):
        for j in range(len(calendar[i])):
            time = calendar[i][j]
            calendar[i][j] = stringTimeToInt(time)
    return calendar


def intToTime(intTime):
    time = [str(intTime // 100), str(intTime % 100) if intTime % 100 > 0 else '00']
    stringTime = ":".join(time)
    return stringTime


def stringTimeToInt(timeString):
    time = timeString.split(':')
    intTime = int(time[0]) * 100 + int(time[1])
    return intTime


def checkMorning(morning1, morning2):
    morning1 = stringTimeToInt(morning1)
    morning2 = stringTimeToInt(morning2)
    return [0, morning1] if morning1 >= morning2 else [0, morning2]


def checkEvening(evening1, evening2):
    evening1 = stringTimeToInt(evening1)
    evening2 = stringTimeToInt(evening2)
    return [evening1, 2400] if evening1 <= evening2 else [evening2, 2400]
