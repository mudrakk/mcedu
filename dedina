def postav_dom(base):
    blocks.fill(
        CONCRETE,
        base,
        positions.add(base, positions.create(7, 4, 7)),
        FillOperation.REPLACE
    )

    blocks.fill(
        AIR,
        positions.add(base, positions.create(1, 1, 1)),
        positions.add(base, positions.create(6, 3, 6)),
        FillOperation.REPLACE
    )

    blocks.fill(
        CONCRETE,
        positions.add(base, positions.create(0, 5, 0)),
        positions.add(base, positions.create(7, 5, 7)),
        FillOperation.REPLACE
    )

    blocks.place(
        OAK_DOOR,
        positions.add(base, positions.create(3, 1, 0))
    )

    blocks.place(
        GLASS,
        positions.add(base, positions.create(3, 2, 7))
    )

    mobs.spawn(
        mobs.animal(VILLAGER),
        positions.add(base, positions.create(3, 1, -1))
    )


def dedina():
    start_pos = player.position()

    for i in range(5):
        offset = positions.create(i * 12, 0, 0)
        base = positions.add(start_pos, offset)
        postav_dom(base)

    start = positions.add(start_pos, positions.create(0, 0, -2))
    end = positions.add(start_pos, positions.create(60, 0, -3))

    blocks.fill(
        COBBLESTONE,
        start,
        end,
        FillOperation.REPLACE
    )


player.on_chat("dedina", dedina)
