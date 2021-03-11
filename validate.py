seen = set()
seen_xy = set()
n = int(input())
for _ in range(n):
    [i, x, y] = [int(x) for x in input().split()]
    if i in seen:
        print(f"ME CAGO EN DIOS {i}")
    if (x,y) in seen_xy:
        print(f"SEEN XY {x} {y}")
    seen.add(i)
    seen_xy.add((x,y))

