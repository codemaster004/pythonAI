import random
import hashlib


# random.seed('hej')
#
# my_hash = hashlib.sha1()
# my_hash.update(b'Hell')
# hashed = my_hash.digest()
# print(hashed)
#
# my_list = list(bytes(hashed))
# print(my_list)


def random_coding():
    with open('test/todo-code.txt', 'rb') as file:
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

        with open('test/coded.txt', 'wb') as copy:
            copy.write(new_bytes)


def random_decoding():
    with open('test/todo-decode.txt', 'rb') as file:
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

        with open('test/decoded.txt', 'wb') as copy:
            copy.write(new_bytes)


def normal_coding():
    with open('codeTest.txt', 'rb') as file:
        data = file.read()
        byte_list = list(bytes(data))

        r = 7
        byte_list = [i + r if i + r <= 255 else i + r - 256 for i in byte_list]

        new_bytes = bytes(byte_list)

        with open('decodeTest.txt', 'wb') as copy:
            copy.write(new_bytes)


def normal_decoding():
    with open('decodeTest.txt', 'rb') as file:
        data = file.read()
        byte_list = list(bytes(data))

        r = 7
        byte_list = [i - r if i - r >= 0 else i - r + 256 for i in byte_list]

        new_bytes = bytes(byte_list)

        with open('codeTest.txt', 'wb') as copy:
            copy.write(new_bytes)


# normal_coding()
#
# normal_decoding()

# random_coding()
#
# random_decoding()
