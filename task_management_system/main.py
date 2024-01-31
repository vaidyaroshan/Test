from task_pakage.create_task import create_task
from task_pakage.edit_task import edit_task
from task_pakage.categorize_task import categorize_task
task1=create_task("Complete your assignment","Finish TASK MANAGEMENT SYSTEM")
## display the task
print("task 1: ",task1)
## edit the task
edit_task(task1,new_title="Upadated Assignment",new_description="Review and submitted to Rashmi Mam")
## display the  updated task 
print("Updated Task 1 :",task1)
## categorize the task
categorize_task(task1,"Zappcode Academy")
## display the categorized task
print("Categorized task1",task1)