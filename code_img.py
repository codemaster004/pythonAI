from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import random
import os
import time


folder_to_track = '/Users/fd/Documents/Python/PyAutomation/todo-code_files'
final_directory = '/Users/fd/Documents/Python/PyAutomation/coded_files'


def code_and_move_file(src, filename):
    print('...Coding file...')
    x = random.randint(1, 255)
    with open(src, 'rb') as file:
        data = file.read()
        my_list = list(bytes(data))
        my_list = [i + x if i + x <= 255 else i + x - 256 for i in my_list]
        new_bytes = bytes(my_list)
        with open(f'{final_directory}/{filename.split(".")[0]}.txt', 'wb') as copy:
            copy.write(new_bytes)
        print('...File successfully coded and moved...')

        os.remove(f'{folder_to_track}/{filename}')
        print('...Base file successfully removed...')
        print('Done!\n')


def random_code_and_move_file(src, filename):
    print('...Coding file...')
    with open(src, 'rb') as file:
        data = file.read()
        byte_list = list(bytes(data))

        my_seed = byte_list[0] * 4096 + byte_list[1] * 256 + byte_list[2] * 16 + byte_list[3]

        random.seed(my_seed)

        randoms = []

        def get_r(index):
            if index + 1 > len(randoms):
                if index > 3:
                    randoms.append(random.randint(1, 255))
                else:
                    randoms.append(0)
            return randoms[index]

        byte_list = [byte_list[i] + get_r(i) if byte_list[i] + get_r(i) <= 255 else byte_list[i] + get_r(i) - 256 for i
                     in range(len(byte_list))]

        new_bytes = bytes(byte_list)

        with open(f'{final_directory}/{filename.split(".")[0]}.txt', 'wb') as copy:
            copy.write(new_bytes)
        print('...File successfully coded and moved...')

        os.remove(f'{folder_to_track}/{filename}')
        print('...Base file successfully removed...')
        print('Done!\n')


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print('New file detected...')
        for filename in os.listdir(folder_to_track):
            src = f'{folder_to_track}/{filename}'
            if filename[0] != '.':
                random_code_and_move_file(src, filename)


if __name__ == '__main__':
    for filename in os.listdir(folder_to_track):
        src = f'{folder_to_track}/{filename}'
        if filename[0] != '.':
            random_code_and_move_file(src, filename)

    print('Folder monitoring begun\n')
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, folder_to_track, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
