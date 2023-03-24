import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'gucc_inventory_project.settings')

import django

django.setup()
from canoe_club.models import Trip, Kit, Social, User, UserProfile


def populate():
    members1 = [
        {'is_admin': False,
         'is_member': True,
         'email': '5658525s@student.gla.ac.uk',
         'username': 'Ben',
         'password': 'password'
         },
        {'is_admin': False,
         'is_member': True,
         'email': '4658742s@student.gla.ac.uk',
         'username': 'Ayleen',
         'password': 'password'
         }
    ]

    members2 = [
        {'is_admin': False,
         'is_member': True,
         'email': '3658444s@student.gla.ac.uk',
         'username': 'Tay',
         'password': 'password'
         },
        {'is_admin': False,
         'is_member': True,
         'email': '2658999s@student.gla.ac.uk',
         'username': 'Renee',
         'password': 'password'
         },
        {'is_admin': True,
         'is_member': True,
         'email': '1658321s@student.gla.ac.uk',
         'username': 'Kai',
         'password': 'password'
         }
    ]

    kitOwner1 = {
        'is_admin': False,
        'is_member': True,
        'email': '9658999s@student.gla.ac.uk',
        'username': 'Allan',
        'password': 'password'
    }

    kitOwner2 = {
        'is_admin': False,
        'is_member': True,
        'email': '1058999s@student.gla.ac.uk',
        'username': 'Amy',
        'password': 'password'
    }

    kitOwner3 = {
        'is_admin': False,
        'is_member': True,
        'email': '1158999s@student.gla.ac.uk',
        'username': 'Liz',
        'password': 'password'
    }

    trips = [
        {'name': 'Intermediate Weekend',
         'location': 'Inverness',
         'date': '2023-03-24',
         'length': 3,
         'members': members1
         },
        {'name': 'Beginner Day Trip',
         'location': 'The Spean',
         'date': '2023-04-01',
         'length': 1,
         'members': members2
         }
    ]

    socials = [
        {'name': 'St Paddys',
         'date': '2023-03-17',
         'details': 'A big night out meet at 8pm',
         'location': "Bank street"
         },
        {'name': 'Chill Potluck',
         'date': '2023-04-05',
         'details': 'A chill potluck where everyone brings food to share and chill ',
         'location': "Kai's Flat"
         }
    ]

    kits = [
        {'name': 'club_paddle',
         'size': 0,
         'colour': 'red',
         'brand': 'Palm',
         'owner': kitOwner1,
         'type': 'paddle',
         "maintenance": False,
         'maintenance_problem': None,
         'amount': 4,},
        {'name': 'wetsuit',
         'size': 0,
         'colour': 'green',
         'brand': 'O\'Neill',
         'owner': kitOwner2,
         'type': 'wetsuit',
         "maintenance": True,
         'maintenance_problem': 'tear in wetsuit',
         'amount': 2,},
        {'name': 'canoe',
         'size': 0,
         'colour': 'blue',
         'brand': 'Pelican',
         'owner': kitOwner3,
         'type': 'boat',
         "maintenance": True,
         'maintenance_problem': None,
         'amount': 2, }
    ]

    for trip in trips:
        users = []
        for member in trip['members']:
            u = add_user(member['is_admin'], member['is_member'], member['email'], member['username'],
                         member['password'])
            users.append(u)
            add_user_profile(u)
        add_trip(trip['name'], trip['location'], trip['date'], trip['length'], users)
        print(trip['name'], trip['location'], trip['date'], trip['length'])

    for social in socials:
        add_social(social['name'], social['date'], social['details'], social['location'])
        print(social['name'], social['date'], social['details'], social['location'])

    for kit in kits:
        u = add_user(kit['owner']['is_admin'], kit['owner']['is_member'], kit['owner']['email']
                        , kit['owner']['username'], kit['owner']['password'])
        user = add_user_profile(u)

        add_kit(kit['name'], kit['size'], kit['colour'], kit['brand'], user, kit['type'],
                kit['maintenance_problem'], kit["maintenance"], kit['amount'])
        print(kit['name'], kit['size'], kit['colour'], kit['brand'], kit['type'],
              kit['maintenance_problem'],kit["maintenance"], kit['amount'])


def add_user(is_admin, is_member, email, username, password):
    u = User.objects.get_or_create(is_admin=is_admin, is_member=is_member, email=email, username=username,
                                   password=password)[0]
    u.save()
    return u


def add_user_profile(user):
    up = UserProfile.objects.get_or_create(user=user)[0]
    up.save()
    return up


def add_trip(name, location, date, length, members):
    t = Trip.objects.get_or_create(name=name, location=location, date=date)[
        0]  # because we're calling get or create you don't want information that could create duplicate copies
    t.length = length
    t.members.set(members)
    t.save()
    return t


def add_social(name, date, details, location):
    s = Social.objects.get_or_create(name=name, date=date, details=details, location=location)[0]
    s.save()
    return s


def add_kit(name, size, colour, brand, owner, type, maintenance_problem, maintenance, amount=0):
    k = Kit.objects.get_or_create(name=name, size=size, colour=colour, brand=brand, owner=owner, maintenance=maintenance, type=type)[0]
    if maintenance_problem is not None:
        k.maintenance_problem = maintenance_problem
    k.amount = amount + 1
    k.save()
    return k


if __name__ == '__main__':
    print('Starting canoe club population script...')
    populate()
