from heapq import heapreplace, heappush, heappop
import sys
N, M, K = map(int, input().split())
L = N+1
guns = [[] for _ in range(L*L)]
board = [0] * (L*N) + [1] * L

for x in range(0, L*N, L):
    board[x+N] = 1
    line = map(int, input().split())
    for xy, gun in enumerate(line, x):
        if gun:
            guns[xy].append(-gun)

class Player:
    order = []
    delta = (-L, 1, L, -1)
    guns_heap = guns

    def __init__(self, x, y, d, s):
        self.coord = (x - 1) * L + (y - 1)
        self.direc = d
        self.stat = -s
        self.gun = 0
        self.score = 0

        Player.order.append(self)

    def move(self):
        next_coord = self.coord + Player.delta[self.direc]
        self.direc = (self.direc + 2) % 4 if board[next_coord] == 1 else self.direc
        self.coord = self.coord + Player.delta[self.direc]

    def compare(self):
        if not Player.guns_heap[self.coord]:
            return
        elif not self.gun:
            self.gun = heappop(Player.guns_heap[self.coord])
        elif self.gun > Player.guns_heap[self.coord][0]:
            self.gun = heapreplace(Player.guns_heap[self.coord], self.gun)

    def fight(self, another_player):
        winner, loser = sorted([self, another_player], key=lambda x: (x.stat + x.gun, x.stat))
        score = winner.stat + winner.gun - loser.stat - loser.gun
        loser.lose()
        winner.win(score)
        return (loser, winner)

    def lose(self):

        if self.gun:
            heappush(Player.guns_heap[self.coord], self.gun)
        self.gun = 0

        for d in range(4):
            next_direc = (self.direc + d) % 4
            next_coord = self.coord + Player.delta[next_direc]
            if board[next_coord]:
                continue

            self.direc = next_direc
            self.coord = next_coord
            self.compare()
            return

    def win(self, score):

        self.score += score
        self.compare()


for _ in range(M):
    x, y, d, s = map(int, input().split())
    Player(x, y, d, s)

for player in Player.order:
    board[player.coord] = player

for turn in range(K):
    for player in Player.order:
        board[player.coord] = 0
        player.move()

        if board[player.coord]:
            loser, winner = player.fight(board[player.coord])
            board[loser.coord] = loser
            board[winner.coord] = winner
        else:
            player.compare()
            board[player.coord] = player

answer = []
for player in Player.order:
    answer.append(str(-player.score))
print(guns)
print(' '.join(answer))