# from lesson5 import greetings as g
# import lesson5
#
# # greetings('Anna')
# lesson5.greetings('Samat')
# g('Kirill')


import random
from random import randint, choice


# time.sleep(5)
# print(f'{datetime.now().day} декабря ')


import datetime
from datetime import datetime


def greetings(name):
    hours = datetime.now().hour
    if hours >= 4 or hours <= 11:
        print(f'GOOD MORNING !{name}')

greetings('kirill')

# start = datetime.now()
# guys = ['kirill', 'alice', 'murat', 'anna', 'kate']
#
# print(random.randint(1, 2000))
# print(randint(1, 5))
# print(random.sample(guys, 2))
# print(choice(guys))