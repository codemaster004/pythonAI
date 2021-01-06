import random
import hashlib

some_string = 'Hello World'
my_bytes = bytes(some_string, 'utf-8')
print('Word: ', my_bytes)

print('Word in bites: ', list(bytes(my_bytes)))

my_list = list(bytes(my_bytes))
my_list_validation = my_list[:]

randoms = []


def get_r(index):
    if index + 1 > len(randoms):
        if index > 3:
            randoms.append(random.randint(1, 255))
        else:
            randoms.append(0)
    return randoms[index]


my_list = [my_list[i] + get_r(i) if my_list[i] + get_r(i) <= 255 else my_list[i] + get_r(i) - 256 for i in range(len(my_list))]

x = 7
my_list_validation = [i + x if i + x <= 255 else i + x - 256 for i in my_list_validation]

print('Word in random every bite: ', my_list)
print('Word in not random move: ', my_list_validation)

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

