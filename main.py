import os

def read_constraint_table(file_path):
    constraint_table = []
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
                task = columns[1]
                duration = int(columns[2])
                predecessors = columns[3].split(',') if columns[3] else []
                # Create a dictionary representing the task
                task_info = {'task': task, 'duration': duration, 'predecessors': predecessors}
                # Append the task to the constraint table
                constraint_table.append(task_info)
    return constraint_table

# Provided file path
provided_file_path = r"C:\Users\Antoine Dupont\Documents\!EFREI\OneDrive - Efrei\!Cours\Graph Theory\Project\GraphTheoryProject\constraint_table.txt"

# Check if the file exists
if not os.path.isfile(provided_file_path):
    print("File not found.")
else:
    # Example usage
    constraint_table = read_constraint_table(provided_file_path)
    print(constraint_table)
