import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'gucc_inventory_project.settings')

import django
django.setup()
from canoe_club.models import Trip, Kit, Social


def populate():
    members = [
        {
            # list of members
        }
    ]

    trips = [
        {'name': 'Intermediate Weekend',
         'location': 'Inverness',
         'date': '24/03/2023',
         'length': 3,
         'members': '{:}'
         },
        {'name': 'Beginner Day Trip',
         'location': 'The Spean',
         'date': '01/04/2023',
         'length': 1,
         'members': '{:}'
         }
    ]

    socials = [
        {'name': 'St Paddys',
         'date': '17/03/2023',
         'details': 'A big night out meet at 8pm',
         'location': "Bank street"
         },
        {'name': 'Chill Potluck',
         'date': '05/04/2023',
         'details': 'A chill potluck where everyone brings food to share and chill ',
         'location': "Kai's Flat"
         }
    ]

    kits = [
        {'name': 'club_paddle',
         'size': 0,
         'colour': 'red',
         'brand': 'Palm',
         'owner': 'Club',
         'type': 'paddle',
         'maintenance problem': 'N/A',
         'amount': 4,
         'image': 'image'}
    ]

    for trip in trips:
        t = add_trip(trip['name'], trip['location'], trip['date'], trip['length'], trip['members'])
        print(trip['name'], trip['location'], trip['date'], trip['length'], trip['members'])

    for social in socials:
        s = add_social(social['name'], social['date'], social['details'], social['location'])
        print(social['name'], social['date'], social['details'], social['location'])

    for kit in kits:
        k = add_kit(kit['name'], kit['size'], kit['colour'], kit['brand'], kit['owner'], kit['type'],
                    kit['maintenance_problem'], kit['image'], kit['amount'])
        print(kit['name'], kit['size'], kit['colour'], kit['brand'], kit['owner'], kit['type'],
                    kit['maintenance_problem'], kit['image'], kit['amount'])


def add_trip(name, location, date, length, members):
    t = Trip.objects.get_or_create(name=name, location=location)[
        0]  # because we're calling get or create you don't want information that could create duplicate copies
    t.date = date
    t.length = length
    t.members = members
    t.save()
    return t


def add_social(name, date, details, location):
    s = Social.objects.get_or_create(name=name)[0]
    s.date = date
    s.details = details
    s.location = location
    s.save()
    return s


def add_kit(name, size, colour, brand, owner, type, maintenance_problem, image, amount=0):
    k = Kit.objects.get_or_create(name=name, size=size, colour=colour, brand=brand, owner=owner, type=type)[0]
    if maintenance_problem is not None:
        k.maintenance_problem = maintenance_problem
    k.amount = amount + 1
    k.image = image
    k.save()
    return k


if __name__ == '__main__':
    print('Starting canoe population script...')
    populate()
