# collaborative_ai_team/main.py

from project_management.team_leader import TeamLeader

def main():
    # Initialize the Team Leader
    team_leader = TeamLeader()
    
    # Define project requirements
    requirements = "A web application project requiring front-end, back-end, database, testing, and optimization."
    
    # Start the project analysis and task execution
    team_leader.analyze_project(requirements)
    
    # Save the log after completion
    team_leader.save_log_to_file()

    print("\nProject execution complete. Check the logs/project_log.txt file for details.")

if __name__ == "__main__":
    main()
