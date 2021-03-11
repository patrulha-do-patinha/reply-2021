from dataclasses import dataclass
import sys, math, itertools

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

def to_flat(x, y):
    return y * width + x
def to_2d(i):
    return (i % width, i // width)

[width, height] = [ int(x) for x in input().split() ]
[buildings_count, antennas_count, reward ] = [ int(x) for x in input().split() ]

for _ in range(buildings_count):
    [x, y, latency_weight, connection_speed] = [int(x) for x in input().split()]
    buildings[to_flat(x, y)] = Building(x, y, latency_weight, connection_speed)

for i in range(antennas_count):
    [area, speed] = [int(x) for x in input().split() ]
    antennas.append(Antenna(i, area, speed))

# max_heat = 0
# heat = [0] * (width*height)
# for building in buildings:
#     for dx in range(-avg_area, avg_area):
#         for dy in range(-avg_area, avg_area):
#             nx = building.x + dx
#             ny = building.y + dy
#             if nx >= width or ny >= height:
#                 continue
#             i = ny * width + nx
#             heat[i] += dx + dy
#             if heat[i] > max_heat:
#                 max_heat = heat[i]
# if max_heat > 0:
#     for i in range(len(heat)):
#         heat[i] = heat[i] / max_heat

buildings_list = sorted(buildings, key=lambda b: b.speed, reverse=True)
antennas = sorted(antennas, key=lambda a: a.speed, reverse=True)

for i, antenna in enumerate(antennas):
    best_points = 0
    best_building = None
    # best_in_area = None
    if len(buildings) == 0:
        break
    for building in buildings_list[:10]:
        points = 0
        # in_area = []
        for dx in range(-antenna.area, antenna.area):
            for dy in range(-antenna.area, antenna.area):
                if dy + dx > antenna.area:
                    continue
                nx = building.x + dx
                ny = building.y + dy
                if nx >= width or ny >= height or nx < 0 or ny < 0:
                    continue
                n = to_flat(nx, ny)
                if n in buildings:
                    b2 = buildings[n]
                    points += b2.speed * antenna.speed
                    points -= (dx + dy) * b2.latency_weight
                    # in_area.append(n)
        if points > best_points:
            best_points = points
            best_building = building
            # best_in_area = in_area

    if best_building != None:
        antenna.x = best_building.x
        antenna.y = best_building.y
        del buildings[to_flat(antenna.x, antenna.y)]
        # for key in best_in_area:
        #     del buildings[key]

antennas_to_place = [a for a in antennas if a.x != None and a.y != None ]
print(len(antennas_to_place))
for antenna in antennas_to_place:
    print(f"{antenna.i} {antenna.x} {antenna.y}")

