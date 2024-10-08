# collaborative_ai_team/project_management/team_leader.py
from agents.frontend_agent import FrontEndAgent
from agents.backend_agent import BackEndAgent
from agents.database_agent import DatabaseAgent
from agents.testing_agent import TestingAgent
from agents.optimization_agent import OptimizationAgent
import os

class TeamLeader:
    def __init__(self):
        # Initialize specialized agents
        self.agents = {
            'frontend': FrontEndAgent(),
            'backend': BackEndAgent(),
            'database': DatabaseAgent(),
            'testing': TestingAgent(),
            'optimization': OptimizationAgent()
        }
        # Initialize a project log list to record progress
        self.project_log = []

    def analyze_project(self, requirements):
        """
        Analyze project requirements and create a task breakdown.
        """
        self.project_log.append("Analyzing project requirements...")
        print("Team Leader: Analyzing project requirements...")
        
        tasks = self.break_down_tasks(requirements)
        self.assign_tasks(tasks)

    def break_down_tasks(self, requirements):
        """
        Break down project requirements into specific tasks for each agent.
        """
        # Placeholder task breakdown (customize as needed)
        tasks = {
            'frontend': ["Design UI", "Develop HTML/CSS/JS"],
            'backend': ["Develop API", "Integrate Database"],
            'database': ["Set up Database", "Design Schema"],
            'testing': ["Unit Tests", "Integration Tests"],
            'optimization': ["Optimize Performance", "Code Review"]
        }
        self.project_log.append("Task breakdown complete.")
        print("Team Leader: Task breakdown complete.")
        return tasks

    def assign_tasks(self, tasks):
        """
        Assign tasks to agents based on their expertise.
        """
        for agent_name, agent_tasks in tasks.items():
            self.project_log.append(f"Assigning tasks to {agent_name} agent...")
            print(f"Team Leader: Assigning tasks to {agent_name} agent...")
            agent = self.agents.get(agent_name)
            if agent:
                agent.execute_tasks(agent_tasks, self)

    def update_project_log(self, update):
        """
        Update the project log with a new entry.
        """
        self.project_log.append(update)
        print(update)  # Output for real-time tracking

    def save_log_to_file(self, filename="logs/project_log.txt"):
        """
        Save the project log to a file, creating the directory if it doesn't exist.
        """
        # Ensure the directory exists
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        # Save the log to the file
        with open(filename, 'w') as log_file:
            for entry in self.project_log:
                log_file.write(f"{entry}\n")
        print("Team Leader: Project log saved to file.")