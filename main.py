from art import *


def create_contact(names, phone_number, is_favorite):

    contact = {
        'names': names,
        'phone_number': phone_number,
        'is_favorite': is_favorite,
    }
    return contact

annuaire = {}

def add_contact(c):

    phone_number = c['phone_number']
    annuaire[phone_number] = c

c = create_contact("theo", "6474467", False)
add_contact(c)
c = create_contact("ocb", "642331324", True)
add_contact(c)
c = create_contact("moi", "6475786767", True)
add_contact(c)

def get_names():

    names = []


    for n in annuaire:
        v = annuaire[n]
        names.append(v['names'])

    names.sort()

    return names

def display_all():
    for a in annuaire:
        print(annuaire[a])


def get_contact(phone_number):

    for number in annuaire:
        if number == phone_number :
            c=annuaire[number]
            return c





def menu() :
    print("Menu")
    print("Taper 'Names' pour voir les noms de vos contacts")
    print("Taper 'Contact' pour voir vos contacts")
    print("Taper le  numéro pour voir le contact associé")
    input('Faites votre choix')

menu
if input == 'Names' :
    print(get_names())
elif input == 'Contact' :
    display_all()
else :











