print(" ")
print("**************Guess the number***************")
print(" ")
print("10 time of change")
print(" ")

change = 1
while change <=10:
    n = int(input("Enter your number :"))
    num = 18
    print(f"{change} // play")
    if n >50:
        print("You enter vary big number")
    elif n > 18 :
        print("You enter big number")
    elif n<18:
        print("You enter small number")
    elif n == num:
        print("This the number")
        print("You wine")
        break


    change = change + 1\

print("Game is over")
print(f"The number is {num}")

