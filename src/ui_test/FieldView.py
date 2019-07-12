from tkinter import Canvas
import time
import tkinter as tk

from src.models.map.MapTile import MapTile

tile_size = 60
click_range = 0.3


class FieldView(Canvas):

    def __init__(self, top, size):
        super().__init__(top, width=size * tile_size, height=size * tile_size, scrollregion=(0, 0, size * tile_size, size * tile_size))
        self.selected_town_id = -1
        self.hbar = tk.Scrollbar(self, orient="horizontal", command=self.xview)
        self.drag_start_x = 0
        self.drag_start_y = 0
        self.map = None
        self.updatable_map_objects = list()
        self.selected_user_callback = None
        self.start_click_timestamp = 0
        self.hbar.pack(side="bottom", fill='x')
        self.vbar = tk.Scrollbar(self, orient="vertical", command=self.yview)
        self.vbar.pack(side="right", fill='y')
        self.config(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set, yscrollincrement='2', xscrollincrement='2')
        self.pack(side='left', expand=True, fill='both')
        self.size = size
        self.bind("<Button-1>", self.drag_start)
        self.bind("<ButtonRelease-1>", self.button_released)

    def drag_start(self, event):
        self.start_click_timestamp = time.time()
        self.drag_start_x = event.x
        self.drag_start_y = event.y

    def button_released(self, event):
        if time.time() - self.start_click_timestamp < click_range:
            self.click_performed(event.x, event.y)

    def click_performed(self, x, y):
        if self.map:
            map_x = int(self.canvasx(x) / tile_size)
            map_y = int(self.canvasy(y) / tile_size)
            town = self.map.map[map_y][map_x].userIdTown
            if town != -1 and self.selected_user_callback:
                self.selected_user_callback(town)
                self.user_selected(town)

    def draw_unit_selector(self, x, y):
        selection = self.create_rectangle(x * tile_size, y * tile_size, (x + 1) * tile_size, (y + 1) * tile_size, width=1.5, outline='#00ff00')
        self.updatable_map_objects.append(selection)

    def draw_map(self, map):
        self.delete("all")
        self.map = map
        self.update_map_objects()

    def update_map_objects(self):
        for obj in self.updatable_map_objects:
            self.delete(obj)
        self.updatable_map_objects.clear()
        for y, row in enumerate(self.map.map):
            for x, tile in enumerate(row):
                self.draw_tile_bg(tile)

    def draw_tile_bg(self, tile: MapTile):
        x = tile.pos_x
        y = tile.pos_y
        rectangle = self.create_rectangle(x * tile_size, y * tile_size, (x + 1) * tile_size, (y + 1) * tile_size, width=0.5, fill="white")
        self.tag_lower(rectangle)

        if tile.warUserId == self.selected_town_id:
            war_influence = self.create_text((x * tile_size) + (tile_size / 2), (y * tile_size) + (tile_size / 2), fill="red", font="Times 6", text=str(tile.warInfluence))
            self.updatable_map_objects.append(war_influence)
        if tile.religionUserId == self.selected_town_id:
            religion_influence = self.create_text((x * tile_size) + (tile_size / 2), (y * tile_size) + (tile_size / 2), fill="blue", font="Times 6", text=str(tile.religionInfluence))
            self.updatable_map_objects.append(religion_influence)
        if tile.economicDominationUserId == self.selected_town_id:
            economic_influence = self.create_text((x * tile_size) + (tile_size / 2), (y * tile_size) + (tile_size / 2), fill="yellow", font="Times 6", text=str(tile.economicInfluence))
            self.updatable_map_objects.append(economic_influence)

    def user_selected(self, town):
        self.selected_town_id = town
        for y, row in enumerate(self.map.map):
            for x, tile in enumerate(row):
                if tile.userIdTown == town:
                    self.draw_unit_selector(x, y)
                    self.draw_map(self.map)
