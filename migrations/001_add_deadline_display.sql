-- Migration: add deadline_display to Goal
-- Adds a user-facing deadline string to avoid timezone conversion issues in the UI
ALTER TABLE goal ADD COLUMN deadline_display VARCHAR(25);
