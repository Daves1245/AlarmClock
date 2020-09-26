"""
alarm.py: The callback function for when
the alarm is set off. This should be editted
to fit the individual's need.
I have hooked up a buzzer to a Pi for the meantime
but will look for other solutions.
"""

# The actual alarm - this should be called
# to set off whatever alarm mechanism will be used
from gpiozero import Buzzer, PWMOutputDevice, Button, LED
from time import sleep
import threading
import signal

hour = 15
minute = 32

# GPIO pin config
led_gpio = 20
buzzer_gpio = 26
stop_gpio = 19
snooze_gpio = 13

# Frequency to play buzzer at
freq = 500

# Alarm clock config
on = True
do_snooze = False
snooze_time = 1
max_snooze_time = 15 * 60

def sig_handler(signum, frame):
    global on
    on = False
    print("")
    return

def stop_callback():
    global on
    on = False
    print("")
    return

def snooze_callback():
    global on
    global do_snooze
    global snooze_time

    print("Snooze pressed!")
    do_snooze = True
    snooze_time *= 2
    if snooze_time > max_snooze_time:
        on = False

def interrupt():
    global on
    global do_snooze
    global snooze_time
    return

def alarm_callback():
    global on, do_snooze, snooze_time, max_snooze_time
    snooze_time = 1
    stop = threading.Thread(target = interrupt)
    stop.start()

    signal.signal(signal.SIGINT, sig_handler)

    with LED(led_gpio) as led, Button(stop_gpio) as stop, PWMOutputDevice(buzzer_gpio, 
        initial_value = 0.0, frequency = freq) as buzzer, Button(snooze_gpio) as snooze:
        stop.when_pressed = stop_callback
        snooze.when_pressed = snooze_callback
        while on:
            print("on")
            buzzer.pulse()
            led.on()
            sleep(1)
            print("off")
            buzzer.off()
            led.off()
            sleep(1)
            if do_snooze:
                sleep(snooze_time)
                do_snooze = False

if __name__ == "__main__":
    alarm_callback()
