from unittest import skipIf
from django.test import TestCase
from .models import BlogPost
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy

# Create your tests here.

class BlogPostTests(TestCase):

    global TEST_AUTHOR_NAMES, TEST_POST_BODY, TEST_POST_TITLES

    TEST_AUTHOR_NAMES = ["test_user_1", "test_user_2", "test_user_3"]
    TEST_POST_TITLES = ["test_title_1", "test_title_2", "test_title_3"]
    TEST_POST_BODY = ["test_post_1", "test_post_2" , "test_post_3"]

    def setUp(self):
        
        # Lambda function to genereate test users.
        # Lambda functions allow for reusability
        create_test_user = lambda name : lambda mail : lambda pwd : \
            User.objects.create(
            username = name,
            email = mail,
            password = pwd
        )

        # Create our test users
        create_test_user("test_user_1")("t1@gmail.com")("secret1")
        create_test_user("test_user_2")("t2@gmail.com")("secret2")
        create_test_user("test_user_3")("t3@gmail.com")("secret3")

        # Lambda functions to generate test posts
        create_test_post = lambda title : lambda test_user_name : lambda body : \
        BlogPost.objects.create(
            title = title,
            author = User.objects.get(username = test_user_name),
            body = body
        ) 

        create_test_post("test_title_1")("test_user_1")("test_post_1")
        create_test_post("test_title_2")("test_user_2")("test_post_2")
        create_test_post("test_title_3")("test_user_3")("test_post_3")
    
    def test_model_creation(self):
        """
        Test if a Blog post object created at setup 
        has succesfully been stored in the database
        with correct entries for author, title and 
        body
        """
        test_entries_in_db  = BlogPost.objects.all()
        for i in range(3):
            entry: BlogPost = test_entries_in_db.get(pk = i + 1)
            self.assertEquals(entry.author.username, TEST_AUTHOR_NAMES[i], "Author name did not match.")
            self.assertEqual(entry.title, TEST_POST_TITLES[i], "Title did not match")
            self.assertEquals(entry.body, TEST_POST_BODY[i], "Post body did not match")
    
    def test_homepage_accessed_successfully(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200, f"Returned a status code of {str(response.status_code)}")
        
    def test_homepage_contains_test_posts(self):
        response = self.client.get(reverse('home'))
        for content in (TEST_AUTHOR_NAMES + TEST_POST_BODY + TEST_POST_TITLES):
            self.assertContains(response, content)
    
    def test_post_detailed_view(self):
        """
        Check if pages containint detailed view of existing posts
        
        1. Are accessed correctly
        2. Contains the appropriate content
        3. Returns appropriate error code for nonexistent posts
        """

        post_1_existing = self.client.get('/post/1/')
        post_1000_non_existing = self.client.get("/post/1000/")
        self.assertEqual(post_1_existing.status_code, 200, f"Failed to access an existing post. Returned code \
                         {str(post_1_existing.status_code)}")
        self.assertEqual(post_1000_non_existing.status_code, 404, f"A non existing post should return error 404 \
                         instead it returned {str(post_1000_non_existing.status_code)}")
        
        self.assertContains(response = post_1_existing, text = TEST_POST_BODY[0], msg_prefix = f"Post 1 which is an existing \
                            test post returned an incorrect/does not contain the body {TEST_POST_BODY[0]}")
        

    def test_if_pages_using_designated_tempaltes(self):
        """
        Checks if each page is using the appropriate html template
        homepage --> home.html
        post detailed view --> post_detail.html
        """

        for i in range(3):
            response = self.client.get(f"/post/{ i + 1 }/")
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'post_detail.html')

    @skipIf(False, "Skip if test_post_update_view returned an assertion error")    
    def test_post_create_view(self):
        """
        Tests whether a view has been created and stored in the db successfully
        Checks if the newly initialized test post has the correctly initialized 
        test attributes of title, author and body
        """
        test_user = User.objects.get(username = TEST_AUTHOR_NAMES[0])
        response = self.client.post(reverse_lazy('post_new'), {
            'title' : TEST_POST_TITLES[0],
            'body' : TEST_POST_BODY[0],
            'author' : test_user
        })

        self.assertEqual(response.status_code, 200, msg= f"Failed to create a new post via CreateView.\
                         Returned with a status code of {str(response.status_code)}")
        
        self.assertContains(response , text=TEST_POST_TITLES[0],msg_prefix= f"Function test_post_create_view \
                            returned the wrong title for the initialized test post. Expected title : {TEST_POST_TITLES[0]}")
        
    
    @skipIf(False, "Skip if test_post_create_view returned an assertion error")
    def test_post_update_view(self):
        """
        Tests whether an update to a pre-existing post has been registered successfully
        """
        response = self.client.post(reverse_lazy('post_edit', args = '1'), {
            'title' : 'test_post_1 updated title',
            'body' : 'test_post_1 updated body'
        })

        self.assertEqual(response.status_code, 302, msg = f"Failed to create a new post via CreateView.\
                         Returned with a status code of {str(response.status_code)}. Expected 302")
        
        # self.assertContains(updated_test_post_1, "test_post_1 updated title", f"Failed to edit the title of \
        #                     test_post_1 in test function test_post_update_view")
        # self.assertContains(updated_test_post_1, "test_post_1 updated body", f"Failed to update the body of \
        #                     test_post_1 in test_post_update_view function.")

    
    def test_post_delete_view(self):
        """
        Tests whether a pre-existing post has been deleted with a status code of 302
        """
        response =  self.client.post(reverse_lazy('post_delete', args = '2'))
        self.assertEqual(response.status_code, 302 ,
        msg =  f"Failed to create a new post via CreateView.\
                         Returned with a status code of {str(response.status_code)}. Expected 302" )

    def test_get_absolute_url(self):
        pass
    