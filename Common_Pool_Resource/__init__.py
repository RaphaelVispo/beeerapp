from otree.api import *
from otree.common import get_constants
from Common_Pool_Resource.config import Config
from database import *
from settings import database

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Common_Pool_Resource'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10


def creating_session(subsession: BaseSubsession):
    if subsession.round_number == 1:
        subsession.no_of_fish = subsession.session.config['no_of_fishes']
    else:
        subsession.no_of_fish = subsession.in_round(subsession.round_number-1).no_of_fish 
class Subsession(BaseSubsession):
    no_of_fish = models.IntegerField() 
class Group(BaseGroup):
    pass


class Player(BasePlayer):
    fishes = models.IntegerField(label="Enter how many fish you want to fish")

def fishes_min(player : Player):
    return 0

def fishes_max(player : Player):
    return player.session.config['boat_size']

# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['fishes']


    @staticmethod
    def vars_for_template(player: Player):
        session_config = player.session.config['config']
        game_config = database.game_config.document(session_config).get().to_dict()

        return  dict(
            names=game_config,
            fishes= get_fishes(player),
            threshold = player.session.config["threshold"], 
            boat_size = player.session.config["boat_size"],
            round_number = player.round_number
            )
    
    @staticmethod
    def is_displayed(player):
        return  get_fishes(player) > 0

def vars_for_admin_report(subsession: Subsession):

    constant  = subsession.session.config

    list_no_of_fishes = [s.no_of_fish for s in subsession.in_all_rounds()]
    label =  [str(num+1) for num in range(subsession.round_number)]
    # print(all_)
    return dict(label=label, all_rounds= list_no_of_fishes, threshold = constant["threshold"])

class ResultsWaitPage(WaitPage):
    template_name = 'cheating_game/ResultsWaitPage.html'
    after_all_players_arrive = 'set_fishes'

    @staticmethod
    def is_displayed(player):
        return  get_fishes(player) > 0


def set_fishes (group: Group):        

    got_fish = [p.field_maybe_none('fishes') 
                    if p.field_maybe_none('fishes') else 0 
                    for p in group.get_players()]
    
    # Gettingthe first player as the player for get_fishes
    group.subsession.no_of_fish = get_fishes(group.get_players()[0]) - sum(got_fish)

    if group.subsession.no_of_fish >= group.session.config["threshold"]:
        group.subsession.no_of_fish *= 2

    print(f"No of fishes: {group.subsession.no_of_fish}")


class Results(Page):
    
    @staticmethod
    def vars_for_template(player):
        return dict(
            fishes = get_fishes(player) ,
            isWin = player.round_number == C.NUM_ROUNDS
        )
    
    @staticmethod
    def is_displayed(player):
        return ((get_fishes(player) > 0 and player.subsession.round_number == C.NUM_ROUNDS) # if Win 
                or  get_fishes(player) <= 0 )                           # if Lose 


def get_fishes(player: Player) -> int:
    fishes = 0

    try:
        fishes = player.in_round(player.round_number-1).group.subsession.no_of_fish 
    except:
        fishes = player.session.config['no_of_fishes']

    print(fishes)

    return fishes

class Instructions(Page):
    template_name = 'cheating_game/Instructions.html'

    @staticmethod
    def vars_for_template(player: Player):

        session_config = player.session.config['config']
        game_config = database.game_config.document(session_config).get().to_dict()
        print (game_config)
        # Config(player.session.config['boat_size'], player.session.config['threshold'], get_fishes(player)))

        config = Config(game_config["instruction"]["header"], game_config["instruction"]["steps"])
        config.format_string(player.session.config['boat_size'], player.session.config['threshold'], get_fishes(player))
        return  dict(Config=config)

    @staticmethod
    def is_displayed(player):
        return get_fishes(player) > 0

page_sequence = [Instructions, MyPage, ResultsWaitPage, Results]
