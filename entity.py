from matrix import matrix
import random

t = matrix(3,3,custom=[[" ","O","^"],[" ","O","^"],[" ","O","^"]])
tc = matrix(3,3,custom=[[" ","O","^"],[" ","O","^"],[" ","O","^"]])

class ai:
    def __init__(self,terrain,constant,startpos,name,stampchar="auto"):
        global land
        land = terrain
        self.constant = constant
        self.name = name
        self.state = "idle"
        self.pos = startpos
        if stampchar == "auto":
            land.set_char(self.pos[0],self.pos[1],name[0])
            self.char = name[0]
        elif stampchar == False:
            land.set_char(self.pos[0],self.pos[1],stampchar)
            self.char = stampchar
#        else:
#            land.set_char(self.pos[0],self.pos[1],name[0])
    def move(self,direction):
        land.set_char(self.pos[0],self.pos[1],self.constant.get_char(self.pos[0],self.pos[1]))
        if direction == 0:
            movelist = [(self.pos[0])+1,self.pos[1]]
            self.pos = [(self.pos[0])+1,self.pos[1]]
        elif direction == 1:
            movelist = [(self.pos[0])-1,self.pos[1]]
            self.pos = [(self.pos[0])-1,self.pos[1]]
        elif direction == 2:
            movelist = [(self.pos[0]),(self.pos[1])+1]
            self.pos = [(self.pos[0]),(self.pos[1])+1]
        elif direction == 3:
            movelist = [(self.pos[0]),(self.pos[1])-1]
            self.pos = [(self.pos[0]),(self.pos[1])-1]
        land.set_char(self.pos[0],self.pos[1],self.char)
    def coords(self):
        return self.pos

jeff = ai(t,tc,[0,0],"jeff")
        
"""
    def move(self,direction,stamp=True):
        if direction == 0:
            movelist = [(self.pos[0])+1,self.pos[1]]
            land.move_char(self.pos,movelist,auto=self.constant.get_char(self.pos[0],self.pos[1]))
            self.pos = [(self.pos[0])+1,self.pos[1]]
        elif direction == 1:
            movelist = [(self.pos[0])-1,self.pos[1]]
            land.move_char(self.pos,movelist,auto=self.constant.get_char(self.pos[0],self.pos[1]))
            self.pos = [(self.pos[0])-1,self.pos[1]]
        elif direction == 2:
            movelist = [(self.pos[0]),(self.pos[1])+1]
            land.move_char(self.pos,movelist,auto=self.constant.get_char(self.pos[0],self.pos[1]))
            self.pos = [(self.pos[0]),(self.pos[1])+1]
        elif direction == 3:
            movelist = [(self.pos[0]),(self.pos[1])-1]
            land.move_char(self.pos,movelist,auto=self.constant.get_char(self.pos[0],self.pos[1]))
            self.pos = [(self.pos[0]),(self.pos[1])-1]
"""
