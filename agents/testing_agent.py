# collaborative_ai_team/agents/testing_agent.py
from utils.communication import CommunicationChannel
import unittest

class TestingAgent:
    def __init__(self, communication_channel: CommunicationChannel):
        self.tasks = []
        self.communication_channel = communication_channel
        
        # Subscribe to backend agent updates
        self.communication_channel.subscribe('backend', self.handle_backend_update)

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
        suite = unittest.TestLoader().discover('tests')
        result = unittest.TextTestRunner().run(suite)
        result_summary = f"TestingAgent: Unit tests completed with {len(result.failures)} failures."
        team_leader.update_project_log(result_summary)


    def run_integration_tests(self, team_leader):
        """
        Simulate running integration tests.
        """
        result = "TestingAgent: Integration tests completed successfully."
        team_leader.update_project_log(result)

    def handle_backend_update(self, message):
        print(f"FrontEndAgent received update from Backend: {message}")

    def unknown_task(self, task, team_leader):
        """
        Handle unknown tasks.
        """
        result = f"TestingAgent: Unknown task '{task}' - no action taken."
        team_leader.update_project_log(result)
