# Dungeon Escape

A terminal adventure for learning Python. Requires Python 3 and no extra packages.

From this folder, run:

```sh
python3 dungeon_escape.py
```

Type `help` to see commands. Start with `take potion`, `north`, and `west`
to explore the armory. Use full item names, such as `take brass key`.

Find the brass key to enter the vault, defeat its guardian, and collect the
silver key to open the exit. A collected sword automatically improves your
attacks. During combat, you can `attack`, `use potion`, or `flee`.
Only attacks and successfully drinking a potion give enemies a turn.
Exploring safe rooms for the first time may trigger a random event.

`save` writes one save slot to `dungeon_save.json` beside the Python file,
replacing the previous save. `load` restores it, including enemy health and
uncollected items. Loading replaces your current progress. There is no autosave;
after losing, run the game again and type `load` to resume a saved game.

## Suggested code walkthrough

1. **`ROOMS` and `ENEMIES`:** Nested dictionaries describe the world. For example,
   `ROOMS["hall"]["exits"]["west"]` gives the string `"armory"`.
2. **`new_game()`:** A separate dictionary tracks everything that changes.
   Item lists are copied so taking an item does not change the starting world.
3. **`look()`, `move()`, and `take_item()`:** Functions read and update the shared
   `state` dictionary. Inventory uses list `append()` and `remove()`.
4. **`random_event()` and `attack()`:** `random.randint()` makes exploration and
   combat unpredictable. `enemy_turn()` keeps enemy attacks in one place.
5. **`save_game()` and `load_game()`:** JSON turns dictionaries and lists into
   readable text and back. Validation rejects malformed saves.
6. **`main()`:** A `while` loop reads a command, calls a function, and repeats
   until you escape, lose all health, or quit.

For a first experiment, change a room description, add a potion to a room's
`items` list, or adjust `MAX_HEALTH`. Start a fresh game after changing the rules.
