size = 15         
wall = STONE
air = AIR

base = player.position()


def wx(x):
    return base.getValue(Axis.X) + x

def wy(y):
    return base.getValue(Axis.Y) + y

def wz(z):
    return base.getValue(Axis.Z) + z



for x in range(size):
    for z in range(size):
        for y in range(2):
            blocks.place(wall, world(wx(x), wy(y), wz(z)))



visited = []
stack = []

startX = 1
startZ = 1
stack.append([startX, startZ])
visited.append(str(startX) + "," + str(startZ))

while len(stack) > 0:
    cx, cz = stack[len(stack) - 1]


    dirs = []
    if cx > 1 and str(cx - 2) + "," + str(cz) not in visited:
        dirs.append([-2, 0])
    if cx < size - 2 and str(cx + 2) + "," + str(cz) not in visited:
        dirs.append([2, 0])
    if cz > 1 and str(cx) + "," + str(cz - 2) not in visited:
        dirs.append([0, -2])
    if cz < size - 2 and str(cx) + "," + str(cz + 2) not in visited:
        dirs.append([0, 2])

    if len(dirs) > 0:
        dx, dz = dirs[Math.randomRange(0, len(dirs) - 1)]


        blocks.place(air, world(wx(cx + dx), wy(0), wz(cz + dz)))
        blocks.place(air, world(wx(cx + dx), wy(1), wz(cz + dz)))
        blocks.place(air, world(wx(cx + dx // 2), wy(0), wz(cz + dz // 2)))
        blocks.place(air, world(wx(cx + dx // 2), wy(1), wz(cz + dz // 2)))

        nx = cx + dx
        nz = cz + dz
        stack.append([nx, nz])
        visited.append(str(nx) + "," + str(nz))
    else:
        stack.pop()


blocks.place(air, world(wx(1), wy(0), wz(0)))
blocks.place(air, world(wx(1), wy(1), wz(0)))

blocks.place(air, world(wx(size - 2), wy(0), wz(size - 1)))
blocks.place(air, world(wx(size - 2), wy(1), wz(size - 1)))

player.say("Vždy riešiteľný labyrint hotový!")
