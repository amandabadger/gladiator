class Character:
    name = ""
    stats = {"strength": 0,
        "stamina": 0,
        "wisdom": 0,
        "luck": 0,
        "evasiveness": 0,
        "dexterity": 0}
    health = 100


class NPC(Character):
    def __init__(self, level):
        for _ in level+10:
            self.stats[random.choice(list(stats))]+=1


class Player(Character):
    freedom = False
    statpoints = 0
    
    def __init__(self, name):
        statpoints = 10;
        self.name = name
