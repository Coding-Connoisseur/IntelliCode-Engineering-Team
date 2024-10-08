# collaborative_ai_team/agents/frontend_agent.py

class FrontEndAgent:
    def __init__(self):
        self.tasks = []

    def execute_tasks(self, tasks, team_leader):
        """
        Execute assigned front-end tasks and update the team leader on progress.
        """
        self.tasks = tasks
        for task in self.tasks:
            # Placeholder logic for each task
            if task == "Design UI":
                self.design_ui(team_leader)
            elif task == "Develop HTML/CSS/JS":
                self.develop_html_css_js(team_leader)
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

    def unknown_task(self, task, team_leader):
        """
        Handle unknown tasks.
        """
        result = f"FrontEndAgent: Unknown task '{task}' - no action taken."
        team_leader.update_project_log(result)
