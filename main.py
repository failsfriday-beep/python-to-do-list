with open("new.txt","r")

tasks = []


while True :
    what_to_do = input("choose:  1.add \\ 2.view \\ 3.remove \\ 4.quit : ")
    if what_to_do == "1":
        new_task = input("New task: ")
        tasks.append(new_task) 

    elif what_to_do == "2":
        for i ,task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

    elif what_to_do == "3":
        remove = input("task number to remove :")
        if remove.isdigit():
            remove = int(remove) -1
            if 0 <= remove < len(tasks):
                tasks.pop(remove)
            else:
                print("invalid task number!")
        else:
            print("please enter a number!")


    elif what_to_do == "4":
        break
    else:
        print("not a valid option")


