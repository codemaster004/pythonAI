from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import filetype
import os
import time
import random


folder_to_track = '/Users/fd/Documents/Python/PyAutomation/todo-decode_files'
final_directory = '/Users/fd/Documents/Python/PyAutomation/decoded_files'


def decode_and_move_file(src, filename, extention):
    print('...Decoding file...')

    # with open(src, 'rb') as file:
    #     data = file.read()
    # my_list = list(bytes(data))

    # for x in range(256):
    #     my_list = [i - x if i - x >= 0 else i - x + 256 for i in my_list]
    #     new_bytes = bytes(my_list)
    #     with open(f'{final_directory}/{filename}', 'wb') as copy:
    #         copy.write(new_bytes)
    #
    #     kind = filetype.guess(f'{final_directory}/{filename}')
    #     if kind is not None:
    #         print(f'...Code movement found - {x}...')
    #         break
    #
    # print('...File successfully decoded and moved...')
    # print(f'...File extension successfully found - {kind.extension}...')
    # os.rename(f'{final_directory}/{filename}', f'{final_directory}/{filename}.{kind.extension}')
    # os.remove(f'{folder_to_track}/{filename}.{extention}')
    # print('...Base file successfully removed...')
    # print('Done!\n')

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

        byte_list = [byte_list[i] - get_r(i) if byte_list[i] - get_r(i) >= 0 else byte_list[i] - get_r(i) + 256 for i in
                     range(len(byte_list))]

        new_bytes = bytes(byte_list)

        with open(f'{final_directory}/{filename}', 'wb') as copy:
            copy.write(new_bytes)
        print('...File successfully decoded and moved...')

        kind = filetype.guess(f'{final_directory}/{filename}')
        print(f'...File extension successfully found - {kind.extension}...')

        os.rename(f'{final_directory}/{filename}', f'{final_directory}/{filename}.{kind.extension}')
        os.remove(f'{folder_to_track}/{filename}.{extention}')
        print('...Base file successfully removed...')

        print('Done!\n')


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print('New file detected...')
        for filename in os.listdir(folder_to_track):
            src = f'{folder_to_track}/{filename}'
            if filename[0] != '.':
                decode_and_move_file(src, filename.split(".")[0], filename.split(".")[1])


if __name__ == '__main__':
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
