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
    width_telo: int = None
    height_telo: int = None
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


antennas = sorted(antennas, key=lambda a: a.speed * a.area, reverse=True)
antennas = antennas[:10]
print(len(antennas))
for i, antenna in enumerate(antennas):
    buildings_list = sorted(buildings.values(), key=lambda b: b.speed, reverse=True)
    print(len(buildings))
    current_buildings_list = buildings_list[:150]

    points_for_antenna = []
    antenna.height_telo = antenna.area
    antenna.width_telo = antenna.area
    while (width%antenna.width_telo != 0):
        antenna.width_telo = antenna.width_telo - 1
    while (height%antenna.height_telo != 0):
        antenna.height_telo = antenna.height_telo - 1

    width_squares = int(width / antenna.width_telo)
    height_squares = int(height / antenna.height_telo)

    for height_index in range(antenna.height_telo,height,antenna.height_telo):
        for width_index in range(antenna.width_telo,width,antenna.width_telo):
            if(height_index%2 == width_index%2):
                points_for_antenna.append([height_index,width_index])
    
    arrayPuntuaciones = []
    for point in points_for_antenna:
        pointTotal = 0
        for building in current_buildings_list:
            if(abs(building.x - point[0]) + abs(building.y - point[1]) <= antenna.area):
                pointTotal = pointTotal + building.speed
        arrayPuntuaciones.append(pointTotal)

    indexGanador = arrayPuntuaciones.index(max(arrayPuntuaciones))
    point_for_this_antena = points_for_antenna[indexGanador]
    print(f"{antenna.i} {point_for_this_antena[0]} {point_for_this_antena[1]}")

    for building in current_buildings_list:
        if(abs(building.x - point_for_this_antena[0]) + abs(building.y - point_for_this_antena[1]) <= antenna.area):
            del buildings[(building.x,building.y)]
    

