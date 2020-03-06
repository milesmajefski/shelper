import os
import yaml
import subprocess
import code
import time
import datetime


script_location = os.path.split(__file__)[0]
config_file = os.path.join(script_location, 'config.yaml')
data = None

def load_config():
    global data
    with open(config_file) as f:    
        data = yaml.load(f, Loader=yaml.FullLoader)

def _clear():
    """OS specific command for clearing console"""
    os.system('cls')

def list_commands():
    global data
    _clear()
    print(' c:\n-----------------------')
    for index, command in enumerate(data['commands']):
        print(f' {index}  {command["description"]}')
        print()

    print('Usage:\trun(c)\tclear()')

def run(cmd_number):
    lines = data['commands'][cmd_number]['lines']
    desc = data['commands'][cmd_number]['description']
    for line in lines:
        subprocess.call(line, shell=True)

    print(f'Command #{cmd_number} {desc} has run.')
    

def clear():
    """For user, clears UI and lists commands"""
    _clear()
    list_commands()


if __name__ == '__main__':
    load_config()
    list_commands()
    code.interact(banner='', local=locals())
else:
    load_config()
    list_commands()

