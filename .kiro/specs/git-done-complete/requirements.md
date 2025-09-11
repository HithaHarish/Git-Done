# Requirements Document

## Introduction

This specification defines the requirements for a complete Git-Done application that allows developers to create deadline-driven productivity goals connected to their GitHub activity. The core feature is an embeddable countdown widget that can be integrated into Notion pages, providing public accountability and motivation. The application must handle GitHub OAuth authentication, webhook processing for goal completion verification, and provide embeddable widgets that work seamlessly in external platforms.

## Requirements

### Requirement 1

**User Story:** As a developer, I want to authenticate with my GitHub account, so that I can create goals tied to my repositories and have my commits/PRs automatically tracked.

#### Acceptance Criteria

1. WHEN a user visits the application THEN the system SHALL display a "Login with GitHub" button
2. WHEN a user clicks the GitHub login button THEN the system SHALL redirect to GitHub OAuth authorization
3. WHEN GitHub OAuth is successful THEN the system SHALL store the user's GitHub ID and access token securely
4. WHEN a user is authenticated THEN the system SHALL display their GitHub username and provide access to the dashboard
5. WHEN a user logs out THEN the system SHALL clear their session and redirect to the login page

### Requirement 2

**User Story:** As a developer, I want to create countdown goals with specific completion conditions, so that I can hold myself accountable to shipping code by a deadline.

#### Acceptance Criteria

1. WHEN an authenticated user accesses the dashboard THEN the system SHALL display a goal creation form
2. WHEN creating a goal THEN the system SHALL require a description, deadline, GitHub repository URL, and completion condition
3. WHEN a goal is created THEN the system SHALL validate the repository URL belongs to the authenticated user
4. WHEN a goal is saved THEN the system SHALL automatically set up a webhook on the specified repository
5. WHEN webhook setup fails THEN the system SHALL display an error message and not create the goal
6. WHEN a goal is created successfully THEN the system SHALL display it in the user's goal list with an active countdown

### Requirement 3

**User Story:** As a developer, I want my goals to be automatically marked complete when I fulfill the completion condition, so that I don't have to manually update the status.

#### Acceptance Criteria

1. WHEN a webhook receives a push event THEN the system SHALL check if any commit messages match active goal completion conditions
2. WHEN a webhook receives an issues event THEN the system SHALL check if the closed issue matches any active goal completion conditions
3. WHEN a webhook receives a pull request event THEN the system SHALL check if the merged PR matches any active goal completion conditions
4. WHEN a completion condition is met THEN the system SHALL update the goal status to "completed" and record the completion timestamp
5. WHEN a goal is completed THEN the system SHALL stop the countdown timer and display a success message
6. WHEN webhook payload verification fails THEN the system SHALL reject the request and log the security violation

### Requirement 4

**User Story:** As a developer, I want to embed my countdown timers in my Notion pages, so that I can have public accountability and motivation visible in my workspace.

#### Acceptance Criteria

1. WHEN a goal is created THEN the system SHALL generate a unique embeddable URL for that goal's countdown widget
2. WHEN the embeddable URL is accessed THEN the system SHALL display only the countdown timer without navigation or other UI elements
3. WHEN embedded in Notion THEN the widget SHALL display the goal description, countdown timer, and current status
4. WHEN a goal is completed THEN the embedded widget SHALL update to show the success message in real-time
5. WHEN the embedded widget loads THEN it SHALL be responsive and work properly within Notion's iframe constraints
6. WHEN the goal deadline passes THEN the embedded widget SHALL display an urgent state with appropriate styling

### Requirement 5

**User Story:** As a developer, I want the countdown timers to update in real-time, so that I can see the exact time remaining and feel the urgency of approaching deadlines.

#### Acceptance Criteria

1. WHEN a countdown timer is displayed THEN the system SHALL update the time remaining every second
2. WHEN less than 1 hour remains THEN the system SHALL change the timer styling to indicate urgency
3. WHEN the deadline passes THEN the system SHALL display "00:00:00" and show an overdue message
4. WHEN a goal is completed THEN the system SHALL immediately stop the countdown and show completion status
5. WHEN multiple goals are displayed THEN each timer SHALL update independently without affecting others
6. WHEN the browser tab is inactive THEN the timers SHALL continue updating accurately when the tab becomes active again

### Requirement 6

**User Story:** As a developer, I want to manage my goals (view, edit, delete), so that I can maintain control over my accountability system.

#### Acceptance Criteria

1. WHEN a user accesses their dashboard THEN the system SHALL display all their goals (active, completed, and overdue)
2. WHEN a user wants to delete a goal THEN the system SHALL remove the webhook from GitHub and delete the goal from the database
3. WHEN a user views goal details THEN the system SHALL show creation date, deadline, completion condition, and current status
4. WHEN a goal is overdue THEN the system SHALL clearly indicate this with appropriate styling and messaging
5. WHEN a user has no goals THEN the system SHALL display an encouraging message to create their first goal
6. WHEN goals are listed THEN they SHALL be sorted by deadline (soonest first) with completed goals at the bottom

### Requirement 7

**User Story:** As a developer, I want the application to handle errors gracefully, so that I have a reliable experience even when GitHub is unavailable or webhooks fail.

#### Acceptance Criteria

1. WHEN GitHub API is unavailable THEN the system SHALL display appropriate error messages and allow retry
2. WHEN webhook delivery fails THEN GitHub SHALL retry according to its retry policy
3. WHEN repository access is revoked THEN the system SHALL handle the error and notify the user
4. WHEN invalid completion conditions are provided THEN the system SHALL validate and provide helpful error messages
5. WHEN the database is unavailable THEN the system SHALL display a maintenance message
6. WHEN JavaScript fails to load THEN the system SHALL provide a basic HTML fallback for goal viewing

### Requirement 8

**User Story:** As a developer, I want the embedded widgets to be secure and performant, so that they don't compromise the security or performance of my Notion workspace.

#### Acceptance Criteria

1. WHEN an embedded widget is requested THEN the system SHALL validate the goal ID and return 404 for invalid requests
2. WHEN serving embedded widgets THEN the system SHALL set appropriate CORS headers for Notion integration
3. WHEN embedded widgets load THEN they SHALL be optimized for minimal bandwidth usage
4. WHEN multiple embedded widgets are on the same page THEN they SHALL not interfere with each other
5. WHEN embedded widgets are accessed THEN the system SHALL not expose sensitive user information
6. WHEN serving static assets for embedded widgets THEN the system SHALL set appropriate cache headers for performance