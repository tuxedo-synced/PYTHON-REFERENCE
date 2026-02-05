import os
import warnings
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
warnings.filterwarnings("ignore", category=UserWarning)
import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set over {alarm_time}")
    sound_file = r"New Topics\Dates_And_TIme.py\solo_leveling.mp3"
    is_running = True

    while is_running:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if current_time > alarm_time:
                print("Time is already passed .")
                break
            else:
                print(current_time)
                if current_time == alarm_time:
                    pygame.mixer.init()
                    pygame.mixer.music.load(sound_file)
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():
                        time.sleep(1)
                    print("Wake up!!!")
                    break
                time.sleep(1)
        


if __name__ == "__main__":
    alarm_time = input("Enter the alarm  time (HH:MM:SS): ")
    set_alarm(alarm_time)