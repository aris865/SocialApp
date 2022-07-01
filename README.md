How to run with Visual Studio Code:

Download and extract the source code.

Inside the app's folder open a command promt (Windows) do the following to create a Python Virtual Environment

# macOS/Linux
# You may need to run sudo apt-get install python3-venv first
python3 -m venv .venv

# Windows
# You can also use py -3 -m venv .venv
python -m venv .venv

Open the app's folder with Visual Studio Code

Select View->Command Palette->Python:Select Interpreter and choose the one located in the virtual environment.

Then select Terminal->New Terminal (There now should be (venv) showing in the command prompt) 

Run python manage.py migrate and python manage.py makemigrations

Then python manage.py runserver and the server will be up and running.

You can create a new admin user by typing python manage.py createsuperuser

