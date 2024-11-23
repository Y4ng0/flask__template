
import os
import subprocess
import requests
import json

# Get user input from cookiecutter.json context
project_name = '{{ cookiecutter.project_name }}'
author_name = '{{ cookiecutter.author_name }}'
create_github_repo = '{{ cookiecutter.create_github_repo }}'.lower() == 'yes'
github_token = '{{ cookiecutter.github_token }}'
private_repo = '{{ cookiecutter.private_repo }}'.lower() == 'yes'

# Set the project directory path
project_dir = os.path.abspath(os.path.curdir)

try:
    subprocess.run(['git', 'init'], cwd=project_dir, check=True)
    subprocess.run(['git', 'add', '.'], cwd=project_dir, check=True)
    subprocess.run(['git', 'commit', '-m', 'Initial commit'], cwd=project_dir, check=True)
except subprocess.CalledProcessError as e:
    print(f"An error occurred while initializing")
if create_github_repo and github_token:
    # Create the GitHub repository using the API
    repo_url = f'https://api.github.com/user/repos'
    headers = {
        'Authorization': f'token {github_token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    payload = {
        'name': project_name,
        'private': private_repo  # Change to True if you want a private repository
    }

    response = requests.post(repo_url, headers=headers, data=json.dumps(payload))

    if response.status_code == 201:
        print(f"GitHub repository '{project_name}' created successfully.")
        repo_html_url = response.json()['html_url']
    else:
        print(f"Failed to create GitHub repository. Status code: {response.status_code}")
        print(response.json())
        exit(1)

    # Initialize git repository and make the initial commit
    try:
        subprocess.run(['git', 'remote', 'add', 'origin', f'https://github.com/{author_name}/{project_name}.git'],
                       cwd=project_dir, check=True)
        subprocess.run(['git', 'push', '-u', 'origin', 'master'], cwd=project_dir, check=True)
        print(f"Initial commit pushed to {repo_html_url}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while pushing to GitHub: {e}")

