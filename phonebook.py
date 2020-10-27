import logger


annuaire = {}


def create_contact(names, phone_number, is_favorite):
    logger.test("create_contact()")
    contact = {
        'names': names,
        'phone_number': phone_number,
        'is_favorite': is_favorite,
    }
    return contact



def add_contact(new):
    logger.test(f"add_contact: {new}")
    phone_number = new['phone_number']
    annuaire[phone_number] = new

c = create_contact("theo", "6474467", False)
add_contact(c)
c = create_contact("ocb", "642331324", True)
add_contact(c)
c = create_contact("moi", "6475786767", True)
add_contact(c)

def get_names():
    logger.test("get_names()")
    names = []


    for n in annuaire:
        v = annuaire[n]
        names.append(v['names'])

    names.sort()
    print(names)
    return names


def display_all():
    logger.test(f"display all {annuaire}")
    for a in annuaire:
        print(annuaire[a])


def get_contact(phone_number):
    c = annuaire[phone_number]
    logger.test(f"get_contact={c}")
    return c



