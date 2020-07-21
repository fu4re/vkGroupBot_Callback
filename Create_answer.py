import vkMethods
import os
import importlib

from CommandManager import commandList

def load_commands():
    files = os.listdir('mysite/Commands')
    modules = filter(lambda x: x.endswith('.py'), files)
    for module in modules:
        importlib.import_module('Commands.' + module[0:-3])

def get_answer(body):
    message = 'Я учусь тебя понимать. Продолжай'
    attachment = ''
    for command in commandList:
        if body in command.keys:
            message, attachment = command.process()
    return message, attachment

def create_answer(data):
   load_commands()
   user_id = data['user_id']
   message, attachment = get_answer(data['body'].lower())
   vkMethods.sendMessage(user_id, message, attachment)