# list of meals for meal planner, sorted

from model import *
import random
import csv

# scrambled_eggs = Non_dinner('jajecznica', ['jajko', 'masło', 'bekon'])
# omelette = Non_dinner('omlet', ['jajko', 'pomidor', 'cebula'])
# oatmeal = Non_dinner('owsianka', ['mleko', 'płatki owsiane', 'miód'])
# sandwich = Non_dinner('kanapka', ['chleb', 'masło', 'ser', 'pomidor'])
# corn_flakes = Non_dinner('płatki na mleku', ['mleko', 'płatki'])
# pudding = Non_dinner('budyń', ['mleko', 'budyń w proszku', 'cukier'])
# pancakes = Non_dinner('pankejki', ['tofu', 'mąka', '' ])
#
# spaghetti = Dinner('spagetti', ['makaron', 'pomidory w puszce', 'mięso mielone', 'bazylia'])
# fish_and_chips = Dinner('ryba z frytkami', ['ryba filet', 'frytki', 'kapusta kiszona', 'marchewka', 'przyprawa do ryb',
#                                       'cytryna'])
#
#
# non_dinners = [scrambled_eggs, omelette, oatmeal, sandwich, corn_flakes, pudding]
# dinners = [spaghetti, fish_and_chips]
#
# week = ["Pon", 'Wt', 'Śr', 'Czw', 'Pt', 'Sob', 'Nd']
#
# for day in week:
#     if day:
#         breakfast = random.choice(non_dinners)
#         dinner = random.choice(dinners)
#         supper = random.choice(non_dinners)
#         while breakfast == supper:
#             supper = random.choice(non_dinners)
#         print (f"""Twój jadłospis na {day} to {breakfast}, {dinner}, {supper}.
# Musisz kupić
# {breakfast.get_ingr},
# {dinner.get_ingr},
# {supper.get_ingr}""")

with open("non_dinners.csv", "r+") as file:
    reader = csv.reader(file)
    counter = 1
    for row in reader:
        meal = Non_dinner(name=row['Name'], ingredients=row['Ingr1'])
        non_dinners = []
        non_dinners.append(meal)
        counter += 1

print(non_dinners)
