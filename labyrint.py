size = 15
wall = STONE
air = AIR
base = player.position()

def wx(x): return base.getValue(Axis.X) + x
def wy(y): return base.getValue(Axis.Y) + y
def wz(z): return base.getValue(Axis.Z) + z

def place2(block, x, z):
    for y in range(2):
        blocks.place(block, world(wx(x), wy(y), wz(z)))

def fill_maze():
    for x in range(size):
        for z in range(size):
            place2(wall, x, z)

def carve(x, z):
    place2(air, x, z)

def generate_maze():
    visited = []
    stack = []

    stack.append([1, 1])
    visited.append("1,1")

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

            carve(cx + dx, cz + dz)
            carve(cx + dx // 2, cz + dz // 2)

            nx = cx + dx
            nz = cz + dz
            stack.append([nx, nz])
            visited.append(str(nx) + "," + str(nz))
        else:
            stack.pop()

def make_entrances():
    carve(1, 0)
    carve(size - 2, size - 1)

fill_maze()
generate_maze()
make_entrances()
player.say("Labyrint hotový!")



def on_chat_agent():
    agent.teleport(player.position().add(pos(0, 1, 0)), SOUTH)
    player.say("Agent pri tebe")

player.onChat("agent", on_chat_agent)


def on_chat_left():
    agent.teleport(world(wx(1), wy(0), wz(1)), SOUTH)
    player.say("Left-hand solver ide")

    while True:
       
        agent.turn(LEFT)
        if not agent.detect(AgentDetection.BLOCK, FORWARD):
            agent.move(FORWARD, 1)
            loops.pause(150)
            continue
        agent.turn(RIGHT)

   
        if not agent.detect(AgentDetection.BLOCK, FORWARD):
            agent.move(FORWARD, 1)
            loops.pause(150)
            continue

       
        agent.turn(RIGHT)

player.onChat("left", on_chat_left)
