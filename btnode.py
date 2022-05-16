"""
Module for a binary tree node
"""
from dataclasses import dataclass
from copy import deepcopy
import itertools

def get_player_marks(player: str, board: list) -> list:
    """
    Finds all marks on the board
    """
    return [(j, i) for i in range(3) for j in range(3) if board[i][j] == player]


def check_a_win(coords: list) -> bool:
    """
    Checks if position is a win
    """
    win_situations = [tuple((i, j) for j in range(3)) for i in range(3)]
    win_situations.extend([tuple((j, i) for j in range(3)) for i in range(3)])
    win_situations.extend([tuple((i, i) for i in range(3)), tuple((2 - i, i) for i in range(3))])
    players_triples = list(itertools.combinations(coords, 3))
    return any([item for item in players_triples if item in win_situations])


@dataclass
class BinTrNode:
    """
    Binary Tree Node
    """
    position: list
    left: bool = None
    right: bool = None
    up: bool = None

    def add_move(self, pos: tuple, token: str):
        """
        Creates a new node by making a move
        """
        new_node = BinTrNode(deepcopy(self.position))
        new_node.position[pos[1]][pos[0]] = token
        return new_node

    # def __str__(self):
    #     return "\n".join([str(item).replace("None", "' '").replace(", ", ",") for item in self.position])

    def count_children(self):
        """
        Counts the number of children of a node
        """
        number = 0
        for side in (self.left, self.right):
            if side is not None:
                number += 1
        return number

    def comes_from_left(self, node):
        if node.up is not None:
            if node.up.up is None:
                return node.up.left is node
            return self.comes_from_left(node.up)
        return False
