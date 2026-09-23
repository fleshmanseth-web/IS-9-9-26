"""Dungeon Escape: a small terminal game using only Python's standard library."""

import json  # Converts Python dictionaries/lists to text for saving, and back.
import random  # Supplies random numbers for damage and exploration events.
from pathlib import Path  # Builds file paths that work on different operating systems. This allows you to find other files


MAX_HEALTH = 30
# __file__ is this script's location. Keep saves beside it, wherever you launch it.
# All caps for naming the variable signifies it's a constant
# = path means that variable type is now a path
# The Parenthesis take in a string, and __file__ is shorthand for this scripts location
# .with_name Swaps the script's filename with the new name, keeping the parent directory untouched (e.g., /projects/game/main.py → /projects/game/dungeon_save.json).
SAVE_FILE = Path(__file__).with_name("dungeon_save.json")

# The outer dictionary uses room names as keys. Each value describes one room.
ROOMS = {
    "entrance": {
        "description": "The stone door slams shut behind you. Find another exit!",
        "exits": {"north": "hall"},
        "items": ["potion"],
    },
    "hall": {
        "description": "Dusty banners hang above a four-way crossing.",
        "exits": {"south": "entrance", "west": "armory", "east": "library",
                  "north": "crypt"},
        "items": [],
    },
    "dungeon": {
        "description": "Oh boy...what have you gotten yourself into...",
        "exits": {"south": "crypt"},
        "items": {},
    },
    "armory": {
        "description": "A serviceable sword rests among rusted weapons.",
        "exits": {"east": "hall"},
        "items": ["sword", "potion"],
    },
    "library": {
        "description": "A brass key glints between crumbling books.",
        "exits": {"west": "hall", "north": "laboratory"},
        "items": ["brass key"],
    },
    "laboratory": {
        "description": "Bubbling bottles illuminate a narrow passage north.",
        "exits": {"south": "library", "north": "vault", "north": "dungeon"},
        "items": ["potion", "potion"],
    },
    "crypt": {
        "description": "Something stirs among the old stone coffins.",
        "exits": {"south": "hall", "east": "vault"},
        "items": ["potion"],
    },
    "vault": {
        "description": "A guardian stands between you and a silver key.",
        "exits": {"west": "crypt", "south": "laboratory", "north": "exit"},
        "items": ["silver key"],
    },
    "exit": {
        "description": "Sunlight spills through the gate. You escaped!",
        "exits": {"south": "vault"},
        "items": [],
    },
}

# Damage lists hold [minimum damage, maximum damage], including both endpoints.
ENEMIES = {
    "crypt": {"name": "skeleton", "health": 12, "damage": [2, 4]},
    "vault": {"name": "guardian", "health": 18, "damage": [3, 5]},
    "dungeon": {"name": "troll", "health": 40, "damage": [1, 10]}
}

# Triple quotes allows you to make multi-line strings, preserving formatting, syntax, and allowing for single and double quotes to be freely used
HELP = """
Commands:
  go north         Move north, south, east, or west (or just type north).
  look             Describe your room again.
  take brass key   Pick up a visible item; use its full name.
  inventory        Show your items and health.
  attack           Fight the enemy in this room.
  use potion       Restore up to 12 health. Enemies get a turn afterward!
  flee             Retreat to the previous room without taking damage.
  map              Show the exits of rooms you have visited.
  save / load      Save or restore your progress (one save slot).
  help / quit      Show commands or leave the game.

Find the brass key to enter the vault, then the silver key to open the exit.
A sword improves your attacks automatically. Keys are kept after use.
Enemies block movement and item collection until defeated or you flee.
Saving replaces the previous save. Quitting does not automatically save.
"""
#This is where I stopped learning, I'll be back though

def new_game():
    """Create fresh, mutable game data separately from the room descriptions."""
    # This triple quoted line at the start of a function is called a docstring, and is stored for runtime. It can be accessed during runtime by typing help(new_game)
    # This dictionary is our entire game state. Functions receive it as `state`.
    # Changing state["health"], for example, updates the same dictionary main uses.
    return {
        # The brackets create a new dictionary, and the return function immediately hands it back to the code that called for it and prevents any other code from running in the defined function
        # A version number lets us recognize the format of a saved game.
        "version": 1,
        "room": "entrance",
        "previous_room": None,
        "health": MAX_HEALTH,
        "inventory": [],  # A list can contain duplicates, such as two potions.
        "visited": ["entrance"],  # Remember visits so events happen only once.
        # A dictionary comprehension builds one entry per room.
        # .copy() gives each game its own item lists instead of modifying ROOMS.
        "room_items": {name: room["items"].copy() for name, room in ROOMS.items()},
        # Store changing health separately from each enemy's starting statistics.
        "enemy_health": {room: enemy["health"] for room, enemy in ENEMIES.items()},
    }


def current_enemy(state):
    """Return a living enemy's description, or None if the room is safe."""
    room = state["room"]
    # .get(key, default) returns 0 for rooms that do not have an enemy.
    if state["enemy_health"].get(room, 0) > 0:
        return ENEMIES[room]
    return None


def look(state):
    room = state["room"]
    # f-strings insert the values inside {...}; \n starts a new line.
    print(f"\n--- {room.title()} ---")
    print(ROOMS[room]["description"])
    # Joining a dictionary uses its keys: north, south, east, or west here.
    print("Exits: " + ", ".join(ROOMS[room]["exits"]))
    items = state["room_items"][room]
    print("Items: " + (", ".join(items) if items else "none"))
    enemy = current_enemy(state)
    if enemy:  # None counts as false; an enemy dictionary counts as true.
        print(f"A {enemy['name']} blocks your way! "
              f"Enemy health: {state['enemy_health'][room]}")
    print(f"Your health: {state['health']}/{MAX_HEALTH}")


def random_event(state):
    """Roll once when first entering a safe room, so revisiting cannot farm loot."""
    roll = random.randint(1, 6)
    # Each number has equal probability: 1/6 trap, 1/6 potion, 4/6 neither.
    if roll == 1:
        damage = random.randint(1, 3)
        state["health"] = max(0, state["health"] - damage)  # Never go below zero.
        print(f"A hidden dart hits you for {damage} damage!")
    elif roll == 2:
        state["room_items"][state["room"]].append("potion")
        print("You spot an extra potion tucked into a crack in the wall!")
    else:
        print("You hear distant footsteps, but nothing approaches.")


def move(state, direction):
    # Early returns stop the function before it can perform an invalid move.
    if current_enemy(state):
        print("An enemy blocks your way. Attack, use a potion, or flee.")
        return
    # First find the current room, then its exits, then the requested direction.
    # Without a supplied default, .get() returns None when the direction is absent.
    destination = ROOMS[state["room"]]["exits"].get(direction)
    if destination is None:
        print("There is no exit in that direction.")
        return
    # Only these two destinations are locked. Other rooms need no key.
    required_key = {"vault": "brass key", "exit": "silver key"}.get(destination)
    if required_key and required_key not in state["inventory"]:
        print(f"The door is locked. You need the {required_key}.")
        return
    # Remember where we came from before replacing the current location.
    state["previous_room"] = state["room"]
    state["room"] = destination
    if destination not in state["visited"]:
        state["visited"].append(destination)
        # Enemy rooms already have a challenge; the exit immediately wins.
        if destination != "exit" and not current_enemy(state):
            random_event(state)
    look(state)


def take_item(state, item):
    if current_enemy(state):
        print("Defeat the enemy before collecting items.")
    elif item in state["room_items"][state["room"]]:
        # Transfer ONE item: remove it from the floor and add it to inventory.
        # Removing one potion leaves any other potions in the room untouched.
        state["room_items"][state["room"]].remove(item)
        state["inventory"].append(item)
        print(f"You picked up: {item}.")
    else:
        print("That item is not here. Try 'look' to see available items.")


def enemy_turn(state):
    enemy = current_enemy(state)
    if enemy:
        # * unpacks [2, 4], for example, into randint(2, 4).
        damage = random.randint(*enemy["damage"])
        state["health"] = max(0, state["health"] - damage)
        print(f"The {enemy['name']} hits you for {damage}. "
              f"Your health: {state['health']}/{MAX_HEALTH}")


def attack(state):
    enemy = current_enemy(state)
    if not enemy:
        print("There is nothing here to fight.")
        return
    # This conditional expression chooses stronger damage if you have a sword.
    damage = random.randint(6, 10) if "sword" in state["inventory"] else random.randint(2, 5)
    room = state["room"]
    state["enemy_health"][room] = max(0, state["enemy_health"][room] - damage)
    print(f"You hit the {enemy['name']} for {damage} damage.")
    # A defeated enemy cannot retaliate. A surviving enemy gets one attack.
    if state["enemy_health"][room] == 0:
        print(f"The {enemy['name']} is defeated! You can collect items now.")
    else:
        print(f"Enemy health: {state['enemy_health'][room]}")
        enemy_turn(state)


def use_potion(state):
    if "potion" not in state["inventory"]:
        print("You do not have a potion.")
    elif state["health"] == MAX_HEALTH:
        print("You are already at full health. Keep that potion for later.")
    else:
        # min() caps healing at the amount missing from full health.
        healed = min(12, MAX_HEALTH - state["health"])
        state["inventory"].remove("potion")
        state["health"] += healed
        print(f"You recover {healed} health. Health: {state['health']}/{MAX_HEALTH}")
        enemy_turn(state)  # Drinking during a fight spends your turn.


def flee(state):
    if not current_enemy(state) or state["previous_room"] is None:
        print("There is no fight to flee from.")
        return
    # Python evaluates the right-hand side first, so we can swap two values.
    state["room"], state["previous_room"] = state["previous_room"], state["room"]
    print("You retreat safely. The enemy keeps its remaining health.")
    look(state)


def validate_save(data):
    """Check JSON before trusting it as game state. Raise ValueError if invalid."""
    # These small helper functions are nested: only validate_save needs them.
    def require(condition):
        if not condition:
            raise ValueError("The save file has invalid or unsupported game data.")

    def room_name(value):
        return isinstance(value, str) and value in ROOMS

    def item_list(value):
        allowed = ("potion", "sword", "brass key", "silver key")
        return isinstance(value, list) and all(isinstance(x, str) and x in allowed for x in value)

    # `and` short-circuits: the second check runs only if the first one passes.
    # Check the container type before looking up its contents to avoid crashes.
    require(isinstance(data, dict) and data.keys() == new_game().keys())
    require(type(data["version"]) is int and data["version"] == 1)
    require(room_name(data["room"]))
    require(data["previous_room"] is None or room_name(data["previous_room"]))
    # Exact int checks reject JSON true/false, which Python otherwise treats as ints.
    require(type(data["health"]) is int and 0 <= data["health"] <= MAX_HEALTH)
    require(item_list(data["inventory"]))
    require(isinstance(data["visited"], list) and all(room_name(x) for x in data["visited"]))
    require(data["room"] in data["visited"])
    require(isinstance(data["room_items"], dict) and data["room_items"].keys() == ROOMS.keys())
    # all() is true only when EVERY entry passes the check.
    require(all(item_list(items) for items in data["room_items"].values()))
    require(isinstance(data["enemy_health"], dict) and data["enemy_health"].keys() == ENEMIES.keys())
    for room, health in data["enemy_health"].items():
        require(type(health) is int and 0 <= health <= ENEMIES[room]["health"])
    if current_enemy(data):
        # A saved fight needs a neighboring retreat room so flee still works.
        require(data["previous_room"] in ROOMS[data["room"]]["exits"].values())


def save_game(state, path=SAVE_FILE):
    # Write a temporary file first to avoid partially replacing an existing save.
    path = Path(path)
    temporary = path.with_suffix(".tmp")
    try:
        # indent=2 makes the JSON readable if you open the save in a text editor.
        temporary.write_text(json.dumps(state, indent=2), encoding="utf-8")
        temporary.replace(path)
        print(f"Game saved to {path.name}.")
    except OSError as error:
        # Catch file errors (such as a read-only folder) instead of crashing.
        print(f"Could not save the game: {error}")


def load_game(path=SAVE_FILE):
    try:
        # read_text reads the file; json.loads converts that text into Python data.
        data = json.loads(Path(path).read_text(encoding="utf-8"))
        validate_save(data)
        print("Game loaded.")
        return data
    except (OSError, ValueError, RecursionError) as error:
        # Missing files and damaged JSON leave the current game unchanged.
        print(f"Could not load the game: {error}")
        return None


def main():
    state = new_game()
    print("DUNGEON ESCAPE")
    print(HELP)
    look(state)

    # Each loop iteration handles one command. Both conditions must remain true.
    while state["health"] > 0 and state["room"] != "exit":
        try:
            # Normalize input: "  TAKE   Potion " becomes "take potion".
            command = " ".join(input("\n> ").lower().split())
        except (EOFError, KeyboardInterrupt):
            # Exit neatly if input closes or the player presses Ctrl+C.
            print("\nGoodbye! Any previous save is still available.")
            return

        # This if/elif chain dispatches each command to the function that handles it.
        # Only the first matching branch runs.
        if command == "quit":
            print("Goodbye! Any previous save is still available.")
            return
        elif command in ("north", "south", "east", "west"):
            move(state, command)
        elif command.startswith("go "):
            # A string slice skips the first three characters: "go ".
            move(state, command[3:])
        elif command == "look":
            look(state)
        elif command.startswith("take "):
            # Everything after "take " is the item name, including any spaces.
            take_item(state, command[5:])
        elif command == "inventory":
            print("Inventory: " + (", ".join(state["inventory"]) or "empty"))
            print(f"Health: {state['health']}/{MAX_HEALTH}")
        elif command == "attack":
            attack(state)
        elif command == "use potion":
            use_potion(state)
        elif command == "flee":
            flee(state)
        elif command == "map":
            # .items() provides each direction and its destination as a pair.
            for name in state["visited"]:
                exits = ", ".join(f"{direction}: {room}" for direction, room in ROOMS[name]["exits"].items())
                marker = " <-- you" if name == state["room"] else ""
                print(f"{name}{marker} | {exits}")
        elif command == "save":
            save_game(state)
        elif command == "load":
            loaded = load_game()
            if loaded is not None:
                # Replace state only after loading AND validation succeed.
                state = loaded
                look(state)
        elif command == "help":
            print(HELP)
        else:
            print("Unknown command. Type 'help' to see your options.")

    # Reaching here means the loop ended through death or escape, not quit.
    if state["health"] <= 0:
        print("\nYour health reaches zero. Game over! Run again to start fresh or load a save.")
    else:
        print("\nYou win! You found both keys and survived the dungeon.")


# Importing this file lets us test functions without starting the input loop.
if __name__ == "__main__":
    main()
