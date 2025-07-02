import numpy
import pygame

class Particle:
    img = pygame.image.load("redGiant.png")
    F = numpy.array([0.0,0.0])
    P = numpy.array([0.0,0.0])
    v = numpy.array([0.0,0.0])
    m = 0.0

    def __init__(self, m, P, u):
        # where p and u are 2d vectors
        self.m = m
        self.P = numpy.array(P)
        self.v = numpy.array(u)

    def acc(self):
        self.v += (self.F / self.m)

    def move(self):
        self.P += self.v
