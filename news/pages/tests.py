from django.test import SimpleTestCase, TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class PagesTests(SimpleTestCase):

    def test_get_home_page_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200, \
        msg = f"Could not reach homepage. Returned a status code of {str(response.status_code)}")

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200, \
                         msg = f"Could not invoke home page using view function returned a status code of \
                            {str(response.status_code)}")
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200, \
        msg = f"Could not reach homepage. Returned a status code of {str(response.status_code)}")
        self.assertTemplateUsed(response, 'home.html')


class SignupPageTests(TestCase):
    global USERNAME, EMAIL, NO_OF_TEST_OBJECTS
    USERNAME = "TESTUSER"
    EMAIL = "testuser@gmail.com"
    NO_OF_TEST_OBJECTS = 1

    def test_sign_up_page_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200, \
        msg = f"Could not direct to sign up page returned code {str(response.status_code)}")
    
    def test_sign_up_page_view_function(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200, \
        msg = f"View function failed to redirect to sign up page. Returned status code {str(response.status_code)}")

    def test_sign_up(self):
        
        # Store NO_OF_TEST_OBJECTS object in the test database
        for _ in range(NO_OF_TEST_OBJECTS): 
            get_user_model().objects.create_user(USERNAME, EMAIL)

        # Check the number of user objects created (Should be 1)
        number_of_test_objects_got =  get_user_model().objects.all().count()
        self.assertEqual(
            number_of_test_objects_got, 
            NO_OF_TEST_OBJECTS, 
            msg = f"test_sign_up returned an incorrect number of objects initialized \
            expected {str(NO_OF_TEST_OBJECTS)} found {number_of_test_objects_got}"
        )

        # get test object with pk = 1 and check if the username and email matches
        test_object_1 = get_user_model().objects.get(id = 1)
        self.assertEqual(
            test_object_1.username, 
            USERNAME, 
            msg = f"Username for test_user_1 does not match assigned username during creation \
                expected {USERNAME} but got {test_object_1.username}"
        )

        self.assertEqual(
        test_object_1.email, 
        EMAIL, 
        msg = f"Email for test_user_1 does not match assigned username during creation \
            expected {EMAIL} but got {test_object_1.email}"
        )

