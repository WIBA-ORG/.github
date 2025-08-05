#!/usr/bin/env python3
import os
import requests
from datetime import datetime
import sys

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
    
    return sorted(repos, key=lambda x: x['name'].lower())

def get_workflows(org_name, repo_name, token):
    """Get workflows for a repository"""
    headers = {'Authorization': f'token {token}'}
    url = f'https://api.github.com/repos/{org_name}/{repo_name}/actions/workflows'
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json().get('workflows', [])
    return []

def generate_badge_url(org_name, repo_name, workflow_file):
    """Generate GitHub Actions badge URL"""
    return f'https://github.com/{org_name}/{repo_name}/actions/workflows/{workflow_file}/badge.svg'

def generate_readme_content(org_name, repos_data):
    """Generate markdown content for README"""
    content = f"# {org_name} CI/CD Status Dashboard\n\n"
    content += f"*Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC*\n\n"
    
    # Create status summary
    total_repos = len(repos_data)
    repos_with_ci = sum(1 for repo in repos_data if repo['workflows'])
    
    content += f"## Summary\n"
    content += f"- Total Repositories: {total_repos}\n"
    content += f"- Repositories with CI/CD: {repos_with_ci}\n\n"
    
    # Create the main table
    content += "## Repository Status\n\n"
    content += "| Repository | Description | CI/CD Status | Last Push |\n"
    content += "|------------|-------------|--------------|------------|\n"
    
    for repo in repos_data:
        repo_name = repo['name']
        description = repo['description'] or '*No description*'
        if len(description) > 50:
            description = description[:47] + '...'
        
        # Format last push date
        last_push = datetime.strptime(repo['pushed_at'], '%Y-%m-%dT%H:%M:%SZ')
        last_push_str = last_push.strftime('%Y-%m-%d')
        
        # Create badge links
        badges = []
        for workflow in repo['workflows']:
            if workflow.get('state') == 'active':
                badge_url = generate_badge_url(org_name, repo_name, workflow['path'].split('/')[-1])
                workflow_url = f"https://github.com/{org_name}/{repo_name}/actions/workflows/{workflow['path'].split('/')[-1]}"
                badge_name = workflow['name']
                badges.append(f"[![{badge_name}]({badge_url})]({workflow_url})")
        
        badge_str = ' '.join(badges) if badges else '*No CI/CD*'
        
        # Add row to table
        content += f"| [{repo_name}](https://github.com/{org_name}/{repo_name}) | {description} | {badge_str} | {last_push_str} |\n"
    
    # Add legend
    content += "\n## Legend\n"
    content += "- 🟢 Passing - All checks passed\n"
    content += "- 🔴 Failing - One or more checks failed\n"
    content += "- 🟡 In Progress - Workflow currently running\n"
    content += "- ⚪ No Status - No recent runs\n"
    
    return content

def main():
    # Get environment variables
    org_name = os.environ.get('GITHUB_ORG')
    token = os.environ.get('GITHUB_TOKEN')
    
    if not org_name or not token:
        print("Error: GITHUB_ORG and GITHUB_TOKEN environment variables must be set")
        sys.exit(1)
    
    print(f"Fetching repositories for organization: {org_name}")
    repos = get_org_repos(org_name, token)
    
    print(f"Found {len(repos)} repositories")
    
    # Fetch workflows for each repo
    repos_data = []
    for repo in repos:
        print(f"Checking workflows for {repo['name']}...")
        workflows = get_workflows(org_name, repo['name'], token)
        
        repo_data = {
            'name': repo['name'],
            'description': repo['description'],
            'pushed_at': repo['pushed_at'],
            'workflows': workflows
        }
        repos_data.append(repo_data)
    
    # Generate README content
    readme_content = generate_readme_content(org_name, repos_data)
    
    # Write to file
    with open('README.md', 'w') as f:
        f.write(readme_content)
    
    print("README.md updated successfully!")

if __name__ == '__main__':
    main()