# WIBA-ORG: Collaborative Development Hub

Welcome to the **WIBA (What Is Being Argued?)** research organization! This is your central hub for collaborative development of the argument mining platform.

## 🏗️ **Organization Structure**

Our platform is organized into specialized repositories for efficient team collaboration:

### **Core Repositories**

| Repository | Purpose | Team Ownership | Status |
|------------|---------|----------------|---------|
| **[wiba-platform](https://github.com/WIBA-ORG/wiba-platform)** | Core API server & backend | `@backend-team` | ✅ Production Ready |
| **[wiba-python-client](https://github.com/WIBA-ORG/wiba-python-client)** | Official Python SDK | `@sdk-team` | ✅ PyPI Ready |
| **[wiba-models](https://github.com/WIBA-ORG/wiba-models)** | ML models & training | `@ml-team` | ✅ Git LFS Enabled |
| **[wiba-web-interface](https://github.com/WIBA-ORG/wiba-web-interface)** | Frontend application | `@frontend-team` | 🚧 In Development |
| **[wiba-infrastructure](https://github.com/WIBA-ORG/wiba-infrastructure)** | DevOps & deployment | `@devops-team` | 🚧 Setup Complete |
| **[wiba-datasets](https://github.com/WIBA-ORG/wiba-datasets)** | Research data | `@research-team` | ✅ Clean & Organized |
| **[wiba-docs](https://github.com/WIBA-ORG/wiba-docs)** | Documentation hub | `@docs-team` | 📚 Comprehensive |

## 🚀 **Getting Started**

### **1. Team Onboarding**

#### **Join Your Team**
```bash
# Request access from @armaniii to be added to appropriate teams:
# @backend-team, @ml-team, @frontend-team, @devops-team, @research-team, @docs-team
```

#### **Clone Your Repository**
```bash
# Clone the repository you'll be working on
git clone https://github.com/WIBA-ORG/[repository-name].git
cd [repository-name]

# Set up your development environment
pip install -r requirements.txt  # Python repos
npm install                      # Frontend repos
```

### **2. Development Workflow**

#### **🌟 Feature Development Process**

```bash
# 1. Create a feature branch
git checkout -b feature/your-feature-name

# 2. Make your changes
# - Follow code style guidelines
# - Add comprehensive tests
# - Update documentation

# 3. Commit with clear messages
git add .
git commit -m "Add new argument detection endpoint

- Implement /api/detect with batch processing
- Add input validation and error handling  
- Include comprehensive test coverage
- Update API documentation"

# 4. Push and create Pull Request
git push origin feature/your-feature-name
# Create PR through GitHub UI
```

#### **🔍 Pull Request Requirements**

**Before Creating a PR:**
- ✅ All tests pass locally
- ✅ Code follows style guidelines (black, isort, flake8)
- ✅ Documentation is updated
- ✅ Branch is up-to-date with main

**PR Template Checklist:**
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature  
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests pass
- [ ] Manual testing completed

## Documentation
- [ ] Code comments added
- [ ] API docs updated
- [ ] README updated if needed
```

### **3. Automated Quality Assurance**

#### **🔄 CI/CD Pipeline**

Our repositories automatically run comprehensive checks:

```yaml
Automated Checks:
✅ Code Quality    # black, isort, flake8, mypy
✅ Security Scan   # pip-audit, TruffleHog  
✅ Unit Tests      # pytest across Python 3.8-3.12
✅ Integration     # Cross-repository compatibility
✅ Build Process   # Deployment artifacts
✅ Documentation   # Link checking, completeness
```

**Status Checks Required:**
- All repositories require passing CI before merge
- Security scans must pass
- Code review from `CODEOWNERS` required

#### **📊 Monitoring Your Changes**

Check your PR status:
- **GitHub Actions**: See real-time CI/CD progress
- **Status Checks**: All must be green before merge
- **Review Requests**: Automatically assigned based on `CODEOWNERS`

## 🎯 **Team Responsibilities**

### **Backend Team** (`@backend-team`)
**Repository:** `wiba-platform`
```bash
# Key areas of focus:
- Core API endpoints (/api/detect, /api/extract, /api/stance)
- Database models and migrations
- Authentication and security
- Performance optimization

# Development setup:
cd wiba-platform
pip install -r requirements.txt
python -m pytest tests/
python -m src.main  # Start development server
```

### **ML Team** (`@ml-team`) 
**Repository:** `wiba-models`
```bash
# Key areas of focus:
- Model training and fine-tuning
- Performance evaluation and benchmarking
- Model deployment and optimization
- Research integration

# Development setup:
cd wiba-models
pip install torch transformers dspy-ai
python shared/utils/model_loader.py  # Test model loading
```

### **Frontend Team** (`@frontend-team`)
**Repository:** `wiba-web-interface`
```bash
# Key areas of focus:
- Modern web interface development
- User experience and accessibility
- API integration and state management
- Responsive design

# Development setup:
cd wiba-web-interface
npm install
npm run dev  # Start development server
```

### **DevOps Team** (`@devops-team`)
**Repository:** `wiba-infrastructure`
```bash
# Key areas of focus:
- Container orchestration and deployment
- Monitoring and observability
- Infrastructure as code
- Performance and scaling

# Development setup:
cd wiba-infrastructure
docker-compose -f monitoring/docker-compose.yml up
terraform plan  # Infrastructure planning
```

## 🔧 **Advanced Workflows**

### **Cross-Repository Integration**

#### **Testing Integration Changes**
```bash
# Trigger cross-repository integration tests
git push origin main  # Automatically triggers integration tests
# Or manually trigger:
curl -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/WIBA-ORG/wiba-platform/dispatches \
  -d '{"event_type":"integration-test"}'
```

#### **Coordinated Releases**
```bash
# 1. Update version compatibility in DEPENDENCIES.md
# 2. Create release PRs across repositories
# 3. Coordinate release timing
# 4. Update integration tests

# Release checklist:
- [ ] All integration tests pass
- [ ] Documentation updated
- [ ] Version numbers coordinated
- [ ] Release notes prepared
```

### **Working with Large Models**

#### **Git LFS for Model Files**
```bash
# wiba-models repository uses Git LFS
git lfs track "*.safetensors" "*.pkl" "*.bin"
git add .gitattributes
git add model-file.safetensors
git commit -m "Add new model checkpoint"
git push origin main  # Automatically handles large files
```

## 📚 **Development Guidelines**

### **Code Style Standards**

#### **Python (Backend, ML, Client)**
```bash
# Format code
black src/
isort src/
flake8 src/

# Type checking
mypy src/ --ignore-missing-imports

# Testing
pytest tests/ -v --cov=src
```

#### **JavaScript/TypeScript (Frontend)**
```bash
# Format code
npm run format
npm run lint

# Testing
npm test
npm run test:e2e
```

### **Documentation Standards**

#### **Code Documentation**
```python
def detect_arguments(texts: List[str], batch_size: int = 16) -> List[DetectionResult]:
    """Detect arguments in text using WIBA models.
    
    Args:
        texts: List of input texts to analyze
        batch_size: Number of texts to process in each batch
        
    Returns:
        List of DetectionResult objects with confidence scores
        
    Raises:
        ValidationError: If input texts are invalid
        APIError: If detection service fails
        
    Example:
        >>> results = detect_arguments(["Climate change is real."])
        >>> print(results[0].is_argument)  # True
    """
```

#### **API Documentation**
```yaml
# OpenAPI/Swagger documentation required for all endpoints
paths:
  /api/detect:
    post:
      summary: Detect arguments in text
      description: Analyze text to identify argumentative content
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TextsInput'
```

## 🚨 **Common Issues & Solutions**

### **CI/CD Troubleshooting**

#### **Failed Tests**
```bash
# Check test output in GitHub Actions
# Run tests locally to debug:
pytest tests/ -v -x  # Stop on first failure
pytest tests/test_api.py::test_specific_function  # Run specific test
```

#### **Code Quality Issues**
```bash
# Fix formatting issues
black --check src/  # Check what needs formatting
black src/          # Apply formatting
isort --check src/  # Check import sorting
isort src/          # Fix import sorting
```

#### **Security Scan Failures**
```bash
# Check for vulnerabilities
pip-audit requirements.txt
# Update vulnerable packages
pip install --upgrade package-name
```

### **Branch Protection Bypassed Messages**
```
remote: Bypassed rule violations for refs/heads/main:
remote: - Changes must be made through a pull request.
```
This is expected for repository owners during initial setup. Normal development should use PRs.

## 🎉 **Success Metrics**

Track your team's progress:

### **Quality Metrics**
- ✅ **Test Coverage**: >90% for all repositories
- ✅ **Code Quality**: All style checks passing
- ✅ **Security**: Zero high-severity vulnerabilities
- ✅ **Documentation**: All APIs documented

### **Collaboration Metrics**
- 🔄 **Pull Requests**: Regular, focused PRs
- 👥 **Code Reviews**: Timely and thorough reviews
- 🚀 **Releases**: Coordinated, tested releases
- 📈 **Integration**: Daily cross-repo compatibility

## 🆘 **Getting Help**

### **Repository-Specific Issues**
- Create issues in the relevant repository
- Use issue templates for consistent reporting
- Tag appropriate team members

### **Organization-Wide Questions**
- **GitHub Discussions**: For design discussions and questions
- **Email**: airan002@ucr.edu for academic collaboration
- **Admin**: @armaniii for access and permissions

### **Emergency Contacts**
- **System Down**: @devops-team + @armaniii
- **Security Issue**: @security-team + @armaniii  
- **Release Coordination**: @armaniii

---

## 🌟 **Welcome to Professional Development!**

You're now part of a **world-class development ecosystem** designed for:

🔥 **High-Velocity Development** - Ship features fast with confidence  
🛡️ **Quality Assurance** - Automated testing prevents production issues  
🤝 **Team Collaboration** - Clear ownership and review processes  
🚀 **Scalable Growth** - Architecture that grows with your team  
📚 **Knowledge Sharing** - Comprehensive documentation and guides  

**Happy coding, and welcome to the future of argument mining research!** ✨

---

*For the latest updates and announcements, watch this organization and enable notifications. Let's build something amazing together!* 🎯