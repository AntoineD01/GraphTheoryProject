import Myfunctions

def main():
    file_name = "table 13.txt"
    
    table_dict = Myfunctions.create_table(file_name)
    print(table_dict)
    Myfunctions.display_table(table_dict)

    #Myfunctions.add_successors(table_dict)
    #print(table_dict)
    
    #value_matrix = Myfunctions.create_value_matrix(table_dict)
    #Myfunctions.display_matrix(value_matrix)
    
    
    
if __name__ == "__main__":
    main()
