# GitHub Integration Spec

## Overview
Implement GitHub OAuth2 authentication and webhook handling to verify goal completion based on repository activity.

## Requirements

### Authentication
- [ ] GitHub OAuth2 login flow
- [ ] Store user GitHub ID and access token
- [ ] Session management
- [ ] Logout functionality

### Webhook Setup
- [ ] Automatically create webhooks on user repositories
- [ ] Handle webhook verification and security
- [ ] Process push events for commit message matching
- [ ] Process issue events for issue closure
- [ ] Process pull request events for PR merges

### Goal Completion Logic
- [ ] Parse completion conditions (commit messages, issue numbers, PR merges)
- [ ] Verify webhook payload authenticity
- [ ] Update goal status when conditions are met
- [ ] Send real-time updates to frontend

## Implementation Tasks

### Phase 1: OAuth Setup
1. Register GitHub OAuth app
2. Implement OAuth flow endpoints
3. Add user session management
4. Update frontend login flow

### Phase 2: Webhook Infrastructure
1. Create webhook management endpoints
2. Implement payload verification
3. Add webhook event processing
4. Create goal completion checker

### Phase 3: Real-time Updates
1. Add WebSocket support for live updates
2. Implement frontend notification system
3. Add success animations

## Acceptance Criteria
- Users can log in with GitHub
- Webhooks are automatically created for goal repositories
- Goals are marked complete when conditions are met
- Frontend updates in real-time when goals complete