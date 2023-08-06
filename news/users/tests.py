from django.test import TestCase
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomeUserChangeForm
# Create your tests here.

class CustomUserTest(TestCase):

    global TEST_USERS
    TEST_USERS = [("test_user_1", "123xyz", 25), 
                  ("test_user_2", "123xyz", 29)]
    

    def setUp(self) -> None:
        for username, password , age in TEST_USERS:
            CustomUser.objects.create(
                username = username, 
                password = password, 
                age = age
            )

        # Create a test user with no age
        CustomUser.objects.create(
            username = "test_user_no_age", 
            password = "123xyz",
            #age = 33 
        )


    def test_custom_user_creation(self):
        test_user_1 = CustomUser.objects.get(id = 1)
        test_user_no_age = CustomUser.objects.get(username = "test_user_no_age")
        self.assertEqual(test_user_1.age, 25, f"Age for test_user_1 in test case \
                         test_custom_user_creation does not match. Expected 25 got {test_user_1.age}")
        self.assertIsNone(test_user_no_age.age, msg = f"test_user with no age attribute returned age of {test_user_no_age.age}") 

    def test_custom_user_creation_form(self):
        form = CustomUserCreationForm(
            data = {
                "username" : "test_user_1", 
                "password" : "123xyz", 
                "age" : 25
            }
        )

        self.assertEqual(form.data.get("username"), "test_user_1")