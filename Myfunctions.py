def read_constraint_table(file_path):
    tasks = []
    durations = []
    predecessors = []

    # Open the file in read mode
    with open(file_path, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            if line_num <= 2:
                continue  # Skip the first two lines
            
            columns = line.strip().split('|')
            columns = [col.strip() for col in columns if col.strip()]

            # If line has three columns (task, duration, predecessor)
            if len(columns) == 3:
                task = columns[0]
                duration = int(columns[1]) if columns[1].isdigit() else None
                predecessor = columns[2]

                # Add task, duration, and predecessor if they are not placeholders
                if task != '------' and predecessor != '--------------':
                    tasks.append(task)
                    durations.append(duration)
                    predecessors.append(predecessor)

            # If line has two columns (task, duration)
            elif len(columns) == 2:
                task = columns[0]
                duration = int(columns[1]) if columns[1].isdigit() else None
                
                # Add task and duration
                if task != '------':
                    tasks.append(task)
                    durations.append(duration)
                    predecessors.append(None)

    return tasks, durations, predecessors


def display_table(tasks, durations, predecessors):
    print("Task  | Duration | Predecessor")
    print("-" * 30)
    for task, duration, predecessor in zip(tasks, durations, predecessors):
        # Convert None to an empty string if predecessor is None
        predecessor_str = "" if predecessor is None else predecessor
        print(f"{task:<5} | {duration:<8} | {predecessor_str:<12}")


def successors(tasks, predecessors):
    successor_lists = {task: [] for task in tasks}
    
    # Iterate over tasks and predecessors simultaneously
    for task, predecessor in zip(tasks, predecessors):
        if predecessor is not None:
            # Add the task to the list of successors for each predecessor
            for p in predecessor.split(','):
                pred = p.strip()
                if pred in successor_lists:
                    successor_lists[pred].append(task)
            
    return successor_lists

def count_edges(successors):
    total_edges = sum(len(successors[node]) for node in successors)
    return total_edges

