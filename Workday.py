
from atds import Stack()
def main(): 
    print("Current time is" + clock + "and current task is None")
    print("Items on stack are: Stack[]")
    print("[Enter] to continue...")
    print("------------")
    
    tasks = [ ['read work emails',10], \
          ['respond to emails', 10], \
          ['attend meeting', 15], \
          ['coffee break', 15], \
          ['talk to boss', 10], \
          ['read work emails',10], \
          ['respond to emails', 10], \
          ['conference call', 15], \
          ['conversation with colleague', 15], \
          ['coffee break', 15], \
          ['meet with student', 15] ]
    

    clock = 0 
    current_task = None
    WORKDAY_MINUTES = 180 
    
    while clock < WORKDAY_MINUTES: 
        random.randrange(10) == 0:
        if len(tasks) > 0: 
            stack.push(tasks.pop(random.range(len(tasks))))
        if not s.is_empty():
            current_task = stack.peek()
            print("working on", current_task[0])
            current_task[1] -= 1
            print("Still have", current task[1], "minutes to work on this task")

            clock += 1 


    

    



