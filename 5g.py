from dataclasses import dataclass
import sys

buildings = []
antennas = []

@dataclass
class Building:
    x: int
    y: int
    latency_weight: int
    speed: int

@dataclass
class Antenna:
    i: int
    area: int
    speed: int
    x: int = None
    y: int = None

[width, height] = [ int(x) for x in input().split() ]
[buildings_count, antennas_count, reward ] = [ int(x) for x in input().split() ]

for _ in range(buildings_count):
    [x, y, latency_weight, connection_speed] = [ int(x) for x in input().split() ]
    buildings.append(Building(x, y, latency_weight, connection_speed))

for i in range(antennas_count):
    [area, speed] = [int(x) for x in input().split() ]
    antennas.append(Antenna(i, area, speed))



buildings = sorted(buildings, key=lambda b: b.speed, reverse=True)
antennas = sorted(antennas, key=lambda a: a.speed, reverse=True)

for i, antenna in enumerate(antennas):
    building = buildings[i]
    antenna.x = building.x
    antenna.y = building.y


antennas_to_place = [a for a in antennas if a.x != None and a.y != None ]
print(len(antennas_to_place))
for antenna in antennas_to_place:
    print(f"{antenna.i} {antenna.x} {antenna.y}")

