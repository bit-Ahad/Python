# Used to create a vitual enviourment in a folder where you can use download any version serperatly and use it despite of any version installed in your computer


# 1. python -m venv myenv
# This creates a folder named myenv/ containing a standalone Python environment.
# You can name it anything (venv, env, .venv, etc.), but .venv is common for keeping it hidden.

# 2. Activate the virtual environment
# myenv\Scripts\activate

# 3. Install packages
# Now you're working inside the virtual environment, so any pip installs will go here:
# pip install requests

# 5. Deactivate the virtual environment
# To exit the virtual environment:
# deactivate

# -------------------------------

# Freeze dependencies (optional)
# To record your environment's dependencies:
# pip freeze > requirements.txt
# This makes it easy to reproduce the environment elsewhere with:
# pip install -r requirements.txt