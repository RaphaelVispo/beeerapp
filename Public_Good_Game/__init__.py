from otree.api import *
from otree.common import get_constants
from Public_Good_Game.config import Config


doc = """
Your app description
"""
class C(BaseConstants):
    NAME_IN_URL = 'Public_Good_Game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    ENDOWMENT = 1000
    COST = 1000
    PROBABILITY = 99/100
    AGENT_ROLE = "Agent"
    PRINCIPAL_ROLE = "Principal"

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    isWin = models.BooleanField()


class Player(BasePlayer):
    contribution = models.IntegerField(label='Enter the amount', min=0, max=C.ENDOWMENT)
    isWin = models.BooleanField()



def get_contributions(subsession : Subsession):
    contributions = [p.field_maybe_none('contribution') 
                        if p.field_maybe_none('contribution') else 0 
                        for p in subsession.get_players()]
    is_Win_Ans = [p.isWin for p in subsession.get_players() if p.field_maybe_none('isWin')==False]
    is_Win = is_Win_Ans[0] if is_Win_Ans else "Not available" 
    total_contribution = sum(contributions)
    return dict(
        total=total_contribution,
        isWin = total_contribution >=  get_constants("Public_Good_Game").COST or is_Win 
    )

def vars_for_admin_report(subsession):
    return get_contributions(subsession)

# PAGES
class SpinWheelPage(Page):
    form_model = 'player'
    form_fields = ['isWin']
    # pass
    @staticmethod
    def is_displayed(player):
        return player.role == C.AGENT_ROLE
    
    @staticmethod
    def vars_for_template (player):
        return dict(probability=C.PROBABILITY)

class ContributorPage(Page):
    form_model = 'player'
    form_fields = ['contribution']

    @staticmethod
    def is_displayed(player):
        return player.role != C.AGENT_ROLE


def set_payoffs(group):
    principal = group.get_player_by_role(C.AGENT_ROLE)
    group.isWin = principal.isWin
    return get_contributions(group)

class Instructions(Page):
    template_name = 'cheating_game/Instructions.html'

    @staticmethod
    def vars_for_template(player: Player):
        
        return  dict(Config=Config)

class ResultsWaitPage(WaitPage):
    template_name = 'cheating_game/ResultsWaitPage.html'

class Results(Page):
    # pass
    after_all_players_arrive = 'set_payoffs'
    
    @staticmethod
    def vars_for_template(player: Player):
        return  get_contributions(player.group)
    
page_sequence = [Instructions, SpinWheelPage, ContributorPage, ResultsWaitPage, Results]
