from src.ui_test import DropDownWidget
from src.ui_test.FieldView import FieldView, tile_size
from src.ui_test.TasksQueueWidget import TaskQueueWidget

if __name__ == "__main__":
    import tkinter

    from src.GameServer import GameServer
    from src.game_mutators import GameInitializer

    game_server = GameServer()
    users = GameInitializer.generate_test_users()
    game = GameInitializer.itit_game(game_server, users)
    game.process_turn()

    top = tkinter.Tk()
    top.title = "tbs"
    top.geometry("1800x800")
    last_selected_user = None

    def on_close():
        top.destroy()
        game.stop()


    def user_selected(user_id):
        widget.set(user_id)
        tasks_widget.show(game.user_game_models[user_id])
        # for user_id, user in game.user_game_models.items():
        #     user.logger.tasks_log_enabled = False

        # game.user_game_models[user_id].logger.tasks_log_enabled = True
        for i, person in enumerate(game.user_game_models[user_id].persons):
            person.log_skill_levels(game.user_game_models[user_id].logger)


    top.protocol("WM_DELETE_WINDOW", on_close)

    c = FieldView(top, game.map.size)
    c.draw_map(game.map)
    c.selected_user_callback = user_selected
    widget = DropDownWidget.addDropDownWidget(top, game, c)
    tasks_widget = TaskQueueWidget(top)
    c.pack(anchor=tkinter.NW)
    top.mainloop()
