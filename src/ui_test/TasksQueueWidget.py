import tkinter
from tkinter import Frame, Listbox


class TaskQueueWidget(Frame):

    def __init__(self, user_game_model, top, **kw):
        super().__init__(top, width=16, height=10, **kw)
        self.user_game_model = user_game_model
        self.selected_backpack_item = None
        self.selected_task = None
        self.selected_char = None
        self.backpack_listbox = None
        self.tasks_listbox = None
        self.char_list_boxes = list()
        self.item_slots_frame = Frame(self)
        self.char_chooser = None
        self.char_chooser_tkvar = None
        self.move_items_beetwen_backpacks_btn = None

    def init_view(self):
        self.item_slots_frame.pack()
        self.backpack_listbox = Listbox(self, width=16, height=16)
        self.backpack_listbox.pack()
        self.backpack_listbox.bind('<<ListboxSelect>>', self.on_select)
        buttons_frame = Frame(self)
        buttons_frame.pack()
        self.create_tasks_list()

    def create_tasks_list(self):
        label = tkinter.Label(self, text="Unit Tasks")
        label.pack()
        self.tasks_listbox = Listbox(self, width=16, height=16)
        self.tasks_listbox.pack()
        self.tasks_listbox.bind('<<ListboxSelect>>', self.on_task_select)
        buttons_frame = Frame(self)
        buttons_frame.pack()

    def on_select(self, args):
        if self.backpack_listbox.curselection():
            selection_index = self.backpack_listbox.curselection()[0]
            items = self.unit.backpack.items
            self.selected_backpack_item = items[len(items) - selection_index - 1]

    def on_task_select(self, args):
        if self.backpack_listbox.curselection():
            selection_index = self.backpack_listbox.curselection()[0]
            items = self.unit.backpack.items
            self.selected_backpack_item = items[len(items) - selection_index - 1]

    def update_char_slots_view(self):
        def change_dropdown(char):
            self.char_chooser_tkvar.set(char)
            self.selected_char = char

        menu = self.char_chooser['menu']
        menu.delete(0, 'end')
        for char in self.unit.characters:
            menu.add_command(label=char.name, command=change_dropdown(char))
        self.char_chooser_tkvar.set(self.unit.characters[0])

        self.backpack_listbox.delete(0, 'end')
        for item in self.unit.backpack.items:
            self.backpack_listbox.insert(0, item.name)

        self.generate_item_slot_lists_for_each_chars()
        self.update_tasks_list()