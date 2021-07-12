from game import Game
from level_1 import Level1
from level_2 import Level2


def main():
    game = Game("Scratch", 800, 640)
    game.add_level("level 1", Level1)
    game.add_level("level 2", Level2)
    game.set_start_level("level 1")
    game.run()


if __name__ == "__main__":
    main()
