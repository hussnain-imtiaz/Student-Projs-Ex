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

print_help()

def handl_l(data):
    i = 1
    with open("data.txt", "r+") as f:
        f.seek(0)
        if f.read() == "":
            print("No todos for today!")
        else:
            for line in data:
                print(f'{i}. {line}')
                i += 1


def handl_a(data, item):
    if item == "":
        print('Unable to add task: no task provided')
    else:
        data.append(item)
        file = open('data.txt', 'a')
        file.write('\n' + item)
        file.close()
    return data

def handl_r(r_task):
    if r_task == "":
        print('Unable to remove: no index provided')
    else:
        with open("data.txt", "r") as f:
            lines = f.readlines()
        with open("data.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != r_task:
                    f.write(line)

# def handl_c():



while True:
    choice = input('Please choose a command: ')
    if len(choice) == 1 or len(choice) > 2:
        print_help()
    else:
        data = []
        with open('data.txt') as file:
            for line in file:
                data.append(line.strip())
    if choice == '-l':
        handl_l(data)
    elif choice == '-a':
        item = input('Enter a task: ')
        data = handl_a(data, item)
    elif choice == '-r':
        r_task = input('Enter the task to be removed: ')
        handl_r(r_task)
    # elif choice == '-c':

    else:
        print('Invalid argument')
        print_help()


