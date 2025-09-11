# Implementation Plan - MVP (8-Day Timeline)

- [ ] 1. Simplified Backend & Auth Setup
  - Update existing Goal model to include essential fields: embed_token, repo_owner, repo_name, webhook_id
  - Create User model with GitHub ID, username, access_token, and timestamps
  - Configure Flask app with hardcoded GitHub OAuth credentials for demo
  - Implement complete GitHub OAuth2 flow with /auth/github and /auth/callback endpoints
  - Add session management to track authenticated users
  - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5_

- [ ] 2. Core Goal & Webhook Logic
  - Create goal creation endpoint that validates repository access using GitHub API
  - Implement automatic webhook creation on GitHub repository when goal is created
  - Build webhook listener endpoint that processes GitHub push events only
  - Add commit message parsing to check for completion conditions (e.g., #feature-complete)
  - Implement goal completion logic that stops timer and updates status to "completed"
  - Add basic webhook signature verification for security
  - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 3.1, 3.4, 3.5, 3.6_

- [ ] 3. Frontend Dashboard with Real-time Countdowns
  - Update existing frontend to integrate with GitHub OAuth login flow
  - Build goal creation form with repository URL input and completion condition field
  - Implement real-time countdown timers that update every second
  - Add urgency styling (red color) when less than 1 hour remains
  - Create goal list display showing active goals with their countdowns
  - Add basic goal deletion functionality
  - Display success message when goals are completed via webhook
  - _Requirements: 1.1, 2.1, 2.6, 5.1, 5.2, 5.3, 5.4, 5.5, 6.1, 6.2, 6.3_

- [ ] 4. Embeddable Widget System
  - Generate unique embed tokens for each goal during creation
  - Create /embed/<token> endpoint that serves minimal HTML countdown widget
  - Build lightweight embedded widget with countdown timer and goal description
  - Add /api/embed/<token>/data endpoint for widget to fetch current goal status
  - Configure CORS headers to allow embedding in Notion and other platforms
  - Style embedded widget to be clean and minimal for external display
  - _Requirements: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6_

- [ ] 5. Basic Polish & Demo Preparation
  - Add basic error handling to prevent crashes during demo
  - Create simple error messages for common failures (GitHub API issues, invalid repos)
  - Add loading states and user feedback for goal creation and webhook setup
  - Test complete flow: login → create goal → push commit → verify completion
  - Test embedded widget in Notion to ensure CORS and iframe compatibility
  - Prepare demo script with sample repository and completion conditions
  - _Requirements: 7.1, 7.2, 7.3, 7.4_