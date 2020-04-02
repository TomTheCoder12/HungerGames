from matrix import matrix
from entity import entity
import random
import time



rmgdone = 0
while rmgdone == 0:
    try:
        x = int(input("How wide is the map? >>>"))
        y = int(input("How high is the map? >>>"))

        biomes = []

        p1 = int(input("How much pine forest>>> "))
        p2 = int(input("How much coniferous forest>>> "))
        p3 = int(input("How many mountains>>> "))
        p4 = int(input("How much water >>> "))
        print((x*y)-(p1+p2+p3+p4)," plains biomes.")
        biomes.append(" "*((x*y)-(p1+p2+p3+p4)))
       
        def randgenlist(place,char):
            indbiomes = []
            for i in range(0,place):
                indbiomes.append(char)
            return indbiomes
        biomes.append(randgenlist(p1,"^"))
        biomes.append(randgenlist(p2,"*"))
        biomes.append(randgenlist(p3,"O"))
        biomes.append(randgenlist(p4,"~"))
        
        temp_1 = []
        for i1 in biomes:
          for i2 in i1:
            temp_1.append(i2)
        biomes = temp_1

        #biomes = randgenlist(p5," ")
        terrain = []
        temp_1 = []
        temp_2 = []
        for i1 in range(0,y):
            temp_1 = []
            for i2 in range(0,x):
                if biomes == []:
                  temp_1.append(" ")
                else:
                  rand = random.randint(0,(len(biomes)-1))
                  temp_1.append(biomes[rand])
                  del(biomes[rand])
            temp_2.append(temp_1)

        terrain = temp_2
        print("Terrain generated =")
        t = matrix((len(terrain)),(len(terrain[0])),custom=terrain)
        t.draw_grid()
        time.sleep(1)
        print("^ = Pine forest")
        print("* = Coniferous forest")
        print("O = Mountain")
        print("~ = Water")
        rmgdone = 1
    except:
        print("Invalid generation")

print("Preparing objects")

#Crossbow, trap, sword, dagger, axe

names = ["Fred","Frodo","Sir Tom Higgithenobotham","Tom Arto","Jake Sell","Dungham MacFred","Donaldus Troomp","Tom Dickenharry","William Wallace Son of Scotia","The Irish Potato Blight","The queen of England","Impy","Art","D-Bug","Ele-D","Jeff"]

people = []
for x in range(0,3):
    rand = random.randint(0,len(names)-1)
    people.append(names[rand])
    names.remove(names[rand])
print("The combatants are: ")
for x in range(0,len(people)):
    print(people[x])

#Game loop
while not input("Press enter for next timestep (type 0 to quit) >>> ") == "0":
    t.draw_grid()
    
    
