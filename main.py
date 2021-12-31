from time import sleep
from subprocess import getoutput
getoutput("pip3 install psutil")
from win32gui import GetForegroundWindow
from win32process import GetWindowThreadProcessId
from psutil import Process


open("stats.txt", 'a').close()
f = open("stats.txt", 'r')
stats = f.read().split("\n")
f.close()

apps = []
time = []

if stats != ['']:
    delay = float(stats[0])
    stats[0] = ""
    for item in stats:
        if item != "":
            split = item.split(":")
            apps.append(split[0])
            time.append(float(split[1]))
else:
    delay = 5

print("Started tracking app usage")
while True:
    sleep(delay)
    try:
        pid = GetWindowThreadProcessId(GetForegroundWindow())
        app = Process(pid[-1]).name()
    except:
        app = ""
    if app != "":
        try: index = apps.index(app)
        except ValueError: index = None
        if index != None: time[index] = float(time[index]) + delay
        else:
            apps.append(app)
            time.append(delay)

    f = open("stats.txt", "w")
    f.write(f'{delay}\n')
    for app in apps:
        f.write(f"{app}:{time[apps.index(app)]}\n")
    f.close()
