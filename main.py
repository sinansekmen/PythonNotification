import time
import psutil
from plyer import notification

while(True):
    battery = psutil.sensors_battery()
    percent = battery.percent

    notification.notify(

        title = "Laptopun pili Bitiyorrr!!!!!",
        message=str(percent)+ "% Aq su yakmıyor bu"
    )

    time.sleep(5*5)

    continue