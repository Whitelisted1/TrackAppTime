open("stats.txt", 'a').close()
f = open("stats.txt", "r")
apps = f.read().split("\n")
f.close()

apps[0] = ""
seconds_in_day = 60 * 60 * 24
seconds_in_hour = 60 * 60
seconds_in_minute = 60

if apps != [""]:
    print("[App Name] - [days]:[hours]:[minutes]:[seconds]")
    for app in apps:
        if app != "":
            splitapp = app.split(":")
            seconds = int(round(float(splitapp[1])))
            days = seconds // seconds_in_day
            hours = (seconds - (days * seconds_in_day)) // seconds_in_hour
            minutes = (seconds - (days * seconds_in_day) - (hours * seconds_in_hour)) // seconds_in_minute
            seconds = (seconds - (days * seconds_in_day) - (hours * seconds_in_hour) - (minutes * seconds_in_minute))
            print(f"{splitapp[0]} - {days}:{hours}:{minutes}:{seconds}")
else:
    print("No time information is available")

input("\nPress enter to exit")