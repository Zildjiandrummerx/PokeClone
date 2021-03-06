
# Pokemon Stats
HP = 'HP'
ATTACK = 'Attack'
DEFENSE = 'Defense'
SPATTACK = 'SpAttack'
SPDEFENSE = 'SpDefense'
SPEED = 'Speed'

# Attack Categories
PHYSICAL = 'physical'
SPECIAL = 'special'

NATURE_MATRIX = [
    {HP: 1, ATTACK: 1.1, DEFENSE: 1, SPATTACK: 0.9, SPDEFENSE: 1, SPEED: 1},    # ADAMANT
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1},        # BASHFUL
    {HP: 1, ATTACK: 0.9, DEFENSE: 1.1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1},    # BOLD
    {HP: 1, ATTACK: 1.1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 0.9},    # BRAVE
    {HP: 1, ATTACK: 0.9, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1.1, SPEED: 1},    # CALM
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 0.9, SPDEFENSE: 1.1, SPEED: 1},    # CAREFUL
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1},        # DOCILE
    {HP: 1, ATTACK: 1, DEFENSE: 0.9, SPATTACK: 1, SPDEFENSE: 1.1, SPEED: 1},    # GENTLE
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1},        # HARDY
    {HP: 1, ATTACK: 1, DEFENSE: 0.9, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1.1},    # HASTY
    {HP: 1, ATTACK: 1, DEFENSE: 1.1, SPATTACK: 0.9, SPDEFENSE: 1, SPEED: 1},    # IMPISH
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 0.9, SPDEFENSE: 1, SPEED: 1.1},    # JOLLY
    {HP: 1, ATTACK: 1, DEFENSE: 1.1, SPATTACK: 1, SPDEFENSE: 0.9, SPEED: 1},    # LAX
    {HP: 1, ATTACK: 1.1, DEFENSE: 0.9, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1},    # LONELY
    {HP: 1, ATTACK: 1, DEFENSE: 0.9, SPATTACK: 1.1, SPDEFENSE: 1, SPEED: 1},    # MILD
    {HP: 1, ATTACK: 0.9, DEFENSE: 1, SPATTACK: 1.1, SPDEFENSE: 1, SPEED: 1},    # MODEST
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 0.9, SPEED: 1.1},    # NAIVE
    {HP: 1, ATTACK: 1.1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 0.9, SPEED: 1},    # NAUGHTY
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1.1, SPDEFENSE: 1, SPEED: 0.9},    # QUIET
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1},        # QUIRKY
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1.1, SPDEFENSE: 0.9, SPEED: 1},    # RASH
    {HP: 1, ATTACK: 1, DEFENSE: 1.1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 0.9},    # RELAXED
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1.1, SPEED: 0.9},    # SASSY
    {HP: 1, ATTACK: 1, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1},        # SERIOUS
    {HP: 1, ATTACK: 0.9, DEFENSE: 1, SPATTACK: 1, SPDEFENSE: 1, SPEED: 1.1}     # TIMID
]

# Commands
DO_ATTACK = 'attack'
DO_ATTACK_SELECTION = 'selected_attack'