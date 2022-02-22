print ("Welcome to my quiz!")

# Remember playing = user
user = input("Do you want to play? ")

if user.lower() != "yes":
    quit()

print ("Alright, let's get started!")
score = 0

answer = input("Is Avak bad at valorant? ")
if answer.lower() == "no":
    print("Correct!")
    score +=1
    # You can also write score = score + 1
else:
    print("Incorrect!")

answer = input("Will Yousif ever grow more than 2 brain cells? ")
if answer.lower() == "no":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

answer = input("Does Vincent ask random questions? ")
if answer.lower() == "yes":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
answer = input("Are you silly? ")
if answer.lower() == "yes":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")

pctScore = str((score/4) * 100)

print("You finished! You scored " + str(score) + " points!")
print("That is " + str(pctScore) + "%.")

if float(pctScore) >= 50:
    print("You passed!")
else:
    print("You failed, dumb fuck.")