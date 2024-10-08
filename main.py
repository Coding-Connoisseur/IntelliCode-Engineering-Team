# collaborative_ai_team/main.py

from project_management.team_leader import TeamLeader
from utils.communication import CommunicationChannel


def main():
    # Initialize the communication channel
    communication_channel = CommunicationChannel()
    
    # Initialize the Team Leader and pass the communication channel to agents
    team_leader = TeamLeader(communication_channel)
    
    # Define project requirements
    requirements = "This project involves a user interface, backend API development, server-side logic, database integration, authentication for login, and performance optimization."    
    # Start the project analysis and task execution
    
    team_leader.analyze_project(requirements)
    
    # Save the log after completion
    team_leader.save_log_to_file()

    print("\nProject execution complete. Check the logs/project_log.txt file for details.")

if __name__ == "__main__":
    main()
