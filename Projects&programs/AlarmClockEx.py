#Alarm clock program

import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm is set for {alarm_time}")
    sound_file= "Hope.mp3"
if __name__=="__main__":
    alarm_time = input("Enter the alarm time in hours,mins and seconds(00:00:00)")
    set_alarm(alarm_time)