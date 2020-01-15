from pygame import mixer
from datetime import datetime
from time import time


def musickloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_know(msg):
    with open("mylog.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
    # musickloop("96.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exersise = time()
    watersese = 1200 # 20m
    eyessese = 1800 # 30m
    exersese = 2700 # 45 m
    while True:
        if time() - init_water > watersese:
            print("Water Drinking time. write 'drank' to stop the alam.")
            musickloop("96.mp3","drank")
            init_water = time()
            log_know("Drank water at")
        if time() - init_eyes > eyessese:
            print("Eay excersie time. write 'eay' to stop the alam.")
            musickloop("96.mp3","eay")
            init_eyes = time()
            log_know("Eay exersige at")
        if time() - init_exersise > exersese:
            print("Exersige time. write 'exer' to stop the alam.")
            musickloop("96.mp3","exer")
            init_exersise = time()
            log_know("Exersige  at")








