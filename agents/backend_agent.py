# collaborative_ai_team/agents/backend_agent.py
from utils.communication import CommunicationChannel


class BackEndAgent:
    def __init__(self, communication_channel: CommunicationChannel):
        self.tasks = []
        self.communication_channel = communication_channel
        
        # Subscribe to backend agent updates
        self.communication_channel.subscribe('backend', self.handle_backend_update)

# In backend_agent.py
    def execute_tasks(self, tasks, team_leader):
        for task in self.tasks:
            try:
                if task == "Develop API":
                    self.develop_api(team_leader)
                elif task == "Integrate Database":
                    self.integrate_database(team_leader)
                else:
                    self.unknown_task(task, team_leader)
            except Exception as e:
                error_message = f"BackEndAgent: Error executing task '{task}': {e}"
                team_leader.update_project_log(error_message)
                print(error_message)  # For real-time error tracking


    def develop_api(self, team_leader):
        """
        Simulate API development.
        """
        result = "BackEndAgent: API development completed."
        team_leader.update_project_log(result)

    def integrate_database(self, team_leader):
        """
        Simulate database integration.
        """
        result = "BackEndAgent: Database integration completed."
        team_leader.update_project_log(result)

    def handle_backend_update(self, message):
        print(f"FrontEndAgent received update from Backend: {message}")

    def unknown_task(self, task, team_leader):
        """
        Handle unknown tasks.
        """
        result = f"BackEndAgent: Unknown task '{task}' - no action taken."
        team_leader.update_project_log(result)
