import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'gucc_inventory_project.settings')

import django

django.setup()
from canoe_club.models import Trip, Kit, Social


def populate():
    trips = [
        {'name': 'name',
         'location': 'location',
         'date': '05/03/2023',
         'length': 2,
         'members': '{:}'
         },
        {'name': 'name2',
         'location': 'location2',
         'date': '06/03/2023',
         'length': 3,
         'members': '{:}'
         }
    ]

    socials = [
        {'name': 'name',
         'date': 'date',
         'details': 'details',
         'location': 'location'
         }
    ]

    kit = [
        {'name': 'name',
         'size': 0,
         'colour': 'red',
         'brand': 'brand',
         'owner': 'owner',
         'type': 'type',
         'maintenance problem': 'maintenance problem'}
    ]

    for trip, trip_data in trips.items():
        t = add_trip(name=trip_data['name'], location=trip_data['location'], date=trip_data['date'],
                     members=trip_data['members'])


def add_trip(name, location, date, length, members):
    t = Trip.objects.get_or_create(name=name, location=location)[0]  # because we're calling get or create you don't want information that could create duplicae copies
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


def add_kit(name, size, colour, brand, owner, type, maintenanceProblem):
    k = Kit.objects.get_or_create(name=name, size=size, colour=colour, brand=brand, owner=owner, type=type)
    k.maintenanceProblem = maintenanceProblem
    k.save()
    return k


if __name__ == '__main__':
    print('Starting Canoe population script...')
    populate()
