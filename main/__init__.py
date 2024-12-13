from otree.api import *


doc = """
Your app description
"""

def make_field5(label):
    return models.IntegerField(
        choices=[1, 2, 3, 4, 5],
        widget=widgets.RadioSelect,
        label=label,
        blank=False,
    )


class C(BaseConstants):
    NAME_IN_URL = 'main'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    statement1 = make_field5('The quality of customer service')
    statement2 = make_field5('The user-friendliness of the software')
    statement3 = make_field5('The speed of processing your request')
    statement4 = make_field5('The value for money of the product/service')


# PAGES
class MyPage(Page):
    form_model = 'player'
    form_fields = ['statement1', 'statement2', 'statement3', 'statement4']

class Results(Page):
    pass


page_sequence = [MyPage, Results]
