class User:
    def __init__(self):
        self.rank_index = 0
        self.available_ranks = [i for i in range(-8, 9) if i != 0]
        self.rank = self.available_ranks[self.rank_index]
        self.progress = 0

    def inc_progress(self, kata_rank):
        if kata_rank not in self.available_ranks:
            raise ValueError
        dif = self.available_ranks.index(kata_rank) - self.available_ranks.index(self.rank)
        if dif == 0:
            self.progress += 3
        if dif == -1:
            self.progress += 1
        if dif < -1:
            self.progress += 0
        if dif >= 1:
            self.progress += (10 * dif ** 2)
        if self.progress >= 100:
            rnk_up, self.progress = divmod(self.progress, 100)
            self.rank_index += rnk_up
        if self.rank_index > len(self.available_ranks) - 1:
            self.rank_index = len(self.available_ranks) - 1
        self.rank = self.available_ranks[self.rank_index]
        if self.rank == self.available_ranks[-1]:
            self.progress = 0
