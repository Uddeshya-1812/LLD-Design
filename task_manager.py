import uuid 
from datetime import datetime 
from enum import Enum
from queue import PriorityQueue
from threading import RLock

class Status(Enum):
    TO_DO = 1
    IN_PROGRESS = 2
    DONE = 3
    FAIL = 4

class BaseTimeStamp:

    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()

    
class User(BaseTimeStamp) :

    def __init__(self,name):
        super().__init__()
        self.name = name

class Comments(BaseTimeStamp):

    def __init__(self, text=''):
        super().__init__()
        self.text = text 
    


class Task(BaseTimeStamp):

    def __init__(self, user, priority, title, description):
        super().__init__()
        self.title = title
        self.description = description 

        self.status = Status.TO_DO
        self.priority = priority 
        self.user = user 
        self.comments = []
        self.history = []
    

    def add_comment(self, comment):
        if not comment:
            return 
        
        self.comments.append(comment)
        return 


class ActivityLog(BaseTimeStamp):

    def __init__(self, action, user):
        super().__init__()
        self.user = user 
        self.action = action
        


class TaskManager:

    def __init__(self):
        self.id = uuid.uuid4()
        self.task_map = {}
        self.queue = PriorityQueue()
        self.lock = RLock()



    def add_tasks(self, task):
        return 

    def update_tasks(self, task_id):
        return 
    
    def delete_tasks(self, task_id):
        return 
         
    def history(self, task_id):
        return 

    def change_user(self, to_user):
        return 
    
    def filter_tasks(self, filter):
        return 
