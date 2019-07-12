import tkinter


def addDropDownWidget(top, game, field_view):
    choices = list(map(lambda user: '%s' % user.user_id, game.user_game_models))
    tkvar = tkinter.StringVar(top)
    vision_chooser = tkinter.OptionMenu(top, tkvar, *choices)
    tkvar.set(choices[0])

    def change_dropdown(*args):
        user_game_model = [user_game_model for user_game_model in game.user_game_models if user_game_model.user_id == tkvar.get()]
        if user_game_model:
            field_view.user_selected(user_game_model[0].user_id)

    tkvar.trace('w', change_dropdown)
    vision_chooser.place(x=0, y=0)
    return tkvar
