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
    i = 1
    for line in data:
        print(f'{i}. {line}')
        i += 1

def handl_a(data, item):
    data.append(item)
    file = open('data.txt', 'a')
    file.write('\n' + item)
    file.close()
    return data


if len(args) == 1 or len(args) > 2:
    print_help()

else: 
    choice = args[1]
    data = []
    with open('data.txt') as file:
        for line in file:
            data.append(line.strip())

    if choice == '-l':
        handl_l(data)
    elif choice == '-a':
        item = input('Enter the item: ')
        data = handl_a(data, item)
    elif choice == '-r':
        run_func()
    elif choice == '-c':
        run_func()
    else:
        print('Invalid argument')
        print_help()


