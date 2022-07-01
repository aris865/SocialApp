# SocialApp

## Installation

Using Visual Studio Code.

Download and extract the source code.

Inside the app's folder open a command promt (Windows) and do the following to create a Python Virtual Environment

### macOS/Linux
You may need to run ```bash sudo apt-get install python3-venv ``` first

```bash
python3 -m venv .venv
```
### Windows
```bash
python -m venv .venv
```
Open the app's folder with Visual Studio Code

Select View->Command Palette->Python:Select Interpreter and choose the one located in the virtual environment.

Select Terminal->New Terminal (There now should be (venv) showing in the command prompt).

```python 
python manage.py migrate 
python manage.py makemigrations
```

## Usage
To start the live server
```python 
python manage.py runserver
```
To create new admin user
```python 
python manage.py createsuperuser
```
