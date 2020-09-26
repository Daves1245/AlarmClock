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

freq = 1000
hour = 15
minute = 32

led_gpio = 20
buzzer_gpio = 26
stop_gpio = 19
snooze_gpio = 13

# Is the alarm clock running
on = True

def sig_handler(signum, frame):
    global on
    on = False
    print("")
    return

def stop_callback():
    return

def snooze_callback():
    return

def interrupt():
    global on
    stop = Button(stop_gpio)
    snooze = Button(snooze_gpio)
    while on:
        if stop.is_pressed:
            print("Stop pressed!")
            stop.wait_for_release()
            on = False
        if snooze.is_pressed:
            print("Snooze pressed!")
            snooze.wait_for_release()
    return

def alarm_callback():
    global on
    stop = threading.Thread(target = interrupt)
    stop.start()

    signal.signal(signal.SIGINT, sig_handler)

    with LED(led_gpio) as led, PWMOutputDevice(buzzer_gpio, initial_value = 0.0,
            frequency = freq) as buzzer:
        while on:
            print("on")
            buzzer.pulse()
            led.on()
            sleep(1)
            print("off")
            buzzer.off()
            led.off()
            sleep(1)
        buzzer.close()
alarm_callback()
