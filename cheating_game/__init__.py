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


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['input']


class ResultsWaitPage(WaitPage):
    template_name = 'cheating_game/ResultsWaitPage.html'
    # pass

class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
