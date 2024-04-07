import networkx as nx 
import matplotlib as plt

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
    successor_lists = {}

    # Iterate over tasks and predecessors simultaneously
    for task, predecessor in zip(tasks, predecessors):
        # If predecessors is None or empty, set successors to an empty list
        if predecessor is None or predecessor.strip() == '':
            successors = []
        else:
            # Split predecessor string by comma and add to successor list
            successors = [p.strip() for p in predecessor.split(',') if p.strip()]
        # Add task and its successors to the dictionary
        successor_lists[task] = successors

    return successor_lists
    
    



