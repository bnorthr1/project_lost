import logging as log
import functools


def validate_user_input(user_input, validation_type):
    """
    Validates that the user input is of the given validation type
    :return: True if the input is valid, False otherwise
    """
    has_number = any(character.is_number() for character in user_input)
    has_spaces = any(character == ' ' for character in user_input)
    has_characters = any(character.is_alpha() for character in user_input)
    is_yes_or_no = user_input in ['yes', 'no']

    validation_type_to_conditions = {
        "name": False if any([has_number]) else True,
        "number": False if any([has_spaces, has_characters]) else True,
        "yesno": False if not is_yes_or_no else True
    }

    return validation_type_to_conditions[validation_type]


def user_input_name(message_prompt):
    taking_user_input = True
    while taking_user_input:
        try:
            user_input = input(message_prompt + " ")
            taking_user_input = False

            return user_input

        except ValueError:
            print("Stop trying to break my code")
        except TypeError:
            print("How did you manage to not give me a string?")
        except KeyboardInterrupt:
            print("Sorry you got stuck, I'll try harder!")
            quit()



def user_input_yes_or_no(message_prompt):
    taking_user_input = True
    while taking_user_input:
        try:
            user_input = input(message_prompt + " ")
            user_input = user_input.lower()

            if user_input not in ("yes", "no"):
                print("Please enter 'yes' or 'no'")
            else:
                taking_user_input = False
                return user_input

        except ValueError:
            print("Stop trying to break my code")
        except TypeError:
            print("How did you manage to not give me a string?")
        except KeyboardInterrupt:
            print("Sorry you got stuck, I'll try harder!")
            quit()

def user_input_fight_options(message_prompt):
    taking_user_input = True
    while taking_user_input:
        try:
            user_input = input(message_prompt + " ")
            user_input = user_input.lower()

            if user_input not in ("attack", "run"):
                print("Please enter 'attack' or 'run'")
            else:
                taking_user_input = False
                return user_input

        except ValueError:
            print("Stop trying to break my code")
        except TypeError:
            print("How did you manage to not give me a string?")
        except KeyboardInterrupt:
            print("Sorry you got stuck, I'll try harder!")
            quit()


def user_input_over_world_options(message_prompt):
    taking_user_input = True
    while taking_user_input:
        try:
            user_input = input(message_prompt + " ")
            user_input = user_input.lower()

            if user_input not in ("rest", "fight", "travel", "introspect", "shop", "inventory", "exit"):
                print("You are only able to 'rest', 'fight', 'travel', or 'introspect' right now")
            else:
                taking_user_input = False
                return user_input
        except ValueError:
            print("Stop trying to break my code")
        except TypeError:
            print("How did you manage to not give me a string?")
        except KeyboardInterrupt:
            print("Sorry you got stuck, I'll try harder!")
            quit()


def user_input_pick_fight(message_prompt):
    taking_user_input = True
    while taking_user_input:
        try:
            user_input = input(message_prompt + " ")
            user_input = user_input.lower()

            if user_input not in ("orc", "goblin"):
                print("You can only fight an orc or a goblin right now")
            else:
                taking_user_input = False
                return user_input
        except ValueError:
            print("Stop trying to break my code")
        except TypeError:
            print("How did you manage to not give me a string?")
        except KeyboardInterrupt:
            print("Sorry you got stuck, I'll try harder!")
            quit()


def user_pick_item(message_prompt):
    taking_user_input = True
    while taking_user_input:
        try:
            user_input = input(message_prompt + " ")
            user_input = user_input.lower()

            if user_input not in ("potion", "ether", "torch"):
                print("We only have potions, ether's, and torches available right now")
            else:
                taking_user_input = False
                return user_input
        except ValueError:
            print("Stop trying to break my code")
        except TypeError:
            print("How did you manage to not give me a string?")
        except KeyboardInterrupt:
            print("Sorry you got stuck, I'll try harder!")
            quit()


def user_pick_item_number(message_prompt):
    taking_user_input = True
    while taking_user_input:
        try:
            user_input = input(message_prompt + " ")
            user_input = int(user_input.lower())

            if user_input < 0:
                print("Please enter the number you would like to buy")
            else:
                taking_user_input = False
                return user_input
        except ValueError:
            print("Stop trying to break my code")
        except TypeError:
            print("How did you manage to not give me a string?")
        except KeyboardInterrupt:
            print("Sorry you got stuck, I'll try harder!")
            quit()


# # Decorator function that runs user inputs through try except block
# def user_input_decorator(func):
#     log.info("Entering user_input_decorator")
#
#     # Preserves the identity of passed in function for introspection
#     # @functools.wraps(func)
#     #THIS IMMEDIATELY RUNS AT STARTUP, WHY
#     def wrapper(*args, **kwargs):
#         try:
#             func(*args, **kwargs)
#             return func(*args, **kwargs)
#         except ValueError:
#             print("Stop trying to break my code")
#         except TypeError:
#             print("How did you manage to not give me a string?")
#         except KeyboardInterrupt:
#             print("Sorry you got stuck, I'll try harder!")
#             quit()
#
#     log.info("leaving user_input_decorator")
#     return wrapper()
#
#
# @user_input_decorator
# def user_input_name(message_prompt):
#     user_input = input(message_prompt + " ")
#
#     return user_input
#
#
# @user_input_decorator
# def user_input_yes_or_no(message_prompt):
#     user_input = input(message_prompt + " ")
#     user_input = user_input.lower()
#     taking_user_input = True
#
#     while taking_user_input:
#         if user_input not in ("yes", "no"):
#             print("Please enter 'yes' or 'no'")
#         else:
#             taking_user_input = False
#             return user_input
