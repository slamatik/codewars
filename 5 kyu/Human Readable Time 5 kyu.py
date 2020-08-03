def make_readable(seconds):
    secs = seconds % 60
    mins = (seconds % 3600 - secs) // 60
    hrs = seconds // 3600
    return f"{hrs:02d}:{mins:02d}:{secs:02d}"


print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))
