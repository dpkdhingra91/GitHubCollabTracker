import requests
import os

# Set your GitHub username and token
GITHUB_USERNAME = "your_github_username"
GITHUB_TOKEN = "your_github_token"

# GitHub API URL
BASE_URL = "https://api.github.com"

def get_repos(username):
    url = f"{BASE_URL}/user/repos"
    repos = []
    page = 1
    while True:
        response = requests.get(url, auth=(username, GITHUB_TOKEN), params={'page': page, 'per_page': 100})
        if response.status_code != 200:
            print(f"Error fetching repos: {response.json()}")
            break
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos

def get_collaborators(repo):
    url = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{repo}/collaborators"
    response = requests.get(url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))
    if response.status_code == 200:
        return [collaborator['login'] for collaborator in response.json()]
    else:
        print(f"Error fetching collaborators for {repo}: {response.json()}")
        return []
def main():
    repos = get_repos(GITHUB_USERNAME)
    all_collaborators = {}
    for repo in repos:
        repo_name = repo['name']
        collaborators = get_collaborators(repo_name)
        all_collaborators[repo_name] = collaborators
        print(f"Repository: {repo_name}, Collaborators: {collaborators}")
    
    # Optionally, you can save this information to a file or process it further
    print("\nOverall Collaborators:")
    for repo, collaborators in all_collaborators.items():
        print(f"{repo}: {collaborators}")
if __name__ == "__main__":
    main()