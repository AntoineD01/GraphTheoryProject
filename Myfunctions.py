
def display_table_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        table = [line.strip().split() for line in lines]
        for row in table:
            print("\t".join(row))

def create_table_dict_from_file(file_name):
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