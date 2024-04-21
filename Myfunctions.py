from collections import deque

def menu():
    print(f'\n\n\n||| Welcome to Graph Theory 3000 |||\n')
    nb_table = 15
    while (nb_table>14 or nb_table<1):
        nb_table = int(input(f'Which table do you want to try ?\n'))
    file_name = "table " + str(nb_table) + ".txt"

    # Creation of the dictionary storing the data
    table_dict = create_table(file_name)
    print(f'Here is the table : \n')
    display_table(table_dict)

    # Creation of the matrix
    print(f'\n\nHere is the corresponding matrix : \n')
    Matrix = create_matrix(table_dict)
    display_matrix(Matrix)

    # Check if it is a valid scheduling graph
    if is_valid_scheduling_graph(table_dict):
        print("\nThe graph is a valid scheduling graph.")
        
        # Compute calendars
        calendars, critical_path = compute_calendars(table_dict)
        print("\nCalendars:")
        for node, calendar in calendars.items():
            print(f"Task {node}: Start Time = {calendar['start_time']}, End Time = {calendar['end_time']}")
        print("\nCritical Path:", critical_path)

        ranks = find_rank(table_dict)
        # Sort the ranks dictionary by values (ranks)
        sorted_ranks = {k: v for k, v in sorted(ranks.items(), key=lambda item: item[1])}

        # Display ranks in ascending order
        print("\nRanks:")
        for edge, rank in sorted_ranks.items():
            print(f"Task {edge}: Rank {rank}")

        early_date = compute_early_date(table_dict, calendars)
        sorted_early_date = sorted(early_date.items(), key=lambda x: x[1])
        print("\nEarliest date:")
        for node, early in sorted_early_date:
            print(f"Task {node}: Earliest date = {early}")

        latest_date = compute_latest_date(table_dict, calendars, critical_path)
        sorted_latest_date = sorted(latest_date.items(), key=lambda x: x[1])
        print("\nLatest date:")
        for node, latest in sorted_latest_date:
            print(f"Task {node}: Latest date = {latest}")

        total_float = compute_total_float(table_dict, early_date, latest_date)
        sorted_total_float = sorted(total_float.items(), key=lambda x: x[1])
        print("\nTotal Float:")
        for node, float_value in sorted_total_float:
            print(f"Task {node}: Total Float = {float_value}")

    else:
        print("The graph is not a valid scheduling graph.")


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
    
    # Find edges with no successors
    edges_with_no_successors = []
    for edge_name, data in table_dict.items():
        if not data["successors"]:
            edges_with_no_successors.append(edge_name)
    
    # Create omega with specified properties
    omega_edge_name = max(table_dict.keys()) + 1
    table_dict[omega_edge_name] = {"duration": 0, "predecessors": edges_with_no_successors, "successors": []}

    # Add omega as a successor to edges with omega as a successor
    for edge in edges_with_no_successors:
        table_dict[edge]["successors"].append(omega_edge_name)

    # Move alpha to the beginning of the dictionary
    table_dict = {0: table_dict[0], **table_dict}

    return table_dict

def create_matrix(table_dict):
    # Find the maximum edge number
    max_edge = max(table_dict.keys())

    # Initialize an empty matrix with zeros
    edges_matrix = [['*'] * (max_edge + 1) for _ in range(max_edge + 1)]

    for edge, data in table_dict.items():
        # Check if the edge has successors
        if data["successors"]:
            # Iterate through the successors of the current edge
            for successor in data["successors"]:
                duration = data["duration"]
                edges_matrix[edge][successor] = duration

    return edges_matrix

def display_matrix(matrix):
    # Find the maximum width of elements in the matrix
    max_width = max(len(str(element)) for row in matrix for element in row)
    num_rows = len(matrix)
    num_columns = len(matrix[0])

    # Display column numbers
    print(" ".rjust(max_width), end=" ")  
    for col_num in range(num_columns):
        print(str(col_num).rjust(max_width), end=" ")
    print()  

    
    for row_num, row in enumerate(matrix):
        print(str(row_num).rjust(max_width), end=" ")  
        for element in row:
            if element == '*':  
                print("*".rjust(max_width), end=" ")  
            else:
                print(str(element).rjust(max_width), end=" ") 
        print()


def topological_sort(table_dict):
    # Perform topological sorting using depth-first search (DFS)
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)
        for successor in table_dict[node]["successors"]:
            if successor not in visited:
                dfs(successor)
        order.append(node)

    for node in table_dict:
        if node not in visited:
            dfs(node)

    return list(reversed(order))


def compute_calendars(table_dict):
    # Perform topological sorting to get the order of tasks
    order = topological_sort(table_dict)

    # Forward pass to compute ES and EF
    es = {node: 0 for node in table_dict}
    ef = {node: 0 for node in table_dict}
    for node in order:
        duration = table_dict[node]["duration"]
        predecessors = table_dict[node]["predecessors"]
        if predecessors:  # Check if there are predecessors
            es[node] = max(ef[predecessor] for predecessor in predecessors)
        ef[node] = es[node] + duration

    # Backward pass to compute LS and LF
    ls = {node: ef[max(table_dict)] for node in table_dict}
    lf = {node: ef[max(table_dict)] for node in table_dict}
    for node in reversed(order):
        successors = table_dict[node]["successors"]
        if successors:  # Check if there are successors
            lf[node] = min(ls[successor] for successor in successors)
        ls[node] = lf[node] - table_dict[node]["duration"]

    # critical path
    critical_path = [node for node in order if es[node] == ls[node]]

    
    calendars = {}
    for node in order:
        start_time = es[node]
        end_time = ef[node]
        calendars[node] = {"start_time": start_time, "end_time": end_time}

    return calendars, critical_path

    
def is_valid_scheduling_graph(table_dict):
    visited = set()
    stack = set()

    def has_cycle(node):
        if node in stack:
            return True
        if node in visited:
            return False

        visited.add(node)
        stack.add(node)

        for neighbor in table_dict[node]["successors"]:
            if has_cycle(neighbor):
                return True

        stack.remove(node)
        return False

    # Check for cycles
    for node in table_dict:
        if has_cycle(node):
            print("Error: The graph contains a cycle.")
            return False

    # Check for negative edge weights
    for node, data in table_dict.items():
        if data["duration"] < 0:
            print(f"Error: Negative duration for task {node}.")
            return False

    # If no issues found, the graph is valid
    return True

def compute_early_date(table_dict, calendars):
    early_date = {}

    # Compute ranks for vertices on the critical path (LS values)
    for node in calendars:
        early_date[node] = calendars[node]["start_time"]

    # Propagate ranks backward through the graph
    for node in reversed(topological_sort(table_dict)):
        if node not in early_date:
            # If the node is not on the critical path, compute its rank
            successors = table_dict[node]["successors"]
            if successors:
                max_successor_date = max(early_date[successor] for successor in successors)
                early_date[node] = max_successor_date + table_dict[node]["duration"]
            else:
                # If the node has no successors, its rank is its own duration
                early_date[node] = table_dict[node]["duration"]

    return early_date

def find_rank(table_dict):
    # Create a dictionary to store the in-degree of each edge
    in_degree = {edge: 0 for edge in table_dict}

    # Calculate the in-degree for each edge
    for edge, data in table_dict.items():
        for successor in data["successors"]:
            in_degree[successor] += 1

    # Initialize a queue to perform topological sorting
    queue = deque()

    # Enqueue edges with in-degree 0
    for edge, degree in in_degree.items():
        if degree == 0:
            queue.append(edge)

    # Initialize a dictionary to store the rank of each edge
    rank = {edge: 0 for edge in table_dict}

    # Perform topological sorting
    while queue:
        current_edge = queue.popleft()
        for successor in table_dict[current_edge]["successors"]:
            # Decrease the in-degree of successors
            in_degree[successor] -= 1
            # If the in-degree becomes 0, enqueue the successor
            if in_degree[successor] == 0:
                queue.append(successor)
                # Set the rank of the successor
                rank[successor] = rank[current_edge] + 1

    return rank

def compute_latest_date(table_dict, calendars, critical_path):
    latest_date = {}
    # Compute ranks for vertices on the critical path (LF values)
    for node in calendars:
        latest_date[node] = calendars[node]["end_time"]
    # Propagate ranks forward through the graph
    for node in reversed(topological_sort(table_dict)):
        successors = table_dict[node]["successors"]
        if successors:
            min_successor_date = latest_date[successors[0]] - table_dict[node]["duration"]
            for i in range (1,len(successors)):
                successor_date = latest_date[successors[i]] - table_dict[node]["duration"]
                if successor_date<min_successor_date:
                    min_successor_date = successor_date
            latest_date[node] = min_successor_date
        else:
            # If the node has no successors, its latest date is the same as the end time of the project
            latest_date[node] = calendars[max(table_dict)]["end_time"]
    return latest_date

def compute_total_float(table_dict, earliest_date, latest_date):
    total_float = {}

    for node in table_dict:
        total_float[node] = latest_date[node] - earliest_date[node]

    return total_float
