import Myfunctions

def main():
    file_name = "table 1.txt"
    table_dict = Myfunctions.create_table(file_name)
    Myfunctions.display_table(table_dict)
    
    
    
if __name__ == "__main__":
    main()
