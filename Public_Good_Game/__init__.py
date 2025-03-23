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
    AGENT_ROLE = "Agent"
    PRINCIPAL_ROLE = "Principal"

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    contribution = models.IntegerField(label='Enter the amount', min=0, max=C.ENDOWMENT)
    isWin = models.BooleanField(label="pick")

def vars_for_admin_report(subsession):
    players = subsession.get_players()
    contributions = []
    isWin = True

    for p in players:
        try: 
            try:
                contributions.append(p.contribution)
            except:
                isWin = p.isWin
        except:
            pass

    total_contribution = sum(contributions)
    return dict(total=total_contribution,
                isWin=isWin
                )

# PAGES
class SpinWheelPage(Page):
    form_model = 'player'
    form_fields = ['isWin']
    # pass
    @staticmethod
    def is_displayed(player):
        return player.role == C.AGENT_ROLE
    

class ContributorPage(Page):
    form_model = 'player'
    form_fields = ['contribution']

    @staticmethod
    def is_displayed(player):
        return player.role != C.AGENT_ROLE


def set_payoffs(group):
    principal = group.get_player_by_role(C.AGENT_ROLE)
    isWin = principal.isWin
    print (principal, isWin)

class Instructions(Page):
    template_name = 'cheating_game/Instructions.html'

    @staticmethod
    def vars_for_template(player: Player):
        
        return  dict(Config=Config)

class ResultsWaitPage(WaitPage):
    template_name = 'cheating_game/ResultsWaitPage.html'
    after_all_players_arrive = 'set_payoffs'
class Results(Page):
    pass


page_sequence = [Instructions, SpinWheelPage, ContributorPage, ResultsWaitPage, Results]
