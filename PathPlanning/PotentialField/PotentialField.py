"""
Potential Field Path Planning Algorithm
"""
from PathPlanning.utils import *

class PotentialFieldPlanner(PathPlanner):
    def __init__(self, map, iterations=1e4, step_size=2, ka=1, kr=1e4, da=10, dr=100):
        PathPlanner.__init__(self)
        self.map = map
        self.iterations = iterations
        self.step_size = step_size
        self.motions = [
            Vector(1, 0),  # right
            Vector(0, 1),  # up
            Vector(-1, 0),  # left
            Vector(0, -1),  # down
            Vector(-1, -1),  # left and down
            Vector(-1, 1),  # left and up
            Vector(1, -1),  # right and down
            Vector(1, 1),  # right and up
        ]
        self.ka = ka
        self.kr = kr
        self.da = da
        self.dr = dr

    def plan(self, start, target):
        self.finalPath = []
        self.finalPath.append(start)
        for iteration in range(int(self.iterations)):
            currentPos = self.finalPath[-1]
            if currentPos.dist(target) < self.step_size:
                print('final')
                break

            lowestPotential = float('inf')
            nextPos = currentPos
            for motion in self.motions:
                newPos = currentPos + motion * self.step_size
                newPotential = self.calculate_attractive_potential(newPos, target) + self.calculate_repulsive_potential(newPos)
                if newPotential < lowestPotential:
                    lowestPotential = newPotential
                    nextPos = newPos
            self.finalPath.append(nextPos)

    def calculate_attractive_potential(self, pos, target):
        if pos.dist(target) <= self.da:
            return 0.5 * self.ka * pos.dist(target) ** 2
        else:
            return self.ka * (self.da * pos.dist(target) - 0.5 * self.da ** 2)

    def calculate_repulsive_potential(self, pos):
        pr = 0
        for obs in self.map.obstacles:
            if obs.dist(pos) == 0:
                return float('inf')
            if obs.dist(pos) <= self.dr:
                pr = pr + 0.5 * self.kr * (1/obs.dist(pos) - 1/self.dr) ** 2
        return pr