// Git-Done Frontend Application
class GitDoneApp {
    constructor() {
        this.goals = [];
        this.countdownIntervals = new Map();
        
        // Check if the dashboard exists on the page (i.e., user is logged in)
        if (document.getElementById('dashboard')) {
            this.bindEvents();
            this.loadGoals();
        }
    }

    bindEvents() {
        document.getElementById('goal-form').addEventListener('submit', (e) => {
            e.preventDefault();
            this.createGoal();
        });
    }

    async createGoal() {
        const form = document.getElementById('goal-form');
        
        // The backend knows the user, so we don't need to send user_github_id
        const goalData = {
            description: document.getElementById('description').value,
            deadline: document.getElementById('deadline').value,
            repo_url: document.getElementById('repo-url').value,
            completion_condition: document.getElementById('completion-condition').value
        };

        try {
            const response = await fetch('/api/goals', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(goalData)
            });

            if (response.ok) {
                const newGoal = await response.json();
                console.log('New goal created:', newGoal);
                this.goals.push(newGoal);
                this.renderGoals(); // Re-render all goals to include the new one
                form.reset();
            } else {
                const errorText = await response.text();
                console.error('Failed to create goal:', errorText);
                alert('Failed to create goal: ' + errorText);
            }
        } catch (error) {
            console.error('Error creating goal:', error);
        }
    }

    async loadGoals() {
        try {
            // This will now only fetch goals for the logged-in user
            const response = await fetch('/api/goals');
            if (response.ok) {
                this.goals = await response.json();
                console.log('Loaded goals:', this.goals);
                this.renderGoals();
            } else {
                console.error('Failed to load goals:', response.status);
            }
        } catch (error) {
            console.error('Error loading goals:', error);
        }
    }

    renderGoals() {
        const container = document.getElementById('goals-container');
        container.innerHTML = ''; // Clear existing goals

        this.goals.forEach(goal => {
            const goalElement = this.createGoalWidget(goal);
            container.appendChild(goalElement);
        });
    }

    createGoalWidget(goal) {
        const widget = document.createElement('div');
        widget.className = 'goal-widget card'; // Added .card for better styling
        widget.id = `goal-${goal.id}`;
        
        let statusText = 'Counting down...';
        if (goal.status === 'completed') {
            statusText = 'Completed! Well done.';
        } else if (goal.status === 'failed') {
            statusText = "Time's up!";
        }

        const embedUrl = goal.embed_url || 'Not available';
        
        widget.innerHTML = `
            <h3>${goal.description}</h3>
            <p><strong>Repository:</strong> <a href="${goal.repo_url}" target="_blank">${goal.repo_url}</a></p>
            <div class="countdown" id="countdown-${goal.id}">--:--:--</div>
            <div class="goal-status" id="status-${goal.id}">${statusText}</div>
            <div class="embed-info">
                <p><strong>Embed URL:</strong> <input type="text" value="${embedUrl}" readonly onclick="this.select()" style="width: 100%; margin-top: 5px; padding: 5px; background: #161b22; border: 1px solid #30363d; color: #f0f6fc; border-radius: 4px;"></p>
                <small style="color: #8b949e;">Copy this URL to embed in Notion or other platforms</small>
            </div>
        `;

        // Start countdown after the widget is added to DOM
        if (goal.status === 'active') {
            setTimeout(() => this.startCountdown(goal), 100);
        } else {
            widget.querySelector(`#countdown-${goal.id}`).classList.add('completed');
        }

        return widget;
    }

    startCountdown(goal) {
        const countdownElement = document.getElementById(`countdown-${goal.id}`);
        if (!countdownElement) {
            console.error(`Countdown element not found for goal ${goal.id}`);
            return;
        }

        const deadline = new Date(goal.deadline);
        console.log(`Starting countdown for goal ${goal.id}, deadline: ${deadline}`);

        const updateCountdown = () => {
            const now = new Date();
            const timeLeft = deadline - now;

            if (timeLeft <= 0) {
                countdownElement.textContent = '00:00:00';
                countdownElement.classList.add('urgent');
                document.getElementById(`status-${goal.id}`).textContent = "Time's up! Push that commit!";
                clearInterval(this.countdownIntervals.get(goal.id));
                return;
            }

            const hours = Math.floor(timeLeft / (1000 * 60 * 60));
            const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
            const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

            countdownElement.textContent = `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

            if (timeLeft < 3600000) { // Less than 1 hour
                countdownElement.classList.add('urgent');
            }
        };

        // Clear any existing interval for this goal before starting a new one
        if (this.countdownIntervals.has(goal.id)) {
            clearInterval(this.countdownIntervals.get(goal.id));
        }
        
        updateCountdown();
        const interval = setInterval(updateCountdown, 1000);
        this.countdownIntervals.set(goal.id, interval);
    }
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new GitDoneApp();
});