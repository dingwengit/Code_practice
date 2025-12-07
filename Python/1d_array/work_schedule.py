'''
An employee wants to find all possible work schedules for their week.
They must work exactly their total weekly hours,
and no day can exceed the maximum daily hours, though days off (0 hours) are allowed. Some days may already be fixed by their employer.

Let’s suppose the employee’s currently scheduled workweek is
represented as a 7-character string, for example: “08??840”.
Each character represents one day of the week.
The days already scheduled by their employer are the numerical digits,
and the flexible days are represented as question marks.

Implement a function that takes a workweek string in the format above,
and returns an array of all possible valid workweeks
that satisfy the weekly and daily hour limits.

Example

Suppose the given workweek (pattern) = "08??840", total weekly working hours (work_hours) = 24, and maximum daily working hours (day_hours) = 4

    The known hours (0+8+8+4+0) sum to 20.
    The two unknown days must sum to 4 without exceeding the daily limit of 4 hours

Therefore, the function should return this list, which contains every possible valid schedule for the week:

[
”0804840”,
”0813840”,
”0822840”,
”0831840”,
”0840840”
]
'''

def work_hours(s):
    total_weekly_hours = 24
    slot_hours = []
    max_daily_hours = 4

    def get_slots(s):
        total, slots = 0, 0
        for c in s:
            if c == '?':
                slots +=1
            else:
                total += int(c)
        return total, slots

    def fill_slots(total, slots, hours, idx):
        nonlocal slot_hours
        if idx >= slots:
            if sum(hours) == total:
                slot_hours.append(hours.copy())
            return
        for i in range(max_daily_hours+1):
            hours[idx] = i
            fill_slots(total, slots, hours, idx+1)

    cur_total, slots = get_slots(s)
    left_hours = total_weekly_hours - cur_total
    hours = [0] * slots
    fill_slots(left_hours, slots, hours, 0)

    return slot_hours

def set_string(s, item):
    res, idx = [], 0
    for c in s:
        if c == "?":
            res.append(f"{item[idx]}")
            idx += 1
        else:
            res.append(c)
    return "".join(res)

s = "08??840"
res = work_hours(s)
for item in res:
    print(set_string(s, item))