import numpy

class Particle:
    F = numpy.array([0,0])
    a = numpy.array([0,0])
    def __init__(self, m, p, u):
        # where p and u are 2d vectors
        self.m = m
        self.p = numpy.array(p)
        self.v = numpy.array(u)

    def acc(self):
        self.v += self.a

    def move(self):
        self.p += self.v