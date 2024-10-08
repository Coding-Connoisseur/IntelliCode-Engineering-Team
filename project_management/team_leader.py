# collaborative_ai_team/project_management/team_leader.py
from agents.frontend_agent import FrontEndAgent
from agents.backend_agent import BackEndAgent
from agents.database_agent import DatabaseAgent
from agents.testing_agent import TestingAgent
from agents.optimization_agent import OptimizationAgent
from utils.communication import CommunicationChannel
import os

class TeamLeader:
    def __init__(self, communication_channel: CommunicationChannel):
        self.agents = {
            'frontend': FrontEndAgent(communication_channel),
            'backend': BackEndAgent(communication_channel),
            'database': DatabaseAgent(communication_channel),
            'testing': TestingAgent(communication_channel),
            'optimization': OptimizationAgent(communication_channel)
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
        Dynamically break down project requirements into specific tasks for each agent.
        """
        tasks = {
            'frontend': [],
            'backend': [],
            'database': [],
            'testing': [],
            'optimization': []
        }
        
        # Convert requirements to lowercase for case-insensitive matching
        requirements = requirements.lower()
        
        # Analyze keywords and dynamically assign tasks
        if "ui" in requirements or "frontend" in requirements or "user interface" in requirements:
            tasks['frontend'].extend(["Design UI", "Develop HTML/CSS/JS"])
        
        if "api" in requirements or "backend" in requirements or "server" in requirements:
            tasks['backend'].extend(["Develop API"])
        
        if "database" in requirements or "data storage" in requirements:
            tasks['database'].extend(["Set up Database", "Design Schema"])
        
        if "testing" in requirements or "quality assurance" in requirements or "qa" in requirements:
            tasks['testing'].extend(["Unit Tests", "Integration Tests"])
        
        if "optimization" in requirements or "performance" in requirements or "speed" in requirements:
            tasks['optimization'].extend(["Optimize Performance", "Code Review"])
        
        if "authentication" in requirements or "login" in requirements or "user authentication" in requirements:
            tasks['backend'].append("Implement Authentication")

        # Logging for debugging purposes
        self.project_log.append("Dynamic task breakdown complete based on requirements.")
        print(f"Team Leader: Task breakdown - {tasks}")
        
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