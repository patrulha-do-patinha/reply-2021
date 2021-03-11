from dataclasses import dataclass
import sys, math, itertools

buildings = []
antennas = []

@dataclass
class Building:
    x: int
    y: int
    latency: int
    speed: int

    heat: int = 0

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
    buildings.append(Building(x, y, latency, connection_speed))

for i in range(antennas_count):
    [area, speed] = [int(x) for x in input().split() ]
    antennas.append(Antenna(i, area, speed))

for a in buildings:
    for b in buildings:
        d = abs(a.x - b.x) + abs(a.y - b.y)
        a.heat += b.speed / ((b.latency * d) + 0.0001)
for a in buildings:
    for b in buildings:
        if a.x == b.x and a.y == b.y: continue
        if b.heat > a.heat:
            d = abs(a.x - b.x) + abs(a.y - b.y)
            a.heat -= b.heat / d

buildings = sorted(buildings, key=lambda b: b.heat, reverse=True)
antennas = sorted(antennas, key=lambda a: a.speed, reverse=True)

for i, antenna in enumerate(antennas):
    building = buildings[i]
    antenna.x = building.x
    antenna.y = building.y


antennas_to_place = [a for a in antennas if a.x != None and a.y != None ]
print(len(antennas_to_place))
for antenna in antennas_to_place:
    print(f"{antenna.i} {antenna.x} {antenna.y}")

