# Exercício - Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

from os import system

def line():
    print(35* '-')
    
list = []
line()

def task_or_command(): #ask the user to type a command or a task
    print('Commands: list, undo, remake, clear')
    print('Type Q to quit!')
    print()
    action = input('Type a task or command: ').lower()
    return action

def is_command(arg): #check if the user typed a command and return true if its / false if isn't
    if arg in ['list', 'undo', 'remake', 'clear']:
        return True 
    return False
    
def list_tasks():
    print()
    for i in list:
        print(i)
    print()
    
def commands(command): #check wich command the user typed
    if command == 'list' and list != []: #command list
        list_tasks()
        
    if command == 'list' and list == []: #command list
        print()
        print('Nothing to list')
     
    elif command == 'undo': #command undo
        poped = list.pop()
        list_tasks()
        
    elif command == 'remake': #command remake
        try:
            list.append(poped)
            list_tasks()
        except:
            print('No remake to do')
    
    elif command == 'clear':
        system('cls')
    
    elif command == 'q': #DO THIS 
        ...
    
def main():
    action = task_or_command()
    if is_command(action): #verify if its an command, if its execute the command
        commands(action)
    else:
        list.append(action)
        list_tasks()
        
while True:
    main()
    line()