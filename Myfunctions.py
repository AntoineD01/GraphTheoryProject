def read_constraint_table(file_path):
    tasks = []
    durations = []
    predecessors = []

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Skip the header line
        next(file)
        # Read each line of the file
        for line in file:
            # Split the line into columns
            columns = line.strip().split('|')
            # Remove empty strings and strip whitespace from each column
            columns = [col.strip() for col in columns if col.strip()]
            # Ignore lines without enough columns
            if len(columns) == 3:
                # Extract task, duration, and predecessors
                task = columns[0]
                # Check if duration is numeric before converting
                duration = int(columns[1]) if columns[1].isdigit() else None
                predecessor = columns[2]
                # Store values in separate lists
                tasks.append(task)
                durations.append(duration)
                predecessors.append(predecessor)

    # Return the stored values as a tuple of lists
    return tasks, durations, predecessors
