def build_snowman():
    size=3
    for position in range (2,11,4):
        shapes.sphere(SNOW, pos(10,(position-2)*1.75,0), size*2, ShapeOperation.REPLACE)
        player.say(f"Position: {position}")
        player.say(f"Size: {size}")
        size -= 1
player.on_chat("snowman", build_snowman)
