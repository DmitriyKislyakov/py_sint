import random
class Cell:
    def __init__(self, mine=False, around_mines=0, fl_open=False):
        self.mine = mine
        self.around_mines = around_mines
        self.fl_open = fl_open

class GamePole:
    def __init__(self, N: int, M: int):
        self.n = N
        self.m = M
        self.pole = [[Cell() for i in range(self.n)] for j in range(self.n)]
        self.init()

    def init(self):
        self.mine =random.sample(range(self.n**2), self.m)
        print(self.mine)
        self.count = 0
        for i in range(self.n):
            for j in range(self.n):
                if self.count in self.mine:
                    self.pole[i][j].mine = True
                    self.pole[i][j].fl_open = True #скрыть в готовом варианте
                self.count += 1

    def show(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.pole[i][j].fl_open == False:
                    print('#', end=' ')
                elif self.pole[i][j].mine == True:
                    print("*", end=' ')
                else:
                    print(self.pole[i][j].around_mines, end='  ')
            print()


pole = GamePole(10, 12)
pole.show()


