import random

list=["r","p","s"]

change=10
your_p=0
computer_p=0
no_of_change=1

print("///// Rock Paper Scissors GAME /////")
print("r for Rock\np for Paper\ns for Scissors")
print("10 round of play")

while no_of_change<=change:
    y_c=input(f"{no_of_change} / Rock Paper and Scissors")
    c_c=random.choice(list)

    if y_c==c_c:
        print("0 points to each")

    # if yser enter r
    if y_c=="r" and c_c=="p":
        computer_p=computer_p+1
        print(f"Your guess {y_c} and Computer guess is {c_c}")
        print("Computer wins 1 point")
        print(f"Computer point is {computer_p} and your point is {your_p}")

    elif y_c=="p" and c_c=="s":
        computer_p=computer_p+1
        print(f"Your guess {y_c} and Computer guess is {c_c}")
        print("Computer wins 1 point")
        print(f"Computer point is {computer_p} and your point is {your_p}")

    elif y_c=="r" and c_c=="s":
        your_p=your_p+1
        print(f"Your guess {y_c} and Computer guess is {c_c}")
        print("You wins 1 point")
        print(f"Computer point is {computer_p} and your point is {your_p}")

    elif y_c=="p" and c_c=="r":
        your_p=your_p+1
        print(f"Your guess {y_c} and Computer guess is {c_c}")
        print("You wins 1 point")
        print(f"Computer point is {computer_p} and your point is {your_p}")

    elif y_c=="s" and c_c=="p":
        your_p=your_p+1
        print(f"Your guess {y_c} and Computer guess is {c_c}")
        print("You wins 1 point")
        print(f"Computer point is {computer_p} and your point is {your_p}")

    elif y_c=="s" and c_c=="r":
        computer_p=computer_p+1
        print(f"Your guess {y_c} and Computer guess is {c_c}")
        print("Computer wins 1 point")
        print(f"Computer point is {computer_p} and your point is {your_p}")
    else:
        print("Your Input is Wrong\n")

    no_of_change=no_of_change+1
    print(f"{no_of_change-1} is left out of {change}")

print("Game over")

if computer_p > your_p:
    print("Computer wins and you loose")

if computer_p < your_p:
    print("you win and computer loose")

print(f"Your point is {your_p} and Computer point is {computer_p}")
