from functools import reduce
from random import random


def display_even(limit=2):
    count = 0
    message = ""
    for x in range(1, limit):
        if x % 2 == 0:
            print(x)
            count += 1
    message = f"We have {count} even number" if count <= 1 else f"We have {count} even numbers"
    return message


def fizz_buzz(number=0):
    if number % 15 == 0:
        return "FizzBuzz"
    if number % 5 == 0:
        return "Buzz"
    if number % 3 == 0:
        return "Fizz"
    return number


products = ["tergal bleu foncé", "tergal jaune", "tergal bordeaux"]
prices = [17, 3, 5]
shopping_cards = [
    ("tergal bleu foncé", 17),
    ("tergal jaune", 3),
    ("tergal bordeaux", 5),
]


# def sort_item(item):
#    return item[1]

def get_price(item): item[1]


# prices_mapped = list(map(get_price(), shopping_cards))
prices_mapped = list(map(lambda item: item[1], shopping_cards))
prices_mapped = [item[1] for item in shopping_cards]
print(f"Price list : {prices_mapped}")

# def filter_card(item): return item if item[1] < 10 else None
# filtered = list(filter(filter_card(shopping_cards[1]), shopping_cards))
filtered = list(filter(lambda item: item[1] < 10, shopping_cards))
filtered = [item[1] for item in shopping_cards if item[1] < 10]
print(f"Items cheaper than 10 EURO :{filtered}")

prices = []
for product in shopping_cards: prices.append(product[1])
total = reduce(lambda x, y: x + y, list(prices))
print(f"Total = {total}")

my_list_comprehension_time2 = [x * 2 for x in range(10) if x % 2 == 0]
my_list_comprehension_power2 = [x ** 2 for x in range(10) if x % 2 == 0]
print(f"my_list_comprehension_time2: {my_list_comprehension_time2}")
print(f"my_list_comprehension_power2 : {my_list_comprehension_power2}")

matrix = [[j * 2 for j in range(1, 3)] for i in range(1, 3)]
print(f"[[2, 4],[2, 4]] = {matrix}")

zipped = list(map(lambda item: item, zip(products, prices)))
zipped = [item for item in zip(products, prices)]
print(f"zipped = {zipped}")
# sorted_shopping_cards = sorted(shopping_cards, key=lambda item: item[1])
# sorted_shopping_cards = sorted(shopping_cards, sort_item)
# print(f"Sorted\n{sorted_shopping_cards} \n\nUnserted\n{shopping_cards}")
# print(fizz_buzz(301))
# print(display_even(5))

# 13- Stacks
browsing_session = []
for x in range(1, 4):
    browsing_session.append(x)
print(f"\n13- Stack")
print(f"Total browsing sessions : {browsing_session}")
print(f"last session closed : {browsing_session.pop()}")
print(f"Remaining browsing sessions : {browsing_session}")
print(f"Redirect : {browsing_session[-1]}") if browsing_session else print(f"No session opened!")

# 14- Queues
from collections import deque

waiting_queue = deque([])
count = 0
for x in range(1, 4):
    waiting_queue.append(x)
print(f"\n14- Queue")
print(f"Total clients waiting : {waiting_queue}")
count += 1
print(f"Receive the {count} client : {waiting_queue.popleft()}")
print(f"Remaining clients waiting : {waiting_queue}")
print(f"Next client to receive : {waiting_queue[0]}") if waiting_queue else print(f"Empty queue!")
len_waiting_queue = len(waiting_queue)
for x in range(len_waiting_queue): count += 1; print(f"Receive the {count} client : {waiting_queue.popleft()}")
print(f"Next client to receive : {waiting_queue[0]}") if waiting_queue else print(f"Empty queue!")

point = (1,)

print(f"point = {point}")

x = 1;
y = 2
print(f"Before: x, y = {x, y}")
x, y = y, x
print(f"After permutation: x, y = {x, y}")

print(f"\nBuiltin len(iterable)")
print(f"len('1234') : {len('1234')}")
print(f"len([1, 2, 2, 3]) : {len([1, 2, 2, 3])}")
print(f"len(deque([1, 2, 2, 3])) : {len(deque([1, 2, 2, 3]))}")
from array import array

print(f"len(array('i', [1, 2, 2, 3])) : {len(array('i', [1, 2, 2, 3]))}")
print(f"len((1, 2, 2, 3)) : {len(([1, 2, 2, 3]))}")
print(f"len(set([1, 2, 2, 3])) : {len(set([1, 2, 2, 3]))}")
print(f"len(dict(a=1, b=2, c=2, d=3)) : {len(dict(a=1, b=2, c=2, d=3))}")

print(f"\niterable[index|key]")
print(f"'1224'[0] : {'1224'[0]}")
print(f"[1, 2, 2, 3][0]: {[1, 2, 2, 3][0]}")
print(f"deque([1, 2, 2, 3])[0] : {deque([1, 2, 2, 3])[0]}")
from array import array

print(f"array('i', [1, 2, 2, 3])[0]) : {array('i', [1, 2, 2, 3])[0]}")
print(f"(1, 2, 2, 3)[0] : {(1, 2, 2, 3)[0]}")
# print(f"len(set([1, 2, 2, 3])) : {set([1, 2, 2, 3])[0]}") #  TypeError: 'set' object is not subscriptable
print(f"dict(a=1, b=2, c=2, d=3)['a']) : {dict(a=1, b=2, c=2, d=3)['a']}")
"""
print(f"\n del iterable[index|key]")
string = '1224'
# del my_str
print(f"my_str : {my_str if len(my_str) else 'No more str'}") #  SyntaxError: f-string: invalid syntax
try:
    my_list = [1, 2, 2, 3]
    del my_list
    if len(my_list):
        print(f"my_list: {my_list}")  #  SyntaxError: f-string: invalid syntax
except NameError:
    return  "is not defined"

print(f"del deque([1, 2, 2, 3])[0] : {del deque([1, 2, 2, 3])[0]}")
from array import array
print(f"del array('i', [1, 2, 2, 3])[0]) : {del array('i', [1, 2, 2, 3])}")

print(f"del (1, 2, 2, 3)[0] : {del (1, 2, 2, 3)[0]}")
# print(f"len(set([1, 2, 2, 3])) : {set([1, 2, 2, 3])[0]}") #  TypeError: 'set' object is not subscriptable
print(f"del dict(a=1, b=2, c=2, d=3)['a']) : {del dict(a=1, b=2, c=2, d=3)['a']}")"""

print(f"Emboîtement des iterable")
# s = str("ab", "cd")
# print(f"s : {s}")
l = [[1, 2], [3, 4]]
print(f"l : {l}")
t = ((1, 2), (3, 4))
print(f"t : {t}")
# s = {{1, 2}}
# print(f"s : {s}") #  TypeError: unhashable type: 'set'
# d = {{"1": 2}}
# print(f"d : {d}") #  TypeError: unhashable type: 'dict'
# array(array('i', [1,2]), array('i', [3,4]))
"""
q = deque(deque([1, 3, deque(["dfg", 3])]))
print(f"q : {q}")
tuple()
set()
dict()
min()
ord()
chr()
"""

from collections import deque, namedtuple

print(f"\nhash(object) - type(object)")
print(f"hash(range(1,3)) : {hash(range(1, 3))} - type(range(1,3)) : {type(range(1, 3))}")
print(f"hash(123) : {hash(123)} - type(123) : {type(b'123')}")
print(f"hash('123') : {hash('123')} - type('123') : {type('123')}")
print(f"hash(b'123') : {hash(b'123')} - type(b'123') : {type(b'123')}")
print(f"hash((1,2,3)) : {hash((1, 2, 3))} - type((1,2,3)) : {type((1, 2, 3))}")
print(
    f"hash(frozenset([1,2,3])) : {hash(frozenset([1, 2, 3]))} - type(frozenset([1,2,3])) : {type(frozenset([1, 2, 3]))}")
print(
    f"hash(namedtuple('Triangle', 'x y z')) : {hash(namedtuple('Triangle', 'x y z'))} - type(namedtuple('Triangle', "
    f"'x y z')) : {type(namedtuple('Triangle', 'x y z'))}")
# print(f"hash({1, 2, 3}) : {hash({1, 2, 3})} - type({1, 2, 3}) : {type({1, 2, 3})}") TypeError: unhashable type: 'set'
# print(f"hash(dict(1=2, 3=3)) : {hash(dict('1'=2, '3'=3))} - type(dict(1+=2, 3=3)) : {type(dict(1=2, 3=3))}")
# print(f"hash([1,2,3]) : {hash([1,2,3])} - type([1,2,3]) : {type([1,2,3])}") #  TypeError: unhashable type: 'list'
# print(f"hash(deque([1,2,3])) : {hash(deque([1,2,3]))} - type(deque([1,2,3])) : {type(deque([1,2,3]))}") #
# TypeError: unhashable type: 'collections.deque'

"""

hash(range(1,3)) : -7299810140967063839 - type(range(1,3)) : <class 'range'>
hash(123) : 123 - type(123) : <class 'bytes'>
hash('123') : 1404880117889103899 - type('123') : <class 'str'>
hash(b'123') : 1404880117889103899 - type(b'123') : <class 'bytes'>
hash((1,2,3)) : 529344067295497451 - type((1,2,3)) : <class 'tuple'>


"""
print(f"\nList, Tuple, Set and Dict Comprehension")
from sys import getsizeof

l = [x * 2 for x in range(1, 17, 2)]
print("unpacked list : ", *l)
print(f"list [x * 2 for x in range(1,7,2)] : {l} size/len of list = {getsizeof(l)} / {len(l)}")
t = tuple([x * 2 for x in range(1, 17, 2)])
print("unpacked tuple : ", *t)
print(f"tuple tuple([x * 2 for x in range(1,7,2)]) : {t} size/len of tuple = {getsizeof(t)} / {len(t)}")
s = set([x * 2 for x in range(1, 17, 2)])
print("unpacked set : ", *s)
print(f"set set([x * 2 for x in range(1,7,2)]) : {s} size/len of set = {getsizeof(s)} / {len(s)}")
d = dict([(x, x * 2) for x in range(1, 17, 2)])
print("unpacked dict : ", {**d})
print(f"dict dict([x * 2 for x in range(1,7,2)]) : {d} size/len of dict = {getsizeof(d)} / {len(d)}")
# values = (x * 2 for x in range(1,77777,2))
print(
    f"generator (x * 2 for x in range(1,7,2)) : {(x * 2 for x in range(1, 17, 2))} size/len of generator = {getsizeof((x * 2 for x in range(1, 17, 2)))}")
print(f"set([x * 2 for x in range(1,7,2)]) : {{x * 2 for x in range(1,7,2)}}")
print(f"dict([x * 2 for x in range(1,7,2)]) : {{x: x * 2 for x in range(5)}}")

# Exercice :
from pprint import pprint

sentence = "This is a common interview question"
# chars_set = set(sentence)
chars_frequency_dict = dict((x, sentence.count(x)) for x in set(sentence))
chars_dict_sorted_by_frequency = sorted(chars_frequency_dict.items(), key=lambda item: item[1])
print(chars_frequency_dict)
print(f"chars_dict_sorted_by_frequency : {chars_dict_sorted_by_frequency}")
print(f"Corresponding characters : {chars_dict_sorted_by_frequency[-1]}")


# m = filter(d.items(), lambda item[1]: if max(item[1]))
# max_occurence = max(d.values())
# for k, v in d.items():
#    if v == max_occurence:
#        most_repeated_character = k
#        break
# print(f"Set of characters : {chars_set}")

# Exceptions
def get(index) -> int:
    numbers = [x for x in range(1, 5)]
    try:
        return numbers[index]
    except IndexError:
        return f"the index range should be 0 up to {len(numbers)}"


print(f"get(5): {get(5)}")

"""
# ---------------------------------

class Tag:
    def __init__(self, name: str):
        self.name = name
        self.hash = int(random())

    def __str__(self):
        return f"#{self.name}"

    def __hash__(self):
        return self.hash


# --------------------


class TagCloud:
#    keep tract on the various tags in a block
    

    def __init__(self):
        self.tags = dict()

    def __str__(self):
        return f"{self.tags}"

    def add(self, tag: str) -> None:
        self.tags[tag] += 1

    def remove(self, tag: str) -> None:
        if tag in self.tags:
            if self.tags[tag] > 0:
                self.tags[tag] -= 1
        else:
            print(f"#{tag} not founded.")


# ---------------


print("\nTag and TagCloud")
t1 = Tag('Python')
t2 = Tag('Django')
t3 = Tag('AWS')
tc = TagCloud()
tc.add(t1.name)
tc.add(t2.name)
tc.add(t3.name)
print(tc)
tc.remove(t2.name)
print(tc)
"""
# ---Polumorphisme---
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Square(Shape):
    def draw(self):
        print('A square')


class Rectangle:
    def draw(self):
        print('A Rectangle')



def draw(shape: Shape):
    shape.draw()

for x in [Square(), Rectangle()]:
    x.draw()
"""


class Square:
    def draw(self):
        print('A square')


class Rectangle:
    def draw(self):
        print('A Rectangle')


def draw(foos):
    for f in foos:
        f.draw()


draw([Square(), Rectangle()])

# Inheritance of built-in classes
class TrackableList(list):
    def append(self, object):
        print("Append callded")
        super().append(object)


TrackableList().append('1')

from pathlib import Path
current_folder = Path()
#  related_path_from_current_folder = Path("blog/__init__.py")
related_path_from_current_folder = Path("blog/pathlib_experimentation.py")
print(related_path_from_current_folder.exists())
print(related_path_from_current_folder.is_file())
print(related_path_from_current_folder.is_dir())
print(related_path_from_current_folder.name)
print(related_path_from_current_folder.stem)
print(related_path_from_current_folder.suffix)
print(related_path_from_current_folder.parent)
print(related_path_from_current_folder.parents)
print(related_path_from_current_folder.with_name("pathlib_renamed.txt"))
print(related_path_from_current_folder.with_suffix(".html"))
print(Path.cwd())

