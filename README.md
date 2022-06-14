# Final project (AQA Engineer courses)
    For the implementation of 1-4 test-cases download and install the django app: git clone https://github.com/thejungwon/docker-webapp-django.git
    Open the app at localhost:8000
    For the implementation of 5-6 test-cases use URL: https://petstore.swagger.io/#/

# Tasks:
    It is necessary to create a framework that will check test cases.
    Tests must be written with pytest.
    Tests must be run in Jenkins with a report's formation in Allure.

# Test-case 1:
1. Create a group in db
2. Open the site
3. Log in to admin
4. Check the created group appears on the site
    
# Test-case 2: 
1. Open the site
2. Log in to admin
3. Create a user
4. Add the user to the group
5. Check the user is added to the group in db
    
# Test-case 3:
1. Open the site
2. Log in to admin
3. Create a user
4. Check the user is in db
5. Log out
6. Log in with new user
7. Check log in is successful
    
# Test-case 4:
1. Open the site
2. Log in to admin
3. Delete the first generated picture
4. Go back to the main site's page
5. Check there is no first picture on the main page
    
# Test-case 5 (API):
1. Create a user
2. Log in with the user
3. Get info of the user
4. Log out
5. Delete the user
    
# Test-case 6 (API):
1. Add a new pet to the store
2. Check the pet is added
3. Update the pet's name
4. Check the name is updated
