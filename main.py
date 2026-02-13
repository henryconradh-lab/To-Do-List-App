import json
from pathlib import Path 

#this is our storage variable
DATA = Path("data.json")

#LOAD THE LIST TASK
def loadtask():
  if not DATA.exists():
     return[]
  try:
    return json.loads(DATA.read_text(encoding="utf-8"))
  except json.JSONDecodeError:
    return []

#SAVE THE LIST TASK
def savetasks(tasks):
  DATA.write_text(json.dumps(tasks, indent=2), encoding="utf-8")
  
#ADD A TASK TO THE LIST
def addtask(tasks):
   title = input("Task Title: ").strip()
   if not title: 
      print("title cannot be empty")
      return
   tasks.append({"title":title,"done":False})
   savetasks(tasks)
   print("Task added")
   
   
#LIST THE TASK
def listtask(tasks):
   if not tasks:
      print("No tasks yet.")
      return
   
   for i, task in enumerate(tasks, start=1):
      status = "✅" if task["done"] else "🕒"
      print(f"{i}. {status} {task['title']}")
   
#MAKE A MARK DONE FUNCTION
def markdone(tasks):
   listtask(tasks)
   if not tasks:
      return
   
   choiceMark = input("Which task would you like to mark as finished?").strip()
   if not choiceMark.isdigit():
      print("Please input valid number")
      return   
   
   idx = int(choiceMark) - 1 
   if idx < 0 or idx >= len(tasks):
      print("Please input valid number")
      return
   
   tasks[idx]["done"] = True
   savetasks(tasks)
   print("Task marked done!")
   
#geek for geeks

#DELETE A TASK
def deletetask(tasks):
   listtask(tasks)
   if not tasks:
      return
   
   choicedelete = input("Which task would you like to delete?").strip()
   if not choicedelete.isdigit():
      print("Please input valid number")
      return   
   
   idx = int(choicedelete) - 1 
   if idx < 0 or idx >= len(tasks):
      print("Please input valid number")
      return
   
   #NEXT CLASS
   removed = tasks.pop(idx)
   savetasks(tasks)
  
   print(f"Deleted:{removed['title']}")


#HERE WILL BE OUR MENU
def main():
  tasks=loadtask()
  
  #THE MENU CODE
  while True:
    print("\n=== TO-DO APP ===")
    print("1) List my Tasks")
    print("2) Add my new task")
    print("3) Marking done")
    print("4) Delete task")
    print("5) Exit my todo list")
    
    choice = input("Choose an option from the menu: ").strip()
    
    #1 if 4 elif 1 else
    
    if choice == "1":
       listtask(tasks)
    elif choice == "2":
       addtask(tasks)
    elif choice == "3":
       markdone(tasks)
    elif choice == "4":
       deletetask(tasks)
    elif choice == "5":
       print("bye bye")
       break
    else:
       print("invalid")


if __name__ == "__main__":
  main()