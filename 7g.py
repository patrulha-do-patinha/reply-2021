from dataclasses import dataclass
import sys, math, itertools

buildings = dict()
antennas = []

@dataclass
class Building:
    x: int
    y: int
    latency: int
    speed: int

@dataclass
class Antenna:
    i: int
    area: int
    speed: int
    x: int = None
    y: int = None

def to_flat(x, y):
    return y * width + x
def to_2d(i):
    return (i % width, i // width)

[width, height] = [ int(x) for x in input().split() ]
[buildings_count, antennas_count, reward ] = [ int(x) for x in input().split() ]

for _ in range(buildings_count):
    [x, y, latency, connection_speed] = [int(x) for x in input().split()]
    buildings[to_flat(x, y)] = Building(x, y, latency, connection_speed)

for i in range(antennas_count):
    [area, speed] = [int(x) for x in input().split() ]
    antennas.append(Antenna(i, area, speed))

heat = [0] * (width*height)
for i in range(width*height):
    points = 0
    (x, y) = to_2d(i)
    for building in buildings.values():
        d = abs(building.x - x) + abs(building.y - y)
        points += building.speed / ((building.latency * d) + 0.0001)
    heat[i] = points

for i in range(width*height):
    for j in range(width*height):
        if i == j: continue
        if heat[j] > heat[i]:
            (ix, iy) = to_2d(i)
            (jx, jy) = to_2d(j)
            d = abs(ix-jx) + abs(iy-jy)
            heat[i] -= heat[j] / d

best_points = sorted(enumerate(heat), key=lambda p: p[1], reverse=True)
antennas = sorted(antennas, key=lambda a: a.speed, reverse=True)

for i, point in enumerate(best_points):
    (x, y) = to_2d(point[0])
    if i >= len(antennas):
        break
    antenna = antennas[i]
    antenna.x = x
    antenna.y = y


antennas_to_place = [a for a in antennas if a.x != None and a.y != None ]
print(len(antennas_to_place))
for antenna in antennas_to_place:
    print(f"{antenna.i} {antenna.x} {antenna.y}")

