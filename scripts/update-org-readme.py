#!/usr/bin/env python3
import os
import requests
from datetime import datetime
import sys
import re

def get_org_repos(org_name, token):
    """Fetch all repositories for an organization"""
    headers = {'Authorization': f'token {token}'}
    repos = []
    page = 1
    
    while True:
        url = f'https://api.github.com/orgs/{org_name}/repos?page={page}&per_page=100'
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Error fetching repos: {response.status_code}")
            sys.exit(1)
            
        data = response.json()
        if not data:
            break
            
        repos.extend(data)
        page += 1
    
    return {repo['name']: repo for repo in repos}

def get_workflows(org_name, repo_name, token):
    """Get workflows for a repository"""
    headers = {'Authorization': f'token {token}'}
    url = f'https://api.github.com/repos/{org_name}/{repo_name}/actions/workflows'
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        workflows = response.json().get('workflows', [])
        # Filter for active workflows and prioritize main CI workflows
        active_workflows = [w for w in workflows if w.get('state') == 'active']
        # Prioritize common CI workflow names
        priority_names = ['ci', 'main', 'test', 'build', 'deploy']
        
        def workflow_priority(workflow):
            name_lower = workflow['name'].lower()
            for i, priority in enumerate(priority_names):
                if priority in name_lower:
                    return i
            return len(priority_names)
        
        return sorted(active_workflows, key=workflow_priority)[:2]  # Limit to 2 badges per repo
    return []

def generate_badge_url(org_name, repo_name, workflow_file):
    """Generate GitHub Actions badge URL"""
    return f'https://github.com/{org_name}/{repo_name}/actions/workflows/{workflow_file}/badge.svg'

def update_core_repositories_section(readme_content, org_name, repos_data, token):
    """Update the Core Repositories section with CI/CD badges"""
    
    # Define the core repositories and their current info
    core_repo_info = {
        'wiba-platform': {'purpose': 'Core API server & backend', 'team': '`@backend-team`'},
        'wiba-python-client': {'purpose': 'Official Python SDK', 'team': '`@sdk-team`'},
        'wiba-models': {'purpose': 'ML models & training', 'team': '`@ml-team`'},
        'wiba-web-interface': {'purpose': 'Frontend application', 'team': '`@frontend-team`'},
        'wiba-infrastructure': {'purpose': 'DevOps & deployment', 'team': '`@devops-team`'},
        'wiba-datasets': {'purpose': 'Research data', 'team': '`@research-team`'},
        'wiba-docs': {'purpose': 'Documentation hub', 'team': '`@docs-team`'}
    }
    
    # Build the new Core Repositories table
    new_table = "### **Core Repositories**\n\n"
    new_table += "| Repository | Purpose | Team Ownership | CI/CD Status |\n"
    new_table += "|------------|---------|----------------|---------------|\n"
    
    for repo_name in core_repo_info.keys():
        if repo_name in repos_data:
            repo = repos_data[repo_name]
            info = core_repo_info[repo_name]
            
            # Get workflows for this repo
            workflows = get_workflows(org_name, repo_name, token)
            
            # Generate badges
            badges = []
            for workflow in workflows:
                badge_url = generate_badge_url(org_name, repo_name, workflow['path'].split('/')[-1])
                workflow_url = f"https://github.com/{org_name}/{repo_name}/actions/workflows/{workflow['path'].split('/')[-1]}"
                badges.append(f"[![{workflow['name']}]({badge_url})]({workflow_url})")
            
            badge_str = ' '.join(badges) if badges else '*No CI/CD*'
            
            new_table += f"| **[{repo_name}](https://github.com/{org_name}/{repo_name})** | {info['purpose']} | {info['team']} | {badge_str} |\n"
        else:
            # Repository not found, keep original entry without CI/CD
            info = core_repo_info[repo_name]
            new_table += f"| **[{repo_name}](https://github.com/{org_name}/{repo_name})** | {info['purpose']} | {info['team']} | *Repository not found* |\n"
    
    # Add timestamp
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    new_table += f"\n*CI/CD status last updated: {timestamp} UTC*\n"
    
    # Replace the Core Repositories section
    # Pattern to match from "### **Core Repositories**" to the next major section
    pattern = r'### \*\*Core Repositories\*\*.*?(?=\n## |\Z)'
    
    # Perform the replacement
    updated_content = re.sub(pattern, new_table, readme_content, flags=re.DOTALL)
    
    return updated_content

def main():
    # Get environment variables
    org_name = os.environ.get('GITHUB_ORG')
    token = os.environ.get('GITHUB_TOKEN')
    
    if not org_name or not token:
        print("Error: GITHUB_ORG and GITHUB_TOKEN environment variables must be set")
        sys.exit(1)
    
    # Read the existing README
    readme_path = 'profile/README.md'  # Organization profile README path
    
    try:
        with open(readme_path, 'r') as f:
            readme_content = f.read()
    except FileNotFoundError:
        print(f"Error: {readme_path} not found")
        sys.exit(1)
    
    print(f"Fetching repositories for organization: {org_name}")
    repos_data = get_org_repos(org_name, token)
    
    print(f"Found {len(repos_data)} repositories")
    
    # Update the Core Repositories section
    updated_content = update_core_repositories_section(readme_content, org_name, repos_data, token)
    
    # Write back to file
    with open(readme_path, 'w') as f:
        f.write(updated_content)
    
    print(f"{readme_path} updated successfully!")

if __name__ == '__main__':
    main()