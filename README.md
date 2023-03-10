# PicQuest

[View the Live Project here](https://picquest.herokuapp.com/)

![Initial Image]()
* Amiresponsive images or equivalent can go here

PicQuest is an app where users are give the task to photograph something during the day/week e.g. a duck, some street art, a stranger, an interesting plant or tree. The app allows users to easily create accounts with their names which they can add and remove images from. Users are encouraged to like images and add comments in order to to connect with eachother. Moderators can monitor images and comments posted.
The home page is centred around a “most liked” feature - presented in a continuously updating collage style. This allows users to compare and contrast their photographs with those of other users. 

## Collaborators
The team for this hackathon project is made up of [@Enquil](https://github.com/Enquil) - Jim Olesen, [@Dante-Cadiz](https://github.com/Dante-Cadiz) - [Dante Cadiz](https://www.linkedin.com/in/dante-cadiz-460735213/), [@debbiect246](https://github.com/debbiect246) - [Deborah Thompson](https://www.linkedin.com/in/debbie-thompson-1baa4733/), [@lizac9](https://github.com/lizac9) - [Liza Carelli](https://www.linkedin.com/in/liza-c-8636bb219/) and [@MariusBujor](https://github.com/MariusBujor) - Marius Bujor.

## Content
* Navigation to subheadings (UI design, UX design etc.) can go here

## UI Design
* page layout
#### **Typography:**
The font ‘Shadows Into Light’ was chosen for the title, which welcomes the user to the website and the fallback font for this is 'Cursive'. The body font is called ‘Roboto’. This font results in a more balanced and clear legibility for the remainder of website. In the case that the 'Roboto' font can't be loaded, they will fall back to a sans-serif font.

#### **Colour Scheme:**

![Colour Palette](https://res.cloudinary.com/lizac/image/upload/v1671387872/PicQuest/color_palette_qil4ra.png)


[Back to Top](#PicQuest)


## UX Design

### Wireframes:

Wireframes created in the UX stage:
![Wireframes](https://res.cloudinary.com/lizac/image/upload/v1671364439/PicQuest/wireframes1_tr1mtj.png)
![wirefr](https://res.cloudinary.com/lizac/image/upload/v1671364433/PicQuest/wireframes2_hrmgrx.png)

* Flowchart can go here
* User Experience with images and responses to user inputs
* Accessibility

## Datamodel
* Can also go into UX design subheading, but probably better with separate subheading.

## Technologies Used

### **Languages & Frameworks Used:**
- [Django](https://en.wikipedia.org/wiki/Django_(web_framework))
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/CSS)

[Back to Top](#PicQuest)

## Libraries & Programs Used:

1. [Git](https://git-scm.com/):
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
2. [GitHub](https://github.com/):
    - GitHub is used to store the project's code after being pushed from Git.
3. [Balsamiq](https://balsamiq.com/):
    - Balsamiq was used to create the wireframes during the design process.
4. [Am I responsive?](https://ui.dev/amiresponsive?url=https%3A%2F%2Fbytes.dev):
    - This application was used for visualization of the application on diferent devices.
5. [Cloudinary](https://cloudinary.com/):
    - Cloudinary was used to store and link the images.
6. [Heroku](https://dashboard.heroku.com/) 
    - Heroku was used for deployment, the specification is in the deployment section.
7. The Code Institute's GitHub full template for Python is used in order for the program to display properly in the deployed site on Heroku.
8. [Google Fonts](https://fonts.google.com/):
    - Google fonts were used to import the 'Shadows Into Light' and 'Roboto' font into the style.css file which is used on all pages throughout the project.
9. [Font Awesome](https://fontawesome.com/):
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.

## Testing
* Lighthouse tests at https://web.dev/measure/
* Pep-8
* Jigsaw validator https://jigsaw.w3.org/css-validator/
* HTML markup https://validator.w3.org/

## Deployment
The site has been deployed through Heroku.
The site has been developed on GitPod, committed and pushed to GitHub. Heroku will update automatically once the site is deployed. 

Deployment Heroku proccess:
1. Log in Heroku. 
2. Click in the "New" button in the top right.
3. Select "Create New App"
4. Choose a name to the App and choose a region.
5. Click in "Create App" button.
6. You must then create a Config Var called PORT. Set this to 8000.
7. When you create the app, you will need to add two buildpacks from the Settings tab. Select  "Add Buildpacks". 
8. Add Python and save, do the same for Node.js, in that order. Python must show first in the list.
The ordering is as follows:
    1. heroku/python
    2. heroku/nodejs
9. Go to Deploy in the nav bar. In Deployment Method, select GitHub/Connect to GitHub.
10. In Connect to GitHub, write the repository name and click in search.
11. Once the route for the repository appears under the search, click the "Connect" button.
12. The deployment can be Manual or Automatic, select your preference. Automatic has the advantage of updating your deployed site as you push the commit in GitHub.
13. Verify that "Branch to deploy" is master/main.
14. Click Deploy and the link with live project will appear
### Deployed link
[Click here to open the app!](https://picquest.herokuapp.com/)

- The link to access [this repository](https://github.com/lizac9/project3-hangman). 
- The steps to "[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo)" the repository. 
- The steps to "[Clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository)" the repository.

[Back to Top](#PicQuest)

## Site Expansion and Future Improvement
* Any ideas that might we might not have time to implement
* Sort functionality when viewing daily photos, newest/oldest/likes etc.
* Sort functionality to own page, newest/oldest/likes etc.
* Password change function
* Password reset function

## Known Issues & Bugs
* Sign-out form needs to be edited to center in screen 

## Credits

#### **Content:**
This site was created for educational purposes for the december 2022 hackathon project Re:Unity by Code Institute. 

#### **Code:**
External resources relevant to this code:
[This YouTube Tutorial](https://www.youtube.com/watch?v=1T6G7Znrbfg) for showing how to handle user image uploads to Cloudinary
[Code Institute's Django Blog Project](https://github.com/Code-Institute-Solutions/Django3blog/tree/master/12_final_deployment) for site pagination HTML

#### **Media:**
- The favicon came from [Favicon](https://favicon.io/).
- The colour palette was displayed by [Coolors](https://coolors.co/fefcf3-f5ebe0-f0dbdb-dba39a).
- The logo photo came from [dreamstime.com](https://www.dreamstime.com/vector-male-photographer-logo-camera-image113070741)

[Back to Top](#PicQuest)
