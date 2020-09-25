"""
alarm.py: The callback function for when
the alarm is set off. This should be editted
to fit the individual's need.
I have hooked up a buzzer to a Pi for the meantime
but will look for other solutions.
"""

# The actual alarm - this should be called
# to set off whatever alarm mechanism will be used
from gpiozero import Buzzer, PWMOutputDevice

freq = 100
hour = 15
minute = 32

gpio_pin = 17 # We provide 3.3V to the buzzer

def alarm_callback():
    buzzer = PWMOutputDevice(gpio_pin, initial_value = 0.0, frequency = freq)
    while True:
        buzzer.on()
        buzzer.off()
    buzzer.close()
