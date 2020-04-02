from matrix import matrix
import random

t = matrix(5,5,custom= [["X","X","X","X","X"],["X"," ","O","^","X"],["X"," ","O","^","X"],["X"," ","O","^","X"],["X","X","X","X","X"]])
tc = matrix(5,5,custom=[["X","X","X","X","X"],["X"," ","O","^","X"],["X"," ","O","^","X"],["X"," ","O","^","X"],["X","X","X","X","X"]])
meta = matrix(5,5,custom=[["X","X","X","X","X"],["X","","","","X"],["X","","","","X"],["X","","","","X"],["","","","",""],["X","X","X","X","X"]])

class entity:
    global offspring
    offspring=[]
    def __init__(self,terrain,meta,constant,startpos,name,parentstats = False,stampchar="auto"):
        global land
        land = terrain
        self.constant = constant
        self.name = name
        meta = meta
        self.state = "idle"
        self.pos = startpos
        self.inv = []
        if stampchar == "auto":
            land.set_char(self.pos[0],self.pos[1],name[0])
            self.char = name[0]
        else:
            land.set_char(self.pos[0],self.pos[1],stampchar)
            self.char = stampchar

        #Stats
        if parentstats == False:
            self.stealth = random.randint(0,100)
            self.damage = random.randint(0,100)
            self.health = random.randint(0,250)
            self.cunning = random.randint(0,100)
            self.perceptiveness = random.randint(0,100)
            
            self.net_speed = random.randint(0,4)
            
            self.pine_speed = random.randint(0,4)
            self.conifer_speed = random.randint(0,4)
            self.water_speed = random.randint(0,4)
            self.mountain_speed = random.randint(0,4)

            self.allstats = [self.stealth,self.damage, self.health, self.cunning,self.perceptiveness,self.net_speed,self.pine_speed,self.conifer_speed,self.water_speed, self.mountain_speed]
        else:
            self.stealth = parentstats[0] + random.randint(-10,10)
            self.damage = parentstats[1] + random.randint(-10,10)
            self.health = parentstats[2] + random.randint(-10,10)
            self.cunning = parentstats[3] + random.randint(-10,10)
            self.perceptiveness = parentstats[4] + random.randint(-10,10)
            
            self.net_speed = parentstats[5] + random.randint(-1,1)
            
            self.pine_speed = parentstats[6] + random.randint(-1,1)
            self.conifer_speed = parentstats[7] + random.randint(-1,1)
            self.water_speed = parentstats[8] + random.randint(-1,1)
            self.mountain_speed = parentstats[9] + random.randint(-1,1)

            self.allstats = [self.stealth,self.damage, self.health, self.cunning,self.perceptiveness,self.net_speed,self.pine_speed,self.conifer_speed,self.water_speed, self.mountain_speed]
            

    def move(self,direction):
        land.set_char(self.pos[0],self.pos[1],self.constant.get_char(self.pos[0],self.pos[1]))
        if direction == 0 and meta.get_char((self.pos[0])+1,self.pos[1]) != "X":
            movelist = [(self.pos[0])+1,self.pos[1]]
            self.pos = [(self.pos[0])+1,self.pos[1]]
        elif direction == 1 and meta.get_char((self.pos[0])-1,self.pos[1]) != "X":
            movelist = [(self.pos[0])-1,self.pos[1]]
            self.pos = [(self.pos[0])-1,self.pos[1]]
        elif direction == 2 and meta.get_char((self.pos[0]),(self.pos[1])+1) != "X":
            movelist = [(self.pos[0]),(self.pos[1])+1]
            self.pos = [(self.pos[0]),(self.pos[1])+1]
        elif direction == 3 and meta.get_char((self.pos[0]),(self.pos[1])-1) != "X":
            movelist = [(self.pos[0]),(self.pos[1])-1]
            self.pos = [(self.pos[0]),(self.pos[1])-1]
        else:
            return False
        land.set_char(self.pos[0],self.pos[1],self.char)
    def coords(self):
        return self.pos
    def location(loc):
        if self.pos == loc:
            return self.name
    def stats(self):
        print("1 = Stealth")
        print("2 = Damage")
        print("3 = Health")
        print("4 = Cunning")
        print("5 = Perceptiveness")
        print("6 = Net speed")
        print("7 = Speed in pine biome")
        print("8 = Speed in conifer biome")
        print("7 = Speed in water")
        print("7 = Speed in the mountains")
        for x in len(self.allstats):
            print(x,": ",self.allstats[x])
    def reproduce(self,name):
        allstats = self.allstats
        offspring.append(entity(land,meta,self.constant,self.pos,name,parentstats=allstats))
        print(self.name, " gave birth to ",name, " at ",self.pos)
    def get_inv():
        return self.inv
    def add_inv(add):
        for x in len(add):
            self.inv.append(add[x])
    def set_inv(setinv):
        self.inv = setinv


jeff = entity(t,meta,tc,[1,1],"jeff")


