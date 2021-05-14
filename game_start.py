import lost_virtue.character_entity as character_entity
from lost_virtue.enemy_factory import EnemyFactory
import lost_virtue.story_text as narrator
from lost_virtue.character_overworld_options import character_options_switch
import logging as log

# log.basicConfig(level=log.DEBUG)

# Create needed game objects
game_active = True
enemy_factory = EnemyFactory()
player_character = character_entity.PlayerEntity()
narrator.game_opening(player_character)

# start the game
while game_active:
    log.info("entering game_active")
    character_options_switch(player_character, enemy_factory, narrator)
    log.info("Game is ending")