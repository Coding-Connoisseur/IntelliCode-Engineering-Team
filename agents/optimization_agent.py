# collaborative_ai_team/agents/optimization_agent.py
from utils.communication import CommunicationChannel

class OptimizationAgent:
    def __init__(self, communication_channel: CommunicationChannel):
        self.tasks = []
        self.communication_channel = communication_channel
        
        # Subscribe to backend agent updates
        self.communication_channel.subscribe('backend', self.handle_backend_update)

    def execute_tasks(self, tasks, team_leader):
        """
        Execute assigned optimization tasks and update the team leader on progress.
        """
        self.tasks = tasks
        for task in self.tasks:
            # Placeholder logic for each task
            if task == "Optimize Performance":
                self.optimize_performance(team_leader)
            elif task == "Code Review":
                self.code_review(team_leader)
            else:
                self.unknown_task(task, team_leader)

    def optimize_performance(self, team_leader):
        """
        Simulate performance optimization.
        """
        result = "OptimizationAgent: Performance optimization completed."
        team_leader.update_project_log(result)

    def code_review(self, team_leader):
        """
        Simulate a code review process.
        """
        result = "OptimizationAgent: Code review completed with suggestions."
        team_leader.update_project_log(result)

    def handle_backend_update(self, message):
        print(f"FrontEndAgent received update from Backend: {message}")

    def unknown_task(self, task, team_leader):
        """
        Handle unknown tasks.
        """
        result = f"OptimizationAgent: Unknown task '{task}' - no action taken."
        team_leader.update_project_log(result)
