import Myfunctions

def main():
    file_path = "Constraint Table Test.txt"  
    tasks, durations, predecessors = Myfunctions.read_constraint_table(file_path)

    print("Tasks:", tasks)
    print("Durations:", durations)
    print("Predecessors:", predecessors)

    Myfunctions.display_table(tasks, durations, predecessors)

if __name__ == "__main__":
    main()
