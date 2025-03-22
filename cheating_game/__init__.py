from otree.api import *
import time

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'cheating_game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    input = models.IntegerField(label='Enter the result', min=1, max=6)



def vars_for_admin_report(subsession):
    from collections import Counter 

    # Counter for each value of the user's input
    players = [p.input for p in subsession.get_players()]
    c = len(players)
    Input = Counter(players)

    # Creating a 
    ratio = [0] * 6
    label = ['1', '2', '3', '4', '5', '6']
    for values in Input:
        ratio[values-1] = Input[values] / c 

    return dict(ratio=ratio, label= label)


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['input']


class ResultsWaitPage(WaitPage):
    template_name = 'cheating_game/ResultsWaitPage.html'

    # after_all_players_arrive = set_payoffs


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
