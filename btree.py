"""
Binary Tree module
"""
from dataclasses import dataclass
from btnode import BinTrNode, get_player_marks, check_a_win


@dataclass
class BinaryTree:
    """
    Binary Tree class
    """
    root: BinTrNode
    token: str
    enemy_token: str

    @staticmethod
    def get_poss_moves(node: BinTrNode) -> list:
        """
        Returns a list of possible moves from a node
        """
        moves = [(i, j) for i in range(3) for j in range(3) if node.position[j][i] is None]
        return moves if len(moves) <= 2 else list(sorted(moves, key=lambda x: (x[1], x[0])))[:2]

    def build_tree(self, node: BinTrNode, token: str):
        """
        Builds a tree by some strange rules
        """
        node_moves = self.get_poss_moves(node)
        if len(node_moves) == 1:
            new_node = node.add_move(node_moves[0], token)
            node.left = new_node
            new_node.up = node
        elif len(node_moves) == 2:
            first_new, second_new = node.add_move(node_moves[0], token), node.add_move(node_moves[1], token)
            node.left, node.right = first_new, second_new
            first_new.up, second_new.up = node, node
            token_to_put_next = self.token if token == self.enemy_token else self.enemy_token
            self.build_tree(first_new, token_to_put_next)
            self.build_tree(second_new, token_to_put_next)

    def find_best_move(self):
        """
        Finds the best move in a tree by strange rules
        """
        leaves = self.find_leaves(self.root)
        results = [0, 0]
        for leaf in leaves:
            leaf_value = self.leaf_value(leaf)
            if leaf.comes_from_left(node=leaf):
                results[0] += leaf_value
            else:
                results[1] += leaf_value
        poss_moves = self.get_poss_moves(self.root)
        poss_moves = list(map(lambda x: (x[1], x[0]), poss_moves))
        return poss_moves[0] if results[0] == max(results) or len(poss_moves) == 1 else poss_moves[1]

    def leaf_value(self, leaf):
        """
        For cases if node is a leaf
        """
        if check_a_win(get_player_marks(self.token, leaf.position)):
            return 1
        if check_a_win(get_player_marks(self.enemy_token, leaf.position)):
            return -1
        return 0

    def find_leaves(self, node: BinTrNode):
        """
        Finds all leaves for some node
        """
        if node.left is not None and node.right is not None:
            return self.find_leaves(node.left) + self.find_leaves(node.right)
        elif node.right is not None:
            return self.find_leaves(node.right)
        elif node.left is not None:
            return self.find_leaves(node.left)
        return [node]
