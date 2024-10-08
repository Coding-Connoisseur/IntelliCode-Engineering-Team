# collaborative_ai_team/agents/database_agent.py
from utils.communication import CommunicationChannel

class DatabaseAgent:
    def __init__(self, communication_channel: CommunicationChannel):
        self.tasks = []
        self.communication_channel = communication_channel
        
        # Subscribe to backend agent updates
        self.communication_channel.subscribe('backend', self.handle_backend_update)

    def execute_tasks(self, tasks, team_leader):
        """
        Execute assigned database tasks and update the team leader on progress.
        """
        self.tasks = tasks
        for task in self.tasks:
            # Placeholder logic for each task
            if task == "Set up Database":
                self.setup_database(team_leader)
            elif task == "Design Schema":
                self.design_schema(team_leader)
            else:
                self.unknown_task(task, team_leader)

    def setup_database(self, team_leader):
        """
        Simulate database setup.
        """
        result = "DatabaseAgent: Database setup completed."
        team_leader.update_project_log(result)

    def design_schema(self, team_leader):
        """
        Simulate schema design.
        """
        result = "DatabaseAgent: Database schema design completed."
        team_leader.update_project_log(result)

    def handle_backend_update(self, message):
        print(f"FrontEndAgent received update from Backend: {message}")

    def unknown_task(self, task, team_leader):
        """
        Handle unknown tasks.
        """
        result = f"DatabaseAgent: Unknown task '{task}' - no action taken."
        team_leader.update_project_log(result)
