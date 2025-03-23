import sys

def verify_os():
    print("Checking OS...")
    if platform.system() == "Linux":
        print("OS is a Linux.")
    else:
        print("Exodus is only compatible with Linux")
        sys.exit(1)

def verify_module_installation(module):
    print(f"Checking if module '{module}' is working...")
    try:
        __import__(module)
        print(f"Module '{module}' is working!")
    except Exception as e:
        print(f"Module '{module}' is not working. Is he installed?")
        sys.exit(1)

def clone_repo(repo_url):
    print(f"Cloning repo '{repo_url}'...")
    try:
        git.Repo.clone_from(repo_url, "Exodus")
        print(f"Repo '{repo_url}' successfully cloned!")
    except Exception as e:
        print(f"Error while cloning repo '{repo_url}'.\n{e}")
        sys.exit(1)

def create_db(db_name):
    db_path = "Exodus/databases/"
    db_path += db_name
    print(f"Creating a new database '{db_name}'...")
    try:
        connection = sqlite3.connect(db_path)
        print(f"Database '{db_name}' added!")
    except Exception as e:
        print(f"Error while creating database '{db_name}'.")
        sys.exit(1)

########################

verify_module_installation("platform")
verify_module_installation("sqlite3")
verify_module_installation("git")
import platform
import sqlite3
import git

verify_os()

print("\n[ EXODUS ASSISTANT ]")
print("[1]\t\tInstall Exodus")
print("")
option_taken = input("Option: ")
if option_taken == "1":
    print("")
    clone_repo("https://github.com/Lichen13/Exodus")
    create_db("root_db.db")
else:
    print("\nWrong option.")
