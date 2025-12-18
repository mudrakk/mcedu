def detonaciacia (size):
    agent.set_slot(1) 
    for height in range(size):
        for lane in range(size):
            agent.set_assist(PLACE_ON_MOVE, True)
            agent.move(FORWARD, size)
            agent.set_assist(PLACE_ON_MOVE, False)
            agent.move(LEFT, 1)
            agent.move(BACK, size)
        agent.move(UP, 1)
        agent.move(RIGHT, size)
    agent.set_slot(2)
    agent.place(DOWN)
    agent.move(UP, 30)
player.on_chat("det", detonaciacia)
