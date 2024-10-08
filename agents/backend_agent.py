# collaborative_ai_team/agents/backend_agent.py

class BackEndAgent:
    def __init__(self):
        self.tasks = []

    def execute_tasks(self, tasks, team_leader):
        """
        Execute assigned back-end tasks and update the team leader on progress.
        """
        self.tasks = tasks
        for task in self.tasks:
            # Placeholder logic for each task
            if task == "Develop API":
                self.develop_api(team_leader)
            elif task == "Integrate Database":
                self.integrate_database(team_leader)
            else:
                self.unknown_task(task, team_leader)

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

    def unknown_task(self, task, team_leader):
        """
        Handle unknown tasks.
        """
        result = f"BackEndAgent: Unknown task '{task}' - no action taken."
        team_leader.update_project_log(result)
