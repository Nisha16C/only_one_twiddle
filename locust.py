from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # Set the time between consecutive requests

    @task
    def visit_website(self):
        self.client.get("/")


# class action(HttpUser):
#     wait_time = between(1, 3)  # Set the time between consecutive requests

#     @task
#     def view_notifications(self):
#         # Define the HTTP request to test the notifications endpoint
#         self.client.get("/notifications/")


# class c_msg(HttpUser):
#     wait_time = between(1, 3)  # Set the time between consecutive requests

#     @task
#     def send_message(self):
#         # Generate a random user ID within the desired range
#         user_id = 2
#         # Define the HTTP request to test the send_message_view
#         response = self.client.get(f"/c_msg/send-message/{user_id}/")
        
    
# class chat(HttpUser):
#     wait_time = between(1, 3) 

#     @task
#     def view_user_list(self):
#         self.client.get("/chat/user-list/")

#     @task
#     def send_random_message(self):
#         # Generate a random user ID within the desired range
#         user_id = 2 
#         # Send a GET request to the send_message URL with a random user ID
#         self.client.get(f"/chat/send-message/{user_id}/")


# class pages(HttpUser):
#     wait_time = between(1, 3)  # Set the time between consecutive requests

#     @task
#     def view_home_redirect(self):
#         self.client.get("/")

#     @task
#     def view_homepage(self):
#         self.client.get("/home/")

#     @task
#     def view_about(self):
#         self.client.get("/about/")



# class profiles(HttpUser):
#     wait_time = between(1, 3)  # Set the time between consecutive requests

#     @task
#     def edit_profile(self):
#         username = 'advance'
#         self.client.get("/my/edit_profile/")


#     @task
#     def view_edit_profile(self):
#         username = 'Ak'
#         self.client.get(f"/my/{username}/")

#     @task
#     def view_following(self):
#         # Replace 'example_username' with a valid username from your application
#         username = 'Nisha16C'
#         self.client.get(f"/my/{username}/following/")

#     @task
#     def view_followers(self):
#         # Replace 'example_username' with a valid username from your application
#         username = 'advance'
#         self.client.get(f"/my/{username}/followers/")


# class config(HttpUser):
#     wait_time = between(1, 3)

#     @task
#     def login(self):
#         self.client.get("/accounts/login/")

#     @task
#     def view_email_settings(self):
#         self.client.get("/accounts/email/")

#     @task
#     def set_password(self):
#         self.client.get("/accounts/password/set/")

#     @task
#     def logout(self):
#         self.client.get("/accounts/logout/")

#     @task
#     def view_compose_tweet(self):
#         self.client.get("/compose/search/")

#     @task
#     def compose_message(self):
#         user_id = 2
#         self.client.get(f"/compose/{user_id}/")
