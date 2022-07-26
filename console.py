import pdb 
from models.task import Task
import repositories.task_repository as task_repository  

task_repository.delete_all()

new_task = Task("Go for a run", "Jack Jarvis", 20)
task_repository.save(new_task)

task_1 = Task("Go for a walk with the dog", 'Jack Jarvia', 60)
task_repository.save(task_1)

task_2 = Task("Go and feed the cat", 'Victor McDade', 5)
task_repository.save(task_2)


#delete one by its id
# task_repository.delete_one(new_task.id)

#update one
task_2.mark_complete()

#update 
task_repository.update(task_2)

#save and update the database repository
result = task_repository.select_all()


for task in result:
    print(task.__dict__)
    
    
# found_task = task_repository.select(new_task.id)
# print(found_task.__dict__)

pdb.set_trace()