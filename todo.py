from typing import List
from tabulate import tabulate



class Todo:
    """Todo class"""
    def __init__(self, key, title, desc, done) -> None:
        self.key = key
        self.title = title
        self.desc = desc
        self.done = done

    def get_key(self):
        return self.key

    def get_title(self):
        return self.title
    
    def get_desc(self):
        return self.desc
    
    def get_done(self):
        return self.done
    
    def set_done(self):
        self.done = True
    
    def set_undone(self):
        self.done = False


todoList: List[Todo] = []
todoList.append(Todo('1', 'test1', 'test desc 1', 'False'))
todoList.append(Todo('2', 'test2', 'test desc 2', 'False'))
todoList.append(Todo('3', 'test3', 'test desc 3', 'True'))
todoList.append(Todo('4', 'test4', 'test desc 4', 'True'))

def todo_list() -> List[Todo]:
    return todoList

def set_done(key) -> None:
    todo = next((x for x in todoList if x.key == key), None)
    todo.set_done()
    print(todo.done)