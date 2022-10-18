# Copyright (C) 2022 Dhanuka Warusadura

# GTK handler code

import gtk_ui

handlers = {}

def get_initial_password(data):
    initial_password = data.get_text()
    window = data.get_window()
    if initial_password:
        window.destroy()
        gtk_ui.main_window()
    else:
        return

def get_guard_field_password(data):
    master_password = data.get_text()
    window = data.get_window()
    if master_password:
        window.destroy()
        gtk_ui.main_window()
    else:
        return

handlers['initial_pwd_button_pressed'] = get_initial_password
handlers['submit_button_pressed'] = get_guard_field_password
