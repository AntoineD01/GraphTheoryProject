
def display_table_from_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        table = [line.strip().split() for line in lines]
        for row in table:
            print("\t".join(row))