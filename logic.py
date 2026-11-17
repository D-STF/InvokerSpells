import random
from spells import Spells_DotA1, Spells_DotA2

class InvokerSpells:
    def __init__(self, mode='dota1'):
        self.mode = mode
        self.target_spell = None
        self.spells = Spells_DotA1 if mode == 'dota1' else Spells_DotA2
        self.orbs = []
        self.invoked_spell = None
        self.score = 0
        self.time_left = 60.0
        self.is_game_over = False

        self.next_spell()


    def invoke(self):
        if self.is_game_over or len(self.orbs) < 3:
            return

        if self.mode == 'dota2':
            cast = tuple(sorted(self.orbs))
        else:
            cast = tuple(self.orbs)

        self.invoked_spell = self.spells.get(cast)

        if self.invoked_spell == self.target_spell:
            self.score += 1
            self.next_spell()


    def press_orb(self, orb_type):
        if self.is_game_over:
            return
        if orb_type in ('Q', 'W', 'E'):
            self.orbs.append(orb_type)
            if len(self.orbs) > 3:
                self.orbs.pop(0)

    def next_spell(self):
        random_cast = random.choice(list(self.spells.keys()))
        self.target_spell = self.spells[random_cast]


    def updating(self, delta_time):
        if not self.is_game_over:
            self.time_left -= delta_time
            if self.time_left <= 0:
                self.time_left = 0
                self.is_game_over = True

    def reset(self, mode=None):

        if mode in ('dota1', 'dota2'):
            self.mode = mode
            self.spells = Spells_DotA1 if self.mode == 'dota1' else Spells_DotA2


        self.orbs = []
        self.invoked_spell = None
        self.score = 0
        self.time_left = 60.0
        self.is_game_over = False

        self.next_spell()

    def toggle_mode(self):
        next_mode = 'dota2' if self.mode == 'dota1' else 'dota1'
        self.reset(next_mode)


if __name__ == "__main__":
    time = 60.0
    choice = input("Mode:")

    if choice == 'dota1':
        game = InvokerSpells(mode='dota1')
    if choice == 'dota2':
        game = InvokerSpells(mode='dota2')




    print("Заклинание:", game.target_spell['name'])

    game.press_orb('Q')
    game.press_orb('W')
    game.press_orb('E')

    game.invoke()
    print(f"Ваше заклинание: {game.invoked_spell['name']}")



