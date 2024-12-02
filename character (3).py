class Character:
    def __init__(self, name, hp, attack, defense, role=None):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.role = role

    def take_damage(self, damage):
        
        damage_taken = max(0, damage - self.defense)
        self.hp -= damage_taken
        return damage_taken

    def is_alive(self):

        return self.hp > 0

    def __str__(self):
        return f"Name: {self.name}, Role: {self.role}, HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}"

class Hero(Character):
    def __init__(self, name, hp, attack, defense, role):
        super().__init__(name, hp, attack, defense, role)
        self.exp = 0

    def special_attack(self):

        if self.role == "Warrior":
            return self.attack * 1.5
        elif self.role == "Mage":
            return self.attack * 2
        elif self.role == "Archer":
            return self.attack * 1.2
        else:
            return self.attack

    def gain_exp(self, amount):

        self.exp += amount
        print(f"{self.name} gained {amount} experience. Total EXP: {self.exp}")

    def __str__(self):

        return f"Name: {self.name}, Role: {self.role}, HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}, EXP: {self.exp}"

class Monster(Character):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)

    def __str__(self):

        return f"Monster Name: {self.name}, HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}"
