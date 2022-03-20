open("stats.txt", 'a').close()
f = open("stats.txt", "r")
apps = f.read().split("\n")
f.close()

apps[0] = ""
seconds_in_day = 60 * 60 * 24
seconds_in_hour = 60 * 60
seconds_in_minute = 60


times = []
for app in apps:
    if app != "":
        time = float(app.split(":")[1])
        times.append(time)
totaltime = sum(times)

if apps != [""]:
    print("[App Name] - [days]:[hours]:[minutes]:[seconds]")
    for i, app in enumerate(apps):
        if app != "":
            splitapp = app.split(":")
            seconds = int(round(float(splitapp[1])))
            totalseconds = seconds
            days = seconds // seconds_in_day
            hours = (seconds - (days * seconds_in_day)) // seconds_in_hour
            minutes = (seconds - (days * seconds_in_day) - (hours * seconds_in_hour)) // seconds_in_minute
            seconds = (seconds - (days * seconds_in_day) - (hours * seconds_in_hour) - (minutes * seconds_in_minute))
            print(f"{splitapp[0]} - {days}:{hours}:{minutes}:{seconds} (≈{round(totalseconds/totaltime*100, 2)}%)")
else:
    print("No time information is available")

input("\nPress enter to exit")
