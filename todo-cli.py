import todo as core
from typing import List
from tabulate import tabulate

def format_table_todo_list(todoList):
    table = []
    for todo in todoList:
        table.append([todo.key, todo.title, todo.desc, todo.done])
        
    print(tabulate(table, headers=['key', 'title', 'description', 'done?']))

todo_list = core.todo_list()
format_table_todo_list(todo_list)

core.set_done('1')