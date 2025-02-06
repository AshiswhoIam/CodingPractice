#Alarm clock program

import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm is set for {alarm_time}")
    sound_file= "Projects&programs\\Hope.mp3"
    is_running = True
    while is_running:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("It's time to wake up! 🔥🔥🔥")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
            
            is_running= False
        
        time.sleep(1)

#AlarmClockEx
if __name__=="__main__":
    alarm_time = input("Enter the alarm time in hours,mins and seconds(00:00:00): ")
    set_alarm(alarm_time)