import pygame
import random
from particle import Particle
from box import Box

pygame.init()
screen = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()
FPS = 60

box =  Box(10, 790, 10, 790)

particles = []
for i in range(100):
    particles.append(Particle(random.randint(50, 750), random.randint(50, 750), int(random.random() * 400) - 300, int(random.random() * 400) - 300, 0, 0, random.randrange(1, 5), 1))


def draw_Box():
    pygame.draw.rect(screen, "white", (box.left, box.top, (box.right - box.left), (box.bottom - box.top)), 2)

def draw_Particle(particle):
    pygame.draw.circle(screen, "white", (particle.px, particle.py), particle.radius, 2)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
            running = False

    screen.fill("black")

    # Coded
    draw_Box()
    for i in range(len(particles)):
        particles[i].update(1/FPS, box)
        j = i + 1
        for j in range(len(particles)):
            particles[i].handleParticleCollision(particles[j])
    for p in particles:
        draw_Particle(p)
   #p1.update(1/FPS, box)
   #p1.handleParticleCollision(p2)
   #p2.update(1/FPS, box)
   #p2.handleParticleCollision(p1)

   #draw_Particle(p1)
   #draw_Particle(p2)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()