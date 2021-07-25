# Maisigh.ie

## Code Institute MS4 Project in Full Stack Frameworks
The brief was to build a full-stack site based around business logic used to control a centrally-owned dataset. The requirements included the set up of an authentication mechanism and to provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

# Contents

1. [Project Overview](#project-overview)
2. [UX](#ux)
3. [Features](#features)
4. [Information Architecture](#information-architecture)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)



# Project Overview

## [Maisigh.ie Ecommerce App](http://maisigh-ms4.herokuapp.com)


![Am I Responsive Image](https://res.cloudinary.com/nclerkin/image/upload/v1626972992/amiresponsive_wvj4nm.png "Am I Responsive Image") 

[View website](http://maisigh-ms4.herokuapp.com) 
 
[Maisigh.ie](http://maisigh-ms4.herokuapp.com) is an Ecommerce site that allows users to locate sustainable, Irish jewellery. For any non-native Irish speakers who may be slightly confused re the website name, 'maisigh' (pronounced mosh-she) is a Gaeilge word meaning 'to decorate, to accessorise or beautify'! 

Maisigh knows that simply having a good product is no longer enough to win a customer’s heart. They now want more than just quality, and demand products that align with their personal values. 
In the face of climate change, those of us who care enough are already considering the consequences of our shopping habits. Enter Maisigh. Maisigh is fully committed to providing Irish handcrafted jewellery with minimal impact on the environment. Customers will adore the selection of fashion-forward, ethically-sourced products that they will fall in love with.

My own goals as a developer creating this project were to: 
- Develop a Ecommerce platform that enables the commercial process of buying and selling online. For customers, this would involve a search feature that allows users to locate desired products, a cart feature that lets them manage their order and a payment feature that allow them to purchase their items securely. For employees, this would allow admin users to add, update and delete product and blog content when required. 
- Create an app that is highly accessible, responsive and simplistic in design.
- Create the backend code and frontend forms allowing admin users to carry out CRUD operations.
- Create the backend and frontend functionality for users to locate products based on the item's fields providing full search functionality on the site.
- Provide these search results in a manner that is visually appealing and user-friendly.

[^ Back To Top ](#contents)

# UX


## Goals

### External user’s goal:

- Purchase desired items by a secure means.
- Easily find inspiration for an accessory or locate a specific jewellery piece based on type, price, alphabetically, rating or from a personal wish list. 
- Share desired items or purchases with social following or with friends directly.
- Have an enjoyable experience on primary visit as well as future visits.


### Site owner's goal:
- Provide a professional, accessible and secure ecommerce site where users can find desired items.
- Promote handcrafted, fashionable and sustainable Irish jewellery online.
- Earn profit by making a selection of handcrafted, sustainable Irish jewellery available to users. 
- Provide an enjoyable experience for users to encourage them to return to the site by featuring sitewide intuitive prompts. 
- Expand the Maisigh brand and customer base.


## User Stories

### External Users

As a new user, I would like to:
- View a visually clean and appealing homepage so that I can instantly understand the purpose of the site and navigate its offering easily.
- Access the site from any mobile, tablet or desktop devices so that I can have an equally enjoyable experience regardless of the selected device/platform.
- View content without the requirement to register so that I can quickly locate a specific jewellery piece.
- Browse and filter jewellery by product type, rating, name or price so that I can easily find inspiration for a jewellery piece.
- View a list of items by product type/name/details keyword search criteria so that I can quickly locate a specific jewellery piece.
- Learn more about where the products come from so that I can trust that I'm purchasing ethically-sourced products supporting the environment.
- View more specific product information about a particular jewellery piecesuch as materials used, dimensions etc.
- View the total cost of a potential order containing multiple products.
- Register a profile easily so that I can store address and billing information to streamline order process on future visits.

As a returning user, I would like to:
- Log in and out without encountering issues so that I can have an enjoyable user experience.
- View my account so that I can review previous orders for product info or shipping status for current orders.
- Edit my personal details on my account so that I can update info such as shipping info if my details have changed.
- Save a wish list of desired products to my account so that I can possibly purchase the item in the future when I can afford the item.
- Have the ability to contact the company so that I can ask a question regarding a product or purchase.
- Receive discounts on future orders so that I am incentivised to remain loyal to the brand.


### Business/Admin Users

As a business/admin user, I would like to have access to all of the above as well as:

- The ability to view, add, edit or remove product categories so that I can keep the categories relevant to what users are searching for.
- The ability to view, add, edit or remove products so that I can review and reflect the current stock levels and product information.
- The ability to view, add, edit or remove blog articles so that I can keep the content relevant to the customer's interests that they will enjoy.
- Ensure intuitive text is present so that I can provide an enjoyable user experience when users interact with the content or features.
- View the Maisigh logo in as many locations on the website so that I can create awareness for the brand.
- Offer a discount to customers so that I can gain repeat customers for the brand. 
- View analytics/reports for the checkout process so that I can highlight and fix any potential cart abandonment issues relating to the design and make necessary improvements.  


## Design

![IMAGE](https://res.cloudinary.com/nclerkin/image/upload/v1627190869/banner.2PNG_fg3oiw.png "IMAGE")

### Typography
I wanted to use [Montserrat](https://fonts.google.com/specimen/Montserrat#about) for the headings and [Open Sans](https://fonts.google.com/specimen/Open+Sans/#about) as a supporting body font to achieve the desired clean-cut, fashion-forward brand image.

### Icons
Font Awesome icons have been used for this project.

### Color Scheme
The Maisigh brand monochrome colour scheme was implemented along with pops of natural fashion blush, sea blue and sage green to reflect the Irish and environmentally-friendly green products represented throughout the site.
I wanted to keep the colour palette simplistic and clean to allow for the imagery from the accessories to stand out and inject the site with colour.
However, the colour red is used for error messages or promotion content sitewide to captivate the user's attention.

I ended up creating and using the below palette once it had passed rigorous Accessibility testing in **A11y's Color Contrast Accessibility Validator**. 

![Maisigh Color Palette](https://res.cloudinary.com/nclerkin/image/upload/v1624755385/maisigh-color-palette_m9zkcd.png "Maisigh Color Palette")


## Wireframes

This folder contains [wireframes](static/wireframes.pdf "Maisigh Wireframes") including homepage, category, individual product and checkout pages designed at the beginning of the project for desktop, tablet and mobile devices. I have also included the projected [sitemap](https://res.cloudinary.com/nclerkin/image/upload/v1625089596/sitemap_qccb7z.png "Maisigh Sitemap") and data [schema](https://res.cloudinary.com/nclerkin/image/upload/v1625089596/schema_odygsg.png "Maisigh Schema").
**Please note the finalised project contains slight variations to the original wireframes**

[^ Back To Top ](#contents)

# Features
![IMAGE](https://res.cloudinary.com/nclerkin/image/upload/v1627190831/fix-6.2_nowqyc.png "IMAGE")
# Features


## Existing Features
- A clean, simplistic responsive website.
- Clear, sticky navigation if excessive scrolling is required so the nav is always available to the user. Breadcrumbs have been also implemented to reming the user view where they are and easily jump back to where they came from.
- Monochrome palette to allow for jewellery and blog articles to focus and capture the user’s attention.
- Carousel hitting the three main user stories, the 'about us' feature with the text 'sustainable Irish jewellery' with a CTA inviting users to instantly see what the website's purpose', the 'inspiration' feature which aims to entice users to browse the full collection and the third feature capturing the user's attention with the CTA displaying the action of obtaining freebies if the user helps with brand promotion.
- ‘Trending’ section of jewellery on the homepage for inspiration.
- Footer with blog contact us and social media links and brand footer with the main brand features.
- Pages for ‘Collection’ and individual pre-filtered categories which can be further filtered by price, rating and alphabetically.
- Search functionality that pulls from the data in the product description and name.
- Individual product page containing a short description with relevant product information, image, price, rating, quantity selector, add to wishlist CTA, option for users to leave a review for a product or read reviews that have been left my past customers.
- Simple user-friendly register & login pages. 
- Confirm deletion modals for defensive programming.
- Route protections to keep pages secure and redirect users that shouldn't have access.
- User profile with access to previous order list, wishlist and the ability to update delevery information.
- Toasts messaging upon form submissions and CRUD actions.
- 404 & 500 custom built error pages to keep the user on the site when an error appears and to guide them back to the content.
- A placeholder default image as a temporary fix if a product image isn't readily available.
- Admin user has access to all products and can edit or remove them, they also have access to manage categories, reviews, orders and blog articles as well as edit them, remove them or add new ones.


## Features Left to Implement
- Maisigh newsletter sign up form to update users of new products and possible discounts.
- Pagination for inspiration browsing when more products are added to the site
- Complete Google & Social Newtwork Sign-in to allow users to sign in quicker and more securely
- Additional categories as more products are added to the inventory and site
- Automated review checks for admin before they are published live on the site or smart filtering for inappropriate content.
- Enable comments and social media sharing functionality on each product and blog post.
- Expand the admin profile to include usage and analytics reports to validate possible affiliate marketing.
- Full contact form functionality that notifies the team when a query is received
- Ability to add additional photos to the product page and implement zoom feature so the user can see closer detail.
- Cross-selling products that are often purchased together and the ability for admin to change these products as required.
- Allow email alerts to ping users of wishlist items when the item has beturned back in stock, running low in stock or has been recently discount to allure the user back to the site.


[^ Back To Top ](#contents)

# Information Architecture

## Database Choice

I chose to work with Django's default database **SQLite3** in the development of this project. During deployment, I switched to the Heroku add-on database, **PostgreSQL**.

## Data Modeling
I used Django Allauth and it's default `django.contrib.auth.models` for the **User model** in the profile app.

The Product and Checkout apps are structured on the CI walkthrough project, Boutique Ado.

### Profile app

#### UserProfile model

| Name             | Database Key         | Field Type           | Validation                                          |
| ---------------- | -------------------- | -------------------- | --------------------------------------------------- |
| User             | user                 | OneToOneField 'User' | on_delete=models.CASCADE                            |
| Full Name        | default_full_name    | models.CharField     | max_length=50, default='', blank=True               |
| Phone Number     | default_phone_number | models.CharField     | max_length=20, default='', blank=True               |
| Street Address 1 | street_address1      | models.CharField     | max_length=80, default='', blank=True               |
| Street Address 2 | street_address2      | models.CharField     | max_length=80, default='', blank=True               |
| Town or City     | default_town_or_city | models.CharField     | max_length=40, default='', blank=True               |
| County           | default_county       | models.CharField     | max_length=80, default='', blank=True               |
| Postcode         | default_postcode     | models.CharField     | max_length=20, default='', blank=True               |
| Country          | default_country      | models.CharField     | blank_label='Select Country', null=True, blank=True |

### Products app

#### Category model

| Name          | Database Key  | Field Type | Validation                             |
| ------------- | ------------- | ---------- | -------------------------------------- |
| Name          | name          | CharField  | max_length=254                         |
| Friendly Name | friendly_name | CharField  | max_length=254, default='', blank=True |

#### Product model

| Name        | Database Key | Field Type          | Validation                                                    |
| ----------- | ------------ | ------------------- | ------------------------------------------------------------- |
| Category    | category     | models.ForeignKey   | 'Category', default='', blank=True, on_delete=models.SET_NULL |
| Sku         | sku          | models.CharField    | max_length=254, default='', blank=True                        |
| Name        | name         | models.CharField    | max_length=254                                                |
| Price       | price        | models.DecimalField | max_digits=6, decimal_places=2                                |                         |
| Description | description  | models.TextField    
| Rating      | rating       | models.DecimalField | max_digits=6, decimal_places=2, null=True, blank=True         |
| Image       | image        | models.ImageField   | default='', blank=True                                        |
| Image URL   | image_url    | models.URLField     | max_length=1024, default='', blank=True                       |

### Checkout app

#### Order model

| Name                     | Database Key    | Field Type           | Validation                                                                          |
| ------------------------ | --------------- | -------------------- | ----------------------------------------------------------------------------------- |
| Order Number             | order_number    | models.CharField     | max_length=32, null=False, editable=False                                           |
| User Profile             | user_profile    | models.ForeignKey    | UserProfile, on_delete=models.SET_NULL, null=True, blank=True,related_name='orders' |
| Full Name                | full_name       | models.CharField     | max_length=50, null=False, blank=False                                              |
| Email                    | email           | models.EmailField    | max_length=254, null=False, blank=False                                             |
| Phone Number             | phone_number    | models.CharField     | max_length=20, null=False, blank=False                                              |
| Country                  | country         | CountryField         | blank_label='Select Country \*', null=False, blank=False                            |
| Postcode                 | postcode        | models.CharField     | max_length=20, default='', blank=True                                               |
| Town or City             | town_or_city    | models.CharField     | max_length=40, null=False, blank=False                                              |
| Street Address 1         | street_address1 | models.CharField     | max_length=80, null=False, blank=False                                              |
| Street Address 2         | street_address2 | models.CharField     | max_length=80, null=False, blank=False                                              |
| County                   | county          | models.CharField     | max_length=80, default='', blank=True                                               |
| Date                     | date            | models.DateTimeField | auto_now_add=True                                                                   |
| Order Total              | order_total     | models.DecimalField  | max_digits=10, decimal_places=2, null=False, default=0                              |
| Grand Total              | grand_total     | models.DecimalField  | max_digits=10, decimal_places=2, null=False, default=0                              |
| Original Basket          | original_basket | models.TextField     | null=False, blank=False, default=''                                                 |
| Stripe Payment Intent ID | stripe_pid      | models.CharField     | max_length=254, null=False, blank=False, default=''                                 |

#### Order Line Item model

| Name            | Database Key   | Field Type          | Validation                                                                         |
| --------------- | -------------- | ------------------- | ---------------------------------------------------------------------------------- |
| Order           | order          | models.ForeignKey   | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| Product         | product        | models.ForeignKey   | Product, null=False, blank=False, on_delete=models.CASCADE                         |
| Product Size    | product_size   | models.CharField    | max_length=2, default='', blank=True                                               |
| Quantity        | quantity       | models.IntegerField | null=False, blank=False, default=0                                                 |
| Line Item Total | lineitem_total | models.DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False            |

### Blog app

#### BlogPost model

| Name         | Database Key | Field Type           | Validation                                                 |
| ------------ | ------------ | -------------------- | ---------------------------------------------------------- |
| Title        | title        | models.CharField     | max_length=254, unique=True                                |
| Date Created | created_on   | models.DateTimeField | auto_now_add=True                                          |
| Date Updated | updated_on   | models.DateTimeField | auto_now= True                                             |
| Slug         | slug         | models.SlugField     | max_length=254, unique=True                                |
| Author       | author       | models.ForeignKey    | User, on_delete= models.CASCADE, related_name='blog_posts' |
| Body         | body         | models.TextField     
| Image        | image        | models.ImageField    | default='', blank=True                                     |
| Image URL    | image_url    | models.URLField      | max_length=1024, default='', blank=True                    |
| Status       | status       | models.IntegerField  | choices=STATUS, default=0                                  |

### Reviews app

#### Product Review

| Name         | Database Key   | Field Type           | Validation                                                                                |
| ------------ | -------------- | -------------------- | ----------------------------------------------------------------------------------------- |
| Product Name | product        | models.ForeignKey    | 'products.Product', null=True, blank=True, on_delete=models.SET_NULL                      |
| User Profile | user_profile   | models.ForeignKey    | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_review' |
| Date Created | created_on     | models.DateTimeField | auto_now_add=True                                                                         |
| Rating       | review_rating  | models.CharField     | default="3"                                                                               |
| Title        | review_title   | models.CharField     | max_length=254                                                                            |
| Content      | review_content | models.TextField     | max_length=1000, null=False, blank=False, default=''                                      |


CONTINUE 
[^ Back To Top ](#contents)

# Technologies Used
## Languages
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/) with [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

## Libraries and Frameworks 

### Front-End Technologies
- [jQuery](https://jquery.com/) 
- [Bootstrap](https://getbootstrap.com/)
- [Google Fonts](https://fonts.google.com/)   
- [Font Awesome](https://fontawesome.com/)  
 
### Back-End Technologies
- [Django](https://www.djangoproject.com/)
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) 
- [Pillow](https://pypi.org/project/Pillow/) 
- [Gunicorn](https://gunicorn.org/) 
- [Stripe](https://stripe.com/en-nl) 

## Tools

- [GitHub](https://github.com/)
- [GitPod](https://gitpod.io/)
- [Balsamiq](https://balsamiq.com)
- [Heroku](https://www.heroku.com)
- [Heroku PostgreSQL](https://elements.heroku.com/addons/heroku-postgresql)
- [AWS S3 Basket](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3.html)
- [Cloudinary](https://cloudinary.com/)
- [Autoprefixer](https://autoprefixer.github.io/) 
- [DrawSQL](https://drawsql.app/) 
- [Freeformatter CSS Beautify](https://www.freeformatter.com/css-beautifier.html)  
- [Freeformatter HTML Formatter](https://www.freeformatter.com/html-formatter.html) 
- [Freeformatter JS Formatter](https://www.freeformatter.com/javascript-beautifier.html)     
- [Unicorn Revealer Chrome Extension](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln)
- [Favicon.io](https://favicon.io/) 
- [Figma](https://figma.com) 
- [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools)  
- [Coolers](https://coolors.co) 
- [Color Contrast Accessibility Validator](https://color.a11y.com/)  
- [W3C Markup Validation Service](https://validator.w3.org/)  
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)  
- [JS Hint Validator](https://jshint.com/)  
- [Pep8 Online](http://pep8online.com/) 
- [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/)  
- [Am I Responsive?](http://ami.responsivedesign.is/) 


[^ Back To Top ](#contents)

# Testing
The Testing process has been documented in this [TESTING.md file](TESTING.md "TESTING.md File")

[^ Back To Top ](#contents)

# Deployment




### Requirements:
- [Python 3](https://www.python.org) 
- [PIP](https://pypi.org/project/pip/) 
- [Git](https://git-scm.com/) 
- [Amazon AWS S3 Bucket](https://aws.amazon.com/)


## Local Deployment
### How to clone Maisigh:
![Local Deployment](https://res.cloudinary.com/nclerkin/image/upload/v1626992601/deployment_s6vy1z.png "Local Deployment")
1. Log in to GitHub and go to [this repository](https://github.com/natashaclerkin/maisigh-MS4).
2. At the top of the repository, select **Code** and copy the **Clone URL**.
3. In the IDE, open a Terminal window and change to the directory where you want the cloned directory to be made and type `git clone` and paste in `https://github.com/natashaclerkin/maisigh-MS4.git`.
4. Click enter and the project will be created and cloned locally.

### Working with the local copy:
1. Create a file called `env.py` to hold the app's environment variables, which should contain the following:
```console
import os

os.environ.setdefault("SECRET_KEY", "**Secret key goes here**")
os.environ.setdefault("DEVELOPMENT", "TRUE")
os.environ.setdefault('STRIPE_PUBLIC_KEY',"**Stripe generated key goes here**")
os.environ.setdefault('STRIPE_SECRET_KEY', "**Stripe generated key goes here**")
os.environ.setdefault('STRIPE_WH_SECRET', "**Stripe generated key for individual webhook endpoint goes here**")
```
To find Stripe keys, login to Stripe and then under the 'Developers' tab to locate both keys.

The webhook secret key can be found under 'Webhooks', an endpoint should then be set to receive all events and match the below url structure:
```
<siteurl>/checkout/wh/
```
Different endpoints are required for the local and deployed projects. Ensure the `STRIPE_WH_SECRET` is updated accordingly in `env.py`.

2. Create a `.gitignore` file in the root directory of the project and add the `env.py`along with the below to prevent from being made public:
```
core.Microsoft*
core.mongo*
core.python*
env.py
__pycache__/
*.py[cod]
*.sqlite3
*.pyc
node_modules/
db.json
```
3. Install all the project dependencies from the terminal window of the IDE by typing:
```
pip3 install -r requirements.txt
```
4. Apply database migrations using:
```
python manage.py migrate
```
5. Create a new superuser with:
```
python manage.py createsuperuser
```
6. Type the below into the terminal to run the app locally. 
```
python manage.py runserver
```


## Heroku Deployment

To deploy the app to Heroku from the repository, the following steps were actioned:


1. Log In to Heroku.
2. Select **Create new app** from the dropdown menu in the dashboard.
3. Choose a unique app name ( e.g.'maisigh-ms4') and selectthe closest locationn.
4. Below **Resources** locate **Heroku Postgres** and add it to the app.
5. In the CLI, install **dj_database_url** and **psycopg2** to use Postgres on the deployed site.
```
pip3 install dj_database_url
pip3 install psycopg2
```
6. Log into Heroku via the CLI.
```
heroku login -i
```
7. Migrate the database into Postgres.
```
heroku run python manage.py migrate
```
8. Create a new superuser.
```
python manage.py createsuperuser
```
9. Install gunicorn.
```
pip3 install gunicorn
```
10. Freeze the app's requirements.
```
pip3 freeze > requirements.txt
```
11. Create a **Procfile** and include the following without leaving a blank line and the end of the file:
```
web: gunicorn maisigh-ms4.wsgi:application
```
12. Temporarily disable Heroku's static file collection.
```
heroku config:set DISABLE_COLLECTSTATIC=1 --app maisigh-ms4
```
13. Add the hostname of the Heroku app to `settings.py`.
```
ALLOWED_HOSTS = ['maisigh-ms4.herokuapp.com', 'localhost']
```
14. In Heroku, click the **Deploy** tab and choose GitHub under **Deployment method**.
15. In **Connect to GitHub** enter the GitHub repo name and click **Connect** once found.
16. Go to the **Settings** tab and under **Config Vars** choose **Reveal Config Vars**.
17. Enter the following keys and values, some of which will differ from those in the `env.py`:

|**Key**|**Value**|
|:-----|:-----|
|AWS_ACCESS_KEY_ID|`variable goes here`|
|AWS_SECRET_ACCESS_KEY|`variable goes here`|
|DATABASE_URL|`added by Heroku when Postgres installed`|
|DISABLE_COLLECTSTATIC|`1` variable to be deleted later|
|EMAIL_HOST_PASS|`variable goes here`|
|EMAIL_HOST_USER|`variable goes here`|
|SECRET_KEY|`variable goes here>`|
|STRIPE_PUBLIC_KEY|`variable goes here`|
|STRIPE_SECRET_KEY|`variable goes here`|
|STRIPE_WH_SECRET|`different from env.py`|
|USE_AWS|True|

18. Return to the **Deploy** tab and under **Automatic deploys** select **Enable Automatic Deploys**.
19. In the GitPod CLI add, commit and push all changes and Heroku will automatically deploy the app.
```
git add .
git commit -m "Initial commit"
git push
```
20. To launch the deployed site, select **Open App** from its page within Heroku.

21. The media files for the deployed site are hosted in AWS S3 Bucket. In order to successfully use this service the following needs to be set:
- **AWS account**
- **Bucket Policy**
- **Group**
- **Access Policy**
- **User**

22. Once these settings are implemented, AWS needs to be connected to Django using the following steps:

23. Install boto3, django-storages and update the `requirements.txt` file.
```
pip3 install boto3
pip3 install django-storages
pip3 freeze > requirements.txt
```
24. In `settings.py`, add storages to INSTALLED APPS as well as the code below. Then create a `custom_storages.py`file.

```
if 'USE_AWS' in os.environ:
    # Cache control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'ffrccc-project'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```

25. Insert the below values from the the AWS downloaded`.csv` file to the Heroku Convig Vars in Settings:

|**Key**|**Value**|
|:-----|:-----|
|AWS_ACCESS_KEY_ID|`value goes here`|
|AWS_SECRET_ACCESS_KEY|`value goes here`|

26. Remove the `DISABLE_COLLECTSTATIC` variable from Convig Vars and deploy the Heroku app.
27. In AWS, Create a new folder called `media` next to the `static` folder and upload any required media files to it, making sure they are publicly accessible in **Permissions**.

 
[^ Back To Top ](#contents)

# Credits
## Code
I took inspiration from the following sources however I did implement my own custom code:

- I undertook a significant amount of research into backend development in preparation for the project. As well as the Code Institute's Boutique Ado tutorial which provided great guidance for the project, I also watched a significant amount of Youtube tutorials notably [Corey Schafer](https://www.youtube.com/user/schafer5). 



## Content and Media
The main content for the site was created by myself and the About and Product Detail content were adapted from [Lilywho.](https://lilywho.ie/collections/lilywho-jewellery/products/lilywho-cz-bar-yellow-gold-necklace-lw-n011-y) and the blog content from [Lebrusanstudio.](https://www.lebrusanstudio.com/pages/what-is-ethical-jewellery-and-why-does-it-matter)


Site Imagery was sourced from the following sources:

### Slider
- Slider image #1 - [Louella Jewellery](https://www.facebook.com/louellajewellery/photos/a.456107394444679/3097406220314770)
- Slider image #2 - [Pexels](https://www.pexels.com/photo/person-in-white-long-sleeve-shirt-holding-gold-leather-handbag-5705495)
- Slider image #3 - [Glamour](https://media.glamour.com/photos/5f5af8bc11435a3061457904/master/w_2560%2Cc_limit/sustainable%252520jewelry%252520brands.jpg)

### Inventory
- Gold Necklace #1 - [Lilywho](https://lilywho.ie/collections/lilywho-jewellery/products/lilywho-cz-bar-yellow-gold-necklace-lw-n011-y)
- Gold Necklace #2 - [Lilywho](https://lilywho.ie/collections/lilywho-jewellery/products/lilywho-18ct-gold-lab-diamond-necklace-lw-n070-18ct-gold)
- Rose Gold Necklace #1 - [Lilywho](https://lilywho.ie/collections/lilywho-jewellery/products/pre-order-lilywho-zig-zag-bar-rose-gold-necklace-lw-n025-r)
- Rose Gold Necklace #2 - [Lilywho](https://lilywho.ie/collections/lilywho-jewellery/products/lilywho-rose-gold-necklace-lw-n003-r)
- Silver Necklace #1 - [Lilywho](https://lilywho.ie/collections/lilywho-jewellery/products/lilywho-two-ring-silver-necklace-lw-n001-s)
- Silver Necklace #2 - [Lilywho](https://lilywho.ie/collections/lilywho-jewellery/products/lilywho-horseshoe-silver-necklace)
- Gold Bracelet #1 - [Lilywho](https://lilywho.ie/products/lilywho-id-yellow-gold-bracelet-lw-b006-y)
- Gold Bracelet #2 - [Seoidin](https://seoidin.com/collections/bracelets/products/classic-gold-double-circles-bracelet)
- Silver Bracelet #1 - [Lilywho](https://lilywho.ie/products/lilywho-id-silver-bracelet-lw-b006-s)
- Silver Bracelet #2 - [Lilywho](https://lilywho.ie/products/lilywho-tennis-bracelet-lw-b011-s)
- Rose Gold Bracelet #1 - [Seoidin](https://seoidin.com/collections/bracelets/products/pearl-bracelet-2)
- Rose Gold Bracelet #2 - [Seoidin](https://seoidin.com/products/three-tone-rose-gold-bracelet?_pos=1&_sid=73bc81ace&_ss=r)
- Gold Earrings #1 - [Lilywho](https://lilywho.ie/collections/lilywho-jewellery/products/lilywho-rectangle-mini-hoop-yellow-gold-earrings-lw-e086-y)
- Gold Earrings #2 - [Lilywho](https://lilywho.ie/collections/lilywho-jewellery/products/lilywho-cz-mini-bar-yellow-gold-earrings-lw-e034-y)
- Silver Earrings #1 - [Lilywho](https://lilywho.ie/collections/lilywho-jewellery/products/lilywho-silver-earrings-lw-e003-s)
- Silver Earrings #2 - [Lilywho](https://lilywho.ie/collections/lilywho-jewellery/products/lilywho-silver-earrings-lw-e011-s)
- Rose Gold Earrings #1 - [Lilywho](https://lilywho.ie/products/lilywho-thick-stone-hoop-rose-gold-gold-earrings-lw-e028-r)
- Rose Gold Earrings #2 - [Lilywho](https://lilywho.ie/collections/lilywho-jewellery/products/lilywho-spike-hoop-rose-gold-earrings-lw-e038-r)

### About Us
- About us - [Pexels.com](https://www.pexels.com/@multimediayreaccion)

### Blog
- Blog post #1 - [Glamour.com](https://media.glamour.com/photos/5f5af8a354d1df4e3c1016bb/master/pass/sustainable%20jewelry%20brand.jpg)
- Blog post #2 - [TUN.com](https://www.tun.com/blog/wp-content/uploads/2019/12/sustainable-jewelry.jpg)

### Miscellaneous
- No Image - [Deposit Photos](https://www.google.com/url?sa=i&url=https%3A%2F%2Fdepositphotos.com%2Fvector-images%2Fno-image-available.html&psig=AOvVaw3ke_Ec4FTVWrR29aMEdVJ_&ust=1626273444230000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCNjxifWi4PECFQAAAAAdAAAAABAJ)


## Acknowledgements

I would like to thank my mentor Guido Cecilio for his continued support and overall guidance throughout the project. 

[^ Back To Top ](#contents) 

# Disclaimer

If there are any issues with the copyright of content, please contact me directly and I will amend it as soon as possible. This project is for educational purposes only.

[^ Back To Top ](#contents) 