from optparse import Values
from db.run_sql import run_sql
import repositories.user_respository as user_repository

from models.task import Task
  
def select_all():  
    tasks = []
    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        user = user_repository.select(row["user_id"])
        task = Task(row['description'], user,  row['duration'], row['completed'], row['id'] )
        tasks.append(task)

    return tasks 

def save(task):
    sql = "INSERT INTO tasks (description, user_id, duration, completed) VALUES (%s,%s,%s,%s) RETURNING id"
    values = [task.description, task.user.id , task.duration, task.completed]
    results = run_sql(sql, values)
    id = results[0]['id']
    task.id = id

def delete_all():
    sql = "DELETE FROM tasks"
    run_sql(sql)
    
    
def select(id):
    task = None
    sql = "SELECT * FROM tasks WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    
    if len(result) > 0:
        result = result[0]
        user = user_repository.select['user_id']
        task = Task(result["description"], result["assignee"], result['duration'], result['completed'], result['id']) 
    return task


def delete_one(id):
    sql = "DELETE FROM tasks WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
    
def update(task):
    sql = "UPDATE tasks SET (description, user_id, duration, completed) = (%s, %s, %s,%s) WHERE id = %s"
    values = [task.description, task.user.id, task.duration, task.completed, task.id]
    run_sql(sql, values)