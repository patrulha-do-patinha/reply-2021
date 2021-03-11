from dataclasses import dataclass
import sys, math

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

def to_flat(x, y):
    return y * width + x
def to_2d(i):
    return (i % width, i // width)

[width, height] = [ int(x) for x in input().split() ]
[buildings_count, antennas_count, reward ] = [ int(x) for x in input().split() ]

for _ in range(buildings_count):
    [x, y, latency_weight, connection_speed] = [int(x) for x in input().split()]
    buildings.append(Building(x, y, latency_weight, connection_speed))

for i in range(antennas_count):
    [area, speed] = [int(x) for x in input().split() ]
    antennas.append(Antenna(i, area, speed))


avg_area = math.floor(sum((a.area for a in antennas)) / len(antennas))

max_heat = 0
heat = [0] * (width*height)
for building in buildings:
    for dx in range(-avg_area, avg_area):
        for dy in range(-avg_area, avg_area):
            nx = building.x + dx
            ny = building.y + dy
            if nx >= width or ny >= height:
                continue
            i = ny * width + nx
            heat[i] += dx + dy
            if heat[i] > max_heat:
                max_heat = heat[i]
if max_heat > 0:
    for i in range(len(heat)):
        heat[i] = heat[i] / max_heat

placed = set()

buildings = sorted(buildings, key=lambda b: b.speed, reverse=True)
antennas = sorted(antennas, key=lambda a: a.speed, reverse=True)
for i, antenna in enumerate(antennas):
    building = buildings[i]
    best_heat = 1
    best_heat_n = to_flat(building.x, building.y)
    for dx in range(-antenna.area, antenna.area):
        for dy in range(-antenna.area, antenna.area):
            if dy + dx > antenna.area:
                continue
            nx = building.x + dx
            ny = building.y + dy
            if nx >= width or ny >= height or nx < 0 or ny < 0:
                continue
            n = to_flat(nx, ny)
            if n in placed:
                continue
            if heat[n] < best_heat:
                best_heat = heat[n]
                best_heat_n = n
    if best_heat_n not in placed:
        (nx, ny) = to_2d(best_heat_n)
        antenna.x = nx
        antenna.y = ny
        placed.add(best_heat_n)


# best_places = sorted(enumerate(heat), key=lambda h: h[1])
# for i, antenna in enumerate(antennas):
#     place = best_places[i][0]
#     x = place % width
#     y = place // width
#     antenna.x = x
#     antenna.y = y
    


antennas_to_place = [a for a in antennas if a.x != None and a.y != None ]
print(len(antennas_to_place))
for antenna in antennas_to_place:
    print(f"{antenna.i} {antenna.x} {antenna.y}")

