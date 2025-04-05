from datetime import date

date_notes = """
2024-05-23 2024-05-24
2024-05-23 2024-05-24
2024-05-23 2024-05-24
2024-14-23 2024-05-24
2024-05-23
March 1st
2024-05-24 2024-05-31
2024-06-01 2024-06-05
2024-06-2 2024-06-11
"""

date_notes2 = """
2024-05-23 2024-05-24
2024-05-23 2024-05-24
2024-05-23 2024-05-24
"""

date_notes3 = """
2024-14-23 2024-05-24
2024-05-23
March 1st
2024-05-24 2024-05-31
2024-06-01 2024-06-05
2024-06-2 2024-06-11
"""

errors = {
    "ROOM MAX CAPACITY": "no rooms available",
    "DATE FORMAT": "invalid format of a date",
    "DATE RANGE": "check check-in and check-out dates"
}


if len(date_notes) == 0:
    print("NO Reservations")

reservations = date_notes2.strip().split("\n")

available_rooms = []

for reservation in reservations:

    print(f"Processing: {reservation}")

    dates = reservation.split()

    if len(dates) != 2:
        print(f"'{reservation}' contains error. ONLY 2 DATES PER LINE")
        # raise Exception(errors["DATE RANGE"])
        continue

    try:
        check_in = date.fromisoformat(dates[0])
        check_out = date.fromisoformat(dates[1])

        print(f"{check_in} and {check_out} dates are valid")

    except ValueError as e:
        print(f"'{reservation}' contains error. CAN NOT CONVERT ONE OF THE DATES")
        continue # process next line

    if check_out < check_in:
        print(f"'{reservation}' contains error. CHECKOUT MUST BE AFTER CHECK IN")
        # raise Exception(errors["DATE RANGE"])
        continue
    else:

        if len(available_rooms) == 0:
            available_rooms.append([check_in, check_out])

        for index, room in enumerate(available_rooms):
            # if checkout < check in -> place a new person there
            if room[1] <= check_in and index < len(available_rooms)-1:
                room[0], room[1] = check_in, check_out
            else:
                print(print(f"Motel is at full capacity"))
                continue

    print(f"Hotel Capacity: {available_rooms}")





















