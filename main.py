try:
    from win32gui import GetForegroundWindow
    from win32process import GetWindowThreadProcessId
    from win32api import GetLastInputInfo, GetTickCount
    from psutil import Process
    from apscheduler.schedulers.background import BackgroundScheduler
except ModuleNotFoundError:
    from pip._internal import main as pipmain
    print("Unable to find needed packages, installing them now...")

    pipmain(["install", "--user", "pywin32"])
    pipmain(["install", "--user", "psutil"])
    pipmain(["install", "--user", "apscheduler"])

    from win32gui import GetForegroundWindow
    from win32process import GetWindowThreadProcessId
    from win32api import GetLastInputInfo, GetTickCount
    from psutil import Process
    from apscheduler.schedulers.background import BackgroundScheduler

from time import sleep

sched = BackgroundScheduler()

open("stats.txt", 'a').close()
f = open("stats.txt", 'r')
stats = f.read().split("\n")
f.close()

apps = []
times = []

if stats != ['']:
    delay = float(stats[0])
    stats[0] = ""
    for item in stats:
        if item != "":
            split = item.split(":")
            apps.append(split[0])
            times.append(float(split[1]))
else:
    f = open("stats.txt", 'w')
    f.write("5")
    f.close()
    delay = 5

def getInactiveTime():
    return (GetTickCount()-GetLastInputInfo())/1000

def main():
    if getInactiveTime() > 300:
        return

    try:
        pid = GetWindowThreadProcessId(GetForegroundWindow())
        app = Process(pid[-1]).name()
    except:
        app = ""
    if app != "":
        try: index = apps.index(app)
        except ValueError: index = None

        if index != None:
            times[index] = float(times[index]) + delay
        else:
            apps.append(app)
            times.append(delay)

    f = open("stats.txt", "w")
    f.write(f'{delay}\n')
    for app in apps:
        f.write(f"{app}:{times[apps.index(app)]}\n")
    f.close()


print("Started tracking app usage")

sched.add_job(main, 'interval', seconds=delay)
sched.start()
try:
    while True: # since "sched" is a seperate thread, occupy this thread. Not very efficient, if I find something better I'll use it
        sleep(1000000)
except KeyboardInterrupt:
    pass
