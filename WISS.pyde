from Vehicle import Vehicle
from Food import Food
from Count import Count

def setup():
    global vehicle
    global food
    global count
    size(640, 360)
    velocity = PVector(0, 0)
    vehicle = Vehicle(width / 2, height / 2)
    
    # pos da comida
    food = Food(random(50, width - 50), random(50, height - 50))
    count = Count(0)

def draw():
    background(255)
    mouse = PVector(mouseX, mouseY)
    distance = food.getPos() - vehicle.getPos();
    
    if (distance.mag() < 10 ):
        count.update()
        print(count.getCount())
        food.update(PVector(random(50, width - 50), random(50, height - 50)))
        
    vehicle.boundaries(25)
    vehicle.arrive(food.getPos())
    vehicle.update()
    vehicle.display()
    
    food.display()
    count.display()
    
