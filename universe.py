import pygame
import numpy
import particle
import force

class Universe:
    particles = []
    forces = []
    paused = False

    def __init__(self):
        self.paused = True

    def simulate(self):
        currForces = {}
        # dict of particles indexes and all forces acting on it
        for pIndex in range(len(self.particles)):
            currForces[pIndex] = []
        for f in self.forces:
            for pIndex in f.Npair:
                currForces[pIndex].append(f.value)

        for pIndex in currForces:
            self.particles[pIndex].F = sum(currForces[pIndex])
        # calculates resulant force on each particle

        for p in self.particles:
            p.acc()
            p.move()

        for f in self.forces:
            f.updateForce(self.particles)

    def createParticle(self, m, p, u):
        self.particles.append(particle.Particle(m, p, u))
        A = len(self.particles) - 1
        for B in range(len(self.particles) - 1):
            self.forces.append(force.GForce(A, B, self.particles))