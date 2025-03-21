import sys

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

print("[ E X O D U S   A S S I S T A N T ]")
print("[1] Install Exodus")
