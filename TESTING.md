 

 

 

 

# Project Testing 
 
# Contents 
1. [Responsive Testing](#responsive-testing) 
2. [Automated Testing](#automated-testing) 
3. [Manual Testing](#manual-testing) 
4. [Bugs](#bugs) 
 
[< Take me back to the README file](README.md "README.md File") 
# Responsive Testing 
 
Responsiveness of the site is tested with [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools). 
The website is tested on Chrome, Firefox, Safari and Edge on the following devices:  
- Desktop: 1024px, 1280px, 1440px, 1600px and 1680px.  
- Mobile & Tablet: Galaxy S5, iPhone 5/SE, iPhone 6/7/8, iPhone 6/7/8 Plus, iPhone X, iPad, iPad Pro and Google Nexus 10. 
 
 
[^ Back To Top ](#contents)  
 
 
# Automated Testing 
## Validation Programs 
 
I used the [W3C Markup Validation Service](https://validator.w3.org/) to check the HTML of all URLs, there were simple error notifications such as duplicate IDs which I resolved and receive no further errors. 

![HTML Validation Initial Results](https://res.cloudinary.com/nclerkin/image/upload/v1627142206/html-val-1_qorwf8.png "HTML Validation Initial Results") 

 
![HTML Validation Final Results](https://res.cloudinary.com/nclerkin/image/upload/v1627142507/html-val-2_qlrgey.png "HTML Validation Final Results") 
 
I used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to check the CSS validity, the code passed the validator with no errors except the Bootstrap-related issues that were out of my hands.
  
![CSS Validation Final Results](https://res.cloudinary.com/nclerkin/image/upload/v1627142236/css-val-1_bjveuz.png "CSS Validation Final Results") 

[JS Hint Validator](https://jshint.com/) to check the JS rules. No errors were highlighted, just warnings stating missing semicolons and warnings of template literal syntax being available in ES6. Other than these minor issues, all files and scripts passed.

![JS Validation Final Results](https://res.cloudinary.com/nclerkin/image/upload/v1627144551/js-val_koblsp.png "JS Validation Final Results") 
 
Flake8 was used to check for any errors in the Python code and refactored when required. Migrations and a few longer lines in Settings.py and additional linting errors were not refactored. All other Python code was passed through the [PEP8](http://pep8online.com/), where it passed with no errors.  
![Pylint](https://res.cloudinary.com/nclerkin/image/upload/v1627170648/pylint_bosvh5.png "Pylint Refactoring") 
![Python validator](https://res.cloudinary.com/nclerkin/image/upload/v1627161814/pep8_ec0bex.jpg "Python Validation Final Results") 
 
I constantly tested the code in [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools) and often ran Lighthouse audits to identify and fix issues that affected the site's performance, accessibility and user experience and all results consistently scored between 90-100%. 

  ![Lighthouse testing](https://res.cloudinary.com/nclerkin/image/upload/v1627145570/lighthouse_cqwd3u.png " Lighthouse testing Results") 
 
 
[^ Back To Top ](#contents)  
 
 
# Manual Testing 
## Manual Testing of User Stories 
| USER | USER STORY TEST | OUTCOME | STATUS | 
| ----------| -------------------- | --------------------| ----------| 
| New User | **View a visually clean and appealing homepage so that I can instantly understand the purpose of the site and navigate its offering easily.** | As a new user, when I click the URL, I land on The homepage to view a clean, sleek website with a monochrome design and the main focus on the colourful imagery and bold CTA's. The sticky navbar is constantly on screen for ease of navigation and allows me to select 'Collection' or select a jewellery category, search for a product, login/register and a bag icon with a price to indicate where future items would be placed. A delivery banner informs me that if I spend over €50 I will get free delivery. There's also a carousel with three images, three titles and three CTAs. The first slide displays a title reading ‘Irish Sustainable Jewellery so I am instantly aware of the site's purpose.Towards the bottom of the homepage, there is a banner that shows the brand's USP. There is also a trending section and a footer with secondary nav links such as socials, blog section, 'about us' and 'contact us. | Approved | 
| New User | **Access the site from any mobile, tablet or desktop device so that I can have an equally enjoyable experience regardless of the selected device/platform.** | As a new user, when I attempt to navigate the site on multiple devices, I am greeted with a responsive website on all tested devices. | Approved | 
| New User | **View content without requiring to register so that I can quickly locate a specific jewellery piece**  |   As a new non-authenticated user, I can select 'Collection' from the nav and I can search jewellery by name and short description content.      |   Approved        |
| New User | **Browse and filter jewellery by product type, rating, name or price so that I can easily find inspiration for a jewellery piece.**  |   As a new user, I click filtered jewellery categories from the Nav to view a selection of relevant jewellery pieces and I can view all jewellery from the Collection link in the navbar.      |   Approved        |
| New User | **View a list of items by product type/name/details keyword search criteria so that I can quickly locate a specific jewellery piece.**  |     As a new user, I can access the search bar in the nav which brings me to all relevant search results based on the entered keyword and I have the ability to search jewellery by name and description content.     |   Approved        |
| New User | **Learn more about where the products come from so that I can trust that I'm purchasing ethically sourced products supporting the environment.**  |   As a new user, when I land on the site I am immediately presented with the striking slider image and CTA which invites me to 'learn more about Maisigh'. There is also an 'about us' section in the footer. Both links divert me to a page with content about the brand and their products and how they are sourced.      |   Approved        |
| New User | **View more specific product information about a particular jewellery piece such as materials used, dimensions etc.**  |   As a new user, I can select a product and it brings me to a page with an image, name, price, product information including materials used and sizing information. There is also a facility to view reviews left by previous customers on the specific product     |   Approved        |
| New User | **View the total cost of a potential order containing multiple products.**  |   As a new user, I can select several items and they successfully save to the shopping bag and I can review all items before proceeding with my purchase. I am also notified if I'm close to the free shipping threshold.      |   Approved        |
| New User | **Register a profile easily so that I can store address and billing information to streamline the order process on future visits.**  |   As a new user, I can register with the website and I receive a confirmation email to validate my account. This is a simple, user-friendly purchase.      |   Approved        |
| Returning User | **Log in and out without encountering issues so that I can have an enjoyable user experience.**  |   As a returning user, I can select the 'log in' link in the navbar which directs me to the login page and when I enter my details correctly, I can access my profile including past orders and a wishlist if I had saved items to it already.      |   Approved        |
| Returning User | **View my account so that I can review previous orders for product info or shipping status for current orders.**  |   As a returning registered user, I can view my account from the navbar and can review past orders details.  |   Approved - Shipping status for current orders in future release       |
| Returning User | **Edit my personal details on my account so that I can update info such as shipping info if my details have changed.**  |   As a returning registered user, I can view my account from the navbar and can update my saved information or enter my details to improve the checkout process in the future.  |   Approved      |
| Returning User | **Save a wish list of desired products to my account so that I can possibly purchase the item in the future when I can afford the item.**  |   As a returning registered user, I can view any item and add it to the wish list. A toast pops up with confirmation that it has been added to the wish list which can be viewed from My Account. To view the actual wish list I can access it from the navbar and can review the items I have added. If I haven't added anything to my wish list there's a CTA to bring me back to view the collection. |   Approved     |
| Returning User | **Have the ability to contact the company so that I can ask a question regarding a product or purchase.**  |   As a returning user, I can select the 'contact us' link which brings me to a form where I can enter my information and query. When I submit the query, I am presented with a toast that confirms my message has been received and a member of the company will get back to me.  |   Approved  |
| Returning User | **Receive discounts on future orders so that I am incentivised to remain loyal to the brand.**  |   As a returning user who has placed an order, once I view my order confirmation, I see a CTA which invites me to review the order once received or share the order online in order to receive a discount on the next order. This links to the blog and an article about this process.   |   Approved       |
| Returning User | **Receive discounts on future orders so that I am incentivised to remain loyal to the brand.**  |   As a returning user who has placed an order, once I view my order confirmation, I see a CTA which invites me to review the order once received or share the order online in order to receive a discount on the next order. This links to the blog and an article about this process.   |   Approved       |
| Business/Admin User | **The ability to view, add, edit or remove product categories so that I can keep the categories relevant to what users are searching for.**  |   As a logged-in Admin user, I can select 'manage categories' which brings me to the admin portal where I can view the current categories that are present on the site and I have options available to edit or delete these categories as well as the option to create a new category.  |   Approved       |
| Business/Admin User | **The ability to view, add, edit or remove products so that I can review and reflect the current stock levels and product information.**  |   As a logged-in Admin user, I can view all products from the live locations on the site and admin portal. As well as being able to view the current products and descriptions as regular users, I have access to 'edit' and 'delete' links. I have full functionality to edit or delete the product and I am presented with a confirmation modal before deleting a product. I can also add new products from the nav or from the admin portal. Toast messaging confirms site actions taken.  |   Approved       |
| Business/Admin User | **The ability to view, add, edit or remove blog articles so that I can keep the content relevant to the customer's interests that they will enjoy.**  |   As a logged-in Admin user, I can view all blog articles from the live locations on the site and admin portal. As well as being able to view the current posts as regular users, I have access to 'edit' and 'delete' links. I have full functionality to edit or delete the post and I am presented with a confirmation modal prior to deleting an article. I can also add new articles from the nav or from the admin portal. Toast messaging confirms site actions taken.  |   Approved       |
| Business/Admin User | **Ensure intuitive text is present so that I can provide an enjoyable user experience when users interact with the content or features.**  |   As an Admin/Business user, I have implemented there is consistent toast messaging throughout the site to provide a friendly efficient service to customers. |   Approved       |
| Business/Admin User | **View the Maisigh logo in as many locations on the website so that I can create awareness for the brand.**  |   As an Admin/Business user, I can see the logo is constantly in view as a sticky nav as I navigate through the site. This will successfully create awareness for the brand. |   Approved       |
| Business/Admin User | **Offer a discount to customers so that I can gain repeat customers for the brand.**  |   As an Admin/Business user, I can see on the carousel there is a link to the blog which includes a post about reviewing an order or tagging the brand in an order on social media to obtain a discount on the next purchase. The social media tags will drive business from social media to the site and the reviews will drive business from one product to another. |   Approved       |
| Business/Admin User | **View analytics/reports for the checkout process so that I can highlight and fix any potential cart abandonment issues relating to the design and make necessary improvements.**  |   To be implemented in a future release  |    Not Approved     |


## Manual Feature Testing 

|  FEATURE CATEGORY   |  FEATURE     |  ACTION & EXPECTED OUTCOME    |  OPERATIONAL ON ALL DEVICES?  |
| --------------------| -------------------- |  --------------------|  ----------|
| Navigation | Search | **Search the database using the query as a keyword and returns any products that have the keyword in their name or description. On mobile devices, selecting the icon reveals a dropdown search bar, with the same functionality as the desktop search**   |    Approved     |
| Navigation | Maisigh Logo | **Return the user to the home page.**   |    Approved      |
| Navigation | My Account (Authenticated user) | **On mobile devices, the hamburger menu should activate the menu. Display a dropdown menu with the 'My Profile' and 'Logout' links. My profile will direct the user to their own profile page with previous orders if applicable. Logout will direct the user to the homepage.**   |    Approved     |
| Navigation | My Account (Non-authenticated user) | **On mobile devices, the hamburger menu should activate the menu. Display a dropdown menu with the 'Register' and 'Login' links. Register will direct the user to the registration page and Login will direct the user to the login page**   |    Approved     |
| Navigation | My Account (Authenticated superuser) | **On mobile devices, the hamburger menu should activate the menu. Display a dropdown menu with the same authenticated user links as above with the addition of 'Product Management' and 'Blog Management'. Blog management will direct the superuser to a page that allows them to add a new blog article. Product management will direct the superuser to a page that allows them to add a new product.**   |    Approved     |
| Navigation | Bag | **With nothing in the bag, the price should display €0.00 in light green font. Add an item and the price should update and become bold. On mobile devices, the bag icon will take the user to their bag details.**   |    Approved     |
| Navigation | Breadcrumbs | **Breadcrumbs present on desktop and mobile for collection page, category pages, individual product pages, blog page, individual blog post pages**   |    Approved     |
| Footer | Social icons | **Direct the user to the appropriate social media sites.**   |    Approved     |
| Footer | Contact Us | **Direct the user to the Contact Us submission form.**   |    Approved     |
| Footer | About Us | **Direct the user to the Maisigh About Us page.**   |    Approved     |
| Footer |Blog| **Direct the user to the Blog articles.**   |    Approved     |
| Homepage |Carousel| **Three images present. On desktop devices, the title and CTAs are present. The 'Learn more about Maisigh' CTA should direct the user to the 'About Us' page. The 'Browse our collection' CTA should direct the user to the main collection products page. The 'Tag us in your Maisigh orders for freebies' CTA should divert the user to the Blog.**   |    Approved     |
| Products | Collection & Category Pages | **All images are links and should divert users to their corresponding detail page. Sorting selector allows the user to sort the products alphabetically, by price, or rating**|    Approved     |
| Products | Collection & Category Pages for superusers | **As well as the above, superusers should be able to edit or delete the specific product and should either divert them to the edit page or the deletion model respectively**|    Approved     |
| Products | Individual Product Pages | **All pages on all devices should display the name, image, price, rating score, description, correct breadcrumb naming, 'keep shopping CTA'. 'add to bag CTA', 'add to wishlist CTA',  quantity selectors with the minus selector disabled if no products have been added, reviews section with 'add review CTA' and 'read review CTA'. All CTAs direct the user to the relevant landing page.**|    Approved     |
| Products | Individual Product Pages for superusers | **As well as the above, superusers should be able to edit or delete the specific product and should either divert them to the edit page or the deletion model respectively. The cancel button in the model closes it keeping the user on the same page. The delete button removes the product from the database.**|    Approved     |
| Profile | Default Delivery Information  | **Display a form with placeholders. 'Update Information' button updates the information.**|    Approved     |
| Profile | Order History  | **Order number should direct the user to the order confirmation page.**|    Approved     | 
| Shopping Bag | Bag Page  | **This page presents product detail with quantity selector icons to allow the increase or decrease of the product. An 'update' link to amend the quantity after the use of the selector. The 'remove' link takes the product out of the user's bag. The 'keep shopping' button directs the user to the collection page. The 'secure checkout' button - directs the user to the checkout page.**|    Approved     | 
| Checkout | Authenticated user who ordered previously or completed delivery info | **Form presents the user with an order summary and a pre-filled delivery information form. Checkbox when selected will save details to the default delivery details. Payment box connected to stripe and if an invalid card is inputted an error message will appear.The 'adjust bag' button directs the user back to the bag page to review their order and make adjustments if required.  The 'complete order' button completes and processes the order and a pink overlay should appear with a loading spinner until the order is complete. A confirmation email will be delivered to the user's email containing all information. If the bag is empty, a 'keep shopping' button directs the user to the collection page.**|    Approved     |
| Checkout | Non-authenticated user  | **Form presents the user with an order summary and empty delivery information form.  Users are presented with links to create an account or login to save the information to the default delivery details. Payment box connected to stripe and if an invalid card is inputted an error message will appear.The 'adjust bag' button directs the user back to the bag page to review their order and make adjustments if required.  The 'complete order' button completes and processes the order and a pink overlay should appear with a loading spinner until the order is complete. A confirmation email will be delivered to the user's email containing all information. If the bag is empty, a 'keep shopping' button directs the user to the collection page.**|    Approved     |
| Checkout | Success page  | **A confirmation box is displayed with all details entered at the time of booking. A CTA with the text 'Get discount on your next purchase' is linked to the blog page to allow users to learn more about using a discount on their next purchase.**|    Approved     |
| Products | Blog Page| **All blog posts, CTAs and images should divert users to their corresponding blog post.**|    Approved     |
| Products | Blog Page for superusers | **As well as the above, superusers should be able to edit or delete the specific blog post and should either divert them to the edit page or the deletion model respectively**|    Approved     |
| Products | Individual Blog Posts | **All pages on all devices should display the same image from the blog page. There should be blog content and the time and user info who created the post.**|    Approved     |
| Products | Individual Blog Posts for superusers | **As well as the above, superusers should be able to edit or delete the specific post and should either divert them to the edit page or the deletion model respectively. The cancel button in the model closes it keeping the user on the same page. The delete button removes the product from the database.**|    Approved     |


[^ Back To Top ](#contents) 




# Bugs

Minor bugs were found and resolved with **Devtools** like the below:

![Bug 1](https://res.cloudinary.com/nclerkin/image/upload/v1627170956/bug-6_q9gie5.png "Bug 1") 
![Fix 1](https://res.cloudinary.com/nclerkin/image/upload/v1627170957/fix-6_nj56ek.png "Fix 1") 
![Bug 2](https://res.cloudinary.com/nclerkin/image/upload/v1627170956/bug-2_nytclg.png "Bug 2") 
![Fix 2](https://res.cloudinary.com/nclerkin/image/upload/v1627170956/fix-2_u0vcae.png "Fix 2") 
![Bug 3](https://res.cloudinary.com/nclerkin/image/upload/v1627170956/bug-5_vk0vk6.png "Bug 3") 
![Fix 3](https://res.cloudinary.com/nclerkin/image/upload/v1627170957/fix-5_jipqhq.png "Fix 3") 
![Bug 4](https://res.cloudinary.com/nclerkin/image/upload/v1627170956/bug-3_o7x2pl.png "Bug 4") 
![Fix 4](https://res.cloudinary.com/nclerkin/image/upload/v1627170956/fix-3_lmqxja.png "Fix 4") 
![Bug 5](https://res.cloudinary.com/nclerkin/image/upload/v1627170956/bug-4_c5vqx0.png "Bug 5") 
![Fix 5](https://res.cloudinary.com/nclerkin/image/upload/v1627170957/fix-4_jjgalr.png "Fix 5") 

However, I did run into issues with the following:

## Remaining Bugs:

- In specific smaller devices, the positioning of certain nav elements are not ideal or visually pleasing. I will refactor the layout in the next release when more time is available to implement the fix.

!["Remaining Bug 1](https://res.cloudinary.com/nclerkin/image/upload/v1627375408/bug-1_ea7nmh.png "Remaining Bug 1") 

- All success messages are displayed on the same toast. I believe product/blog updates shouldn't display with the items in the shopping bag. I will display the messaging separately in the next release when more time is available to implement the fix.

!["Remaining Bug 2](https://res.cloudinary.com/nclerkin/image/upload/v1627375625/toast_ryd4cz.png "Remaining Bug 2") 

- There are minor positioning-related bugs that I would like to fix such as the below and search dropdown which merit fixing in the next release when more time is available to implement the fixes.

!["Remaining Bug 3](https://res.cloudinary.com/nclerkin/image/upload/v1627375407/bug-8_ucoojq.png "Remaining Bug 3") 



[^ Back To Top ](#contents) 

[< Take me back to the README file](README.md "README.md File")