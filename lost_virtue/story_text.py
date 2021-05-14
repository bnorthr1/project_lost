import random


def game_opening(player_character):
    text_game_opening = f"You are a simple {player_character.player_class} named {player_character.player_name}, " \
                        f"it's been three years since you were separated from your family during the Awakening, " \
                        f"and since Old Man Mengsk found you half-starved and nearly dead, since then " \
                        f"you've helped tend to his farm, and clear out the nearby woods of monsters"
    print(text_game_opening)


def introspect():
    player_thinks_about_family = "Did my family ever make it to Leon? the grueling journey from our home is no small " \
                                 "undertaking, I hope no one else died escaping the Horrors..."
    player_thinks_about_mengsk = "I owe my life to Old Man Mengsk, I hope all my work over the years has been enough " \
                                 "to repay his kindness"
    player_thinks_about_awakening = "The Awakening wrought so much destruction... I wonder if the Horrors will one " \
                                    "day find their way to our village"
    player_thinks_about_little_sister = "Ayve turns eleven this year, I hope my little sister hasn't forgotten about " \
                                        "me in all this time"
    player_thinks_about_brothers_death = "I woke up in the middle of the night screaming again, I could still feel " \
                                         "the blood of my brother Ophelio splattering across me as he was ripped " \
                                         "apart by a Horror... that creatures eyes... a bottomless abyss that will " \
                                         "forever haunt me"

    introspection_list = [player_thinks_about_family, player_thinks_about_awakening, player_thinks_about_brothers_death,
                          player_thinks_about_mengsk, player_thinks_about_little_sister]

    random_thought = random.randrange(0, len(introspection_list))
    players_thought = introspection_list[random_thought]
    print(players_thought)
