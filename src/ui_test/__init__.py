from src.ui_test import DropDownWidget
from src.ui_test.FieldView import FieldView

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
    top.geometry("1000x800")

    def on_close():
        top.destroy()
        game.stop()

    def user_selected(user_id):
        widget.set(user_id)

    top.protocol("WM_DELETE_WINDOW", on_close)

    c = FieldView(top, len(game.map.size))
    c.draw_map(game.map)
    c.selected_user_callback = user_selected
    c.place(x=100, y=0, relwidth=1, relheight=1)
    widget = DropDownWidget.addDropDownWidget(top, game, c)
    top.mainloop()
