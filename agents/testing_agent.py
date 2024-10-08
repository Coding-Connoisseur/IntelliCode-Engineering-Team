# collaborative_ai_team/agents/testing_agent.py

class TestingAgent:
    def __init__(self):
        self.tasks = []

    def execute_tasks(self, tasks, team_leader):
        """
        Execute assigned testing tasks and update the team leader on progress.
        """
        self.tasks = tasks
        for task in self.tasks:
            # Placeholder logic for each task
            if task == "Unit Tests":
                self.run_unit_tests(team_leader)
            elif task == "Integration Tests":
                self.run_integration_tests(team_leader)
            else:
                self.unknown_task(task, team_leader)

    def run_unit_tests(self, team_leader):
        """
        Simulate running unit tests.
        """
        result = "TestingAgent: Unit tests completed successfully."
        team_leader.update_project_log(result)

    def run_integration_tests(self, team_leader):
        """
        Simulate running integration tests.
        """
        result = "TestingAgent: Integration tests completed successfully."
        team_leader.update_project_log(result)

    def unknown_task(self, task, team_leader):
        """
        Handle unknown tasks.
        """
        result = f"TestingAgent: Unknown task '{task}' - no action taken."
        team_leader.update_project_log(result)
