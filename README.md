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

### Tools

- [Font Awesome](https://fontawesome.com/)

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
