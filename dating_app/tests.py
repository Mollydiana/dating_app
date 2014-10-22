from dating_app.models import Dater
from time import sleep
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.test import TestCase, LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from forms import EmailUserCreationForm
from test_utils import run_pyflakes_for_package, run_pep8_for_package


class FormTestCase(TestCase):
    def test_clean_username_exception(self):
        # Create a player so that this username we're testing is already taken
        Dater.objects.create_user(username='test-user')

        # set up the form for testing
        form = EmailUserCreationForm()
        form.cleaned_data = {'username': 'test-user'}

        # use a context manager to watch for the validation error being raised
        with self.assertRaises(ValidationError):
            form.clean_username()

    def test_clean_username(self):
        # Create a player so that this username we're testing is already taken
        Dater.objects.create_user(username='test-user2')

        # set up the form for testing
        form = EmailUserCreationForm()
        form.cleaned_data = {'username': 'test-user'}

        # use a context manager to watch for the validation error being raised
        form.clean_username()

    # def test_register_sends_email(self):
    #     form = EmailUserCreationForm()
    #     form.cleaned_data = {
    #         'username': 'test',
    #         'email': 'test@test.com',
    #         'password1': 'test-pw',
    #         'password2': 'test-pw',
    #     }
    #     form.save()
    #     # Check there is an email to send
    #     self.assertEqual(len(mail.outbox), 0)
    #     # Check the subject is what we expect
    #     self.assertEqual(mail.outbox[0].subject, 'Welcome!')


class SyntaxTest(TestCase):

    def test_syntax(self):

        """
        Run pyflakes/pep8 across the code base to check for potential errors.
        """
        packages = ['dating_app']
        warnings = []
        # Eventually should use flake8 instead so we can ignore specific lines via a comment
        for package in packages:
            warnings.extend(run_pyflakes_for_package(package, extra_ignore=("_settings",)))
            warnings.extend(run_pep8_for_package(package, extra_ignore=("_settings",)))
        if warnings:
            self.fail("{0} Syntax warnings!\n\n{1}".format(len(warnings), "\n".join(warnings)))


class ViewTestCase(TestCase):
    def setUp(self):
        pass

    def test_register_page(self):
        username = 'new-user'
        data = {
            'username': username,
            'email': 'test@test.com',
            'password1': 'test',
            'password2': 'test'
        }
        response = self.client.post(reverse('register'), data)

        # Check this user was created in the database
        self.assertTrue(Dater.objects.filter(username=username).exists())

        # Check it's a redirect to the profile page
        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertTrue(response.get('location').endswith(reverse('home')))

    def test_profile_page(self):
        # Create user and log them in
        password = 'passsword'
        user = Dater.objects.create_user(username='test-user', email='test@test.com', password=password)
        self.client.login(username=user.username, password=password)


class SeleniumTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(SeleniumTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(SeleniumTests, cls).tearDownClass()

    def test_admin_login(self):
        # Create a superuser
        Dater.objects.create_superuser('superuser', 'superuser@test.com', 'mypassword')

        # let's open the admin login page
        self.selenium.get("{}{}".format(self.live_server_url, reverse('admin:index')))
        # let's fill out the form with our superuser's username and password
        self.selenium.find_element_by_name('username').send_keys('superuser')
        sleep(.5)
        password_input = self.selenium.find_element_by_name('password')
        sleep(.5)
        password_input.send_keys('mypassword')
        sleep(.5)
        # Submit the form
        password_input.send_keys(Keys.RETURN)
        # sleep for half a second to let the page load
        sleep(.5)

        # We check to see if 'Site administration' is now on the page, this means we logged in successfully
        body = self.selenium.find_element_by_tag_name('body')
        sleep(.5)
        self.assertIn('Site administration', body.text)

    def admin_login(self):
        # Create a superuser
        Dater.objects.create_superuser('superuser', 'superuser@test.com', 'mypassword')
        sleep(.5)
        # let's open the admin login page
        self.selenium.get("{}{}".format(self.live_server_url, reverse('admin:index')))

        # let's fill out the form with our superuser's username and password
        self.selenium.find_element_by_name('username').send_keys('superuser')
        sleep(.5)
        password_input = self.selenium.find_element_by_name('password')
        sleep(.5)
        password_input.send_keys('mypassword')
        sleep(.5)
        # Submit the form
        password_input.send_keys(Keys.RETURN)
        sleep(.5)

    def test_admin_create_card(self):
        self.admin_login()
        sleep(.5)

        # We can check that our Card model is registered with the admin and we can click on it
        # Get the 2nd one, since the first is the header
        self.selenium.find_elements_by_link_text('Users')[0].click()
        sleep(.5)

        # # Let's click to add a new card
        # self.selenium.find_element_by_link_text('Add user').click()
        # sleep(.5)
        #
        # # Let's fill out the card form
        # self.selenium.find_element_by_name('rank').send_keys("ace")
        # sleep(.5)
        # suit_dropdown = self.selenium.find_element_by_name('suit')
        # sleep(.5)
        # for option in suit_dropdown.find_elements_by_tag_name('option'):
        #     if option.text == "heart":
        #         option.click()
        #         sleep(.5)
        #
        # # Click save to create the new card
        # self.selenium.find_element_by_css_selector("input[value='Save']").click()
        #
        # sleep(.5)
        #
        # # Check to see we get the card was added success message
        # body = self.selenium.find_element_by_tag_name('body')
        # self.assertIn('The card "ace of hearts" was added successfully', body.text)

    def test_app_login(self):
        # Create a superuser
        Dater.objects.create_user('user', 'user@test.com', 'apassword')
        sleep(.5)
        # let's open the admin login page
        self.selenium.get("{}{}".format(self.live_server_url, reverse('login')))

        # let's fill out the form with our superuser's username and password
        self.selenium.find_element_by_name('username').send_keys('user')
        sleep(.5)
        password_input = self.selenium.find_element_by_name('password')
        sleep(.5)
        password_input.send_keys('apassword')
        sleep(.5)
        # Submit the form
        password_input.send_keys(Keys.RETURN)
        sleep(.5)
