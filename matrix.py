class matrix:
    def __init__(self,x,y,custom=False,char="-"):
        self.y = y
        self.x = x
        if custom == False:
            self.grid = [[char]*x for _ in range(y)]
            self.graphic = [[char]*x for _ in range(y)]
        else:
            if not type(custom) == list:
                raise Exception("Exception: In Matrix __init__ , \"custom\" must be list ")
            self.grid = custom
            self.graphic = custom
    def draw_grid(self):
        for i in range(0,self.x):
            draw = self.grid[i]
            for x in range(0,len(draw)):
                print(draw[x],end="")
                if x == len(self.grid[0])-1:
                    print()
    def set_char(self,x,y,char):
        self.grid[y][x] = char
    def move_char(self,start_location,end_location,auto=True):
        start_char = self.grid[start_location[0]][start_location[1]]
        self.grid[end_location[1]][end_location[0]] = start_char
        if auto == True:
             background = self.graphic[start_location[0]][start_location[1]]
        else:
            background = auto
        self.grid[start_location[0]][start_location[1]] = background
    def get_char(self,x,y):
        return self.grid[y][x]
    def get_grid(self):
        return self.grid
    def fill(self,start,end,char):
        pass

"""
init creates a list matrix object
draw_grid draws the matrix object
set_char sets a matrix character
move_char moves a character
"""
