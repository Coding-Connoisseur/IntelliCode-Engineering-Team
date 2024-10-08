# collaborative_ai_team/agents/frontend_agent.py

from utils.communication import CommunicationChannel


class FrontEndAgent:
    def __init__(self, communication_channel: CommunicationChannel):
        self.tasks = []
        self.communication_channel = communication_channel
        
        # Subscribe to backend agent updates
        self.communication_channel.subscribe('backend', self.handle_backend_update)

    def execute_tasks(self, tasks, team_leader):
        """
        Execute assigned front-end tasks and update the team leader on progress.
        """
        self.tasks = tasks
        for task in self.tasks:
            # Check for each task and call the appropriate method
            if task == "Design UI":
                self.design_ui(team_leader)
            elif task == "Develop HTML/CSS/JS":
                self.develop_html_css_js(team_leader)
            elif task == "Design User Interface":
                self.design_user_interface(team_leader)
            else:
                self.unknown_task(task, team_leader)

    def design_ui(self, team_leader):
        """
        Simulate UI design.
        """
        result = "FrontEndAgent: UI design completed."
        team_leader.update_project_log(result)

    def develop_html_css_js(self, team_leader):
        """
        Simulate front-end development (HTML, CSS, JS).
        """
        result = "FrontEndAgent: HTML, CSS, and JS development completed."
        team_leader.update_project_log(result)

    def design_user_interface(self, team_leader):
        """
        Simulate user interface design.
        """
        result = "FrontEndAgent: User Interface design completed."
        team_leader.update_project_log(result)

    def unknown_task(self, task, team_leader):
        """
        Handle unknown tasks.
        """
        result = f"FrontEndAgent: Unknown task '{task}' - no action taken."
        team_leader.update_project_log(result)

    def handle_backend_update(self, message):
        print(f"FrontEndAgent received update from Backend: {message}")
