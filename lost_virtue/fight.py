import logging as log
from .tab_text import indented_print
from .check_fight_deaths import check_deaths
from .user_input import user_input_fight_options as input_fight_options


def fight(player_character, enemy_character):
    log.info("entering fight")
    print(f"A {enemy_character.enemy_name} has attacked you!")

    fight_active = True
    while fight_active:
        log.info("Inside a fight")
        character_turn = input_fight_options("What would you like to do? (Attack/Run)")

        # Player Character takes their turn
        player_attack_option = 'attack'
        player_run_option = 'run'
        if character_turn == player_attack_option:
            log.info("Character has attacked")
            player_character.attack(enemy_character)
        elif character_turn == player_run_option:
            log.info("Character has run")
            run_text = f"You run from the {enemy_character.enemy_name}"
            indented_print(run_text, indent_level=1)
            fight_active = False

        # check for any deaths only if we are still in the fight
        if fight_active:
            fight_active = check_deaths(player_character, enemy_character, fight_active)

        # Enemy takes its turn
        # Want to incorporate a random number generator to select enemies moves, but will create later
        if fight_active:
            log.info("Enemy Turn")
            input("Press Enter for the enemy's turn")
            enemy_character.attack(player_character)

        # check for any deaths, only if we are still fighting
        if fight_active:
            fight_active = check_deaths(player_character, enemy_character, fight_active)

