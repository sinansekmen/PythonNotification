import time
import psutil
from plyer import notification

while(True):
    battery = psutil.sensors_battery()
    percent = battery.percent

    notification.notify(

        title = "Laptopun Pil Seviyesi",
        message=str(percent)+ "% Laptop Pil Seviyesi"
    )

    time.sleep(5*5)

    continue