
def display_table(table_dict):
    # Get column names
    column_names = ["Edge", "Duration", "Predecessors"]
    column_width = max(len(name) for name in column_names)
    
    # Print column names
    for name in column_names:
        print(f"{name.rjust(column_width)}", end="\t|\t")
    print()  # New line
    
    # Print table data
    for edge_name, data in table_dict.items():
        print(f"{edge_name}".rjust(column_width), end="\t|\t")
        print(f"{data['duration']}".rjust(column_width), end="\t|\t")
        print(", ".join(str(pred).rjust(column_width) for pred in data['predecessors']))
        # New line after each row


def create_table(file_name):
    lines = []
    with open(file_name, 'r') as file:
        for line in file:
            lines.append(line.strip())
    
    table_dict = {}
    alpha_successors = []  # Initialize a list to store alpha's successors
    
    for line in lines:
        parts = line.split()  # Split the line into parts
        edge_name = int(parts[0])  # The first part is the edge name
        duration = int(parts[1])   # The second part is the duration
        predecessors = []          # Initialize an empty list for predecessors
        successors = []            # Initialize an empty list for successors
        
        if len(parts) > 2:         # Check if there are predecessors
            predecessors = list(map(int, parts[2:]))  # Parse the predecessors
            
        # Store the data in the dictionary
        table_dict[edge_name] = {"duration": duration, "predecessors": predecessors, "successors": successors}
        
        # Populate alpha_successors list
        if not predecessors:  # If edge has no predecessors
            if edge_name != 0:  # Exclude alpha itself
                alpha_successors.append(edge_name)

    # Create alpha with specified properties
    table_dict[0] = {"duration": 0, "predecessors": [], "successors": alpha_successors}
    
    # Populate successors for each edge based on predecessors
    for edge_name, data in table_dict.items():
        for predecessor in data["predecessors"]:
            table_dict[predecessor]["successors"].append(edge_name)
    
    # Add alpha as a predecessor to edges with alpha as a predecessor
    for edge in alpha_successors:
        table_dict[edge]["predecessors"].append(0)


    # Move alpha to the beginning of the dictionary
    table_dict = {0: table_dict[0], **table_dict}
    
    return table_dict














def create_value_matrix(table_dict):
    max_edge = max(table_dict.keys())
    value_matrix = [[0] * (max_edge + 1) for _ in range(max_edge + 1)]
    
    for edge_name, data in table_dict.items():
        
        for predecessor in data['predecessors']:
            value_matrix[predecessor][edge_name] = data['duration']
    
    return value_matrix

def display_matrix(matrix):
    # Find the maximum width of elements in the matrix
    max_width = max(len(str(element)) for row in matrix for element in row)
    
    # Display the matrix
    for row in matrix:
        for element in row:
            print(str(element).rjust(max_width), end=" ")
        print()

def read_lines_from_file(file_name):
    lines = []
    with open(file_name, 'r') as file:
        for line in file:
            lines.append(line.strip())
    return lines