
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
    table_dict = {}
    with open(file_name, 'r') as file:
        lines = file.readlines()
        
        # Add fictitious task alpha
        alpha_successors = []
        for line in lines:
            parts = line.strip().split()
            successors = list(map(int, parts[2:]))
            if not successors:
                alpha_successors.append(int(parts[0]))
        
        table_dict[0] = {"duration": 0, "predecessors": alpha_successors}
        
        # Add tasks from the file
        for line in lines:
            parts = line.strip().split()
            edge_name = int(parts[0])
            duration = int(parts[1])
            predecessors = list(map(int, parts[2:]))
            table_dict[edge_name] = {"duration": duration, "predecessors": predecessors}
        
        # Add fictitious task omega
        omega_predecessors = []
        for edge_name, data in table_dict.items():
            if edge_name != 0:  # Exclude alpha as a predecessor of omega
                successors = [edge for edge in table_dict if edge_name in table_dict[edge]["predecessors"]]
                if not successors:
                    omega_predecessors.append(edge_name)
        
        max_edge_name = max(table_dict.keys())
        table_dict[max_edge_name + 1] = {"duration": 0, "predecessors": omega_predecessors}
        
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