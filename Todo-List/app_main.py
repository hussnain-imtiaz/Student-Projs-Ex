from ast import arg
import sys
args = sys.argv


def print_help():
    help = """
    Command Line Todo application
    =============================
    Command line arguments:
        -l   Lists all the tasks
        -a   Adds a new task
        -r   Removes an task
        -c   Completes an task
    """
    print(help)

def handl_l(data):
    if len(data) == 0:
        print('No todos for today!')
    else:
        i = 1
        for line in data:
            if len(line) > 1:
                print(f'{i}. {line}')
                i += 1

def handl_a(data, item):
    data = [line for line in data if len(line) > 1]
    file = open('data.txt', 'a')
    if len(data) > 0:  
        file.write('\n' + '[ ] ' + item)
    else:
        file.write('[ ] ' + item)
    file.close()
    data.append(item.strip())


def handl_r(data, index):
    data = [line for line in data if len(line) > 1]
    print(data)
    data.pop(index)
    with open('data.txt', 'w') as file:
        file.write('')
    file = open('data.txt', 'a')
    for line in data:
        file.write(line + '\n')
    file.close()
    return data

def handl_c(data, index):
    data[index] = '[x] ' + data[index][4:]
    print(data)
    with open('data.txt', 'w') as file:
        file.write('')
    file = open('data.txt', 'a')
    for line in data:
        file.write(line + '\n')
    file.close()
    return data

if len(args) == 1:
    print_help()

else: 
    choice = args[1]
    data = []
    with open('data.txt') as file:
        for line in file:
            data.append(line.strip())

    if choice == '-l' and len(args) == 2:
        handl_l(data)
    elif choice == '-a':
        if len(args) != 3:
            print('Unable to add: no task provided')
        else:
            item = args[2]
            handl_a(data, item)
    elif choice == '-r':
        if len(args) != 3:
            print('Unable to remove: no index provided')
        else:
            if not(args[2].isnumeric()): 
                print('Unable to remove: index is not a number') 
            elif int(args[2]) > len(data):
                print('Unable to remove: index is out of bound')
            else:
                indx_to_remove = int(args[2]) - 1
                data = handl_r(data, indx_to_remove)
    elif choice == '-c':
        indx_to_check = int(args[2]) - 1
        data = handl_c(data, indx_to_check)
    else:
        print('Unsupported argument')
        print_help()
