#!/usr/bin/env python
import brain_games.games.prime
import brain_games.control_game


def main():
    user_name = brain_games.control_game.welcome_user()
    brain_games.control_game.start_game(
        brain_games.games.prime.game_prime, user_name)


if __name__ == '__main__':
    main()
