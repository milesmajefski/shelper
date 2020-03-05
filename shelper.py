import os
# import sys
import yaml
import subprocess
import code
import time
import datetime

# original_stdout = sys.stdout

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
        # print(f'{index}  {command["description"]}  {command["lines"]}')
        print(f' {index}  {command["description"]}')

        print()
    # print('\nGoing into interactive mode.\n-------------------------------\n')
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

# def redirect_to_file():
#     global original_stdout
#     timestr = time.strftime("%Y-%m-%d_%H-%M-%S")
#     filename = f'shelper_{timestr}.log'
#     print(filename)
    
#     sys.stdout = open(filename, 'w')

# def cancel_redirect():
#     global original_stdout
#     sys.stdout = original_stdout

if __name__ == '__main__':
    load_config()
    list_commands()
    code.interact(banner='', local=locals())
else:
    load_config()
    list_commands()

