from constants import *
from models import *

# Defining Pokemon with Stats

pokemon1 = Pokemon('Bulbasaur', 100, 'grass', 'poison')
pokemon2 = Pokemon('Charmander', 100, 'fire', None)

pokemon1.current_hp = 45
pokemon2.current_hp = 39

pokemon1.stats = {
    HP: 45,
    ATTACK: 49,
    DEFENSE: 49,
    SPATTACK: 65,
    SPDEFENSE: 65,
    SPEED: 45
}

pokemon2.stats = {
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPATTACK: 60,
    SPDEFENSE: 50,
    SPEED: 65
}

pokemon1.attacks = [Attack('tackle', 'normal', PHYSICAL, 35, 40, 100)]
pokemon2.attacks = [Attack('scratch', 'normal', PHYSICAL, 35, 40, 100)]