# Copyright (C) 2022 Dhanuka Warusadura

import os
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

GLADE_FILES = {}
handlers = {}

GLADE_FILES['initial_window'] = os.getcwd() + '/gui/initial_window.glade'
GLADE_FILES['guard_window'] = os.getcwd() + '/gui/guard_window.glade'
GLADE_FILES['main_window'] = os.getcwd() + '/gui/main_window.glade'

def initial_window():
    builder = Gtk.Builder()
    builder.add_from_file(GLADE_FILES.get('guard_window'))

    window = builder.get_object('window')
    window.connect('destroy', Gtk.main_quit)
    window.show_all()
    Gtk.main()

def guard_window():
    builder = Gtk.Builder()
    builder.add_from_file(GLADE_FILES.get('guard_window'))

    window = builder.get_object('window')
    window.connect('destroy', Gtk.main_quit)
    window.show_all()
    Gtk.main()

def main_window():
    builder = Gtk.Builder()
    builder.add_from_file(GLADE_FILES.get('main_window'))

    window = builder.get_object('window')
    window.connect('destroy', Gtk.main_quit)
    window.show_all()
    Gtk.main()

def run():
    guard_window()
    main_window()
