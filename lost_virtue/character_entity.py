import logging as log
from .tab_text import indented_print
from .user_input import user_input_name


class CharacterEntity:
    def __init__(self, name, max_hit_points, current_hit_points, attack_damage, armor):
        log.info("entering __init__ CharacterEntity")
        self.name = name
        self.max_hit_points = max_hit_points
        self.current_hit_points = current_hit_points
        self.attack_damage = attack_damage
        self.armor = armor
        log.info("leaving __init__ CharacterEntity")

    def attack(self, target):
        log.info(f'Entering {type(self)} attack')
        attack_damage = self.attack_damage

        log.debug(f'{self.name} attacking {target.name} for {self.attack_damage} damage')

        target.receive_damage(attack_damage)

        log.info(f'Exiting {type(self)} attack')

    def receive_damage(self, damage):
        log.info(f'Entering {type(self)} receive_damage')
        log.debug(f'{self.name} taking {damage} damage')
        # This prevents damage from hitting negative numbers
        if damage - self.armor < 0:
            damage_reduced_by_armor = 0
        else:
            damage_reduced_by_armor = damage - self.armor

        hit_points_after_damage = self.current_hit_points - damage_reduced_by_armor

        log.debug(f'{self.name} going from {self.current_hit_points} to {hit_points_after_damage}')
        indented_print(f'{self.name} was attacked for {damage_reduced_by_armor} damage!', indent_level=1)
        if hit_points_after_damage > 0:
            indented_print(f"{self.name} has {hit_points_after_damage} hit points left!", indent_level=1)
        else:
            indented_print(f"{self.name} has 0 hit points left!", indent_level=1)

        self.current_hit_points = hit_points_after_damage

        log.info(f'Exiting {type(self)} receive_damage')


class PlayerEntity(CharacterEntity):
    def __init__(self):
        log.info("entering Class PlayerEntity")
        self.player_name = user_input_name("What is your name?:")
        self.player_max_hit_points = 15
        self.current_hit_points = self.player_max_hit_points
        self.attack_damage = 4
        self.armor = 1
        self.player_class = 'farmhand'
        self.player_level = 1
        self.player_experience = 0
        self.player_next_level_experience = 4
        self.player_inventory_dict = {}

        super().__init__(self.player_name, self.player_max_hit_points, self.current_hit_points,
                         self.attack_damage, self.armor)

        log.debug("Exiting Class PlayerEntity")

    def rest(self):
        log.info('Entering player.rest')
        self.current_hit_points = self.player_max_hit_points
        rest_text = "You close your eyes, the horrors you've seen flash in your subconscious as you slowly drift off " \
                    "to sleep"
        wake_up_text = "You are stirred awake as the rays from first morning's light strike your body, " \
                       "You feel well rested"
        player_health_text = f"You have healed back up to {self.current_hit_points} hit points"
        print(rest_text)
        print(wake_up_text)
        indented_print(player_health_text, indent_level=1)
        log.info("Leaving player.rest")

    def receive_experience(self, enemy_character):
        log.info("entering player.receive_experience")
        self.player_experience = self.player_experience + enemy_character.experience_given
        print(f"You received {enemy_character.experience_given} EXP!")
        print(f"Your total EXP is {self.player_experience}")
        if self.player_experience < self.player_next_level_experience:
            print(f"Your next level up is at {self.player_next_level_experience} EXP")
        log.debug(f"players current experience is {self.player_experience}")

        if self.player_experience >= self.player_next_level_experience:
            log.info("player has hit experience threshold")
            self.player_level += 1
            print("Level up!")
            print(f"you are now level {self.player_level}")
            self.player_next_level_experience = 2 * self.player_next_level_experience
            self.level_up()
            log.debug(f"players next level up requires {self.player_next_level_experience}")
        log.info("leaving player.receive_experience")

    def level_up(self):
        log.info("entering player.level_up")
        # player stat increases
        self.player_max_hit_points += 4
        self.attack_damage += 1
        # Every three levels the player increases their armor
        if self.player_level / 3 == 1:
            self.armor += 1
            print(f"Your armor increased to {self.armor}")

        print(f"Your max HP increased to {self.player_max_hit_points}")
        print(f"Your attack damage went up to {self.attack_damage}")
        print(f"You need {self.player_next_level_experience} EXP for your next level up")

        # Heal player to their new max on level up
        self.current_hit_points = self.player_max_hit_points
        log.debug(f"player current_hit_points is now {self.current_hit_points}")

        log.info("leaving player level_up")

    def player_inventory_update(self, item, number_of_item):
        log.info("entering player.player_inventory_update")
        if item not in self.player_inventory_dict:
            # self.player_inventory_dict[item] = number_of_item
            insert_item_dict = {item, number_of_item}
            self.player_inventory_dict.update(insert_item_dict)
        else:
            pass


    def player_show_inventory(self):
        log.info("entering player.player_show_inventory")
        print(self.player_inventory2)
        log.info("leaving player.player_show_inventory")


class EnemyEntity(CharacterEntity):
    def __init__(self):
        log.debug("Initializing enemy")
        self.enemy_name = "goblin"
        self.enemy_max_hit_points = 12
        self.enemy_current_hit_points = 12
        self.enemy_attack_damage = 3
        self.enemy_armor = 1
        self.enemy_type = 'creature'
        super().__init__(self.enemy_name, self.enemy_max_hit_points, self.enemy_current_hit_points,
                         self.enemy_attack_damage, self.enemy_armor)
        log.debug("enemy initialized")
