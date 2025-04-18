from os import environ
from database import *

database = Database()

SESSION_CONFIGS = [
    dict(
        name='Cheating_Game' , 
        app_sequence=['cheating_game', 'payment_info'], 
        num_demo_participants=2,
        number_rounds=3,
        config = "c706227c-9934-4c43-aaa9-424d3057b9c3",
    ),
    dict(
        name='Public_Good_Game' , 
        app_sequence=['Public_Good_Game', 'payment_info'], 
        num_demo_participants=2,
        endowment=233,
        cost = 1000,
        probability = 99/100,
        config = "451692e8-ee33-40a7-88ed-0d2e41748371"
    ),
    dict(
        name='Common_Pool_Resource' , 
        app_sequence=['Common_Pool_Resource', 'payment_info'], 
        num_demo_participants=2,
        threshold = 900, 
        no_of_fishes = 1000,
        boat_size = 500,
        config = "c142d277-57ef-4e3f-b15f-1445efb4d025"
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '4651612482868'

INSTALLED_APPS = ['otree']
