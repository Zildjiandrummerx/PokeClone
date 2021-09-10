from constants import *
from models.battle import *
from models.pokemon import *

# Defining Pokemon with Stats

pokemon1 = Pokemon('Bulbasaur', 100, 'grass', 'poison')
pokemon2 = Pokemon('Charmander', 100, 'fire', None)
pokemon1.current_hp = 45
pokemon2.current_hp = 39

pokemon1.baseStats = {
    HP: 108,
    ATTACK: 130,
    DEFENSE: 95,
    SPATTACK: 80,
    SPDEFENSE: 85,
    SPEED: 102
}

pokemon1.ev = {
    HP: 74,
    ATTACK: 190,
    DEFENSE: 91,
    SPATTACK: 48,
    SPDEFENSE: 84,
    SPEED: 23
}

pokemon1.iv = {
    HP: 24,
    ATTACK: 12,
    DEFENSE: 30,
    SPATTACK: 16,
    SPDEFENSE: 23,
    SPEED: 5
}


pokemon1.compute_stats()
print(pokemon1.stats)


pokemon2.baseStats = {
    HP: 39,
    ATTACK: 52,
    DEFENSE: 43,
    SPATTACK: 80,
    SPDEFENSE: 65,
    SPEED: 65
}

pokemon2.ev = {
    HP: 0,
    ATTACK: 0,
    DEFENSE: 0,
    SPATTACK: 0,
    SPDEFENSE: 0,
    SPEED: 0
}

pokemon2.iv = {
    HP: 21,
    ATTACK: 21,
    DEFENSE: 21,
    SPATTACK: 21,
    SPDEFENSE: 21,
    SPEED: 21
}


# Attacks
pokemon1.attacks = [Attack('tackle', 'normal', PHYSICAL, 35, 40, 100)]
pokemon2.attacks = [Attack('scratch', 'normal', PHYSICAL, 35, 40, 100)]

def ask_command(pokemon):
    command = None
    while not command:
        tmp_command = input(f'What should {pokemon.name} do?').split(' ')
        if len(tmp_command) == 2:
            try:
                if tmp_command[0] == DO_ATTACK and 0 <= int(tmp_command[1]) < 4:
                    command = Command({DO_ATTACK: int(tmp_command[1])})
            except Exception:
                pass
    return command


# Start Battle Loop
battle = Battle(pokemon1, pokemon2)

while not battle.is_finished():

    # Ask for command
    command1 = ask_command(pokemon1)
    command2 = ask_command(pokemon2)

    turn = Turn()
    turn.command1 = command1
    turn.command2 = command2

    if turn.can_start():
        # Execute Turn
        battle.execute_turn(turn)
        battle.print_current_status()