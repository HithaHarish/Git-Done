# GitDone

A minimalist, deadline-driven productivity widget for developers. Connect your GitHub activity to accountability timers that only stop when you ship.

## The Concept

Set a coding goal, set a deadline, and watch the countdown tick. The timer only stops when you make the specific commit, close the issue, or merge the PR you committed to. It's "lofi-beats-to-code-to" meets high-stakes accountability.

## Features

- **GitHub Integration**: OAuth login and webhook-based goal verification
- **Dual Completion Methods**: Complete goals via commit messages OR issue closure
- **Minimalist Design**: Dark mode, glassmorphism, clean typography
- **Real-time Countdowns**: Monospaced timers that create focus
- **Embeddable Widgets**: Share your accountability publicly
- **Progressive Web App**: Install on mobile, works offline

## Quick Start

1. Install dependencies and set up environment:
   ```bash
   pip install -r requirements.txt
   cp .env.example .env
   ```

2. Update `.env` with your values (DATABASE_URL, SECRET_KEY, GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET)

3. Run the application:
   ```bash
   python application.py
   ```

4. Open `http://localhost:5000` in your browser

## Testing

Run tests with pytest:
```bash
pytest                                      # Run all tests
pytest --cov=application --cov-report=html  # With coverage report
```

Test files:
- `tests/test_api.py` - API endpoint tests
- `tests/test_models.py` - Model unit tests
- `tests/conftest.py` - Shared fixtures

## Example Goals

- "Implement user authentication" → Complete when commit contains `#auth-complete`
- "Fix critical bug" → Complete when issue #42 is closed
- "Ship new feature" → Complete when PR to main branch is merged

## Tech Stack

- **Backend**: Flask + SQLAlchemy + PostgreSQL (AWS RDS)
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Integration**: GitHub API + Webhooks
- **Deployment**: AWS Elastic Beanstalk + CloudFront

## Development

The project uses Kiro for development assistance:

- **Specs**: Feature specifications in `.kiro/specs/`
- **Hooks**: Automated workflows in `.kiro/hooks/`
- **Steering**: Project guidelines in `.kiro/steering/`

_Note: If a directory is absent then that feature wasn't used for production._
## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details on:

- Development workflow and setup
- Code quality standards
- AWS architecture protection
- Hacktoberfest participation
- MIT License compliance

Whether you're fixing bugs, adding features, or improving documentation, your contributions help make Git-Done better for everyone.

## License

MIT License


