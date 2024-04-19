import Myfunctions

def main():
    file_name = "table 13.txt"
    
    table_dict = Myfunctions.create_table(file_name)
    Myfunctions.display_table(table_dict)
    print(table_dict)

    Matrix = Myfunctions.create_matrix(table_dict)
    Myfunctions.display_matrix(Matrix)
    
  
if __name__ == "__main__":
    main()
