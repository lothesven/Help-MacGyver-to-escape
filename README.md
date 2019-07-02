# Help-MacGyver-to-escape
Labyrinth game coded with Pygame in which the player plays MacGyver. Player needs to collect objects in the labyrinth to pass the guard at exit location.

Please check the link below for source code:
https://github.com/lothesven/Help-MacGyver-to-escape


# Setup steps


1) The game needs a virtual environment to work properly. You can use Virtualenv for example. To do so, please run the command line below in your command terminal:

pip install virtualenv


2) Create a virtual environement. If you are using virtualenv, you can create a virtual environment named  "env" by running the command lines that are relevant to your local system:

***********
Windows (Powershell):

virtualenv -p py env
./env/scripts/activate.ps1

***********
Mac OS or LINUX:

virtualenv -p python3 env
source env/bin/activate

***********

3) Install all dependencies contained in "requirements.txt". To do so, please run the command line below in command terminal:

pip install -r requirements.txt


4) Launch the game by running the command line below in command terminal:

python mazegyver.py