from queue import PriorityQueue
import uuid 



class Task: 

    def __init__(self, user_id, priority, metadata={}):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.priority = priority 
        self.metadata = metadata
        self.version = 0



class TaskManager : 

    def __init__(self):
        self.pq = PriorityQueue()
        self.task_finder = {}
        '''
        task_finder = {key : (timestamp, task)}
        '''
    
    def add_task(self, task):
        if task is None:
            # using print for logging
            print('Task not defined !')
            return False 
        if task.id in self.task_finder:
            print(f'task {task.id} already present in Queue!')
            return task 
        # this part should be atomic 
        self.task_finder[task.id] = (task, task.version)
        self.pq.put((-task.priority, -task.version, task.id, task))
        print(f'Task {task.id} added to queue successfully')
        return task
    
    def modify_task(self, task_id, new_priority):
        if new_priority is None:
            print("Priority cannot be None ")

        if task_id not in self.task_finder:
            print('Task not present in queue')
            return False 
        
        task, version = self.task_finder[task_id]
        version+=1
        task.priority = new_priority
        task.version = version
        self.task_finder[task_id] = task , task.version
        print(f'Task details, version:{task.version}, priority: {task.priority}, user : {task.user_id}')
        self.pq.put((-task.priority, -task.version ,task.id, task))
        print(f'Update successfull for task {task.id}')
        return task
    
    def remove_task(self, task_id):
        if task_id not in self.task_finder:
            print('Task not present in queue')
            return False 
        del self.task_finder[task_id]
        print(f'Task with {task_id} deleted!')
        return True

    def execute_task(self):
        # this should be atomic 

        while not self.pq.empty():
            _ , version , task_id , task = self.pq.get()
            if task_id  in self.task_finder:
                task, latest_version = self.task_finder[task_id] 

                if -version != latest_version:
                    continue

                del self.task_finder[task_id]
                print(f'Task {task.user_id} executed for task id {task_id} with priority {task.priority} {task.version}')
        
    

    def view_tasks(self):
        return [(self.task_finder[task][0].id, self.task_finder[task][0].priority) for task in self.task_finder]


t1 = Task('A', 2)
t2 = Task('B', 3)
t3 = Task('C', 4)


tm = TaskManager()
tm.add_task(t1)
tm.add_task(t2)
tm.add_task(t3)
tm.modify_task(task_id= t3.id, new_priority=1)
print(tm.view_tasks())
tm.execute_task()
        