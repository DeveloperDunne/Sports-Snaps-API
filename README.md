# Sports Snaps - API 

Sports Snaps API is a Django-based web application for the website [Sports Snaps](https://). The website is a social media platform designed for users to share their most liked sporting photos or moments.


#Site Repositories

[Frontend Repository](https://github.com/)

[API Repository](https://github.com/)

## Table of contents

- [1. Planning](#)
- [2. Relationships & Endpoints](#)
- [3. Admin](#)
- [4. Testing](#)
- [5. Installed Packages](#)
- [6. Security](#)
- [7. Setup](#)
- [8. Deployment](#)
- [9. Credits](#)

## Planning

### Agile Methodology

* All functionality and development of this project were managed using GitHub Projects. This can be found here [Github Projects](https://github.com/)

### MoSCoW

![MoSCoW screenshot](./README_Images/)

This project used the "MoSCoW" method to classify its features and requirements according to their importance towards a minimum viable product (MVP). "MoSCoW" stands for "Must have, Should have, Could have and Won't have," with each classification aiding in the prioritisation of features. This method makes sure that essential components are tackled in priority order.

## Relationships & Endpoints

### Profile
created_at(DateTimeField),
updated_at(DateTimeField),
name(CharField),
email(EmailField),
content(TextField),
image(ImageField),
facebook_link(URLField),
twitter_link(URLField) and
instagram_field(URLField)

### API Endpoints:
/profiles/: to list (GET) profiles.
/profiles/:id/: to show (GET) or update (PUT) a profile.

### Post
owner(ForeignKey),
created_at(DateTimeField),
updated_at(DateTimeField),
title(CharField),
content(TextField),
image(ImageField),
image_filter(CharField)
category(ForeignKey)

### API Endpoints:
/posts/: to list (GET) or create (POST) posts.
/posts/:id/: to show (GET), update (PUT) or delete (DELETE) a post.

### Comments
inheriting the post(ForeignKey) and owner(ForeignKey),
it displays the content(TextField),
created_at(DateTimeField),
updated_at(DateTimeField)

### API Endpoints:
/comments/: to list (GET) all comments or create (POST) a new comment.
/comments/:id/: to show (GET) a specific comment, update (PUT) or delete (DELETE) a comment.

### Likes
post(ForeignKey) and
created_at(DateTimeField)

### API Endpoints:
/likes/: to list (GET) or create (POST) likes.
/likes/:id/: to show (GET) or delete (DELETE) a like.

### Followers defined by owner(ForeignKey),
followed(ForeignKey),
created_at(DateTimeField)

### API Endpoints:
/followers/: to list (GET) profiles.
/followers/:id/: to show (GET) or delete (DELETE) a follow.

### Category
name(CharField)

### API Endpoints:
/category/: to list (GET) categories.

### Contact
email(EmailField),
subject(Charfield),
message(TextField),
created_at(DateTimeField),
read(BooleanField),
admin_response(TextField

## Admin

### Admin Panel

screenshot

### Deployed Admin View

screenshot

### Superusers
As a Superuser one has the ability to perform the following via the admin panel:

CRUD Posts
CRUD Comments
CRUD Profiles
CRUD Contacts
CRUD Category
Change Passwords
Change emails


## Testing

Manual Testing for the overall functionality of the API was performed by entering test data in the backend both via Backend-and Front-end. 

Detailed testing documentation can be found here TESTING.MD

##Languages

Django REST Framework (Python Framework - API)

## Installed Packages


The following packages were installed when developing this project: 

To install, the following command was run in the terminal: pip3 install ...

cloudinary==1.40.0
dj-database-url==0.5.0
dj-rest-auth==2.1.9 
Django==4.2
django-allauth==0.44.0
django-cloudinary-storage==0.3.0
django-cors-headers==3.7.0
django-filter==2.4.0
djangorestframework==3.15.1
djangorestframework-simplejwt==5.3.
gunicorn==22.0.0
Pillow==10.3.0
psycopg2==2.9.9
PyJWT==2.8.0

## Security

### env.py File

API keys and databases are stored in the env.py which is not included in version control to prevent exposure.

## Setup

### Setup

The project was developed using GitHub and GitPod.

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

## Deployment

The website is being hosted and deployed on Heroku:

Navigate to: "Create new app" add a unique name "djangorestframework-api" and select your region. Click "Create App"
Head over to "Settings" tab and apply the respective config VARs
Move to "Deploy" section and select "Github" method"
From here search for the repository name "connect", from the GitHub account.
Hit "Connect" and "Enable Automatic Deploys" to keep the the repository in parallel to Heroku.
Manually "Deploy Main Branch".

### How to Fork

To fork a repository on GitHub, follow these steps:

- Log in to GitHub - or set up a new account.
- Click on the repository name.
- Click the Fork button in the top right corner.

### How to Clone

To clone a repository on GitHub, follow these steps:

- Log in to GitHub - or set up a new account.
- Find or create your repository.
- Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
- Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
- Type 'git clone' into the terminal and paste the link you copied in step 3. Press enter.

## Credits

All credits and acknowledgements have been detailed in the main [Frontend Repo README document](https://github.com/).
 