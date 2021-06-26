"""
Requirements
* Board can start a game
* Board can drop an initial location
* Board can let you move
    * check if your move is correct
    * update Board by your move
* Board can tell you if game ends and your outcome
* Board can reset

            (A)

         (B)   (C)

      (D)   (E)   (F)

   (G)   (H)   (I)   (J)

(K)   (L)   (M)   (N)   (O)


            (A)

         (B)   (C)

      (D)    E    (F)

   (G)   (H)   (I)   (J)

(K)   (L)   (M)   (N)   (O)

"""

class Board:
    def __init__(self):
        self.key = dict(zip([i for i in range(15)], "ABCDEFGHIJKLMNO"))
        self.board = [True for i in range(15)]
        self.all_pathes = self._get_all_pathes()
        self.mid_map = self._get_mid_map()
        self.is_first = True
        self.move_cnt = 0

    def _get_all_pathes(self):
        all_pathes = [
            (0,1,3),
            (0,2,5),
            (10,6,3),
            (10,11,12),
            (14,9,5),
            (14,13,12),
            (1,3,6),
            (1,4,8),
            (6,3,1),
            (6,7,8),
            (9,5,2),
            (9,8,7),
            (2,4,7),
            (2,5,9),
            (11,7,4),
            (11,12,13),
            (13,8,4),
            (13,12,11),
            (3,1,0),
            (3,4,5),
            (3,6,10),
            (3,7,12),
            (5,2,0),
            (5,4,3),
            (5,8,12),
            (5,9,14),
            (12,7,3),
            (12,8,5),
            (12,11,10),
            (12,13,14),
            (4,7,11),
            (4,8,13),
            (7,4,2),
            (7,8,9),
            (8,4,1),
            (8,7,6)
        ]
        return all_pathes

    def find_mid(self, i: int, j: int):
        if (i,j) not in self.mid_map:
            return    
        return self.mid_map[(i, j)]

    def is_valid_move(self, i: int, j: int):
        mid = self.find_mid(i, j)
        if mid is None:
            return False
        return self.board[i] and self.board[mid] and not self.board[j]

    def _get_mid_map(self):
        mid_map = {}
        for path in self.all_pathes:
            mid_map[(path[0], path[2])] = path[1]
        return mid_map

    def first_move(self, i: int):
        if not self.is_first:
            print("已經去除第一個房子了")
            return
        self.board[i] = False
        self.is_first = False

    def move(self, i: int, j: int):
        if not self.is_valid_move(i, j):
            print("無效的移動方式\n")
            return
        self.board[i] = False
        self.board[j] = True
        self.board[self.mid_map[(i,j)]] = False # remove mid
        print("將房子 {} 移動至 {}\n\n".format(self.key[i], self.key[j]))
        self.move_cnt += 1
        
    def reset(self):
        self.board = [True for i in range(15)]
        self.first = True

    def show(self):
        cnt = 0
        for i in range(5):
            print(*(["   "] * (4-i)), sep='', end='')
            for j in range(i+1):
                if self.board[cnt+j]:
                    print("(" + self.key[cnt+j] + ")", end='')
                else:
                    print(" " + self.key[cnt+j] + " ", end='')
                print("   ", end='')
            cnt += (i+1)
            print("\n\n", end='')

    def has_next(self) -> bool:
        for p in self.all_pathes:
            if self.is_valid_move(p[0], p[2]):
                return True
        return False

    def remain(self) -> int:
        return sum(self.board)



class Game:
    def __init__(self):
        self.board = Board()
        self.key = dict(zip("ABCDEFGHIJKLMNO", [i for i in range(15)])) 

    def run(self):
        print("跳房子遊戲")
        self.board.show()
        print("請先移除一個房子")
        while self.board.has_next() or self.board.is_first:
            if self.board.is_first:
                k = input("").replace("\n", "").split(" ")
                k = self.key[k[0].upper()]
                self.board.first_move(k)
            else:
                print("移動房子: ", end='')
                k = input("").replace("\n", "").split(" ")
                c = self.key[k[0].upper()]
                d = self.key[k[1].upper()]
                self.board.move(c, d)
            self.board.show()
            print("\n")
        
        print("遊戲結束")
        r = self.board.remain()
        if r == 1:
            print("恭喜過關! 共走了 {} 步".format(self.board.move_cnt))
        else:
            print("剩餘 {} 個房子，再接再厲".format(r))



if __name__ == '__main__':
    a = Game()
    a.run()
