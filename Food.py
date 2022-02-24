class Food():

    def __init__(self, x, y):
        self.r = 10
        self.position = PVector(x, y)
    
    def getPos(self):
        return self.position;

    def update(self, position):
        self.position = position

    def display(self):
        fill(200, 140, 30)
        noStroke()
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rect(0, 0, self.r, self.r)
