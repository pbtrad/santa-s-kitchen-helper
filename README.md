# Santa's Kitchen Helper
To view the live website, click [here](https://santas-kitchen-helper.herokuapp.com/).  \
  \
![Website responsive mockup](/assets/readme/amiresponsive.png)

Santa's Kitchen Helper is a tool that allows families to organise their events better. It is made mostly for Christmas, yet can be developed for all year round.  \
The application has features that allow families to create their own group, add events and also add reminders of what dishes they will bring to said event.
## Contents

- [UX](#ux)
  - User Stories
  - Design
    - Wireframes
    - Color Scheme
    - Typography
    - Imagery
- [Features](#features)
  - Exisiting Features
  - Features Left to be Implemented
- [Technologies Used](#technologies-used)
  - Languages
  - Frameworks and Libraries
  - Tools
  - Dependencies
- [Testing](#testing)
- [Deployment](#deployment)
  - Github
  - Heroku
- [Credits and Acknowledgments](#credits-and-acknowledgments)

---

## UX

### User Stories

#### As a first time visitor, I want to:
1. Have a mission statement to know what the website is about.
2. Have a way to easily navigate.
3. Be able to register for an account.
4. Get feedback on the requirements of the registration process.
5. Have the option to join a family group.
6. Have the option of creating a family group.
7. Be able to create events in the family group.
8. Be able to see events from other members.

#### As a recurring user, I want to: 
9. Not have to sign in every time I visit the page.
10. Be able to add dishes that I will bring.
11. See previous events.
12. Have the option to edit my profile.
13. See the contact details for the creators.

### Design

### WireFrames
+ All wireframes can be viewed in their file format [here](assets/wireframes)
+ All wireframe images can be viewed [here](WIREFRAME.md)

### Database Design

Using MongoDb NoSQL database the following collections were created.

Users collection:

| Title        | Data Type|
| ------------- |:-------------:|
| id:      | ObjectId |
| name      | string      |
| email | string      |
| pass_ | binary_hashed_string |

Event collection:

| Title        | Data Type|
| ------------- |:-------------:|
| id:      | ObjectId |
| name      | string      |
| date | string      |
| event | string |
| email | string |
| family | string |
| description | string |
| active | boolean |
| food | array |
                   
Family collection:
| Title        | Data Type|
| ------------- |:-------------:|
| id:      | ObjectId |
| name      | string      |
| date | string      |
| events | array |
| members | array |


#### Typograhpy

Heading font: [Emily's Candy](https://fonts.google.com/specimen/Emilys+Candy?subset=latin&query=candy)
Letter font: [Fuzzy Bubbles](https://fonts.google.com/specimen/Fuzzy+Bubbles?query=fuzzy)

[Back to Contents](#contents)

---

## Features

### Existing Features

### Features Left to be Implemented

[Back to Contents](#contents)

---

## Technologies Used
+ HTML - Skeleton frame of the application.
+ CSS - Beautifies the skeleton (HTML).
+ JavaScript - Allows for user interaction and limited dynamic function on the application.
+ Python - Allows dynamic function and back end programs to run. These programs (frameworks, libraries, and databases) are:
    + Flask - Allows use of templating, security, user searching, and other critical functions.
    + Pymongo - Allows Flask (Python) to communicate with MongoDB.
    + PythonDNS - Allows for DNS data transfer.
    + Werkzeug - Encrypts data as it is sent between the user and server.
    + Datetime - Allows Python to take a date/time stamp.
    + Random - Allows for a random number generator.
+ MongoDB - NoSQL database that the application communicates with and stores information on.

### Tools
+ [Adobe Color Wheel](https://color.adobe.com/create/color-wheel)
    + Used to help pick color schemes.
+ [Balsamiq](https://balsamiq.com/)
    + Used to produce the wireframes.
+ [Bootstrap](https://getbootstrap.com/)
    + Used as framework.
+ [GitHub](https://github.com/)
    + Used for version control and deploys application information to Heroku.
+ [Google Fonts](https://fonts.google.com/)
    + Imported font families from here.
+ [Heroku](https://www.heroku.com/)
    + Site where application is deployed.
+ [Jigsaw (Validation Service)](https://jigsaw.w3.org/css-validator/)
    + Used to identify errors in CSS.
+ [JSHint](https://jshint.com/)
    + Used to identify errors in JavaScript.
+ [jQuery](https://jquery.com/)
    + JS library used with Bootstrap.
+ [Lighthouse](https://developers.google.com/web/tools/lighthouse)
    + Used to check for performance, accessibility, best practices, and SEO.
+ [PEP8 online](http://pep8online.com/)
    + Used to identify errors in Python.
+ [RandomKeygen](https://randomkeygen.com/)
    + Used to create random secret key for "env.py"
+ [TinyPNG](https://tinypng.com/)
    + Used to Minimize KB load per image.
+ [W3C Validator](https://validator.w3.org/)
    + Used to identify errors in markup.
+ [VSCode](https://code.visualstudio.com/)
    + Integrated development environment used.
[Back to Contents](#contents)

---

## Testing

1. Have a mission statement to know what the website is about.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Santa letter modal | Navigate to main page, see pop-up modal | Read mission statement | Works as expected |
| Santa letter modal | Click on "About" button, see pop-up modal | Read mission statement | Works as expected |

<details><summary>Screenshots</summary>

![Mission statement image](/assets/readme/user-stories/about-statement.png)
![About button image](/assets/readme/user-stories/about-button.png)

</details>

2. Have a way to easily navigate.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Navigation bar | Click on navigation buttons | Get moved between pages | Works as expected |

<details><summary>Screenshots</summary>

![Navigation bar image](/assets/readme/user-stories/navigation-bar.png)

</details>

3. Be able to register for an account.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Registration form | Navigate to "Register" page and fill out form | Create a usable account | Works as expected |

<details><summary>Screenshots</summary>

![Registration form image](/assets/readme/user-stories/registration-form.png)
![Registration success image](/assets/readme/user-stories/registration-form.png)

</details>

4. Get feedback on the requirements of the registration process.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Registration form | Input details in form | Get visual feedback for good or invalid data | Works as expected |

<details><summary>Screenshots</summary>

![Registration form image](/assets/readme/user-stories/registration-form.png)
![Registration form with invalid data image](/assets/readme/user-stories/registration-form-invalid.png)

</details>

5. Have the option to join a family group.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  |  |  | Works as expected |
|  |  |  | Works as expected |

<details><summary>Screenshots</summary>

![Proof image]()
![Proof image]()

</details>

6. Have the option of creating a family group.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  |  |  | Works as expected |
|  |  |  | Works as expected |

<details><summary>Screenshots</summary>

![Proof image]()
![Proof image]()

</details>

7. Be able to create events in the family group.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  |  |  | Works as expected |
|  |  |  | Works as expected |

<details><summary>Screenshots</summary>

![Proof image]()
![Proof image]()

</details>

8. Be able to see events from other members.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  |  |  | Works as expected |
|  |  |  | Works as expected |

<details><summary>Screenshots</summary>

![Proof image]()
![Proof image]()

</details>

9. Not have to sign in every time I visit the page.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Session cookie | Navigate away from page and to page again | Stay signed in | Works as expected |

<details><summary>Screenshots</summary>

![Signed in image](/assets/readme/user-stories/signed-in.png)
![Closed tab image](/assets/readme/user-stories/signed-in-closed.png)
![Signed in image](/assets/readme/user-stories/signed-in-returned.png)

</details>

10. Be able to add dishes that I will bring.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  |  |  | Works as expected |
|  |  |  | Works as expected |

<details><summary>Screenshots</summary>

![Proof image]()
![Proof image]()

</details>

11. See previous events.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  |  |  | Works as expected |
|  |  |  | Works as expected |

<details><summary>Screenshots</summary>

![Proof image]()
![Proof image]()

</details>

12. Have the option to edit my profile.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
|  |  |  | Works as expected |
|  |  |  | Works as expected |

<details><summary>Screenshots</summary>

![Proof image]()
![Proof image]()

</details>

13. See the contact details for the creators.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Contact page | Click on creator social media link | New tab opens to clicked link | Works as expected |

<details><summary>Screenshots</summary>

![Contact page image](/assets/readme/user-stories/contact-page.png)
![Contact social button image](/assets/readme/user-stories/contact-social-button.png)

</details>  

[Back to Contents](#contents)

---

## Deployment

Santa's Kitchen Helper is deployed at https://santas-kitchen-helper.herokuapp.com/ on Heroku.

**Cloning Santa's Kitchen Helper from GitHub:

Install the following:

* Git
* PIP
* Python3

Create an account at [MongoDB](https://www.mongodb.com/3) to construct database.

* 1: Clone Santa's Kitchen Helper repository using Git by typing the following command into the terminal.

```
git clone https://github.com/pbtrad/santa-s-kitchen-helper.git
```

* 2: Go to this folder in your terminal.
* 3: Enter the following command into your terminal to create virtual environment

```
virtualenv venv 
```

* 4: Intialize the environment by entering the following command.

```
source venv\bin\activate
```

* 5: Install the requirements and dependancies from the requirements.txt file.

```
pip3 install -r requirements.txt
```

* 6: In an IDE create an env.py file where SECRET_KEY and MONGO_URI can be stored, then follow the schema in the schema file.
* 7: Run the application by entering.

```
flask run
```

or

```
python3 app.py
```

**Deploying the website to Heroku**:

* 1: Create a requirements.txt file by entering the following command.

```
pip3 freeze > requirements.txt
```

* 2: Create a Procfile.

```
echo web: python app.py > Procfile
```

* 3: Push files to your repository.
* 4: On Heroku dashboard create a new app.
* 5: Select deployment method and select GitHub.
* 6: On the dashboard set config variables:

| Key  | Value |
| ------------- | ------------- |
| IP  | 0.0.0.0  |
| PORT  | 5000  |
| MONGO_URI | mongodb+srv://:@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority  |
| SECRET_KEY | "your_secret_key" |

* 7: Select the deploy button on the Heroku dashboard.
* 8: Your site is deployed by Heroku.

[Back to Contents](#contents)

---

## Credits and Acknowledgments

### Images

- [Candy Cane Logo/Favicon](https://www.flaticon.com/authors/freepik)
- [Background Image](https://unsplash.com/photos/7VOyZ0-iO0o)
- [Calendar Image](https://unsplash.com/photos/bwOAixLG0uc)

Team 7 🎄

[Back to Contents](#contents)

---
