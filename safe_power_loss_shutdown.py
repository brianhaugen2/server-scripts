import os
import psutil
from datetime import datetime


if __name__ == "__main__":
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print(date_time)
    bat_stat = psutil.sensors_battery()
    print(bat_stat)
    if not bat_stat.power_plugged and bat_stat.secsleft <= 1000:
        print("Shutting Down")
        print()
        os.system("/usr/bin/sudo /usr/sbin/shutdown now")
    else:
        print()
