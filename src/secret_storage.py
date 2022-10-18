# Copyright (C) 2022 Dhanuka Warusadura

import os

def init_directory():
    try:
        os.mkdir('.conf')
        return 0
    except FileExistsError:
        return 1

def init_database():
    pass
