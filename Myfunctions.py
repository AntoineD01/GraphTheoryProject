
def display_table(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        
        # Obtenir les noms de colonnes
        column_names = lines[0].strip().split()
        num_columns = len(column_names)
        column_width = max(len(name) for name in column_names)
        
        # Afficher les noms de colonnes
        for name in column_names:
            print(f"{name.rjust(column_width)}", end="\t")
        print()  # Nouvelle ligne
        
        # Afficher les données du tableau
        for line in lines[1:]:
            elements = line.strip().split()
            for element in elements:
                print(f"{element.rjust(column_width)}", end="\t")
            print()  # Nouvelle ligne

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