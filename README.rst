Travel Memories
Store and share the favorite things you did as you travel.

Getting Up and Running Locally
=============

1. Clone this repo by either running ``git clone https://github.com/DoomPatrol/travel-memories.git`` or downloading as a zip file in the upper right
2. Create a virtual environment with your preferred package. I personally prefer virtualenv (https://virtualenv.pypa.io/en/stable/)
3. Run ``pip install -r requirements/local.txt`` to install all of the dependencies
4. Next you will need to create your database. This projects uses Postgres, so you will need to install that first if you don't already have it. Once you know Postgres is installed run ``createdb travel_memories``. 
5. Your database likely needs credentials, which you should now add to the ``DATABASES`` setting in config/settings/base.py
6. Next Run ``python manage.py migrate`` to run all of the model migrations
7. Finally, run ``python manage.py runserver`` and your local host should be up and running

Notes
=====

- When you create an account locally, it asks to confirm your email. When dev mode, it sends the "email" to the console, where you can get the link you need to confirm your email