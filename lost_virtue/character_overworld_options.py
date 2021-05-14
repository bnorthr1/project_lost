import lost_virtue.user_input as user_input
import logging as log
from .fight import fight
from .tab_text import indented_print


# Working to end game by hitting end of line on character death, still needs work
def character_options_switch(player_character, enemy_factory, narrator):
    log.info("Entering character_options_switch")
    player_choice = user_input.user_input_over_world_options("What would you like to do? (Rest/Travel/Fight"
                                                             "/Introspect/Exit)")

    def player_rest_option():
        log.info("Player has chosen to rest")
        player_character.rest()

    def player_travel_option():
        log.info("Player has chosen to travel")
        travel_text = "You don't want to leave Old Man Mengsk, you still feel the need to help him"
        indented_print(travel_text, indent_level=1)

    # def player_fight_option():
    #     log.info("Player has chosen to fight")
    #
    #     # goblin_enemy = enemy_factory.create_enemy('goblin')
    #     orc_enemy = enemy_factory.create_enemy('orc')
    #     text_fight_start = "press Enter to fight!"
    #
    #     input(text_fight_start)
    #     fight(player_character, orc_enemy)

    def player_shop_option():
        log.info("Player has chosen the store")

        chosen_item_to_buy = user_input.user_pick_item("You can buy a 'potion','ether' or 'torch'")
        chosen_number_to_buy = user_input.user_pick_item_number("How many would you like to buy? (0 for none)")
        player_character.player_inventory_update(chosen_item_to_buy, chosen_number_to_buy)

    def player_check_inventory_option():
        log.info("Player is checking inventory")

        player_character.player_show_inventory()

    def player_fight_option():
        log.info("Player has chosen to fight")

        chosen_enemy_to_fight = user_input.user_input_pick_fight("fight an (orc) or a (goblin)?")
        text_fight_start = "press Enter to fight!"
        if chosen_enemy_to_fight == "goblin":
            goblin_enemy = enemy_factory.create_enemy('goblin')
            input(text_fight_start)
            fight(player_character, goblin_enemy)
        elif chosen_enemy_to_fight == "orc":
            orc_enemy = enemy_factory.create_enemy('orc')
            input(text_fight_start)
            fight(player_character, orc_enemy)

    def player_exit_option():
        log.info("Player has chosen to exit")
        player_exit_choice = user_input.user_input_yes_or_no("Are you sure you wish to exit? (yes/no)")

        if player_exit_choice == "yes":
            quit()

    def player_introspect_option():
        narrator.introspect()

    player_options_switch = {
            'rest': player_rest_option,
            'travel': player_travel_option,
            'fight': player_fight_option,
            'exit': player_exit_option,
            'introspect': player_introspect_option,
            'shop': player_shop_option,
            'inventory': player_check_inventory_option
        }

    # takes character input
    function = player_options_switch.get(player_choice, "I didn't understand that")
    function()
    log.info("Exiting character_options_switch")

    return function

