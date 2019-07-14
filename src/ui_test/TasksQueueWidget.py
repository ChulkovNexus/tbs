import tkinter
from tkinter import Frame, Listbox

from src.models.person.Person import Person
from src.models.tasks import Task

one_person_width = 32
list_width = 400
list_height = 400


class TaskQueueWidget:

    def __init__(self, top):
        self.user_game_model = None
        self.top = top
        self.list_boxes = list()
        self.established_available_tasks_listeners = list()
        self.established_task_queue_listeners = list()
        # self.configure(background='black')

    def show(self, user_game_model):
        if self.user_game_model:
            for person in user_game_model.persons:
                person.available_tasks.remove_listeners(self.established_available_tasks_listeners)
                person.tasks_schedule.remove_listeners(self.established_task_queue_listeners)
        self.established_available_tasks_listeners.clear()
        self.established_task_queue_listeners.clear()
        self.user_game_model = user_game_model
        for view in self.list_boxes:
            view.pack_forget()
        for person in user_game_model.persons:
            self.init_view(person)
        # self.configure(background='black', width=list_width * 2 * len(user_game_model.persons), height=list_height)

    def init_view(self, person):
        available_tasks_listbox = Listbox(self.top)
        available_tasks_listbox.bind('<<ListboxSelect>>', lambda event: self.on_select(event, person))
        scroll = tkinter.Scrollbar(command=available_tasks_listbox.yview)
        available_tasks_listbox.config(yscrollcommand=scroll.set)
        available_tasks_listbox.pack(side="left")
        scroll.pack(side="left", fill=tkinter.Y)
        self.fill_listbox(person.available_tasks, available_tasks_listbox)
        person.available_tasks.listeners.append(lambda: self.fill_listbox(person.available_tasks, available_tasks_listbox))
        self.create_tasks_list(person)
        self.list_boxes.append(available_tasks_listbox)
        self.list_boxes.append(scroll)

    def fill_listbox(self, tasks: Task, listbox):
        listbox.delete(0, tkinter.END)
        for task in tasks:
            listbox.insert(0, f"{task} {task.get_resources_for_consume()}")

    def create_tasks_list(self, person: Person):
        tasks_listbox = Listbox(self.top)
        scroll = tkinter.Scrollbar(command=tasks_listbox.yview)
        tasks_listbox.bind('<<ListboxSelect>>', lambda event: self.on_task_select(event, person))
        tasks_listbox.config(yscrollcommand=scroll.set)
        self.fill_listbox(person.tasks_schedule, tasks_listbox)
        person.tasks_schedule.listeners.append(lambda: self.fill_listbox(person.tasks_schedule, tasks_listbox))
        tasks_listbox.pack(side="left")
        scroll.pack(side="left", fill=tkinter.Y)
        self.list_boxes.append(tasks_listbox)
        self.list_boxes.append(scroll)

    def on_select(self, event, person):
        if self.backpack_listbox.curselection():
            selection_index = self.backpack_listbox.curselection()[0]
            items = self.unit.backpack.items
            self.selected_backpack_item = items[len(items) - selection_index - 1]

    def on_task_select(self, event, person):
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
