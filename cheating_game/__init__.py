from otree.api import *
from cheating_game.config import Config
from settings import database

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'cheating_game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    input = models.IntegerField(label='Enter the result', min=1, max=6)
    dice = models.IntegerField(min=1, max=6)

def get_count(list_answers):
    from collections import Counter 

    round_c = len(list_answers)
    round_result = Counter(list_answers)

    ratio = [0] * 6
    for values in round_result:
        ratio[values-1] = round_result[values] / round_c 

    return ratio

def vars_for_admin_report(subsession: Subsession):

    vars = {}
    # Counter for each value of the user's input
    try: 
        players = [p.input for p in subsession.get_players()]
        print(players)
        all_players = [play.input for sess in subsession.in_previous_rounds() for play in sess.get_players()]
        print(all_players)
        vars = dict(ratio=get_count(players), all_rounds=get_count(all_players)) 
    except:
        rat = [0] * 6 
        vars = dict(ratio=rat, all_rounds=rat)


    return vars

def get_config(player: Player):
    session_config = player.session.config['config']
    game_config = database.game_config.document(session_config).get().to_dict()

    print(game_config)
    config = Config(
        game_config["instruction"]["header"], game_config["instruction"]["steps"], 
        game_config["button"], player.session.config['number_rounds'],
        game_config["dice"], game_config["script"] 
    )
    config.format_string()

    return config

# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['input', 'dice']

    @staticmethod
    def vars_for_template(player: Player):
        config = get_config(player)
        return  dict(Config=config, round_number = player.round_number)
    
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number <= player.session.config['number_rounds']


class Instructions(Page):

    @staticmethod
    def vars_for_template(player: Player):
        config = get_config(player)

        return  dict(Config=config)

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

page_sequence = [Instructions, MyPage]
