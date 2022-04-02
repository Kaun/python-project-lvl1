#!/usr/bin/env python
from brain_games.games import prime
from brain_games.engine import run_game


def main():
    run_game(prime)
    # user_name = brain_games.control_game.welcome_user()
    # brain_games.control_game.start_game(
    #     brain_games.games.prime.game_prime, user_name)


if __name__ == '__main__':
    main()
