class Count():

    def __init__(self, count):
        self.count = count
        self.textCount = 'Comida: 0'

    def update(self):
        self.count = self.count +1
        self.textCount = 'Comida: ' + str(self.count)
    
    def getCount(self):
        return self.count;
    
    def display(self):
        fill(0)
        text(self.textCount, 10, 10)
    
