# Sports Snaps - API 

Sports Snaps API is a Django-based web application for the website [Sports Snaps](https://sportssnaps-37b7ee6411c9.herokuapp.com/). The website is a social media platform designed for users to share their most liked sporting photos or moments.


# Site Repositories

[Frontend Repository](https://github.com/DeveloperDunne/sports-snaps_frontend)

[API Repository](https://github.com/DeveloperDunne/Sports-Snaps-API)

# Table of contents

- [1. Planning](#planning)
- [2. Admin](#admin)
- [3. Relationships and Endpoints](#relationships-and-endpoints)
- [4. Testing](#testing)
- [5. Languages and Technologies](#languages-and-technologies)
- [6. Installed Packages](#installed-packages)
- [7. Security](#security)
- [8. Setup](#setup)
- [9. Deployment](#deployment)
- [10. Credits](#credits)

# Planning

## Agile Methodology

* All functionality and development of this project were managed using GitHub Projects. This can be found here at [Github Projects](https://github.com/users/DeveloperDunne/projects/6/views/1).

## MoSCoW

![MoSCoW screenshot](./README_Images/admin_images/MoSCoW.webp)

This project used the "MoSCoW" method to classify its features and requirements according to their importance towards a minimum viable product (MVP). "MoSCoW" stands for "Must have, Should have, Could have and Won't have," with each classification aiding in the prioritisation of features. This method makes sure that essential components are tackled in priority order.

# Admin

## Root Admin View

![Root screenshot](./README_Images/admin_images/root-route.webp)

## Admin Panel

![Admin Panel screenshot](./README_Images/admin_images/admin-site.webp)

## Superusers
Superusers have the ability to perform the following via the admin panel:

CRUD Posts
CRUD Comments
CRUD Profiles
CRUD Contacts
CRUD Category
Change Passwords
Change emails


# Relationships and Endpoints

## Profile
- created_at(DateTimeField),
- updated_at(DateTimeField),
- name(CharField),
- email(EmailField),
- content(TextField),
- image(ImageField),
- facebook_link(URLField),
- twitter_link(URLField) and
- instagram_field(URLField)

### Endpoints:
- /profiles/: to list (GET) profiles.
- /profiles/:id/: to show (GET) or update (PUT) a profile.

![profiles screenshot](./README_Images/admin_images/admin-profiles.webp)

## Post
- owner(ForeignKey),
- created_at(DateTimeField),
- updated_at(DateTimeField),
- title(CharField),
- content(TextField),
- image(ImageField),
- image_filter(CharField)
- category(ForeignKey)

### Endpoints:
- /posts/: to list (GET) or create (POST) posts.
- /posts/:id/: to show (GET), update (PUT) or delete (DELETE) a post.

![Posts screenshot](./README_Images/admin_images/admin-posts.webp)

## Comments
- owner(ForeignKey),
- content(TextField),
- created_at(DateTimeField),
- updated_at(DateTimeField)

### Endpoints:
- /comments/: to list (GET) all comments or create (POST) a new comment.
- /comments/:id/: to show (GET) a specific comment, update (PUT) or delete (DELETE) a comment.

## Likes
- post(ForeignKey) and
- created_at(DateTimeField)

### Endpoints:
- /likes/: to list (GET) or create (POST) likes.
- /likes/:id/: to show (GET) or delete (DELETE) a like.

![Likes screenshot](./README_Images/admin_images/admin-likes.webp)

## Followers 
- owner(ForeignKey),
- followed(ForeignKey),
- created_at(DateTimeField)

### Endpoints:
- /followers/: to list (GET) profiles.
- /followers/:id/: to show (GET) or delete (DELETE) a follow.

![Followers screenshot](./README_Images/admin_images/admin-followers.webp)

## Category
- name(CharField)

### Endpoints:
- /category/: to list (GET) categories.

![Categories screenshot](./README_Images/admin_images/admin-categories.webp)

## Contact
- email(EmailField),
- subject(Charfield),
- message(TextField),
- created_at(DateTimeField),
- read(BooleanField),
- admin_response(TextField)

![Contact screenshot](./README_Images/admin_images/admin-contact.webp)


# Testing

Manual Testing for the overall functionality of the API was performed by entering test data in the backend both via Backend-and Front-end. 

Detailed testing documentation can be found here TESTING.MD

# Languages and Technologies

- Django REST Framework (Python Framework - API)
- PostgreSQL from CI

# Installed Packages


The following packages were installed when developing this project: 

To install, the following command was run in the terminal: pip3 install ...

- asgiref==3.8.1
- cloudinary==1.40.0
- dj-database-url==0.5.0
- dj-rest-auth==2.1.9
- Django==5.0.7
- django-allauth==0.50.0
- django-cloudinary-storage==0.3.0
- django-cors-headers==4.4.0
- django-filter==24.2
- djangorestframework==3.15.2
- - djangorestframework-simplejwt==5.3.1
- gunicorn==22.0.0
- oauthlib==3.2.2
- pillow==10.4.0
- psycopg2==2.9.9
- PyJWT==2.8.0
- python3-openid==3.2.0
- requests-oauthlib==2.0.0
- setuptools==68.0.0
- sqlparse==0.5.1

# Security

### env.py File

API keys and databases are stored in the env.py which is not included in version control to prevent exposure.

# Setup

### GitHub

The project was developed using GitHub and coded via tehe IDE GitPod.

- Navigate to: "Repositories" and create "New".
- Mark the following field: ✓ Public
- Select template: "Code-Institute-Org/react-ci-template".
- Add a Repository name then create Repository.

### Terminal Commands

Commits:

- git add . 
- git commit -m "commit message"
- git push

To run server:

- python manage.py runserver 

To make migrations:

- python manage.py makemigrations
- python manage.py migrate <- Applies pending migrations

To add dependencies:

- pip3 freeze --local > requirements.txt <-Runs the req.

Creating a Superuser:

- python manage.py createsuperuser

Starting a new Django project:

- django-admin startproject NAMEOFTHEPROJECT .

Create an app:

- python3 manage.py startapp NAMOFTHEAPP

# Deployment

The website is being hosted and deployed on Heroku:

Navigate to: "Create new app" add a unique name "djangorestframework-api" and select your region. Click "Create App"
Head over to "Settings" tab and apply the respective config VARs
Move to "Deploy" section and select "Github" method"
From here search for the repository name "connect", from the GitHub account.
Hit "Connect" and "Enable Automatic Deploys" to keep the the repository in parallel to Heroku.
Manually "Deploy Main Branch".

## How to Fork

To fork a repository on GitHub, follow these steps:

- Log in to GitHub - or set up a new account.
- Click on the repository name.
- Click the Fork button in the top right corner.

## How to Clone

To clone a repository on GitHub, follow these steps:

- Log in to GitHub - or set up a new account.
- Find or create your repository.
- Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
- Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
- Type 'git clone' into the terminal and paste the link you copied in step 3. Press enter.

# Credits

All credits and acknowledgements have been detailed in the main [Frontend Repo README document](https://github.com/DeveloperDunne/sports-snaps_frontend/blob/main/README.md).
 