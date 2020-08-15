class Warrior:
    list_of_ranks = ["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion",
                     "Master", "Greatest"]

    def __init__(self):
        self.level = 1
        self.experience = 100
        self.rank = self.list_of_ranks[0]
        self.achievements = []

    def training(self, array):
        if self.level < array[2]:
            return "Not strong enough"
        else:
            self.achievements.append(array[0])
            self.update_exp(array[1])
            return array[0]

    def battle(self, level):
        if level < 1 or level > 100:
            return "Invalid level"
        elif self.rank_check(level):
            return "You've been defeated"
        else:
            if level == self.level:
                message = "A good fight"
                gained_exp = 10
            elif level + 1 == self.level:
                message = "A good fight"
                gained_exp = 5
            elif level < self.level:
                message = "Easy fight"
                gained_exp = 0
            else:
                message = "An intense fight"
                gained_exp = 20 * (level - self.level) * (level - self.level)
            self.update_exp(gained_exp)
            return message

    def rank_check(self, level):
        if level // 10 > self.level // 10 and level - 5 >= self.level:
            return True
        else:
            return False

    def update_exp(self, exp):
        if self.experience + exp > 10000:
            self.experience = 10000
        else:
            self.experience += exp
        self.level = self.experience // 100
        self.rank = self.list_of_ranks[self.level // 10]


tom = Warrior()
# print(tom.level)
# print(tom.experience)
# print(tom.rank)

bruce_lee = Warrior()
print(bruce_lee.level)
print(bruce_lee.experience)
print(bruce_lee.rank)
print(bruce_lee.achievements)
print(bruce_lee.training(["Defeated Chuck Norris", 9000, 1]))
print(bruce_lee.experience)
print(bruce_lee.level)
print(bruce_lee.rank)
print(bruce_lee.battle(90))
print(bruce_lee.experience)
print(bruce_lee.achievements)
