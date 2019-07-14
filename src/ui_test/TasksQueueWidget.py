import tkinter
from tkinter import Listbox

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

    def init_view(self, person):
        available_tasks_listbox = Listbox(self.top, height=20)
        available_tasks_listbox.bind('<Double-Button>', lambda event: self.on_select(available_tasks_listbox, person))
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
            listbox.insert(tkinter.END, f"{task} {task.get_resources_for_consume()}")

    def create_tasks_list(self, person: Person):
        tasks_listbox = Listbox(self.top, height=20)
        scroll = tkinter.Scrollbar(command=tasks_listbox.yview)
        tasks_listbox.bind('<Double-Button>', lambda event: self.on_task_select(tasks_listbox, person))
        tasks_listbox.config(yscrollcommand=scroll.set)
        self.fill_listbox(person.tasks_schedule, tasks_listbox)
        person.tasks_schedule.listeners.append(lambda: self.fill_listbox(person.tasks_schedule, tasks_listbox))
        tasks_listbox.pack(side="left")
        scroll.pack(side="left", fill=tkinter.Y)
        self.list_boxes.append(tasks_listbox)
        self.list_boxes.append(scroll)

    def on_select(self, listbox, person: Person):
        selection = listbox.curselection()
        if len(selection) > 0:
            person.tasks_schedule.append(person.available_tasks[selection[0]])

    def on_task_select(self, listbox, person):
        selection = listbox.curselection()
        if len(selection) > 0:
            person.tasks_schedule.remove(person.tasks_schedule[selection[0]])
