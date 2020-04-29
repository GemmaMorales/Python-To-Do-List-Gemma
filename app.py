import csv
todos = []
stop = False

def get_todos():
    #global todos
    return todos

def add_one_task(title):
    todos.append(title)
    #todos = todos + [title]
    #print(new_list)
    return todos

    
def print_list():
    #global todos
    print(todos)
    

def delete_task(number_to_delete):
    # your code here
    if number_to_delete in todos:
        todos.remove(number_to_delete)
    else:
        print(number_to_delete + " is not on the To Do list.")
    return todos
    #todos.pop(number_to_delete)


def save_todos():
    myFile = open("todos.csv",'w+')
    write = csv.writer(myFile, quoting=csv.QUOTE_NONE)
    write.writerow(todos)
    pass

    
def load_todos():
    # your code here
    global todos
    try:
        with open("todos.csv", newline='') as myFile:
            reader = csv.reader(myFile)
            for row in reader:
                todos = row
    except:
        open("todos.csv", "w+")
        load_todos()
    pass

# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        
        if response == "6":
            stop = True
        elif response == "3":
            
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")