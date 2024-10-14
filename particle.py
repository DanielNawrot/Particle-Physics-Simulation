import math
class Particle:
    px = 0
    py = 0
    vx = 0
    vy = 0
    ax = 0
    ay = 0
    radius = None
    elasticity = None
    mass = None

    def __init__(self, px, py, vx, vy, ax, ay, mass, elasticity):
        self.px = px
        self.py = py
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.mass = mass
        self.elasticity = elasticity
        self.radius = math.sqrt(self.mass) * 4

    def update(self, dt, box):
        # Uses basic kinematic equations for position and velocity
        self.vx = self.vx + self.ax * dt
        self.vy = self.vy + self.ay * dt
        self.px = self.px + self.vx * dt
        self.py = self.py + self.vy * dt
        self.handleBoxCollision(box)

    def handleBoxCollision(self, box):
        if self.px - self.radius <= box.left or self.px + self.radius >= box.right:
            self.vx = -self.vx
        if self.py + self.radius >= box.bottom or self.py - self.radius <= box.top:
            self.vy = -self.vy * self.elasticity

        if self.py + self.radius >= box.bottom:
            self.py = box.bottom - self.radius
        if self.py - self.radius <= box.top:
            self.py = box.top + self.radius
        if self.px - self.radius <= box.left:
            self.px = box.left + self.radius
        if self.px + self.radius >= box.right:
            self.px = box.right - self.radius

    def handleParticleCollision(self, other):
        # Checks the distance between itself and all other particles to detect whether it overlaps with any other particles
        dist = math.dist((self.px, self.py), (other.px, other.py))
        sumOfR = other.radius + self.radius

        if math.fabs(dist) <= sumOfR and dist > 0:
            overlap = dist - (self.radius + other.radius)
            if overlap < 0:
                self.px += ((other.px - self.px) / (dist)) * (overlap*0.6)
                other.px -= ((other.px - self.px) / dist) * (overlap*0.6)
                self.py += ((other.py - self.py) / dist) * (overlap*0.6)
                other.py -= ((other.py - self.py) / dist) * (overlap*0.6)

            # We use the equation for two dimensional moving bodies collisions
            vxfA = self.vx + (((2 * other.mass)/(self.mass + other.mass)) * ((other.vx - self.vx) * (other.px - self.px) / pow(math.fabs(other.px - self.px), 2))) * (other.px - self.px)
            vyfA = self.vy+ (((2 * other.mass)/(self.mass + other.mass)) * ((other.vy - self.vy) * (other.py - self.py) / pow(math.fabs(other.py - self.py), 2))) * (other.py - self.py)

            vxfB = other.vx + (((2 * self.mass)/(self.mass + other.mass)) * ((self.vx - other.vx) * (self.px - other.px) / pow(math.fabs(self.px - other.px), 2)) * (self.px - other.px))
            vyfB = other.vx + (((2 * self.mass)/(self.mass + other.mass)) * ((self.vx - other.vx) * (self.px - other.px) / pow(math.fabs(self.px - other.px), 2)) * (self.px - other.px))

            self.vx = vxfA
            self.vy = -vyfA

            other.vx = vxfB
            other.vy = -vyfB

