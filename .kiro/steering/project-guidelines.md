# Git-Done Project Guidelines

## Project Vision
Git-Done is a minimalist, deadline-driven productivity widget for developers that connects directly to GitHub activity. The core philosophy is "lofi-beats-to-code-to" meets high-stakes accountability.

## Design Principles
- **Minimalist First**: Every feature should serve the core purpose. No feature bloat.
- **Dark Mode Native**: Design for dark mode first, light mode is secondary.
- **Glassmorphism Aesthetic**: Clean, modern card-based layouts with subtle transparency effects.
- **Monospaced Typography**: Use monospaced fonts for countdowns and code-related elements.

## Tone & Voice
- **Direct and Encouraging**: "You've got 24 hours to merge the feature branch."
- **Success Focused**: "Commit verified. Well done."
- **No Stress Language**: Motivating without being anxiety-inducing.

## Technical Standards
- **Backend**: Python Flask with PostgreSQL (AWS RDS)
- **Frontend**: Vanilla HTML/CSS/JS - no heavy frameworks
- **Progressive Web App**: Must be installable on mobile
- **GitHub Integration**: OAuth2 authentication and webhook handling

## Code Quality
- Keep functions small and focused
- Use meaningful variable names
- Comment complex logic
- Follow PEP 8 for Python code
- Use semantic HTML and modern CSS practices