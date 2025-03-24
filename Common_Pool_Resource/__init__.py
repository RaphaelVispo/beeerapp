from otree.api import *
from Common_Pool_Resource.config import Config

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Common_Pool_Resource'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10
    TRESHOLD = 200
    NO_OF_FISHES = 1000
    BOAT_SIZE = 100

class Subsession(BaseSubsession):
    pass


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
            fishes=C.NO_OF_FISHES,
            threshold = C.TRESHOLD, 
            boat_size = C.BOAT_SIZE,
            round_number = player.round_number
            )

class ResultsWaitPage(WaitPage):
    template_name = 'cheating_game/ResultsWaitPage.html'

class Results(Page):
    pass

class Instructions(Page):
    template_name = 'cheating_game/Instructions.html'

    @staticmethod
    def vars_for_template(player: Player):
        
        return  dict(Config=Config(C.BOAT_SIZE, C.TRESHOLD, C.NO_OF_FISHES))


page_sequence = [Instructions, MyPage, ResultsWaitPage, Results]
