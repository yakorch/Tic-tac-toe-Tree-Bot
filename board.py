"""Module for a Board class"""
from btree import BinaryTree
from btnode import BinTrNode, check_a_win, get_player_marks


class Board:
    """
    Board class
    """
    first_token = "x"
    second_token = "0"

    def __init__(self):
        """
        Creates an empty board
        """
        self.board = [[None for _ in range(3)] for _ in range(3)]

    def get_status(self):
        """
        Returns one state of a board, possible are:
        "x", "0", "draw", "continue".
        """
        marks_first = get_player_marks(self.first_token, self.board)
        marks_second = get_player_marks(self.second_token, self.board)
        for ind, player_marks in enumerate([marks_first, marks_second]):
            if check_a_win(player_marks):
                return self.first_token if ind == 0 else self.second_token
        return "continue" if len([(j, i) for i in range(3) for j in range(3) \
                                  if self.board[i][j] is None]) else "draw"

    def make_move(self, position: tuple, turn: str):
        """
        Makes a move
        position - tuple with coords - (x, y), turn - "x" or "0"
        """
        if not isinstance(position, (tuple, list)) or turn not in \
                (self.first_token, self.second_token) or \
                position[0] not in range(3) or position[1] not in range(3) or \
                self.board[position[0]][position[1]] is not None:
            raise IndexError()
        self.board[position[0]][position[1]] = turn

    def make_computer_move(self):
        """
        Computer's move for second_token
        """
        tree = BinaryTree(root=BinTrNode(list(self.board)),
                          token=self.second_token, enemy_token=self.first_token)
        tree.build_tree(tree.root, self.second_token)
        comp_move = tree.find_best_move()
        self.make_move(comp_move, self.second_token)

    def __repr__(self):
        return "\n".join([str(item).replace("None", "' '")
                          for item in self.board])


# board = Board()
# board.make_move((0, 0), "x")
# board.make_move((0, 1), "x")
# board.make_move((1, 0), "0")
# board.make_move((0, 2), "0")
# print()
# print(board, end="\n\n")
# board.make_computer_move()
# print(board, end="\n\n")
# board.make_move((2, 2), "x")
# board.make_computer_move()
# print(board, end="\n\n")
# print(board.get_status())
# try:
#     board.make_move((4, 4), "")
# except IndexError as err:
#     print(err)

# board.make_move((1, 1), "x")
# for i in [(2, 0), (2, 1), (0, 2), (1, 2)]:
#     board.make_move(i, "x")
# board.make_computer_move()
# print(board.get_status())
# print(board)
