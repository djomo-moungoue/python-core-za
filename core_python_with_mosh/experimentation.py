"""
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
import calendar
import os

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
"""

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
"""

hash(range(1,3)) : -7299810140967063839 - type(range(1,3)) : <class 'range'>
hash(123) : 123 - type(123) : <class 'bytes'>
hash('123') : 1404880117889103899 - type('123') : <class 'str'>
hash(b'123') : 1404880117889103899 - type(b'123') : <class 'bytes'>
hash((1,2,3)) : 529344067295497451 - type((1,2,3)) : <class 'tuple'>

"""
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
"""
"""
# Exercice :
from pprint import pprint

sentence = "This is a common interview question"
# chars_set = set(sentence)
chars_frequency_dict = dict((x, sentence.count(x)) for x in set(sentence))
chars_dict_sorted_by_frequency = sorted(chars_frequency_dict.items(), key=lambda item: item[1])
print(chars_frequency_dict)
print(f"chars_dict_sorted_by_frequency : {chars_dict_sorted_by_frequency}")
print(f"Corresponding characters : {chars_dict_sorted_by_frequency[-1]}")
"""

# m = filter(d.items(), lambda item[1]: if max(item[1]))
# max_occurence = max(d.values())
# for k, v in d.items():
#    if v == max_occurence:
#        most_repeated_character = k
#        break
# print(f"Set of characters : {chars_set}")

# Exceptions
"""
def get(index) -> int:
    numbers = [x for x in range(1, 5)]
    try:
        return numbers[index]
    except IndexError:
        return f"the index range should be 0 up to {len(numbers)}"


print(f"get(5): {get(5)}")
"""
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
"""
"""
# Inheritance of built-in classes
class TrackableList(list):

    def __init__(self):
        pass

    def append(self, object):
        print("Append called")
        super().append(object)

    def __str__(self):
        return f'TractableList{super().__str__()}'


t_list = TrackableList()
t_list.append('1')
print(t_list)

"""
"""
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
"""
"""
directory = Path("blog2")
if not directory.exists():
    directory.mkdir()
print(directory.exists())
# if directory.exists():
#    directory.rmdir()
print(directory.exists())
# if directory.exists():
#    directory.rename("blog3")
print(directory.name)
print([p for p in Path("blog2").iterdir()])
print([p for p in Path("blog2").glob("*.py")])

def delete_folder(path: str) -> None:
    if Path(path).exists():
        dir = Path(path)
        for sub in dir.iterdir():
            if sub.is_dir():
                delete_folder(sub)
            else:
                sub.unlink()
        dir.rmdir()  # if you just want to delete the dir content but not the dir itself, remove this line
        print(f"{str(dir)} recursively deleted")
    else:
        print(f"{str(dir)} doesn't exist")
"""
"""
from time import ctime

file = Path("blog/__init__.py")
if file.exists():
    print(ctime(file.stat().st_ctime))  # display the creation time of the file.
    print(file.read_text())  # read the content of the file as text
    byte = file.read_bytes()  # read the content of the f
    print(byte)
"""
"""
# ZipFile - Working with ZIP Archive
import os
from pathlib import Path
from zipfile import ZipFile

# print(f"Operating System : {os.name}")
#print(f"Current Directory : {Path().resolve()}")
#print(f"Current Directory : {os.getcwd()}")

with ZipFile("zipped_blog.zip", "w") as zipped_blog:
    for path in Path("blog").rglob("*.*"):
        zipped_blog.write(path)
    print(f" CWD : {Path('.').cwd()}")

if Path("zipped_blog.zip").exists():
    with ZipFile("zipped_blog.zip", "r") as zipped_blog:
        print(f"Zip content : {zipped_blog.namelist()}")
        print(f"File info : {zipped_blog.getinfo('blog/tagcloud.py')}")
        zipped_blog.extractall()
"""
"""
village_ouest.csv
haut-nkam, nde
Bafang, Bazou
Bana, Balengou
Bandja, Bangou
Bapouantou, Bagangté


créer le fichier
écrire les village à l'intérieur
lire le contenu et insérer dans un dictionnaire

# [import csv - Lecture et écriture de fichiers CSV](https://docs.python.org/3/library/csv.html)

import csv

with open("villages_de_louest.csv", "w", newline="", encoding="utf-8") as villages_de_louest:  # Return a file object
    csv_writer = csv.writer(villages_de_louest)
    csv_writer.writerow(["Haut-nkam", "Nde"])  # The first line is considered as headers
    csv_writer.writerow(["Bafang", "Bazou"])  # Next lines are considered as data
    csv_writer.writerow(["Bana", "Balengou"])
    csv_writer.writerows([["Bandja", "Bangou"], ["Bapouantou", "Bagangté"]])  # lines cumulates

with open("villages_de_louest.csv", "r") as villages_de_louest:
    csv_reader = csv.reader(villages_de_louest)
#    print(f"\nList Output : {list(csv_reader)}\n")
    print("\nList Output\n")
    for row in csv_reader:
        print(row)
#        print(','.join(row))

with open("villages_de_louest.csv", "r") as villages_de_louest:
    csv_reader = csv.DictReader(villages_de_louest, fieldnames=['Haut-nkam', 'Nde'], restkey="others")
#    print(f"\nDict Output : {list(csv_reader)}\n")
    print("\nDict Output\n")
    for row in csv_reader:
        print(row)
#        print(row['Haut-nkam'], row['Nde'])
"""
"""
[import json - Encodeur JSON : json.dumps() et décodeur JSON : json.loads()](https://docs.python.org/3/library/json.html)


import json
from pathlib import Path

encoder = json.dumps({"Python": 3, "Django": 2, "Pandas": 5})
print(f"Encoder : {encoder}")
with open("tagcloud.json", "w") as jsonfile:
    jsonfile.write(encoder)
#  Path("tagcloud.json").write_text(encoder)

decoder = json.loads('{"Python": 3, "Django": 2, "Pandas": 5}')
print(f"Decoder : {decoder}")
data = Path("tagcloud.json").read_text()
tagcloud = json.loads(data)
print(f"Data : {data}")
print(f"Tagcloud : {tagcloud}")
"""

"""
[import sqlite3 - Interface DB-API 2.0 pour les bases de données SQLite](https://docs.python.org/3/library/sqlite3.html)

Exemple d'utilisation :  Base de données d'un prototype de films Monty Python



def print_data(cursor, table_name: str, output_title: str) -> any:
    result = cursor.execute(f"SELECT * FROM {table_name}")
    fetched_data = result.fetchall()  # query.fetchmany(size=) or query.fetchone()
    return fetched_data


from pathlib import Path
import sqlite3

if not Path("movies").exists():
    Path("movies").mkdir()

# Tout d'abord, nous devons créer une nouvelle base de données et ouvrir une connexion à la base de données pour permettre à sqlite3 de travailler avec elle.
with sqlite3.connect("movies/movies.db") as connection_object: # on-disk database

    # Créer un curseur de base de données afin d'exécuter des instructions SQL et de récupérer des résultats de requêtes SQL.
    cursor_object = connection_object.cursor()  # objet itérable

    # créer une table de base de données film avec des colonnes pour le titre, l'année de sortie et la note de critique.
    # Grâce à la fonctionnalité de typage flexible de SQLite, la spécification des types de données est facultative.
    cursor_object.execute("DROP TABLE IF EXISTS movie")
    cursor_object.execute("CREATE TABLE IF NOT EXISTS movie(title,year,score)")

    # cursor_object.executemany(sql: TEXT, seq_of_parameters) cursor_object.executescript(sql_script: TEXT)
    cursor_object.execute("INSERT INTO movie VALUES('movie1', 1988, 3)")

    # L'instruction INSERT ouvre implicitement une transaction, qui doit être validée (con_commit()) avant que les
    # modifications ne soient enregistrées dans la base de données.
    connection_object.commit() # Toujours l'exécuter après avoir modifié l'état de la base de données

    # Vérifier si la table movie a été crée et les donnés on été inséré
    cursor_object.execute("SELECT name FROM sqlite_master")
    print(f"\nData from ROM : \n{cursor_object.fetchone()}")
    cursor_object.execute("SELECT * FROM movie")
    print(f"{cursor_object.fetchall()}") # query.fetchmany(size=) or query.fetchone()

    data = [('movie'+str(x), 1988+x, 3+x) for x in range(2,5)]
    # Remarquez que les caractères de remplacement ? sont utilisés pour lier les données à la requête. Utilisez toujours les
    # caractères de remplacement au lieu du formatage des chaînes pour lier les valeurs Python aux instructions SQL, afin
    # d'éviter les attaques par injection SQL.
    cursor_object.executemany("INSERT INTO movie values(?,?, ?)", data)
    connection_object.commit()

    connection_object.executescript("INSERT INTO movie VALUES('movie10', 1999, 9.5);")
    cursor_object.executescript(open("movies/movie_records.sql").read())
    connection_object.commit()
    print(f"\nData from ROM :")
    for row in cursor_object.execute("SELECT year, title, score FROM movie order by year"):
        print(f"{row}")

with sqlite3.connect(":memory:") as connection_object_ram: # in-memory database
    cursor_object_ram = connection_object_ram.cursor()
    cursor_object_ram.execute("DROP TABLE IF EXISTS movie_ram")
    cursor_object_ram.execute("CREATE TABLE IF NOT EXISTS movie_ram(title_r,year_r,score_r)")

    db_result_ram = cursor_object_ram.execute("INSERT INTO movie_ram VALUES('movie1_r', 1988, 3)")

    connection_object_ram.commit()

    cursor_object_ram.execute("SELECT name FROM sqlite_master")
    print(f"\nData from RAM : \n{cursor_object_ram.fetchone()}")
    cursor_object_ram.execute("SELECT * FROM movie_ram")
    print(f"{cursor_object_ram.fetchall()}") # query.fetchmany(size=) or query.fetchone()

    db_result_ram = cursor_object_ram.executemany("INSERT INTO movie_ram values(?,?, ?)", data)
    connection_object_ram.commit()
    print(f"\n\nData from RAM :")
    for row in cursor_object_ram.execute("SELECT * FROM movie_ram"):
        print(f"{row}")

# Créer une sauvegarde
with sqlite3.connect("movies/movie_backup.db") as connection_object_backup:
    connection_object.backup(connection_object_backup)
    print(f"\n\nBackup content")
    print(connection_object_backup.execute("SELECT name FROM sqlite_master").fetchone())
    for row in connection_object_backup.cursor().execute("SELECT * FROM movie"):
        print(f"{row}")

# Fermer toutes les connexions
#connection_object.close()
#connection_object_ram.close()
#connection_object_backup.close()
"""

"""
# [import time](https://docs.python.org/3/library/time.html)

import time
import platform
print(f"{platform.system()} {platform.release()} {platform.version()}'s Epoch : {time.gmtime(0)}")
current_time_sec = time.time()
print(f"time() -> float : {current_time_sec}")
print(f"sleep(sec) --> None ... ")
time.sleep(5)
print(f"asctime([tuple] | [struct_time]) -> str : {time.asctime()}")
utc_time = time.gmtime(current_time_sec)
print(f"Empty Arg gmtime(sec) -> struct_time : {utc_time}")
print(f"UTC struct_time asctime([tuple] | [struct_time]) -> str : {time.asctime(utc_time)}")
local_time = time.localtime(current_time_sec)
print(f"localtime(0) -> struct_time : {local_time}")
print(f"Local struct_time asctime([tuple] | [struct_time]) -> str : {time.asctime(local_time)}")
print(f"Tuple('Day Mon Date Hour:Min:Sec Year') asctime([tuple] | [struct_time]) -> str : {time.asctime((2022, 10, 23, 13, 50, 32, 6, 295, 0))}")
print(f"strftime(format[, t]) -> struct_time : {time.strftime('23/10/2022 13:50:32.0', time.gmtime())}")
print(f"strftime(format[, t]) -> struct_time : {time.strftime('23/10/2022 13:50:32.0', time.localtime())}")
"""

"""
class datetime.datetime

from datetime import datetime, timedelta
import time
print(f"Now : {datetime.now()}")
print(f'Datetime object : {datetime(2022, 10, 25)}')
user_input = "2018/01/01"
dt = datetime.fromtimestamp(time.time())
print(f'time converted to datetime object : {dt}')
print(f'string converted to datetime object : {datetime.strptime(user_input, "%Y/%m/%d")}')
print(f'datetime object converted to string : {dt.strftime("%Y/%m/%d")}')
print(f'datetime object attributes : {dt.year}-{dt.month}')
duration = datetime.now() - datetime(1988, 5, 19)
print(f"Duration : {duration}")
print(f"Duration.days : {duration.days} - Duration.seconds : {duration.seconds} - Duration.microseconds : {duration.microseconds}")
print(f"Duration.total_seconds() : {duration.total_seconds()}")
print(f"Duration.total_seconds() : {tim)}")
"""

"""
## [import calendar](https://docs.python.org/3/library/calendar.html)
"""
from calendar import Calendar, TextCalendar, HTMLCalendar, LocaleTextCalendar, LocaleHTMLCalendar
import locale
c = Calendar()
print(f"Calendar().monthdatescalendar(year, month) -> [list[list[int]] : {c.monthdatescalendar(2022, 10)}")
print(f"Calendar().monthdayscalendar(year, month) -> [list[list[int]] : {c.monthdayscalendar(2022, 10)}")
print(f"Calendar().yeardayscalendar(year) -> [list[list[int]] : {c.yeardayscalendar(2022)}")

print(f"locale.locale_alias : {locale.locale_alias}")
print(f"locale.locale_encoding_alias : {locale.locale_encoding_alias}")
print(f"locale.windows_locale) : {locale.windows_locale}")
print(f"locale.normalize(localename) : {locale.normalize('de_de')}")

tc = TextCalendar()
print(f"TextCalendar().formatyear(theyear, w=2, l=1, c=6, m=3) -> str {tc.formatyear(2022, m=6)}")
print(f"TextCalendar().formatmonth(theyear, themonth, w=0, l=0) -> str\n {tc.formatmonth(2022, 10)}")
ltc = LocaleTextCalendar(locale='fr')
print(f"LocaleTextCalendar(firstweekday=0, locale=None).formatyear(theyear, w=2, l=1, c=6, m=3) -> str {ltc.formatyear(2022, w=6, l=1, c=6, m=6)}")
print(f"LocaleTextCalendar(firstweekday=0, locale=None).formatmonth(theyear, themonth, w=0, l=0) -> str\n {ltc.formatmonth(2022, 10)}")

hc = HTMLCalendar()
print(f"HTMLCalendar().formatyear(theyear, width) -> str {hc.formatyear(2022, width=6)}")
print(f"HTMLCalendar().formatmonth(theyear, themonth, w=0, l=0) -> str\n {hc.formatmonth(2022, 10, True)}")
lhc = LocaleHTMLCalendar(calendar.MONDAY, 'de_DE')
print(f"LocaleHTMLCalendar : {lhc}")
print(f"LocaleHTMLCalendar().formatyearpage(theyear, width, css=None, encoding=None) -> str {lhc.formatyearpage(2022, width=3, css=None, encoding='utf-8')}")
print(f"LocaleHTMLCalendar().formatmonth(theyear, themonth, w=0, l=0) -> str {lhc.formatmonth(2022, 10, True)}")
