from otree.api import *
from Public_Good_Game.config import Config


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Public_Good_Game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    ENDOWMENT = 1000
    COST = 5000
    PROBABILITY = 1/2


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    contribution = models.IntegerField(label='Enter the amount', min=0, max=C.ENDOWMENT)


def vars_for_admin_report(subsession):
    players = subsession.get_players()
    contributions = [p.contribution for p in players]
    total_contribution = sum(contributions)
    return dict(total=total_contribution)

# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['contribution']

class Instructions(Page):
    template_name = 'cheating_game/Instructions.html'

    @staticmethod
    def vars_for_template(player: Player):
        
        return  dict(Config=Config)

class ResultsWaitPage(WaitPage):
    template_name = 'cheating_game/ResultsWaitPage.html'

class Results(Page):
    pass


page_sequence = [Instructions, MyPage, ResultsWaitPage, Results]
