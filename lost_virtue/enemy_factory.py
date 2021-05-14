from .character_entity import CharacterEntity
import logging as log


class EnemyEntity(CharacterEntity):
    def __init__(self, enemy_name, enemy_type, hit_points, attack_damage, armor, experience_given):
        log.debug("Initializing enemy")
        self.enemy_name = enemy_name
        self.enemy_max_hit_points = hit_points
        self.current_hit_points = self.enemy_max_hit_points
        self.enemy_attack_damage = attack_damage
        self.enemy_armor = armor
        self.experience_given = experience_given

        # Unique values to child class
        self.enemy_type = enemy_type

        super(EnemyEntity, self).__init__(name=self.enemy_name,
                                          max_hit_points=self.enemy_max_hit_points,
                                          current_hit_points=self.current_hit_points,
                                          attack_damage=self.enemy_attack_damage,
                                          armor=self.enemy_armor)

        log.debug("enemy initialized")


class EnemyFactory:
    def __init__(self):

        # Switch
        self.enemy_creator_switch = {
            'goblin': self._create_goblin,
            'orc': self._create_orc
        }

    def create_enemy(self, enemy_name):
        return self.enemy_creator_switch[enemy_name]()

    # Quick explanation, the key here is 'goblin', it goes to the enemy_creator_switch
    # dictionary, looks up the key 'goblin' and maps to the function '_create_goblin'
    # then executes it (thats why there is a set of paren outside the call)
    # its a little confusing but look it over & ask me if you need help. 
    # This is a SUPER USEFUL pattern in python, I use it constantly

    def _create_goblin(self):
        log.info("inside _create_goblin")
        new_goblin = EnemyEntity(enemy_name='goblin',
                                 enemy_type='creature',
                                 attack_damage=3,
                                 hit_points=10,
                                 armor=0,
                                 experience_given=2)
        return new_goblin

    def _create_orc(self):
        log.info("inside _create_orc")
        new_orc = EnemyEntity(enemy_name='orc',
                              enemy_type='humanoid',
                              attack_damage=6,
                              hit_points=15,
                              armor=2,
                              experience_given=5)
        return new_orc
