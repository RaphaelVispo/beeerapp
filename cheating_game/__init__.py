from otree.api import *
from cheating_game.config import Config

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'cheating_game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    input = models.IntegerField(label='Enter the result', min=1, max=6)



def get_count(list_answers):
    from collections import Counter 

    round_c = len(list_answers)
    round_result = Counter(list_answers)

    ratio = [0] * 6
    for values in round_result:
        ratio[values-1] = round_result[values] / round_c 

    return ratio

def vars_for_admin_report(subsession):

    vars = {}
    # Counter for each value of the user's input
    try: 
        players = [p.input for p in subsession.get_players()]
        all_players = [play.input for sess in subsession.in_all_rounds() for play in sess.get_players()]
        vars = dict(ratio=get_count(players), all_rounds=get_count(all_players)) 
    except:
        rat = [0] * 6 
        vars = dict(ratio=rat, all_rounds=rat)


    return vars


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['input']
    @staticmethod
    def vars_for_template(player: Player):
    
        return  dict(Config=Config)

class ResultsWaitPage(WaitPage):
    template_name = 'cheating_game/ResultsWaitPage.html'
    @staticmethod
    def vars_for_template(player: Player):
    
        return  dict(Config=Config)


class Instructions(Page):

    @staticmethod
    def vars_for_template(player: Player):
    
        return  dict(Config=Config)


page_sequence = [Instructions, MyPage, ResultsWaitPage]
