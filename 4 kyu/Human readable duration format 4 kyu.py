"""
years, days, hours, minutes and seconds.
"""


def format_duration(seconds):
    if seconds == 0:
        return "now"
    data = []
    minute = 60
    hour = minute * 60
    day = hour * 24
    year = day * 365
    year_count, day_count, hour_count, minute_count = 0, 0, 0, 0
    while seconds >= year:
        year_count += 1
        seconds -= year
    while seconds >= day:
        day_count += 1
        seconds -= day
    while seconds >= hour:
        hour_count += 1
        seconds -= hour
    while seconds >= minute:
        minute_count += 1
        seconds -= minute

    if year_count > 0: data.append(f"{year_count} year") if year_count == 1 else data.append(f"{year_count} years")
    if day_count > 0: data.append(f"{day_count} day") if day_count == 1 else data.append(f"{day_count} days")
    if hour_count > 0: data.append(f"{hour_count} hour") if hour_count == 1 else data.append(f"{hour_count} hours")
    if minute_count > 0: data.append(f"{minute_count} minute") if minute_count == 1 else data.append(f"{minute_count} minutes")
    if seconds > 0: data.append(f"{seconds} second") if seconds == 1 else data.append(f"{seconds} seconds")

    if len(data) == 1:
        return "".join(data)
    else:
        return ", ".join(data[:-1]) + f" and {data[-1]}"


print(format_duration(1))
print(format_duration(62))
print(format_duration(120))
print(format_duration(3600))
print(format_duration(3662))
