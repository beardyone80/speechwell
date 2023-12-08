<img src="https://res.cloudinary.com/dpv6kxzru/image/upload/v1701776845/logo-no-background_dplkry.png" alt="Speechwell large logo" width="600" height="600">

# SpeechWell - Empowering Understanding & Support for Children's Speech Disorders

Welcome to SpeechWell, a comprehensive platform dedicated to shedding light on prevalent speech and language disorders affecting children. Our project serves as an invaluable resource, offering insights into the common challenges encountered in children's communication.

The live link can be found here - https://speechwell-61d1e85225c5.herokuapp.com/

## Project Overview

SpeechWell's mission is to provide an extensive understanding of various speech-related conditions commonly found in children. We aim to equip users with curated information on conditions like stuttering, language delay, or articulation disorders. Our platform serves as a centralized directory connecting individuals with a network of skilled therapists specializing in these areas.

## What We Offer

- **Insightful Information:** Explore our curated directory for in-depth knowledge and insights into prevalent communication challenges faced by children.
  
- **Therapist Network:** Connect with certified professionals specializing in speech-related conditions prevalent among children.
  
- **Empowering Support:** Access guidance and support to aid your child's journey towards improved communication and speech wellness.

Join us at SpeechWell and embark on a journey towards empowering yourself with the necessary tools and resources to support your child's communication and speech development.


# Responsive Mockup

I have provided a number of mock-ups below of the different pages in my project. The project is fully responsive and scalable across all common user devices and viewports.

## **Home Page**

![Speechwell home page](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701948069/responsve_home_c2ifhx.jpg)

## **Disorders Page**

![Speechwell disorders page](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701948069/responsve_disorders_nhrkdv.jpg)

## **Therapists Page**

![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701948069/responsve_therapists_shccno.jpg)

## **Login Form**

![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701952036/responsve_login_corrected_rmfxd5.jpg)

## **Sign up form**

![Speechwell sign up form](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701952036/responsve_sign-up_corrected_pc6qwv.jpg)

# User stories and Personas

A number of personas and user stories were generated to guide the scope of the project which can be viewed here:
[User Stories PDF (hosted on Google Drive)](https://drive.google.com/file/d/1Ziyir93tIgMZj-YbDDpDy79r5TDUwm84/view?usp=sharing)

This informed a number of issues that I added to my project board thus adhering to the principles of Agile Methodology. 
![Github issues page](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701949005/project_issues_cxnvpx.jpg)
![Github project board](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701949005/project_board_xwrmfa.jpg)

The use of a project/canban board was extremely useful during the development of my project to make sure I was able to stay focused and plan my tasks efficiently.

# Wireframing and Design Process

I used Balsamiq to sketch out some basic wireframing for my project as detailed below. My initial wireframes are close to the design of the deployed project with some alterations that were made during the coding process as coding progressed. Using the wireframes was pivotal in informing the initial direction I would take when setting out the various pages in the project.
![Balsamiq wirefram index page](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701952874/Index_uj48bj.png)
![Balsamiq wireframe disorders page](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701952874/Disorder_Info_Page_buracg.png)
![Balsamiq wireframe therapist list page](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701952874/Therapist_Directory_djwin3.png)
![Balsamiq wireframe disorder detail page](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701952873/Disorder_Detail_Information_z4seqr.png)
 
 -------------------------------------------------------------------------------------------
 I used the website [app.logo](https://app.logo.com/) to design a clear concise brand for the project with a colour pallet that matches the website colour pallet 
 
**Main index page logo**

<img src="https://res.cloudinary.com/dpv6kxzru/image/upload/v1701776845/logo-no-background_dplkry.png" alt="Speechwell large logo" width="300" height="300">

-------------------------------------------------------------
 **Small navbar brand logo**(White due to navbar colour)
 ![Small logo white](https://res.cloudinary.com/dpv6kxzru/image/upload/v1702033258/logosmall_wmv1ol.jpg)
Having a consistent brand logo across all pages in the navbar, which was also clickable and brought the user back to the home page, was important for a good user experience and to also further the needs of the business in terms of recognition.

# Models
I used [Lucid](https://lucid.app/) to design an initial ERD. I included some rough ideas of how could I could code each model within the document to assist me. The final models varied slightly but using an ERD as part of Agile working made the design process a lot easier.
![ERD Model ](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701960270/Speech_Therapy_Website_Capstone_Project_u3genj.jpg)

My final models have a relationship between the Specialty model and the Therapist model. A many_to_many relationship was established with the 'specialty' field in the Therapist model getting it's value from the Specialty model.
There is also a relationship between the Disorder model and the Therapist model. The author field in the Disorder model takes it value from the Therapist  model.

# Website Features

## __Home Page__

![Home page](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701984992/home_page_ddu5vw.jpg)
 The landing page features a background hero image that covers the full viewport that reflects a calm and professional medical/therapy atmosphere. Reminiscent of a doctors office. This hero image is used consistently on all pages to ensure a good user experience.
 
The page is minimal and clean with a blurb that describes the websites aims and intention and then two buttons that will allow the user to sign up or login to the website.

A design choice was made to keep all pages looking simple and clean as the subject matter, Speech Therapy, is a serious one and users would prefer to have any information presented concisely without the need for 'flashy' aesthetics.
 

## __About Section__

![About page](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701979912/about_d60nul.jpg)
 I provided a simple 'About' page presenting myself as the developer of the website in the context of the project being made for assessment. This will hopefully ensure that it is clear to any users that come across the website that it is not a real business. A small muted text note in the footer reiterates that the website is for assessment purposes only in relation to a course.

## __Therapist Directory__

![Therapist directory](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701985117/therapist_directory_l90uqb.jpg)
  The therapist directory consists of a list of therapists presented using bootstrap cards. The cards include an image (a headshot, or the therapists business logo perhaps) as well as contact details, the therapist areas of expertise, and a short biography.
  
  The directory cards are displayed by iterating through the records in the Therapist model and presenting them using bootstrap in rows and columns. The maximum columns is 4 but this is fully responsive and will shrink down to 1 column on smaller mobile screens and viewports.
  
 The directory can be viewed based on the region of the therapist so that the user can narrow down the list of therapists they would potentially contact. Restricting them to local therapists. Future releases of the project will include a search function for users to view only therapists that specialise in certain areas of speech therapy.

## __Disorders List/Detailed Disorder View__

![Disorder list page](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701981148/disorder_list_page_uvsyyx.jpg)
 A page is provided that lists the most common speech disorders that a user may encounter. Again presented using bootstrap cards and each card can be clicked through to a detailed information page about the disorder.

## __Disorder Detail Page__

![Disorder Detail Page](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701981080/disorder_detail_page_digs2w.jpg)
Upon clicking on a card on the disorder list page detailed information about that disorder will be presented. This information will provide a concise description of each disorder that will inform the user.

## __Sign Up/Login/Sign Out__

![Sign up page](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701981322/register_page_jpppwf.jpg)
![Sign in page](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701981437/login_page_tvs8qx.jpg)
Using the Django allauth package the user will be able to create an account, login to an existing account and log out of their account using the links provided in the navbar. The use of user accounts is important because the projects CRUD functionality (expanded upon below) is restricted to users with the relevant permissions.

## __User Welcome__

![User welcome message](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701979481/user_welcome_nuslyg.jpg)
The navbar will welcome a logged in user by their username and this welcome is consistent across all pages and produced dynamically from the User model.


## __Register as a therapist__

![Register form](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701980128/register_therapist_ekqtxu.jpg)
If a user with the relevant permissions is logged in, they will be able to access a form to add their details to the therapist directory. When a user signs up for the site, and also consistently present within the footer, is a paragraph informing the user that they can contact the site admin to be added to the therapist directory. The emailto: link opens the users preferred email client and prefills some information for ease of use. The site admin can then reply to the user once they have been approved and direct them to the therapist registration form.

## __Update and Delete Therapist Records__

![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701980630/confirm_delete_page_nw6d4k.jpg)
![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701985661/update_form_opmufa.jpg)
 If a user is registered as a superuser in the admin panel they will be able to update and delete therapist records. The delete therapist button redirects to a confirmation page to mitigate and lesson the possibility of accidental deletion.
 
 If a user without the correct permissions is able to access these pages an error message will be shown.  ![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701980926/add_therapist_no_permission_dqctup.jpg)

## __Dynamic Navbar__

**Logged out user**

![Navbar logged out](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701985993/navbar_logged_out_a5zvdx.jpg)

**Logged in superuser/staff**

![Logged in user](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701985982/navbar_logged_in_rcd0s1.jpg)

**Logged in standard user**

![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1702025772/logged_in_user_fy5dde.jpg)

The navbar will also dynamically alter its content depending on the permissions of the logged in user. This will ensure that only registered users can access the full site and only registered users with the correct permissions will be able to access restricted features. Only superuser and staff can see the Register as a therapist link.

### Future features
Future releases of the website will include the following functionality which were unfortunately out of scope for the timeframe I had to complete this project.
- **Search bar**
A search function in the navbar that will allow a user to search the website and also the therapist and disorder model so that they can view information that is precisely relevant to their needs.
- **Full CRUD for 'therapist users'**
Presently the site admin only (superuser) is allowed to delete and update a therapists entry in the database and only users who have 'staff' permission on the backend can upload a therepist record to the database. Future iterations of the website will give the users full ownership of their own record so that they can update it or delete the entry as required using additional forms on the front end.
- **Comment Section**
There will be an implementation of a comment section under each article on the detailed disorder page so that users can provide feedback, support and collobarate with each other as they navigate through their speech therapy journey.
- **Updated Therapist Model**
It is my intention to adjust and grow the Therapist model to include additional information including a way to contact each therapist, and a link to their own website to greatly improve the functionality and usefulness of the directory.
- **Survey Quiz**
Future iterations of the website will also feature a 'survey' form similar to a quiz that caregivers can use to inform where their research could focus. This would be in the form of asking questions of the user such as "Can you child form the following sounds 'xx' 'yy' 'zz' clearly" and integrate the answers into a model of disorders and common symptoms and a model of expected speech milestones that a child would reach by a given age in order to present further information to the user.### Future features
Future releases of the website will include the following functionality

## Testing 
I tested my website using online validators and through manual user testing. The results are detailed below


**HTML**

I passed the website pages through the W3C HTML checker with the results presented below
  -  [Index Page - link to W3C Results](https://validator.w3.org/nu/?doc=https://speechwell-61d1e85225c5.herokuapp.com/) - Passed
  - [Login Page - link to W3C Results](https://validator.w3.org/nu/?showsource=yes&doc=https://speechwell-61d1e85225c5.herokuapp.com/accounts/login/) - Failed due to stray closing `</div>` but I am unable to fix presently due to not knowing where they derive from. I suspect they may be residual from the { extend } tags but I cannot locate them in my code from the rendered code.
![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701958499/login_w3c_error_ddkocz.jpg)
	
- [Disorders Page - link to W3C Results](https://validator.w3.org/nu/?showsource=yes&doc=https://speechwell-61d1e85225c5.herokuapp.com/disorders/) - Passed
- [Therapists Page - link to W3C Results](https://validator.w3.org/nu/?showsource=yes&doc=https://speechwell-61d1e85225c5.herokuapp.com/therapists/) - Passed
- [Regional Therapist Page - link to W3C Results](https://validator.w3.org/nu/?showsource=yes&doc=https://speechwell-61d1e85225c5.herokuapp.com/therapists/Scotland/) - Passed (Scotland provided as example)
- [Log out Page - link to W3C Results](https://validator.w3.org/nu/?showsource=yes&doc=https://speechwell-61d1e85225c5.herokuapp.com/accounts/logout/) - Passed
- [About Page - link to W3C Results](https://validator.w3.org/nu/?showsource=yes&doc=https://speechwell-61d1e85225c5.herokuapp.com/about/) - Passed
--------
**CSS**

No errors were found when passing through the official W3C Jigsaw validator (2 warnings present)

![Jigsaw CSS validator](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701959517/css_validation_iocoou.jpg)

![CSS Warnings](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701959634/css_warning_csrznx.jpg)
------------
 **Python**
I used the Code Institute Python Linter to test with the following results
|   Page	| Result  	| Screenshot  	|
|---	|---	|---	|
|Project Main Settings   	|Passed  	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701974052/project_main_settings_ez4wye.jpg)   	|
|Project Main URLS   	|Passed   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701974053/project_main_urls_x7c3lw.jpg)   	|
|Resources Views   	|Passed   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701974054/resources_views_ovaa7e.jpg)   	|
|Resources URLS   	|Passed  	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701974055/resources_urls_x1teji.jpg)   	|
|Resources Models   	|Passed  	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701974056/resources_models_jd9ncx.jpg)   	|
|Resources Forms   	|Passed   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701974057/resources_forms_bvmmqo.jpg)   	|
|Home Views   	|Passed  	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701974058/home_views_yg0pkx.jpg)   	|
|Home URLS   	|Passed   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701974059/home_urls_ighebj.jpg)   	|
|Disorders Views   	|Passed 	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701974060/disorders_views_g0akcv.jpg)   	|
------
**Lighthouse**
I used Lighthouse within Google Chrome developer tools to test my website. 
![Lighthouse results](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701984435/lighthouse_image_rfuh9z.jpg)
The results can be accessed here in PDF format

[Home Page Desktop](https://drive.google.com/file/d/1B6kgZnEoNoLjtJht3ANvHHFeqC2EBCg5/view?usp=sharing)

[Home Page Mobile](https://drive.google.com/file/d/1YEo3qCxauAzRot6G46e-Hg_wvh5vpf55/view?usp=sharing)

[Therapist Page Desktop](https://drive.google.com/file/d/1LgO8KZNwzZT2preJI5eEwhZIZwiZrq_2/view?usp=sharing)

[Therapist Page Mobile](https://drive.google.com/file/d/1alDJX8rLDqTPi4AB7NlofYY2ULzxiR9b/view?usp=sharing)

[Disorders Page Desktop](https://drive.google.com/file/d/15X9SxXfCrbjqL3O6gHowf_KrdnIuN4ZX/view?usp=sharing)

[Disorders Page Mobile](https://drive.google.com/file/d/1K8DsAgaJpevdc7h6kumK9oPkaAmG0vu1/view?usp=sharing)


## Manual Testing

|Test   	|Action   	|Result   	|Screenshot   	|
|---	|---	|---	|---	|
|#1 Clicking on logo in navbar will redirect user to home page   	|Click on logo   	|PASS   	| N/A  	|
|#2 Clicking on Home in navbar will redirect user to home page   	|Click on home link|PASS   	| N/A  	|
|#3 Clicking on Disorders in navbar will redirect LOGGED IN user to disorder page    	|Click on disorders link|PASS   	|N/A   	|
|#4 Clicking on Find a therapist in navbar will redirect LOGGED IN USER to home page   	|Click on find a therapist link|PASS   	|N/A   	|
|#5 Clicking on Logout in navbar will redirect LOGGED OUT USER to Logout page   	|Click on logout link   	|PASS   	|N/A   	|
|#6 Clicking on Register as a therapist as STAFF or SUPERUSER will redirect to Register as a therapist form   	|Click on register as a therapist as STAFF and SUPERUSER   	|PASS   	|N/A   	|
|#7 LOGGED IN USER will see welcome message on navbar with USERNAME   	|Log in and view navbar   	|PASS   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701979481/user_welcome_nuslyg.jpg)   	|
|#8 Clicking on site admin link in footer will redirect user to email client with pre-filled subject| Click on contact site admin link    	|PASS  	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701979697/admin_contact_zfzlgq.jpg)|
|#9 Clicking on site admin link in footer as LOGGED IN USER will redirect user to email client with pre-filled subject   	|Click on contact site admin link   	|PASS   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701979697/admin_contact_zfzlgq.jpg)   	|
|#10 Clicking on about in footer will redirect user to about page   	|Click on about link   	|PASS   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701979912/about_d60nul.jpg)   	|
|#11 Clicking on about in footer will redirect LOGGED IN USER to about page   	|Click on about link   	|PASS   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701979912/about_d60nul.jpg)   	|
|#12 Clicking on 'Register as a therapist' as STAFF or SUPERUSER will redirect to 'Register as a therapist form'   	|Click on register as therapist link as STAFF or SUPERUSER   	|PASS   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701980128/register_therapist_ekqtxu.jpg)   	|
|#13 Submitting 'Register as a therapist form' as STAFF or SUPERUSER will add entry to database and display entry on therapist page   	|Complete and submit form   	|PASS   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701980204/register_therapist_success_egjmuc.jpg)   	|
|#14 Viewing 'Find a therapist page' as SUPERUSER will show 'Update' and 'Delete' buttons under each card   	|View thereapist page as SUPERUSER   	|PASS   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701980325/therapist_page_SU_jwsyat.jpg)   	|
|#15 Clicking on 'Update button' on find a therapist page as SUPERUSER will redirect to 'Therapist update form'   	|Click on update button   	|PASS   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701980128/register_therapist_ekqtxu.jpg)   	|
|#16 Submitting 'Therapist update form' as SUPERUSER will update entry in database  	|Complete and submit form   	|PASS   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701980532/update_form_success_wdfm7v.jpg)   	|
|#17 Clicking on 'Delete button' on therapist page as SUPERUSER will redirect user to 'Confirm delete page'   	|Click on delete button   	|PASS   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701980630/confirm_delete_page_nw6d4k.jpg)   	|
|#18 Clicking on 'Confirm' on 'Confirm delete page' as SUPERUSER will delete database entry   	|Click on confirm delete   	|PASS   	| N/A  	|
|#19 Clicking on 'Cancel' on 'Confirm delete page' will redirect SUPERUSER back to 'Find a therapist page'   	|Click on cancel button   	|PASS   	|N/A   	|
|#20 If user without permission tries to access update or delete pages permission will be denied and a message displayed   	|Manually enter URL for register therapist page as a logged out user   	|PASS   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701980926/add_therapist_no_permission_dqctup.jpg)   	|
|#21 Clicking on a Disorder card on disorders page will redirect user to disorder detail page   	|Click on card on disorder page   	|PASS  	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701981080/disorder_detail_page_digs2w.jpg)   	|
|#22 Clicking on Disorders button on index page as a LOGGED IN USER will redirect to disorders page  	|Click on disorders button   	|PASS   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701981148/disorder_list_page_uvsyyx.jpg)   	|
|#23 Clicking on Therapists button on index page as LOGGED IN USER will redirect user to therapist page  	|Click on therapist button   	|PASS   	|N/A   	|
|#24 Clicking on Register button on index page as user will redirect user to Sign up page   	|Click on the register button   	|PASS   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701981322/register_page_jpppwf.jpg)|
|#25 Clicking on Log In button on index page as user will redirect user to Login page   	|Click on login button   	|PASS   	|![enter image description here](https://res.cloudinary.com/dpv6kxzru/image/upload/v1701981437/login_page_tvs8qx.jpg)   	|


### Unfixed Bugs
None found through user testing

## Deployment


I deployed my Django project to Heroku, ensuring seamless functionality, especially for static files, in a production environment.

I followed the steps below 

1.  **Heroku Account and Setup:**
    
    -   Created a Heroku account and installed the Heroku CLI for application deployment.
2.  **Configuring Django for Deployment:**
    
    -   Updated my projects main settings.py:
        -   Added 'whitenoise.middleware.WhiteNoiseMiddleware' to the MIDDLEWARE list.
        -   Configured STATIC_ROOT and STATICFILES_STORAGE for WhiteNoise.
        -   I used the following solution for setting the debug flag when deploying
	        - in settings.py I added `DEBUG = 'DEVELOPMENT'  in os.environ`
	        - in my env.py file I added `os.environ['DEVELOPMENT'] = 'True'`
	        
	        This setup ensures that `DEBUG` is set to `False` in the production environment by checking if the 'DEVELOPMENT' environment variable is present. If 'DEVELOPMENT' is not found or if it evaluates to `False`, the `DEBUG` variable will be set to `False` accordingly. Additionally, it sets the 'DEVELOPMENT' environment variable to 'True'.
	        
        
3.  **Requirements and Version Control:**
    
    -   Included 'whitenoise' in requirements.txt
4.  **Heroku Application Creation:**
    
    -   Created a Heroku app using the CLI and configured essential environment variables.
5.  **Database Setup**
    
    -   Configured the production database on Heroku using ElephantSQL
6.  **Deployment to Heroku:**
    
    -   Pushed the code to the Heroku remote repository and ran deployment commands.
7.  **Collecting Static Files:**
    
    -   Executed the 'collectstatic' command to gather static files into STATIC_ROOT.
8.  **Testing and Verification:**
    
    -   Checked the deployed app's URL on Heroku and verified static file serving by WhiteNoise.


The deployment process, using Heroku with WhiteNoise for static file serving, enabled a smooth transition from development to a production-ready Django project. Heroku's platform combined with WhiteNoise ensured a reliable hosting environment, ensuring the project's stability and functionality in production.

The live link can be found here - https://speechwell-61d1e85225c5.herokuapp.com/

## Tech Stack

**Client:** HTML5 | Bootstrap 5.1.3 | CSS | Django 4.2.7

**Server:** Heroku

**Installed apps**
asgiref=3.7.2

click=8.1.7

cloudinary=1.36.0

colorama=0.4.6

crispy-bootstrap5=2023.10

cssbeautifier=1.14.11

dj-database-url=2.1.0

Django=4.2.7

django-allauth=0.58.2

django-ckeditor=6.7.0

django-cloudinary-storage=0.3.0

django-comments-xtd=2.9.10

django-contrib-comments=2.2.0

django-crispy-forms=2.1

django-js-asset=2.1.0

django-resized=1.0.2

djangorestframework=3.14.0

djlint=1.34.0

EditorConfig=0.12.3

Faker=20.1.0

gunicorn=21.2.0

html-tag-names=0.1.2

html-void-elements=0.1.0

jsbeautifier=1.14.11

oauthlib=3.2.2

pathspec=0.11.2

Pillow=10.1.0

psycopg2=2.9.9

PyJWT=2.8.0

python3-openid=3.2.0

pytz=2023.3.post1

regex=2023.10.3

requests-oauthlib=1.3.1

sqlparse=0.4.4

tqdm=4.66.1

whitenoise=6.6.0


## Django Faker module
I used the [django-faker](https://pypi.org/project/django-faker/) module in order to speed up development of my project using some auto generated entries for my database. I created a 'utils' folder in my app and followed documentation in order to write a custom django management command that generated a number of pretend Therapists and added them to a .csv file. I then imported this file into my database using another custom django command. ChatGPT was used extensively for me to be able to implement this feature as it was brand new to me but it will now serve to be a very useful tool moving forward in my development career.

**Generate .csv file with fake data for database**

    import django
    import os
    import sys
    from pathlib import Path
    from faker import Faker
    import csv
    import random
    
    def setup_django_environment():
        # Change 'project_name' to your Django project's name
        project_path = Path('speechwell')
        sys.path.append(str(project_path))
        os.environ['DJANGO_SETTINGS_MODULE'] = 'speechwell.settings'
        django.setup()
    
    def generate_therapists_csv():
        from resources.models import Therapist, Specialty
    
    # Create a list of specialty choices
    SPECIALTY_CHOICES = [
        'Apraxia of Speech', 'Stuttering – Stammering', 'Dysarthria', 'Lisping',
        'Spasmodic Dysphonia', 'Developmental Language Disorder', 'Muteness – Selective Mutism',
        'Aphasia', 'Speech Delay'
    ]

    # Check and create specialties in the database if they don't exist
    for specialty_name in SPECIALTY_CHOICES:
        Specialty.objects.get_or_create(name=specialty_name)

    fake = Faker()
    therapists = []
    for _ in range(30):
        therapist = {
            'username': fake.user_name(),
            'email': fake.email(),
            'phone_number': fake.phone_number(),
            'address': fake.address(),
            'bio': fake.text(max_nb_chars=500),
            'location': random.choice(['Scotland', 'North', 'Midlands', 'South', 'Wales']),
            # Generate random number of specialties per therapist
            'specialty': ', '.join(random.sample(SPECIALTY_CHOICES, random.randint(1, len(SPECIALTY_CHOICES))))
        }
        therapists.append(therapist)

    filename = 'therapists.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['username', 'email', 'phone_number', 'address', 'bio', 'location', 'specialty']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for therapist in therapists:
            writer.writerow(therapist)

        print(f"Therapists data saved to {filename}")
    
    if __name__ == "__main__":
        setup_django_environment()
        generate_therapists_csv()


**Import data from CSV into database**
    
    class Command(BaseCommand):
    help = 'Imports therapists from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        with open(file_path, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Create Therapist objects from CSV data and save them
                therapist = Therapist(
                    username=row['username'],
                    email=row['email'],
                    phone_number=row['phone_number'],
                    address=row['address'],
                    bio=row['bio'],
                    location=row['location'],
                    # Parse and assign specialty appropriately to Therapist objects
                    # This might require additional processing based on how you've saved specialties in the CSV
                )
                therapist.save()

        self.stdout.write(self.style.SUCCESS('Therapists imported successfully'))
	

## Credits 

I used the following resources during the development of my project

### Content 

- The text for the disorders content was taking from a variety of sources in collaboration and consultation with my partner who is a qualified speech therapist herself and the use of search engines. Copyright information for each resource was included at the bottom of each article where possible. A full list of sources can be provided upon request.
- The following tutorial was used to help me initialise my project and set up OS variables and project folder structure [Django Recipe Sharing Tutorial by Dee Mc](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy&ab_channel=DeeMc)
- The fonts used in the project were sourced from [Google Fonts](https://fonts.google.com/)
- Code checking and inspiration was implemented by 'rubber ducking' with and pasting errors into [ChatGPT](https://chat.openai.com/)
- I used [Lucid](https://lucid.app/) to design an initial ERD
- I used the website [app.logo](https://app.logo.com/) to design a logo and navbar brand icon
- This readme file was produced using [Stack Edit](https://stackedit.io/)

### Media
- Images and media storage provided by ["Cloudinary"](https://cloudinary.com/)
 - Profie pictures and hero image were taken from ["Pexels"](https://www.pexels.com/)
 - Fonts used throughout the site were Open Sans from [Google Fonts](https://fonts.google.com/) and bootstrap 'lead' and 'display' classes.
 
### Additional acknowledgemnts
 - Additional assistance was provided by all members of my Code Institute cohort and the staff and facilitators who were invaluable with their technical expertise and unwavering support.
 - My partner Carys who pushed me and encouraged me and supported me every step of the way while also providing a vast amount of technical expertise on the subject of speech therapy.
 - My children, who can finally have 'the big computer' back to play Roblox and Minecraft.
