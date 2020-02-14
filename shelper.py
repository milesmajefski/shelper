import yaml
import subprocess
import code

config_file = './src/shelper/config.yaml'
data = None

def load_config():
    global data
    with open(config_file) as f:    
        data = yaml.load(f, Loader=yaml.FullLoader)

def list_commands():
    global data
    for index, command in enumerate(data['commands']):
        print(f'Command {index} is:\n\t{command["description"]}: {command["cmd"]}')


def run(cmd_number):
    # desc = data['commands'][cmd_number]['description']
    cmd = data['commands'][cmd_number]['cmd']
    subprocess.call(cmd, shell=True)
    # import os
    # os.system(cmd)
    print(f'Command {cmd_number} has run.')



load_config()
list_commands()
code.interact(local=locals())

