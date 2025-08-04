# Contributing to WIBA

Thank you for your interest in contributing to WIBA! This document provides guidelines and information for contributors.

## 🚀 Quick Start

### Prerequisites
- GitHub account
- Git installed and configured
- Python 3.9+ (for Python repositories)
- Node.js 18+ (for frontend repositories)

### Getting Started
1. **Fork** the repository you want to contribute to
2. **Clone** your fork locally
3. **Create** a feature branch
4. **Make** your changes
5. **Test** thoroughly
6. **Submit** a pull request

## 📋 Development Workflow

### 1. Setting Up Your Development Environment

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/REPOSITORY_NAME.git
cd REPOSITORY_NAME

# Add upstream remote
git remote add upstream https://github.com/WIBA-ORG/REPOSITORY_NAME.git

# Install dependencies
pip install -r requirements.txt  # Python repos
npm install                      # Frontend repos

# Install development dependencies
pip install black isort flake8 mypy pytest  # Python
npm install --save-dev                       # Frontend
```

### 2. Creating a Feature Branch

```bash
# Sync with upstream
git fetch upstream
git checkout main
git merge upstream/main

# Create feature branch
git checkout -b feature/your-feature-name
```

### 3. Making Changes

#### Code Quality Standards
- **Python**: Follow PEP 8, use type hints, write docstrings
- **JavaScript/TypeScript**: Use ESLint configuration, write JSDoc comments
- **Documentation**: Update relevant docs for any changes

#### Testing Requirements
- **Unit Tests**: All new code must have corresponding tests
- **Integration Tests**: Update integration tests for API changes
- **Manual Testing**: Test your changes in a realistic environment

### 4. Committing Changes

Use [Conventional Commits](https://www.conventionalcommits.org/) format:

```bash
# Format: type(scope): description
git commit -m "feat(api): add batch processing to argument detection

- Implement batch processing for /api/detect endpoint
- Add input validation for batch requests
- Update documentation and examples
- Add comprehensive test coverage"
```

**Commit Types:**
- `feat`: New features
- `fix`: Bug fixes
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

## 🧪 Testing Guidelines

### Running Tests

```bash
# Python repositories
pytest tests/ -v --cov=src
python -m pytest tests/test_specific.py::test_function

# Frontend repositories
npm test
npm run test:e2e
npm run test:coverage
```

### Writing Tests

#### Python Test Example
```python
import pytest
from src.api.detect import detect_arguments

def test_detect_arguments_single_text():
    """Test argument detection with single text input."""
    result = detect_arguments("Climate change requires action.")
    
    assert result.is_argument is True
    assert result.confidence > 0.5
    assert result.text == "Climate change requires action."

def test_detect_arguments_batch():
    """Test argument detection with batch input."""
    texts = ["Argument text.", "Non-argument text."]
    results = detect_arguments(texts)
    
    assert len(results) == 2
    assert all(hasattr(r, 'is_argument') for r in results)
```

#### Integration Test Example
```python
def test_api_detect_endpoint(client, auth_headers):
    """Test /api/detect endpoint integration."""
    response = client.post(
        "/api/detect",
        json={"texts": ["Test argument."]},
        headers=auth_headers
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "results" in data
    assert len(data["results"]) == 1
```

## 📝 Documentation Standards

### Code Documentation

#### Python Docstrings
```python
def extract_topics(texts: List[str], batch_size: int = 4) -> List[ExtractionResult]:
    """Extract topics from argumentative texts.
    
    Args:
        texts: List of texts to analyze for topic extraction
        batch_size: Number of texts to process in each batch
        
    Returns:
        List of ExtractionResult objects containing extracted topics
        
    Raises:
        ValidationError: If texts are empty or invalid
        ModelError: If topic extraction model fails
        
    Example:
        >>> results = extract_topics(["We need renewable energy."])
        >>> print(results[0].topic)  # "renewable energy"
        
    Note:
        This function requires the wibaextract model to be loaded.
    """
```

#### API Documentation
All API endpoints must be documented with OpenAPI/Swagger:

```python
@app.post("/api/detect", response_model=DetectionResponse)
async def detect_arguments(
    request: TextsInput,
    api_key: str = Security(get_api_token)
) -> DetectionResponse:
    """
    Detect arguments in text using WIBA models.
    
    This endpoint analyzes input texts to identify argumentative content
    using fine-tuned language models. Supports both single text and
    batch processing for efficient analysis.
    
    - **texts**: Single string or list of strings to analyze
    - **Returns**: Detection results with confidence scores
    """
```

### README Updates
When adding new features, update the relevant README.md:
- Add usage examples
- Update installation instructions if needed
- Document new API endpoints or parameters
- Update performance benchmarks if applicable

## 🔍 Code Review Process

### Submitting Pull Requests

1. **PR Description**: Use the provided template
2. **Link Issues**: Reference related issues
3. **Screenshots**: Include for UI changes
4. **Breaking Changes**: Clearly document any breaking changes

### Review Criteria

Reviewers will check:
- **Functionality**: Does the code work as intended?
- **Tests**: Is there adequate test coverage?
- **Documentation**: Are changes properly documented?
- **Style**: Does code follow project conventions?
- **Performance**: Are there any performance implications?
- **Security**: Are there any security concerns?

### Addressing Review Feedback

```bash
# Make requested changes
git add .
git commit -m "address review feedback: improve error handling"

# Push changes (no need for new PR)
git push origin feature/your-feature-name
```

## 🏗️ Repository-Specific Guidelines

### wiba-platform (Backend)
- **Database Changes**: Include migrations
- **API Changes**: Update OpenAPI documentation
- **Performance**: Include benchmark comparisons
- **Security**: Follow OWASP guidelines

### wiba-python-client (SDK)
- **Backward Compatibility**: Avoid breaking changes
- **Examples**: Update usage examples
- **Type Hints**: Comprehensive type annotations
- **Documentation**: Clear docstrings and examples

### wiba-models (ML)
- **Model Files**: Use Git LFS for large files
- **Benchmarks**: Include performance metrics
- **Documentation**: Document model architecture
- **Evaluation**: Include evaluation scripts

### wiba-web-interface (Frontend)
- **Accessibility**: Follow WCAG 2.1 guidelines
- **Responsive Design**: Test on multiple devices
- **Performance**: Optimize bundle size
- **User Experience**: Follow design system

## 🚨 Common Issues

### CI/CD Failures

#### Test Failures
```bash
# Run specific failing test
pytest tests/test_failing.py::test_function -v

# Run with debugging
pytest tests/ -v -s --tb=long
```

#### Code Style Issues
```bash
# Fix formatting
black src/
isort src/

# Check style
flake8 src/
mypy src/
```

#### Security Issues
```bash
# Check for vulnerabilities
pip-audit requirements.txt

# Update vulnerable packages
pip install --upgrade vulnerable-package
```

### Git Issues

#### Sync Fork with Upstream
```bash
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

#### Rebase Feature Branch
```bash
git checkout feature/your-feature
git rebase main
git push origin feature/your-feature --force-with-lease
```

## 📊 Performance Guidelines

### Benchmarking
- Include before/after performance metrics for significant changes
- Use consistent test environments
- Document performance implications in PRs

### Optimization
- Profile code before optimizing
- Measure impact of optimizations
- Consider memory usage and CPU performance
- Test with realistic datasets

## 🔒 Security Guidelines

### Sensitive Data
- Never commit API keys, passwords, or tokens
- Use environment variables for configuration
- Sanitize user inputs
- Follow principle of least privilege

### Dependencies
- Regularly update dependencies
- Review security advisories
- Use `pip-audit` for Python dependencies
- Monitor for known vulnerabilities

## 🎯 Best Practices

### Git Workflow
- Use descriptive commit messages
- Keep commits focused and atomic
- Rebase feature branches before merging
- Use signed commits when possible

### Code Organization
- Follow single responsibility principle
- Use meaningful variable and function names
- Keep functions small and focused
- Separate concerns appropriately

### Error Handling
- Use specific exception types
- Provide helpful error messages
- Log errors appropriately
- Handle edge cases gracefully

## 🤝 Community Guidelines

### Code of Conduct
- Be respectful and inclusive
- Welcome newcomers and help them learn
- Provide constructive feedback
- Focus on what's best for the community

### Communication
- Use clear, professional language
- Be patient with questions and learning
- Share knowledge and help others
- Participate in discussions constructively

## 📞 Getting Help

### Resources
- **Documentation**: [wiba-docs](https://github.com/WIBA-ORG/wiba-docs)
- **Discussions**: GitHub Discussions in relevant repositories
- **Issues**: Repository-specific issue trackers

### Contacts
- **General Questions**: Create an issue in the relevant repository
- **Security Issues**: Email airan002@ucr.edu privately first
- **Organization Access**: Contact @armaniii

---

Thank you for contributing to WIBA! Your contributions help advance research in computational argumentation and make argument mining more accessible to researchers and developers worldwide. 🌟