import Myfunctions

def main():
    file_path = "Constraint Table Test.txt"  
    tasks, durations, predecessors = Myfunctions.read_constraint_table(file_path)
    Myfunctions.display_table(tasks, durations, predecessors)
    print(Myfunctions.successors(tasks, predecessors))
    print(f"({tasks[0]}) --- {durations[0]} -->")

if __name__ == "__main__":
    main()
