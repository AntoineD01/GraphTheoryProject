
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
        for line in lines:
            parts = line.strip().split()
            edge_name = int(parts[0])
            duration = int(parts[1])
            predecessors = list(map(int, parts[2:]))
            table_dict[edge_name] = {"duration": duration, "predecessors": predecessors}
    return table_dict