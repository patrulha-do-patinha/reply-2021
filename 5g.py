from dataclasses import dataclass

buildings = []
antennas = []

@dataclass
class Building:
    x: int
    y: int
    latency_weight: int
    connection_speed: int

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


for antenna in antennas:
    if antenna.i >= width or antenna.i >= height:
        break
    antenna.x = antenna.i
    antenna.y = antenna.i



print(len(antennas))
for antenna in antennas:
    if antenna.x != None and antenna.y != None:
        print(f"{antenna.i} {antenna.x} {antenna.y}")

