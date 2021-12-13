# Santa's Kitchen Helper

![Add Image Here]()

Introduction/Overview

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
