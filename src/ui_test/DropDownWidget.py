import tkinter


def addDropDownWidget(top, game, field_view):
    choices = list(map(lambda user_id: '%s' % user_id, game.user_game_models))
    tkvar = tkinter.StringVar(top)
    vision_chooser = tkinter.OptionMenu(top, tkvar, *choices)
    tkvar.set(choices[0])

    def change_dropdown(*args):
        user_id = [user_id for user_id in game.user_game_models if str(user_id) == tkvar.get()]
        if user_id:
            field_view.user_selected(user_id[0])

    tkvar.trace('w', change_dropdown)
    vision_chooser.pack(side="top")
    return tkvar
