print("Welcome to my quiz!")
print ("*Remember to put a capital letter at the start of each answer* ")

playing = input("Do you want to play? ")

if playing != "Yes":
    quit()
 
print("Okay! Let's play : )")

answer = input("What does CPU stand for? ")
if answer == "Central processing unit":
    print("Correct!")
else:
    print("Incorrect!")

answer1 = input("What does GPU stand for? ")
if answer1 == "Graphics processing unit":
    print("Correct!")
else:
    print("Incorrect!")

answer2 = input("What does RAM stand for? ")
if answer2 == "Random access memory":
    print("Correct!")
else:
    print("Incorrect!")

answer3 = input("What does PSU stand for? ")
if answer3 == "Power supply unit":
    print("Correct!")
else:
    print("Incorrect!")

answer4 = input("Does RGB improve FPS? ")
if answer4 == "Yes":
    print("Correct!")
else:
    print("Incorrect!")
