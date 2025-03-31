from otree.api import *
from otree.common import get_constants
from Common_Pool_Resource.config import Config

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Common_Pool_Resource'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10
    TRESHOLD = 900
    NO_OF_FISHES = 100
    BOAT_SIZE = 100

class Subsession(BaseSubsession):
    no_of_fish = models.IntegerField(initial=C.NO_OF_FISHES)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    fishes = models.IntegerField(label="Enter how many fishes you want to fish", min=0, max=C.BOAT_SIZE)

# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['fishes']

    @staticmethod
    def vars_for_template(player: Player):
        
        return  dict(
            fishes= get_fishes(player),
            threshold = C.TRESHOLD, 
            boat_size = C.BOAT_SIZE,
            round_number = player.round_number
            )
    
    @staticmethod
    def is_displayed(player):
        return get_fishes(player) >= 0

def vars_for_admin_report(subsession: Subsession):

    constanst  = get_constants("Common_Pool_Resource")
    list_no_of_fishes = [s.no_of_fish for s in subsession.in_all_rounds() if s.no_of_fish != constanst.NO_OF_FISHES]
    label =  [str(i) for i in range(1, len(list_no_of_fishes)+1)]
    # print(all_)
    return dict(label=label, all_rounds= list_no_of_fishes, threshold = constanst.TRESHOLD)

class ResultsWaitPage(WaitPage):
    template_name = 'cheating_game/ResultsWaitPage.html'
    after_all_players_arrive = 'set_fishes'

    @staticmethod
    def is_displayed(player):
        return get_fishes(player) >= 0


def set_fishes (group: Group):
    got_fish = [p.field_maybe_none('fishes') 
                    if p.field_maybe_none('fishes') else 0 
                    for p in group.get_players()]
    
    # Gettingthe first player as the player for get_fishes
    group.subsession.no_of_fish = get_fishes(group.get_players()[0]) - sum(got_fish)

    if group.subsession.no_of_fish >= C.TRESHOLD:
        group.subsession.no_of_fish *= 2

    print(f"No of fishes: {group.subsession.no_of_fish}")


class Results(Page):
    
    @staticmethod
    def vars_for_template(player):
        return dict(
            fishes = player.group.subsession.no_of_fish ,
            isWin = player.round_number == C.NUM_ROUNDS
        )


def get_fishes(player: Player) -> int:
    fishes = 0

    try:
        fishes = player.in_round(player.round_number-1).group.subsession.no_of_fish 
    except:
        fishes = C.NO_OF_FISHES

    return fishes

class Instructions(Page):
    template_name = 'cheating_game/Instructions.html'

    @staticmethod
    def vars_for_template(player: Player):
        print(get_fishes(player))
        
        return  dict(Config=Config(C.BOAT_SIZE, C.TRESHOLD, get_fishes(player)))

    @staticmethod
    def is_displayed(player):
        return get_fishes(player) >= 0

page_sequence = [Instructions, MyPage, ResultsWaitPage, Results]
