from functools import reduce


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

x = 1; y = 2
print(f"Before: x, y = {x, y}")
x, y = y, x
print(f"After permuation: x, y = {x, y}")
