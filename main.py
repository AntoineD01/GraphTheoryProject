import Myfunctions

def main():
    # Exemple d'utilisation :
    file_name = "table 1.txt"  # Remplacez "exemple.txt" par le nom de votre fichier
    Myfunctions.display_table_from_file(file_name)
    table_dict = Myfunctions.create_table_dict_from_file(file_name)
    print(table_dict)
    
if __name__ == "__main__":
    main()
