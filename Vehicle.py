class Vehicle():

    def __init__(self, x, y):
        self.acceleration = PVector(0, 0)
        self.velocity = PVector(0, -2)
        self.position = PVector(x, y)
        self.r = 10
        self.maxspeed = 5
        self.maxforce = 0.2

    def update(self):
        # Update velocity
        self.velocity.add(self.acceleration)
        # Limit speed
        self.velocity.limit(self.maxspeed)
        self.position.add(self.velocity)
        self.acceleration.mult(0)

    def applyForce(self, force):
        self.acceleration.add(force)
        
    def boundaries(self, d):

        desired = None

        if self.position.x < d:
            desired = PVector(self.maxspeed, self.velocity.y)
        elif self.position.x > width - d:
            desired = PVector(-self.maxspeed, self.velocity.y)

        if self.position.y < d:
            desired = PVector(self.velocity.x, self.maxspeed)
        elif self.position.y > height - d:
            desired = PVector(self.velocity.x, -self.maxspeed)

        if desired:
            desired.normalize()
            desired.mult(self.maxspeed)
            steer = desired - self.velocity
            steer.limit(self.maxforce)
            self.applyForce(steer)

    def arrive(self, target):

        desired = target - self.position
        d = desired.mag()

        if (d < 100):
            m = map(d, 0, 100, 0, self.maxspeed)
            desired.setMag(m)
        else:
            desired.setMag(self.maxspeed)

        steer = desired - self.velocity
        steer.limit(self.maxforce)

        self.applyForce(steer)
        
    def getPos(self):
        return self.position;
    
    def display(self):
        theta = self.velocity.heading() + PI / 2
        fill(0,125,0)
        stroke(125, 0, 0)
        strokeWeight(1)
        with pushMatrix():
            translate(self.position.x, self.position.y)
            rotate(theta)
            beginShape()
            vertex(0, -self.r * 2)
            vertex(-self.r, self.r * 2)
            vertex(self.r, self.r * 2)
            endShape(CLOSE)
