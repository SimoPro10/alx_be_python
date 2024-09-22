task = input("Enter your task: ")
task_priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
match task_priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {task_priority} priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a {task_priority} priority task but it is not  requires immediate attention today.Consider completing it when you have free time.")
    case "medium":
         if time_bound == "yes":
            print(f"Reminder: '{task}' is a {task_priority} priority task that requires immediate attention today!")
         else:
            print(f"Note: '{task}' is a {task_priority} priority task but it is not  requires immediate attention today.Consider completing it when you have free time.")
    case "low":
         if time_bound == "yes":
            print(f"Reminder: '{task}' is a {task_priority} priority task that requires immediate attention today!")
         else:
            print(f"Note: '{task}' is a {task_priority} priority task but it is not  requires immediate attention today.Consider completing it when you have free time.")
