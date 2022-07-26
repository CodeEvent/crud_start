import pdb 
from models.task import Task
import repositories.task_repository as task_repository  

from models.user import User
import repositories.user_respository as user_repository

task_repository.delete_all()
user_repository.delete_all()



user_1 = User("Jack", "Jarvis")
user_2 = User("Victor", "McDade")

user_repository.save(user_1)
user_repository.save(user_2)





new_task = Task("Go for a run", user_1, 20)
task_repository.save(new_task)

#add go for a walk and feed the cat and save both
task_1 = Task("Go for a walk with the dog", user_1, 60)
task_repository.save(task_1)

task_2 = Task("Go and feed the cat", user_2, 5)
task_repository.save(task_2)



# #delete one by its id
# # task_repository.delete_one(new_task.id)

# #update one
# task_2.mark_complete()

# #update 
# task_repository.update(task_2)

# #save and update the database repository

result = task_repository.select_all()
for task in result:
    print(task.user.__dict__)
    
    
# # found_task = task_repository.select(new_task.id)
# # print(found_task.__dict__)

# pdb.set_trace()