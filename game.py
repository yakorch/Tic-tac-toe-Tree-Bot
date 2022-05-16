from board import Board


def ask_user_move(board: Board) -> None:
    """
    Asks user a move
    """
    while True:
        user_move = tuple(map(lambda x: int(x), input().split()))
        try:
            board.make_move(user_move, board.first_token)
            break
        except IndexError:
            print("Invalid move. position - tuple with coords - (x, y)")
            print(board)
            print()
            continue


def main() -> None:
    i = 0
    board = Board()
    while board.get_status() == "continue":
        print(board)
        print()
        if not i % 2:
            ask_user_move(board)
            print()
        else:
            board.make_computer_move()
        i += 1
    print(board)
    print(f"The end. Status of the game: {board.get_status()}")


if __name__ == "__main__":
    main()
