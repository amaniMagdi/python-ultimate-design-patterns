from user import User
from task import Task
from project_management import ProjectManagement

def main():
    # Create a user and a task
    user1 = User("user1@example.com")
    task1 = Task("Implement Feature A")

    # Initialize ProjectManagement with the task
    project_management = ProjectManagement(task1)

    # Test task operations
    project_management.pickup_task(user1, task1)  # Assign the task
    project_management.process_task(task1)       # Try to process the task
    project_management.block_task(task1, "Need more information")  # Block the task
    project_management.review_task(task1, user1)   # Review the task
    project_management.finish_task(task1)         # Finish the task

if __name__ == "__main__":
    main()
