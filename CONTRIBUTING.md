# Contributing to Git-Done

Thank you for your interest in contributing to Git-Done! This document provides guidelines for contributing to this minimalist, deadline-driven productivity widget for developers.

## Project Vision

Git-Done is a minimalist, deadline-driven productivity widget for developers that connects directly to GitHub activity. The core philosophy is "lofi-beats-to-code-to" meets high-stakes accountability.

## MIT License Compliance

- All contributions must be compatible with the MIT License
- Contributors retain copyright to their contributions
- By submitting a pull request, you agree to license your contribution under MIT
- Include proper attribution for any third-party code or assets
- Ensure all dependencies are MIT-compatible or have permissive licenses

## Hacktoberfest Participation

- **Quality Over Quantity**: Focus on meaningful contributions that improve the project
- **No Spam PRs**: Avoid trivial changes like whitespace fixes or minor typos
- **Valid Contributions Include**:
  - Bug fixes with proper testing
  - Feature enhancements that align with project vision
  - Documentation improvements
  - Performance optimizations
  - Accessibility improvements
  - UI/UX enhancements following design principles
- **PR Requirements**:
  - Clear description of changes and motivation
  - Reference any related issues
  - Include screenshots for UI changes
  - Test your changes thoroughly

## Development Workflow

### Issue Assignment Policy

**⚠️ IMPORTANT: Only work on issues that are assigned to you**

- **Request Assignment First**: Comment on an issue asking to be assigned before starting work
- **Wait for Assignment**: Do not begin work until a maintainer assigns the issue to you
- **Respect the Queue**: If someone else is already assigned or has requested assignment, please find another issue
- **Fair Contribution**: This policy ensures fairness for all contributors and prevents duplicate work
- **Unassigned Work**: PRs for unassigned issues may be closed, even if the work is good quality

**Exception**: You may work on issues labeled `good first issue` or `help wanted` without assignment, but please comment your intent first.

### Getting Started

1. **Find an Issue**: Browse open issues and find one that interests you
2. **Request Assignment**: Comment on the issue asking to be assigned
3. **Wait for Confirmation**: A maintainer will assign the issue to you
4. **Fork the repository** on GitHub
5. **Clone your fork** locally:
   ```bash
   git clone https://github.com/[your-username]/git-done.git
   cd git-done
   ```
6. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
7. **Run the application**:
   ```bash
   python application.py
   ```

### Making Changes

1. **Create a feature branch** from main:
   ```bash
   git checkout -b feature/issue-123-amazing-feature
   ```
2. **Make your changes** following the code quality guidelines
3. **Test thoroughly** - ensure your changes work as expected
4. **Commit with descriptive messages**:
   ```bash
   git commit -m 'Fix: Add amazing feature that improves user experience (#123)'
   ```
5. **Push to your fork**:
   ```bash
   git push origin feature/issue-123-amazing-feature
   ```
6. **Open a Pull Request** with:
   - Clear description of changes
   - Reference to the assigned issue (e.g., "Fixes #123")
   - Screenshots for UI changes

## AWS Architecture Protection

⚠️ **CRITICAL SAFETY MEASURES** ⚠️

- **Protected Files**: 
  - Any CloudFormation templates
  - AWS configuration files
  - Environment variables containing AWS credentials
  - Database connection strings
- **Deployment Safety**:
  - Test all changes locally first
  - Never commit AWS credentials or sensitive data
  - Use environment variables for configuration
  - Validate database migrations before deployment
- **Force Push Policy**: 
  - **NEVER** force push to main branch
  - **NEVER** force push to shared feature branches
  - Only force push to your own feature branches if absolutely necessary
  - Use `git push --force-with-lease` if force push is required

## Design Principles

- **Minimalist First**: Every feature should serve the core purpose. No feature bloat.
- **Dark Mode Native**: Design for dark mode first, light mode is secondary.
- **Glassmorphism Aesthetic**: Clean, modern card-based layouts with subtle transparency effects.
- **Monospaced Typography**: Use monospaced fonts for countdowns and code-related elements.

## Code Quality Standards

- Keep functions small and focused
- Use meaningful variable names
- Comment complex logic
- Follow PEP 8 for Python code
- Use semantic HTML and modern CSS practices

## Code Review Standards

- **Security First**: All PRs reviewed for security implications
- **Performance Impact**: Consider performance implications of changes
- **Backward Compatibility**: Maintain API compatibility where possible
- **Documentation**: Update relevant documentation with changes
- **Testing**: Include tests for new features and bug fixes

## Issue Management

### Reporting Issues

- Use issue templates when available
- Provide clear reproduction steps for bugs
- Include environment details (browser, OS, etc.)
- Search existing issues before creating new ones
- Label issues appropriately (bug, enhancement, documentation, etc.)

### Working on Issues

- **Assignment Required**: Only work on issues assigned to you
- **Request Process**: Comment "I'd like to work on this" and wait for assignment
- **Time Commitment**: If assigned, please provide updates within a week
- **Stale Assignments**: Issues may be reassigned if no progress is made after a week
- **Communication**: Keep maintainers updated on your progress

### For Maintainers

- **Fair Assignment**: Assign issues on a first-come, first-served basis
- **Regular Check-ins**: Follow up on assigned issues that show no activity
- **Reassignment Policy**: Reassign stale issues after reasonable timeframe

## Community Standards

- **Be Respectful**: Follow the code of conduct
- **Be Constructive**: Provide helpful feedback in reviews
- **Be Patient**: Maintainers review PRs as time permits
- **Be Collaborative**: Work together to improve the project

## Types of Contributions Welcomed

### Bug Fixes
- Fix broken functionality
- Resolve performance issues
- Address security vulnerabilities

### Feature Enhancements
- Improve existing features
- Add new functionality that aligns with project vision
- Enhance user experience

### Documentation
- Improve README and guides
- Add code comments
- Create tutorials or examples

### UI/UX Improvements
- Enhance visual design
- Improve accessibility
- Optimize for mobile devices

### Technical Improvements
- Code refactoring
- Performance optimizations
- Test coverage improvements

## Questions?

- Open an issue for questions about the project
- Use GitHub Discussions for broader conversations
- Check existing issues and documentation first

Thank you for contributing to Git-Done! 🚀