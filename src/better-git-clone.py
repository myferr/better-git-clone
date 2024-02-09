import os

def os_do(dothis):
    os.system(dothis)

import sys
import inquirer
import colorama
import git


questions = [
    inquirer.Text(name='gh-user', message="What is the owner of the GitHub repository's username?"),
]
    
answers = inquirer.prompt(questions)
username = answers['gh-user']
        
questions = [
    inquirer.Text(name='gh-repo_name', message="What is the name of the GitHub repository?"),
]
    
answers = inquirer.prompt(questions)
repo_name = answers['gh-repo_name']
git.run(f"clone https://github.com/{username}/{repo_name}/")