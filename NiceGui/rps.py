from nicegui import ui

player_1_choice= ""
player_2_choice= ""

def set_player_choice(player, choice):
    if player == 1:
        player_1_choice = choice
    elif player == 2:
        player_2_choice = choice
    else: 
        pass

ui.label("Spelare 1")
with ui.button_group():
    ui.button('sten', on_click=lambda: set_player_choice (1, "sten"))
    ui.button('sax', on_click=lambda: set_player_choice (1, "sax"))
    ui.button('påse', on_click=lambda: set_player_choice (1, "påse"))

ui.label("Spelare 2")
with ui.button_group():
    ui.button('sten', on_click=lambda: set_player_choice (2, "sten"))
    ui.button('sax', on_click=lambda: set_player_choice (2, "sax"))
    ui.button('påse', on_click=lambda: set_player_choice (2, "påse"))


ui.run(native=True)