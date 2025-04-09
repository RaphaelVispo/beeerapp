from otree.api import *
from otree.common import get_constants
from Public_Good_Game.config import Config
from settings import database


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Public_Good_Game'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    AGENT_ROLE = "Agent"
    PRINCIPAL_ROLE = "Principal"

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    isWin = models.BooleanField()


class Player(BasePlayer):
    contribution = models.IntegerField(label='Enter the amount')
    isWin = models.BooleanField()

def contribution_min(player : Player):
    return 0

def contribution_max(player : Player):
    return player.session.config['endowment']


def get_contributions(subsession : Subsession):
    contributions = [p.field_maybe_none('contribution') 
                        if p.field_maybe_none('contribution') else 0 
                        for p in subsession.get_players()]
    is_Win_Ans = [p.isWin for p in subsession.get_players() if p.field_maybe_none('isWin')==False]
    is_Win = is_Win_Ans[0] if is_Win_Ans else "Not available" 
    total_contribution = sum(contributions)
    return dict(
        total=total_contribution,
        isWin = total_contribution >=  subsession.session.config['cost'] or is_Win 
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
        return dict(probability=player.session.config['probability'])

class ContributorPage(Page):
    form_model = 'player'
    form_fields = ['contribution']

    @staticmethod
    def vars_for_template(player):
        session_config = player.session.config['config']
        game_config = database.game_config.document(session_config).get().to_dict()
        print (game_config)
        return dict(names=game_config)
    
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

        session_config = player.session.config['config']
        game_config = database.game_config.document(session_config).get().to_dict()
        print (game_config)
        # Config(player.session.config['boat_size'], player.session.config['threshold'], get_fishes(player)))

        config = Config(game_config["instruction"]["header"], game_config["instruction"]["steps"])
        config.format_string( player.session.config['probability'],player.session.config['cost'], player.session.config['endowment'])

        return  dict(Config=config)

class ResultsWaitPage(WaitPage):
    template_name = 'cheating_game/ResultsWaitPage.html'

class Results(Page):
    # pass
    after_all_players_arrive = 'set_payoffs'
    
    @staticmethod
    def vars_for_template(player: Player):
        return  get_contributions(player.group)
    
page_sequence = [Instructions, SpinWheelPage, ContributorPage, ResultsWaitPage, Results]
