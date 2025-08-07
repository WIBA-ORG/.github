# WIBA Research Organization

The **WIBA (What Is Being Argued?)** research organization at the University of California, Riverside develops an advanced argument mining platform for computational linguistics research. This repository serves as the central hub for collaborative development of our research infrastructure.

## 🏗️ **Organization Structure**

Our platform is organized into specialized repositories for efficient team collaboration:

### **Core Repositories**

| Repository | Purpose | Team Ownership | Status |
|------------|---------|----------------|---------|
| **[wiba-platform](https://github.com/WIBA-ORG/wiba-platform)** | Core API server & backend | `@backend-team` | ✅ Production Ready |
| **[wiba-python-client](https://github.com/WIBA-ORG/wiba-python-client)** | Official Python SDK | `@sdk-team` | ✅ PyPI Ready |
| **[wiba-models](https://github.com/WIBA-ORG/wiba-models)** | ML models & training | `@ml-team` | ✅ Optimized Dependencies |
| **[wiba-web-interface](https://github.com/WIBA-ORG/wiba-web-interface)** | Frontend application | `@frontend-team` | ✅ Production Ready |
| **[wiba-infrastructure](https://github.com/WIBA-ORG/wiba-infrastructure)** | DevOps & deployment | `@devops-team` | ✅ Enhanced Monitoring |
| **[wiba-datasets](https://github.com/WIBA-ORG/wiba-datasets)** | Research data | `@research-team` | ✅ Clean & Organized |
| **[wiba-docs](https://github.com/WIBA-ORG/wiba-docs)** | Documentation hub | `@docs-team` | 📚 Comprehensive |
| **[wiba-status](https://github.com/WIBA-ORG/wiba-status)** | System monitoring | `@devops-team` | ✅ Active Monitoring |

## **Research Platform Access**

### **Academic Collaboration**

WIBA is a research project at UC Riverside focused on advancing computational argument mining. The platform provides tools for researchers to analyze argumentative text structures.

**Key Services:**
- **API Platform**: [api.wiba.dev](https://api.wiba.dev)
- **System Status**: [status.wiba.dev](https://status.wiba.dev)
- **Documentation**: [docs.wiba.dev](https://docs.wiba.dev)

### **Getting Started**

#### **Team Access**

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

# Set up your development environment (Python 3.9+ required)
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
✅ Unit Tests      # pytest across Python 3.9-3.12
✅ Integration     # Cross-repository compatibility
✅ Build Process   # Deployment artifacts
✅ Health Checks   # System monitoring and status
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
pip install torch transformers dspy-ai  # Optimized dependencies
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
**Repositories:** `wiba-infrastructure`, `wiba-status`
```bash
# Key areas of focus:
- Container orchestration and deployment
- Health monitoring and system status (status.wiba.dev)
- Infrastructure as code
- Performance optimization and scaling

# Development setup:
cd wiba-infrastructure
docker-compose -f monitoring/docker-compose.yml up
terraform plan  # Infrastructure planning

# Status monitoring:
cd wiba-status
python -m pytest tests/  # Health check tests
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

## **Research Collaboration**

The WIBA platform represents a comprehensive research infrastructure for computational argument mining:

**Research Excellence** - Rigorous methodology with peer-reviewed approaches  
**Quality Assurance** - Comprehensive testing ensures reliable research tools  
**Academic Collaboration** - Clear processes for multi-institutional research  
**Scalable Architecture** - Infrastructure designed for research scalability  
**Open Science** - Transparent documentation and reproducible methods  

**University of California, Riverside** - Advancing computational linguistics research through innovative argument mining technologies.

---

*For research collaboration inquiries and latest developments, contact airan002@ucr.edu or monitor this organization for updates.*