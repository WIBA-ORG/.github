# Organization CI/CD Status Dashboard Setup

## Overview
This automation creates a dynamic README for your GitHub organization that displays the CI/CD status of all repositories in a table format.

## Setup Instructions

### 1. Choose Repository Location
You can set this up in either:
- Your organization's `.github` repository (for organization profile README)
- A dedicated repository for monitoring (e.g., `org-dashboard`)

### 2. Create a GitHub Token
1. Go to GitHub Settings > Developer settings > Personal access tokens
2. Create a new token with these permissions:
   - `repo` (to read repository information)
   - `workflow` (to read workflow status)
3. Save the token securely

### 3. Add Files to Repository
Copy these files to your chosen repository:
- `update-org-readme.py` - The script that generates the README
- `.github/workflows/update-org-readme.yml` - The GitHub Action workflow

### 4. Configure GitHub Secrets and Variables
In your repository settings:
1. Go to Settings > Secrets and variables > Actions
2. Add a new secret:
   - Name: `ORG_README_TOKEN`
   - Value: Your GitHub token from step 2
3. Add a new variable:
   - Name: `GITHUB_ORG`
   - Value: Your organization name (e.g., `my-org`)

### 5. Enable GitHub Actions
Ensure GitHub Actions are enabled for your repository.

### 6. Run the Workflow
The workflow will:
- Run automatically every hour
- Run when you push changes to the script or workflow
- Can be triggered manually from the Actions tab

## Customization Options

### Change Update Frequency
Edit the cron schedule in `.github/workflows/update-org-readme.yml`:
```yaml
schedule:
  - cron: '0 * * * *'  # Every hour
  # Examples:
  # - cron: '*/30 * * * *'  # Every 30 minutes
  # - cron: '0 */6 * * *'   # Every 6 hours
  # - cron: '0 0 * * *'     # Daily at midnight
```

### Filter Specific Workflows
Modify the script to only show specific workflows:
```python
# In generate_readme_content function
for workflow in repo['workflows']:
    if workflow.get('state') == 'active' and workflow['name'] in ['CI', 'Deploy']:
        # Only show CI and Deploy workflows
```

### Add Additional Columns
You can extend the table with more information:
- Code coverage badges
- Security scan results
- Dependency update status
- Release version badges

### Group by Topics or Teams
Modify the script to group repositories by GitHub topics or team ownership.

## Troubleshooting

### Common Issues
1. **403 Forbidden**: Check token permissions
2. **Rate Limiting**: Reduce update frequency or implement caching
3. **No badges showing**: Ensure workflows have run at least once

### Testing Locally
```bash
export GITHUB_TOKEN="your-token"
export GITHUB_ORG="your-org"
python update-org-readme.py
```

## Example Output
Your README will look like:
```markdown
# my-org CI/CD Status Dashboard

*Last updated: 2025-08-05 15:30:00 UTC*

## Summary
- Total Repositories: 25
- Repositories with CI/CD: 20

## Repository Status

| Repository | Description | CI/CD Status | Last Push |
|------------|-------------|--------------|-----------|
| [api-service](https://github.com/my-org/api-service) | Main API service | [![CI](badge)](link) [![Deploy](badge)](link) | 2025-08-05 |
| [web-app](https://github.com/my-org/web-app) | Frontend application | [![Tests](badge)](link) | 2025-08-04 |
```