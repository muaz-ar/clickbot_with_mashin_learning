from login import login
from clicks_loop_save import click_save_loop
from datebase.create_db import create_db_and_tables

create_db_and_tables()
login()
click_save_loop()

