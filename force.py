import numpy

class GForce:
    Npair = [-1, -1]
    value = numpy.array([0,0])
    G_CONSTANT = 1

    def __init__(self, A, B, particles):
        self.Npair = [A, B]
        self.updateForce(particles)

    def updateForce(self, particles):
        Mm = particles[self.Npair[0]].m * particles[self.Npair[1]].m
        r = particles[self.Npair[0]].P - particles[self.Npair[1]].P
        mag_r = numpy.linalg.norm(r)
        unit_r = r / mag_r
        self.value = self.G_CONSTANT * (Mm / (mag_r**2)) * unit_r