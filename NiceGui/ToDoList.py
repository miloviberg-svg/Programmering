from nicegui import ui

to_do_list = []

def add_task():
    text = task_input.value
    to_do_list.append(text)

    ass_label = ui.label(text + "\n")

    ui.notify('added to to-do list')

task_input = ui.input(label='Add to to do list', placeholder='start typing',
         validation={'Input too long': lambda value: len(value) < 20})

ui.button('add', on_click=lambda: add_task())

def remove_task():
    text_2 = task_input_1.value
    to_do_list.pop(text_2)

    ass_label = ui.label.remove(text_2)

    ui.notify('removed from to do list')

task_input_1 = ui.input(label='remove from to do list', placeholder='start typing',
         validation={'Input too long': lambda value: len(value) < 20})

ui.button('remove', on_click=lambda: remove_task())

ui.run()