def read_constraint_table(file_path):
    tasks = []
    durations = []
    predecessors = []

    # Open the file in read mode
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            columns = line.strip().split('|')
            columns = [col.strip() for col in columns if col.strip()]
            print(columns)

            if len(columns) == 3:
                task = columns[0]
                duration = int(columns[1]) if columns[1].isdigit() else None
                predecessor = columns[2]

                if task!='------' and predecessor!='--------------':
                    tasks.append(task)
                    durations.append(duration)
                    predecessors.append(predecessor)
            elif len(columns) == 2:
                task = columns[0]
                duration = int(columns[1]) if columns[1].isdigit() else None
                predecessor = None

                if task!='------':
                    tasks.append(task)
                    durations.append(duration)
    return tasks, durations, predecessors

def display_table(tasks, durations, predecessors):
    print("Task  | Duration | Predecessor")
    print("-" * 30)
    for task, duration, predecessor in zip(tasks, durations, predecessors):
        print(f"{task:<5} | {duration:<8} | {predecessor:<12}")
