# Health Management System


def getdate():
    import datetime
    return datetime.datetime.now()
print("Health Management System")
f1 = open("rafi_f.txt","a")
f1.close()
f2 = open("rafiq_f.txt","a")
f2.close()
f3 = open("jubayer_f.txt","a")
f3.close()
f4 = open("rafi_g.txt","a")
f4.close()
f5 = open("rafiq_g.txt","a")
f5.close()
f6 = open("jubayer_g.txt","a")
f6.close()
food_gim = input("food or gim :")
lock_show = input("lock or show :")
parson = input("rafi rafiq or jubayer :")
if food_gim == "food":
    if lock_show == "lock":
        if parson == "rafi":
            text1 = input()
            with open("rafi_f.txt","a") as raf:
                raf.write(f"On this date {getdate()} you eat {text1}")
        elif parson == "rafiq":
            text2 =input()
            with open("rafiq_f.txt","a") as rof:
                rof.write(f"On this date {getdate()} you eat {text2}")
        elif parson == "jubayer":
            text3 =input()
            with open("jubayer_f.txt","a") as juf:
                juf.write(f"On this date {getdate()} you eat {text3}")
    elif lock_show == "show":
        if parson == "rafi":
            with open("rafi_f.txt","r") as raf:
                print(raf.readlines())
        elif parson == "rafiq":
            with open("rafiq_f.txt","r") as rof:
                print(rof.readlines())
        elif parson == "jubayer":
            with open("jubayer_f.txt","r") as juf:
                print(juf.readlines())
elif food_gim == "gim":
    if lock_show == "lock":
        if parson == "rafi":
            text1 = input()
            with open("rafi_g.txt","a") as raf:
                raf.write(f"On this date {getdate()} you gim {text1}")
        elif parson == "rafiq":
            text2 =input()
            with open("rafiq_g.txt","a") as rof:
                rof.write(f"On this date {getdate()} you gim {text2}")
        elif parson == "jubayer":
            text3 =input()
            with open("jubayer_g.txt","a") as juf:
                juf.write(f"On this date {getdate()} you gim {text3}")
    elif lock_show == "show":
        if parson == "rafi":
            with open("rafi_g.txt","r") as raf:
                print(raf.readlines())
        elif parson == "rafiq":
            with open("rafiq_g.txt","r") as rof:
                print(rof.readlines())
        elif parson == "jubayer":
            with open("jubayer_g.txt","r") as juf:
                print(juf.readlines())
else:
    print("Wrong Input")

