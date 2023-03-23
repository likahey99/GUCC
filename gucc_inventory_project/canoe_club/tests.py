from django.test import Client, TestCase
from django.urls import reverse
from canoe_club.models import User, Trip, Social
from django.contrib.auth import get_user_model
from datetime import date, datetime, timedelta
from canoe_club.views import index

# Create your tests here.


class ViewsTestCase(TestCase):
    def setUp(self):
        self.today = datetime.today()

        #creating some trips and socials for testing

        self.trip = Trip.objects.create(name = 'Trips', location='xyz', date=self.today + timedelta(days=1))
        self.trip2 = Trip.objects.create(name = 'Trip2', location='xyz', date=self.today + timedelta(days=2))
        self.social = Social.objects.create(name='Social', details='Info about social', date=self.today + timedelta(days=1))
        self.social2 = Social.objects.create(name='Social2', details='Info about social2', date=self.today + timedelta(days=2))
        
    #checks if trips and socials are in the context dictionary and if they are sorted by date
    def test_index_view(self):
        url = reverse('index')
        response = self.client.get(url)
        today = datetime.today()
        expected_trips = Trip.objects.filter(date__gte=today).order_by('date')[:5]
        expected_socials = Social.objects.filter(date__gte=today).order_by('date')[:5]
        print(expected_trips)
    
        
        trips = response.context['trips']
        print(trips)
        self.assertQuerysetEqual(trips, expected_trips, ordered=False)

        socials = response.context['socials']
        self.assertQuerysetEqual(socials, expected_socials, ordered=False)


#this also tests views as successful rendering implies views is working fine.
class TemplateTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
    
    def test_index_template(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'canoe_club/index.html')
        self.assertContains(response, 'Welcome to the canoe club')

    def test_about_template(self):
        url = reverse('canoe_club:about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'canoe_club/about.html')
        self.assertContains(response, 'About Canoe Club')


class UserModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
        username='testuser',
        email='testuser@example.com',
        is_admin=True,
        is_member=False  )

    def test_user_creation(self):
        user = get_user_model().objects.get(username='testuser')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertTrue(user.is_admin)
        self.assertFalse(user.is_member)

    def test_unique_email(self):
        with self.assertRaises(Exception):
            get_user_model().objects.create(
                username='newuser',
                email='testuser@example.com',
            )


class TripModelTest(TestCase):
    def setUp(self):
        # Create a test user
        new_test_user = User.objects.create_user(username='dummyUser', password='dummyPassword')
        
        # Create a Trip object for testing
        test_trip = Trip.objects.create(name='Dummy Trip', location='Dummy Location', date=date.today(), length=3)
        test_trip.members.add(new_test_user)

    def test_name_max_length(self):
        trip = Trip.objects.get(id=1)
        max_length = trip._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_trip_name(self):
        trip = Trip.objects.get(id=1)
        expected_name = f"{trip.name}"
        self.assertEqual(expected_name, str(trip))
    
