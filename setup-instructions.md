# Organization CI/CD Status Dashboard Setup

## Overview
This automation updates the "Core Repositories" section of your GitHub organization's profile README with live CI/CD status badges for each repository.

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

### 4. Configure GitHub Token
The workflow uses the default `GITHUB_TOKEN` which is automatically provided by GitHub Actions. No additional secrets configuration is needed since the organization name is hardcoded as `WIBA-ORG`.

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
The Core Repositories section will be updated to include CI/CD badges:
```markdown
### **Core Repositories**

| Repository | Purpose | Team Ownership | CI/CD Status |
|------------|---------|----------------|---------------|
| **[wiba-platform](https://github.com/WIBA-ORG/wiba-platform)** | Core API server & backend | `@backend-team` | [![CI](badge)](link) |
| **[wiba-web-interface](https://github.com/WIBA-ORG/wiba-web-interface)** | Frontend application | `@frontend-team` | [![Tests](badge)](link) |

*CI/CD status last updated: 2025-08-05 15:30:00 UTC*
```