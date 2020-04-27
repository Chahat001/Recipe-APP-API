from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):


    def setUp(self):  # function that runs before every test we runs
        """ Creating a test client , create a new user, make sure user is logged in , create a non-admin user to"""
        """ check if they appear on admin page"""
        self.client = Client()      # make client variable accessible in other testcases
        self.admin_user = get_user_model().objects.create_superuser(
            email = 'admin@gmail.com',
            password = ' password123'
        )

        self.client.force_login(self.admin_user)  # login the the user
        self.user = get_user_model().objects.create_user(
            email = 'Simple@gmail.com',
            password = 'password',
            name = 'Test User FullName'
        )

        """ Admin alows seeing users, edit each user detail, and create new user but it have functionality for custom"""
        """ model only not our custom model which we have specified in admin.py to register it with"""

    def test_users_listed(self):
        """ Test that users are listed on user Page"""
        url = reverse('admin:core_user_changelist')  #returns the url to the user list on the admin page,
        res = self.client.get(url)  #http get request on the url retunred

        self.assertContains(res, self.user.name)  # also checks if http request returns 200
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """ Test That the user edit page works"""
        url = reverse('admin:core_user_change', args = [self.user.id])
        """ url = admin/core/user/1"""
        res = self.client.get(url)
        """ check if page renders correctly """
        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """ Test that the create user page works """
        url = reverse('admin:core_user_add') # url = admin/core/user/add
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
