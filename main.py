import pygame
import random
from particle import Particle
from box import Box

WIDTH = 800
HWIGHT = 800
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT)) # Set window resolution to desired size
clock = pygame.time.Clock()
FPS = 60

box =  Box(10, WIDTH - 10, 10, HEIGHT - 10)

particles = []
for i in range(100): 
    # Creates an array of randomly sized and placed particles
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
        particles[i].update(1/FPS, box) # Updates wach particle's velocity & position individually
        j = i + 1
        for j in range(len(particles)):
            particles[i].handleParticleCollision(particles[j]) # Handles each particles collisions individually
    for p in particles:
        draw_Particle(p)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
