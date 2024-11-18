def minimize_average_completion_time(tasks):
    """
    Minimizes the average completion time by scheduling tasks
    in order of non-decreasing processing times.
    
    Parameters:
    tasks (list of tuples): Each tuple contains (task_id, processing_time)
    
    Returns:
    list of tuples: Scheduled tasks in optimal order
    float: The minimized average completion time
    """
    # Step 1: Sort tasks based on processing times
    sorted_tasks = sorted(tasks, key=lambda x: x[1])
    
    # Step 2: Calculate completion times
    completion_times = []
    total_time = 0
    for task in sorted_tasks:
        total_time += task[1]
        completion_times.append((task[0], total_time))
    
    # Step 3: Calculate average completion time
    sum_completion_times = sum(time for _, time in completion_times)
    average_completion_time = sum_completion_times / len(tasks)
    
    return completion_times, average_completion_time

if __name__ == "__main__":
    # Sample Input
    tasks = [('a1', 5), ('a2', 3)]
    
    # Function Call
    scheduled_tasks, avg_completion_time = minimize_average_completion_time(tasks)
    
    # Output
    print("Scheduled Tasks and Completion Times:")
    for task_id, completion_time in scheduled_tasks:
        print(f"Task {task_id}: Completion Time = {completion_time}")
    
    print(f"\nMinimized Average Completion Time: {avg_completion_time}")
    # Sample Input
    tasks = [('a1', 2), ('a2', 1), ('a3', 4), ('a4', 3)]

    # Function Call
    scheduled_tasks, avg_completion_time = minimize_average_completion_time(tasks)

    # Output
    print("Scheduled Tasks and Completion Times:")
    for task_id, completion_time in scheduled_tasks:
        print(f"Task {task_id}: Completion Time = {completion_time}")

    print(f"\nMinimized Average Completion Time: {avg_completion_time}")


