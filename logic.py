import random

Spells_DotA1 = {
    ('Q', 'Q', 'Q'): {'name': 'Icy Path', 'icon': 'icy_path.png'},
    ('Q', 'Q', 'W'): {'name': 'Portal', 'icon': 'portal.png'},
    ('Q', 'Q', 'E'): {'name': 'Frost Nova', 'icon': 'frost_nova.png'},
    ('Q', 'W', 'Q'): {'name': 'Betrayal', 'icon': 'betrayal.png'},
    ('Q', 'W', 'W'): {'name': 'Tornado Blast', 'icon': 'tornado_blast.png'},
    ('Q', 'W', 'E'): {'name': 'Levitation', 'icon': 'levitation.png'},
    ('Q', 'E', 'Q'): {'name': 'Power Word', 'icon': 'power_word.png'},
    ('Q', 'E', 'W'): {'name': 'Invisibility Aura', 'icon': 'invisibility_aura.png'},
    ('Q', 'E', 'E'): {'name': 'Shroud Of Flames', 'icon': 'shroud_of_flames.png'},
    ('W', 'Q', 'Q'): {'name': 'Mana Burn', 'icon': 'mana_burn.png'},
    ('W', 'Q', 'W'): {'name': 'EMP', 'icon': 'emp.png'},
    ('W', 'Q', 'E'): {'name': 'Soul Blast', 'icon': 'soul_blast.png'},
    ('W', 'W', 'Q'): {'name': 'Telelightning', 'icon': 'telelightning.png'},
    ('W', 'W', 'W'): {'name': 'Shock', 'icon': 'shock.png'},
    ('W', 'W', 'E'): {'name': 'Arcane Arts', 'icon': 'shock.png'},
    ('W', 'E', 'Q'): {'name': 'Scout', 'icon': 'scout.png'},
    ('W', 'E', 'W'): {'name': 'Energy Ball', 'icon': 'energy_ball.png'},
    ('W', 'E', 'E'): {'name': 'Lightning Shield', 'icon': 'lightning_shield.png'},
    ('E', 'Q', 'Q'): {'name': 'Chaos Meteor', 'icon': 'chaos_meteor.png'},
    ('E', 'Q', 'W'): {'name': 'Confuse', 'icon': 'confuse.png'},
    ('E', 'Q', 'E'): {'name': 'Disarm', 'icon': 'disarm.png'},
    ('E', 'W', 'Q'): {'name': 'Soul Reaver', 'icon': 'soul_reaver.png'},
    ('E', 'W', 'W'): {'name': 'Firestorm', 'icon': 'firestorm.png'},
    ('E', 'W', 'E'): {'name': 'Incinerate', 'icon': 'incinerate.png'},
    ('E', 'E', 'Q'): {'name': 'Deafening Blast', 'icon': 'deafening_blast.png'},
    ('E', 'E', 'W'): {'name': 'Inferno', 'icon': 'inferno.png'},
    ('E', 'E', 'E'): {'name': 'Fireblast', 'icon': 'fireblast.png'},
}

class InvokerSpells:
    def __init__(self):
        self.orbs = []
        self.target_spell = None
        self.invoked_spell = None
        self.score = 0
        self.time_left = time
        self.is_game_over = False

        self.next_spell()

    def press_orb(self, orb_type):
        if self.is_game_over:
            return
        if orb_type in ('Q', 'W', 'E'):
            self.orbs.append(orb_type)
            if len(self.orbs) > 3:
                self.orbs.pop(0)


    def invoke(self):
        if self.is_game_over or len(self.orbs) < 3:
            return
        cast = tuple(self.orbs)
        self.invoked_spell = Spells_DotA1.get(cast)


    def next_spell(self):
        random_cast = random.choice(list(Spells_DotA1.keys()))
        self.target_spell = Spells_DotA1[random_cast]


    def updating(self, delta_time):
        if not self.is_game_over:
            self.time_left -= delta_time
            if self.time_left <= 0:
                self.time_left = 0
                self.is_game_over = True



if __name__ == "__main__":
    time = 60.0
    game = InvokerSpells()
    print("Заклинание:", game.target_spell['name'])

    game.press_orb('Q')
    game.press_orb('Q')
    game.press_orb('Q')

    game.invoke()
    print(f"Ваше заклинание: {game.invoked_spell['name']}")
    if game.invoked_spell == game.target_spell:
        print("Пора в казино...")


