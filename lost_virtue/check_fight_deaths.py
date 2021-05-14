import logging as log


# Determine if someone in the fight has died
def check_deaths(player_character, enemy_character, fight_active):
    log.info("Entering check_deaths method")
    text_player_death = """You fall to the ground, completely and utterly beaten. With your last gasps of breath 
    escaping your body, you realize that you were not strong enough and that you will never see your family again"""
    text_enemy_death = """You have successfully defeated the enemy! You were stronger than you imagined and won in 
    glorious combat!"""
    text_player_has_died = "Press Enter to die"
    text_continue = "Press Enter to continue"

    log.debug(f"player_current_hit_points is {player_character.current_hit_points}")
    log.debug(f"enemy_current_hit_points is {enemy_character.current_hit_points}")
    if player_character.current_hit_points <= 0:
        print(text_player_death)
        input(text_player_has_died)
        fight_active = False
        quit()
    elif enemy_character.current_hit_points <= 0:
        print(text_enemy_death)
        input(text_continue)
        fight_active = False
        player_character.receive_experience(enemy_character)

    log.info("Leaving check deaths method")
    return fight_active
