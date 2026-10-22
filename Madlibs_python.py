import random 
import time

#We are defining multiple inputs that are stored in variables that will be plugged into the print statement
nounlist = ["Mirror", "Peer", "John", "Connor", "Vibhu", " Dog", "Apple", "Bannana", "thunder", "Cancun", "Italy,", "Doctor", "Ceo","Cto", "Teacher","river", "mountain", "rain", "Sunny", "Robotics"]
verblist = ["Carve", "decorate", "talked", "walked", "scared", "baked","treated", "displayed","cakcled", "amazed", "screamed", "shrieked","shivered" ]
adjectivelist = ["dirty", "beautiful", "terrifiyng", "horrible", "bad" ,"spec", "Eerie","chilled","creepy", "frieghting", "horrific", "ghastly", "petryfying", "sinister", "wicked"]

senses = input("input one of your senses:")

noun1 = input("Input a noun (type random if you want a random place):")
noun2 = input("Input another noun:")
noun3 = input("Input another noun:")
noun4 = input("Input another noun:")

costume1 =  input("Input a costume:")
costume2 =  input("Input anoher costume:")
costume3 =  input("Input another costume:")
costume4 =  input("Input another costume :")
costume5 =  input("Input another costume")

adjective1 =  input("Input adjective:")
adjective2 = input("Input another adjective:")
adjective3 = input("Input another adjective:")
adjective4 = input("Input another adjective:")
adjective5 = input("Input another adjective:")
adjective6 = input("Input another adjective:")

verb1 =input("Input a verb:")
verb2 =input("Input another verb:")
verb3 =input("Input another verb:")
verb4 =input("Input another verb:")
 
if noun1 == "random":
    noun1 = random.choice(nounlist)

if noun2 == "random":
    noun2 = random.choice(nounlist)

if noun3 == "random":
    noun3 = random.choice(nounlist)

if noun4 == "random":
    noun4 = random.choice(nounlist)


if adjective1 == "random":
    adjective1 = random.choice(adjectivelist)

if adjective2 == "random":
    adjective2 = random.choice(adjectivelist)

if adjective3 == "random":
    adjective3 = random.choice(adjectivelist)


if adjective4 == "random":
    adjective4 = random.choice(adjectivelist)


if adjective5 == "random":
    adjective5 = random.choice(adjectivelist)


if adjective6 == "random":
    adjective6 = random.choice(adjectivelist)


if verb1 == "random":
    verb1 = random.choice(verblist)


if verb2 == "random":
    verb2 = random.choice(verblist)


if verb3 == "random":
    verb3 = random.choice(verblist)


if verb4 == "random":
    verb4 = random.choice(verblist)



time.sleep(1)

print(f"It was the night before Halloween, or Halloween Eve,  and I still didn't have a costume. The {noun1} rattled behind me as I stared {noun2} looking at the closet behind me. I looked at the different costumes I had, {costume1} , {costume2} , {costume3} ,{costume4} . I walked to my closet, picking up {costume1} ,  I used my {senses} senses examining the specs of dust that rotted the look of the costume. One by one I went through each of the costumes, costum2 was {adjective1} , {costume3} one was {adjective2} , {costume4} was {adjective3}.I had no clue what to wear as each one didn't match my expectation. My inner light bulb had just been lighted  at that moment. I {verb1} an amazon same day delivery to buy a {costume5} , that  looked absolutely {adjective4} , {adjective5} , {adjective6} .  It cost me around {noun3} . At that moment  when it arrived I {verb2} down the stairs almost {verb3} . The next day I  {verb4} the costume I bought and went with a trick or treating ppythbasket as big as the {noun4} . I placed both my airpod ear and turned on Mission Impossible Music.")


    