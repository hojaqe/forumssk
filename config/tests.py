from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class RegistrationViewTest(TestCase):
    def test_registration_success(self):
        url = reverse('registration')
        response = self.client.post(url, {'username': 'Kalinara', 'password1': '12345', 'password2': '12345'})
        self.assertEqual(response.status_code, 302)

        user = User.objects.get(username='Kalinara')
        self.assertTrue(user.check_password('12345'))

    def test_registration_failure(self):
        url = reverse('registration')
        response = self.client.post(url, {'username': 'Kalinara', 'password1': '12345', 'password2': '12346'})
        self.assertEqual(response.status_code, 200)

        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username='Kalinara')


class LoginViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Kalinara', password='12345')

    def test_login_success(self):
        url = reverse('login')
        response = self.client.post(url, {'username': 'Kalinara', 'password': '12345'})
        self.assertEqual(response.status_code, 302) 

    def test_login_failure(self):
        url = reverse('login')
        response = self.client.post(url, {'username': 'Kalinara', 'password': '12345'})
        self.assertEqual(response.status_code, 200)  


class ChangePasswordViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Kalinara', password='123456')
        self.client.login(username='Kalinara', password='123456')

    def test_change_password_success(self):
        url = reverse('change_password')
        response = self.client.post(url, {'old_password': '123456', 'new_password1': '1234567', 'new_password2': 'n1234567'})
        self.assertEqual(response.status_code, 302)

        self.user.refresh_from_db()
        self.assertTrue(self.user.check_password('1234567'))

    def test_change_password_failure(self):
        url = reverse('change_password')
        response = self.client.post(url, {'old_password': '123456', 'new_password1': '1234567', 'new_password2': '1234567'})
        self.assertEqual(response.status_code, 200) 


class ForgotPasswordViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Kalinara', password='123456')

    def test_forgot_password_success(self):
        url = reverse('forgot_password')
        response = self.client.post(url, {'username': 'Kalinara'})
        self.assertEqual(response.status_code, 302) 

    def test_forgot_password_failure(self):
        url = reverse('forgot_password')
        response = self.client.post(url, {'username': 'Kalinara'})
        self.assertEqual(response.status_code, 200)


# myprojctuser - hoja
# my project - forum
# deploySSK


# sudo ln -s /etc/nginx/sites-available/deploySSK /etc/nginx/sites-enabled

# [Unit]
# Description=gunicorn daemon
# Requires=gunicorn.socket
# After=network.target

# [Service]
# User=sultanhoja228
# Group=www-data
# WorkingDirectory=/home/sultanhoja228/deployssk
# ExecStart=/home/sultanhoja228/deployssk/venv/bin/gunicorn \
#           --access-logfile - \
#           --workers 3 \
#           --bind unix:/run/gunicorn.sock \
#           forum.wsgi:application