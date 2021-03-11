from dataclasses import dataclass
import sys

buildings = dict()
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
    buildings[(x,y)] = Building(x, y, latency_weight, connection_speed)

for i in range(antennas_count):
    [area, speed] = [int(x) for x in input().split() ]
    antennas.append(Antenna(i, area, speed))



buildings_list = sorted(buildings.values(), key=lambda b: b.speed, reverse=True)
antennas = sorted(antennas, key=lambda a: a.speed, reverse=True)

placed_antennas = set()

directions = [(1,0), (0,1), (-1,0), (0,-1), (-1,-1), (-1,1), (1,-1), (1,1) ]

for i, antenna in enumerate(antennas):
    building = buildings_list[i]
    for d in directions:
        nx = building.x + d[0]
        ny = building.y + d[1]
        if (nx, ny) in buildings:
            continue
        if (nx, ny) in placed_antennas:
            continue
        if nx < 0 or ny < 0 or nx >= width or ny >= height:
            continue
        antenna.x = nx
        antenna.y = ny
        placed_antennas.add((nx,ny))
        break


antennas_to_place = [a for a in antennas if a.x != None and a.y != None ]
print(len(antennas_to_place))
for antenna in antennas_to_place:
    print(f"{antenna.i} {antenna.x} {antenna.y}")

