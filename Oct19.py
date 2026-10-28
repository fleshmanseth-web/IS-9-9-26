"""Real-time, drag-and-drop tower defense game using only Tkinter.

Run with: python3 Oct19.py
Drag the blue tower from the tray onto the field to start.
"""

import math
import random
import time
import tkinter as tk
from tkinter import ttk


WIDTH = 960
FIELD_HEIGHT = 440
CANVAS_HEIGHT = 510
PLAYER_MAX_HP = 100
ENEMY_MAX_HP = 140


class TowerDefenseGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Last Stand — Tower Defense")
        self.root.configure(bg="#101b27")
        self.root.resizable(False, False)

        self.player_hp = PLAYER_MAX_HP
        self.enemy_hp = ENEMY_MAX_HP
        self.gold = 0
        self.cannon_damage = 12
        self.tower_x = 170
        self.tower_y = 220
        self.tower_placed = False
        self.enemies = []
        self.projectiles = []
        self.effects = []
        self.spawn_timer = 0
        self.enemy_volley_timer = 0
        self.cannon_timer = 0
        self.manual_fire_ready = 0
        self.dragging = None
        self.drag_pos = None
        self.state = "ready"
        self.message = "Drag your tower from the tray onto the battlefield to begin."
        self.last_time = time.monotonic()

        self._build_ui()
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        self.root.bind("<Escape>", lambda _event: self.root.destroy())
        self.draw()
        self.root.after(33, self.game_loop)

    def _build_ui(self):
        header = tk.Frame(self.root, bg="#101b27", padx=20, pady=12)
        header.pack(fill="x")

        tk.Label(
            header, text="LAST STAND", font=("Helvetica", 20, "bold"),
            fg="#f4f7fb", bg="#101b27"
        ).pack(side="left")
        self.stats = tk.Label(
            header, text="", font=("Helvetica", 11, "bold"),
            fg="#b8c7d8", bg="#101b27"
        )
        self.stats.pack(side="right", pady=5)

        self.canvas = tk.Canvas(
            self.root, width=WIDTH, height=CANVAS_HEIGHT,
            bg="#172b35", highlightthickness=0
        )
        self.canvas.pack(padx=18)

        controls = tk.Frame(self.root, bg="#101b27", padx=18, pady=14)
        controls.pack(fill="x")
        style = ttk.Style()
        style.configure("Game.TButton", font=("Helvetica", 11, "bold"), padding=(12, 9))

        self.fire_button = ttk.Button(
            controls, text="Fire at enemy tower", style="Game.TButton",
            command=self.fire_at_enemy_tower
        )
        self.fire_button.pack(side="left", padx=(0, 8))
        self.upgrade_button = ttk.Button(
            controls, text="Upgrade cannon · 20 gold", style="Game.TButton",
            command=self.upgrade_cannon
        )
        self.upgrade_button.pack(side="left", padx=8)
        self.repair_button = ttk.Button(
            controls, text="Repair tower · 15 gold", style="Game.TButton",
            command=self.repair_tower
        )
        self.repair_button.pack(side="left", padx=8)
        ttk.Button(
            controls, text="Restart", style="Game.TButton", command=self.restart
        ).pack(side="right")

        self.status = tk.Label(
            self.root, text=self.message, font=("Helvetica", 10),
            fg="#a9bac9", bg="#101b27", anchor="w", padx=22, pady=0
        )
        self.status.pack(fill="x", pady=(0, 12))

    def on_mouse_down(self, event):
        if self.state in ("victory", "defeat"):
            return
        if not self.tower_placed:
            if 45 <= event.x <= 135 and FIELD_HEIGHT + 10 <= event.y <= CANVAS_HEIGHT - 5:
                self.dragging = "tray"
                self.drag_pos = (event.x, event.y)
            return
        if math.hypot(event.x - self.tower_x, event.y - self.tower_y) <= 38:
            self.dragging = "tower"
            self.drag_pos = (event.x, event.y)

    def on_mouse_drag(self, event):
        if not self.dragging:
            return
        self.drag_pos = (event.x, event.y)
        if self.dragging == "tower" and event.y < FIELD_HEIGHT:
            self.tower_x = min(790, max(55, event.x))
            self.tower_y = min(FIELD_HEIGHT - 52, max(68, event.y))

    def on_mouse_up(self, event):
        if self.dragging == "tray":
            if 25 <= event.x <= 815 and 45 <= event.y < FIELD_HEIGHT - 25:
                self.tower_x = event.x
                self.tower_y = event.y
                self.tower_placed = True
                self.state = "playing"
                self.spawn_timer = 1.0
                self.message = "Tower placed! It will fire automatically at nearby raiders."
            else:
                self.message = "Drop the tower anywhere on the field to start."
        self.dragging = None
        self.drag_pos = None

    def fire_at_enemy_tower(self):
        now = time.monotonic()
        if self.state != "playing":
            self.message = "Place your tower on the field first."
        elif now < self.manual_fire_ready:
            self.message = "Your tower is reloading."
        else:
            self.enemy_hp = max(0, self.enemy_hp - 12)
            self.manual_fire_ready = now + 0.55
            self.effects.append((self.tower_x, self.tower_y, 865, 220, now + 0.16, "#61d9ff"))
            self.message = "Direct hit on the enemy tower!"
            if self.enemy_hp == 0:
                self.finish("victory")

    def upgrade_cannon(self):
        if not self.tower_placed or self.state != "playing":
            self.message = "Place your tower on the field first."
        elif self.gold < 20:
            self.message = "You need 20 gold for a cannon upgrade."
        else:
            self.gold -= 20
            self.cannon_damage += 5
            self.message = f"Cannon upgraded! Each hit now deals {self.cannon_damage} damage."

    def repair_tower(self):
        if not self.tower_placed or self.state != "playing":
            self.message = "Place your tower on the field first."
        elif self.gold < 15:
            self.message = "You need 15 gold to repair your tower."
        elif self.player_hp == PLAYER_MAX_HP:
            self.message = "Your tower is already at full health."
        else:
            self.gold -= 15
            self.player_hp = min(PLAYER_MAX_HP, self.player_hp + 30)
            self.message = "Tower repaired by 30 HP."

    def restart(self):
        self.player_hp = PLAYER_MAX_HP
        self.enemy_hp = ENEMY_MAX_HP
        self.gold = 0
        self.cannon_damage = 12
        self.tower_x = 170
        self.tower_y = 220
        self.tower_placed = False
        self.enemies.clear()
        self.projectiles.clear()
        self.effects.clear()
        self.spawn_timer = 0
        self.enemy_volley_timer = 0
        self.cannon_timer = 0
        self.manual_fire_ready = 0
        self.state = "ready"
        self.message = "Drag your tower from the tray onto the battlefield to begin."

    def finish(self, result):
        self.state = result
        self.message = (
            "Victory! The enemy tower has fallen. Press Restart to play again."
            if result == "victory" else
            "Defeat! Your tower was destroyed. Press Restart to try again."
        )

    def game_loop(self):
        now = time.monotonic()
        dt = min(0.05, now - self.last_time)
        self.last_time = now
        if self.state == "playing":
            self.update_game(dt)
        self.draw()
        self.root.after(33, self.game_loop)

    def update_game(self, dt):
        self.spawn_timer += dt
        self.enemy_volley_timer += dt
        self.cannon_timer += dt

        if self.enemy_hp > 0 and self.spawn_timer >= 2.7:
            self.spawn_timer -= 2.7
            self.enemies.append({
                "x": 820 + random.randint(-12, 10),
                "y": 220 + random.randint(-38, 38),
                "hp": 30,
                "attack_timer": 0,
            })
            self.message = "A raider has left the enemy tower!"

        if self.enemy_hp > 0 and self.enemy_volley_timer >= 5.0:
            self.enemy_volley_timer -= 5.0
            self.player_hp = max(0, self.player_hp - 8)
            self.effects.append((865, 220, self.tower_x, self.tower_y,
                                 time.monotonic() + 0.18, "#ff6d68"))
            self.message = "The enemy tower fired a blast at your tower (-8 HP)."

        if self.cannon_timer >= 0.62 and self.tower_placed:
            targets = [
                enemy for enemy in self.enemies
                if math.hypot(enemy["x"] - self.tower_x, enemy["y"] - self.tower_y) <= 250
            ]
            if targets:
                target = min(
                    targets,
                    key=lambda enemy: math.hypot(enemy["x"] - self.tower_x,
                                                  enemy["y"] - self.tower_y)
                )
                self.projectiles.append({
                    "x": self.tower_x, "y": self.tower_y,
                    "target": target, "speed": 460,
                })
                self.cannon_timer = 0

        for enemy in self.enemies[:]:
            distance = math.hypot(self.tower_x - enemy["x"], self.tower_y - enemy["y"])
            if distance > 34:
                step = min(72 * dt, distance - 34)
                enemy["x"] += (self.tower_x - enemy["x"]) / distance * step
                enemy["y"] += (self.tower_y - enemy["y"]) / distance * step
            else:
                enemy["attack_timer"] += dt
                if enemy["attack_timer"] >= 0.85:
                    enemy["attack_timer"] -= 0.85
                    self.player_hp = max(0, self.player_hp - 10)
                    self.message = "A raider is attacking your tower!"

        for shot in self.projectiles[:]:
            target = shot["target"]
            if target not in self.enemies:
                self.projectiles.remove(shot)
                continue
            dx, dy = target["x"] - shot["x"], target["y"] - shot["y"]
            distance = math.hypot(dx, dy)
            step = shot["speed"] * dt
            if distance <= step + 7:
                target["hp"] -= self.cannon_damage
                self.projectiles.remove(shot)
                if target["hp"] <= 0 and target in self.enemies:
                    self.enemies.remove(target)
                    self.gold += 10
                    self.message = "Raider defeated! +10 gold."
            elif distance:
                shot["x"] += dx / distance * step
                shot["y"] += dy / distance * step

        now = time.monotonic()
        self.effects = [effect for effect in self.effects if effect[4] > now]
        if self.player_hp <= 0:
            self.finish("defeat")

    def draw(self):
        canvas = self.canvas
        canvas.delete("all")
        self.stats.config(
            text=f"YOUR TOWER  {self.player_hp:3d} HP     "
                 f"ENEMY TOWER  {self.enemy_hp:3d} HP     "
                 f"GOLD  {self.gold:02d}     CANNON  {self.cannon_damage} DMG"
        )
        self.status.config(text=self.message)

        # Field background, distant hills, and a winding road.
        canvas.create_rectangle(0, 0, WIDTH, FIELD_HEIGHT, fill="#19343b", outline="")
        canvas.create_oval(-120, 270, 360, 570, fill="#214448", outline="")
        canvas.create_oval(285, 285, 770, 570, fill="#204248", outline="")
        canvas.create_oval(665, 260, 1090, 560, fill="#214448", outline="")
        road = [0, 335, 180, 300, 385, 335, 575, 300, 760, 330, 960, 295]
        canvas.create_line(*road, fill="#33444a", width=54, smooth=True, capstyle="round")
        canvas.create_line(*road, fill="#68716b", width=3, smooth=True, dash=(5, 11))
        for x, y in ((80, 90), (270, 165), (700, 105), (560, 390), (350, 100)):
            canvas.create_oval(x, y, x + 3, y + 3, fill="#66877d", outline="")

        self.draw_enemy_tower(canvas)
        if self.tower_placed:
            self.draw_player_tower(canvas, self.tower_x, self.tower_y)
        elif self.dragging == "tray" and self.drag_pos:
            self.draw_player_tower(canvas, *self.drag_pos, ghost=True)
        else:
            self.draw_tray(canvas)

        for enemy in self.enemies:
            self.draw_raider(canvas, enemy)
        for shot in self.projectiles:
            canvas.create_oval(shot["x"] - 4, shot["y"] - 4,
                               shot["x"] + 4, shot["y"] + 4,
                               fill="#8aeaff", outline="#e4fbff", width=1)
        for x1, y1, x2, y2, expires, color in self.effects:
            if expires > time.monotonic():
                canvas.create_line(x1, y1, x2, y2, fill=color, width=3)

        canvas.create_rectangle(0, FIELD_HEIGHT, WIDTH, CANVAS_HEIGHT,
                                fill="#10232d", outline="")
        canvas.create_line(0, FIELD_HEIGHT, WIDTH, FIELD_HEIGHT, fill="#34505a", width=2)
        canvas.create_text(24, FIELD_HEIGHT + 17, anchor="w",
                           text="TOWER TRAY", fill="#8097a6",
                           font=("Helvetica", 9, "bold"))
        if self.state == "ready":
            canvas.create_text(215, FIELD_HEIGHT + 35, anchor="w",
                               text="Drag the tower token onto the field to start",
                               fill="#c1d3dc", font=("Helvetica", 11))
        elif self.state == "playing":
            canvas.create_text(215, FIELD_HEIGHT + 35, anchor="w",
                               text="Drag your tower to reposition it  ·  Defeat the enemy tower",
                               fill="#a8bdc6", font=("Helvetica", 11))
        else:
            canvas.create_text(215, FIELD_HEIGHT + 35, anchor="w",
                               text=self.message, fill="#d8e5e9",
                               font=("Helvetica", 11, "bold"))

    def draw_enemy_tower(self, canvas):
        x, y = 865, 220
        canvas.create_oval(x - 58, y - 52, x + 58, y + 60,
                           fill="#492f37", outline="#d76c69", width=2)
        canvas.create_rectangle(x - 35, y - 35, x + 35, y + 43,
                                fill="#74404a", outline="#f18b79", width=2)
        canvas.create_polygon(x - 45, y - 34, x - 20, y - 58, x - 7, y - 34,
                             fill="#9d5360", outline="#f18b79", width=2)
        canvas.create_polygon(x + 7, y - 34, x + 22, y - 58, x + 46, y - 34,
                             fill="#9d5360", outline="#f18b79", width=2)
        canvas.create_rectangle(x - 10, y + 5, x + 10, y + 43,
                                fill="#342b35", outline="#f18b79", width=2)
        canvas.create_oval(x - 10, y - 24, x + 10, y - 4,
                           fill="#ffb46d", outline="")
        self.draw_health_bar(canvas, x - 45, y - 75, 90, self.enemy_hp, ENEMY_MAX_HP,
                             "#ef716b")
        canvas.create_text(x, y + 74, text="ENEMY KEEP", fill="#f0bbb2",
                           font=("Helvetica", 9, "bold"))

    def draw_player_tower(self, canvas, x, y, ghost=False):
        alpha = "#4f91aa" if ghost else "#56c9e7"
        canvas.create_oval(x - 48, y - 48, x + 48, y + 48,
                           outline="#4ba5b7", width=2, dash=(4, 4) if ghost else ())
        canvas.create_oval(x - 30, y - 27, x + 30, y + 31,
                           fill="#24647a", outline="#87e5f1", width=2)
        canvas.create_rectangle(x - 21, y - 11, x + 17, y + 17,
                                fill="#65b9cd", outline="#c0f2f2", width=2)
        canvas.create_oval(x - 9, y - 30, x + 9, y - 12,
                           fill="#c8fbf4", outline="#e4ffff", width=1)
        canvas.create_line(x + 8, y - 5, x + 39, y - 17,
                           fill=alpha, width=8, capstyle="round")
        if not ghost:
            self.draw_health_bar(canvas, x - 35, y - 59, 70,
                                 self.player_hp, PLAYER_MAX_HP, "#6ee2b4")
            canvas.create_text(x, y + 42, text="YOUR TOWER", fill="#b8edf0",
                               font=("Helvetica", 8, "bold"))

    def draw_tray(self, canvas):
        canvas.create_oval(55, FIELD_HEIGHT + 8, 135, CANVAS_HEIGHT - 4,
                           fill="#183b48", outline="#58b9cc", width=2)
        canvas.create_rectangle(78, FIELD_HEIGHT + 27, 112, FIELD_HEIGHT + 46,
                                fill="#65b9cd", outline="#c0f2f2", width=2)
        canvas.create_oval(88, FIELD_HEIGHT + 13, 102, FIELD_HEIGHT + 27,
                           fill="#c8fbf4", outline="")
        canvas.create_line(108, FIELD_HEIGHT + 33, 126, FIELD_HEIGHT + 27,
                           fill="#56c9e7", width=7, capstyle="round")

    @staticmethod
    def draw_health_bar(canvas, x, y, width, hp, max_hp, color):
        canvas.create_rectangle(x, y, x + width, y + 7,
                                fill="#0c1820", outline="#82959c", width=1)
        fill_width = max(0, width * hp / max_hp)
        if fill_width:
            canvas.create_rectangle(x + 1, y + 1, x + fill_width, y + 6,
                                    fill=color, outline="")

    def draw_raider(self, canvas, enemy):
        x, y = enemy["x"], enemy["y"]
        canvas.create_oval(x - 17, y - 15, x + 17, y + 17,
                           fill="#a94945", outline="#f38a6e", width=2)
        canvas.create_oval(x - 8, y - 22, x + 8, y - 7,
                           fill="#d66d59", outline="#ffc18a", width=1)
        canvas.create_polygon(x - 12, y - 18, x - 9, y - 29, x - 2, y - 17,
                             fill="#f2bd7b", outline="")
        canvas.create_polygon(x + 2, y - 17, x + 10, y - 29, x + 12, y - 17,
                             fill="#f2bd7b", outline="")
        self.draw_health_bar(canvas, x - 15, y - 34, 30, enemy["hp"], 30, "#f0ad60")


def main():
    root = tk.Tk()
    TowerDefenseGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
