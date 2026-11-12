class TaskManager:
    def __init__(self):
        self.tasks = {
            101: {
                'id': 101,
                'title': 'Fix login bug',
                'assignee': 'Ali',
                'priority': 'HIGH',
                'status': 'OPEN'
            },
            102: {
                'id': 102,
                'title': 'Update API',
                'assignee': 'Sara',
                'priority': 'MEDIUM',
                'status': 'IN_PROGRESS'
            },
            103: {
                'id': 103,
                'title': 'Write tests',
                'assignee': 'Ali',
                'priority': 'LOW',
                'status': 'DONE'
            }
        }

    def create(self, id_i, title, assignee, priority, status):
        if id_i <= 0:
            print('Invalid ID!')
            return

        if id_i in self.tasks:
            print('ID already exists!')
            return
        
        if title.strip() == '' or assignee.strip() == '':
            print('Title and assignee cannot be empty!')
            return

        priority = priority.strip().upper()
        if priority not in ['LOW', 'MEDIUM', 'HIGH']:
            print('Invalid priority!')
            return

        status = status.strip().upper()
        if status not in ['OPEN', 'IN_PROGRESS', 'DONE']:
            print('Invalid status!')
            return

        self.tasks[id_i] = {
            'id': id_i,
            'title': title.strip(),
            'assignee': assignee.strip(),
            'priority': priority,
            'status': status
        }

        print('Successfully created!')

    def read(self, id_i):
        if id_i not in self.tasks:
            print('Task not found!')
            return

        print('ID:', id_i)
        print('Title:', self.tasks[id_i]['title'])
        print('Assignee:', self.tasks[id_i]['assignee'])
        print('Priority:', self.tasks[id_i]['priority'])
        print('Status:', self.tasks[id_i]['status'])

    def read_all(self):
        if not self.tasks:
            print('No tasks found!')
            return

        for task_id in self.tasks:
            print('ID:', task_id)
            print('Title:', self.tasks[task_id]['title'])
            print('Assignee:', self.tasks[task_id]['assignee'])
            print('Priority:', self.tasks[task_id]['priority'])
            print('Status:', self.tasks[task_id]['status'])
            print('-------------------')

    def is_valid_transition(self, current_status, new_status):
        if current_status == 'OPEN' and new_status == 'IN_PROGRESS':
            return True
        elif current_status == 'IN_PROGRESS' and new_status == 'OPEN':
            return True
        elif current_status == 'IN_PROGRESS' and new_status == 'DONE':
            return True
        elif current_status == 'DONE' and new_status == 'IN_PROGRESS':
            return True
        else:
            return False


    def update(self, id_i, title=None, assignee=None,
               priority=None, status=None):
    
        if id_i not in self.tasks:
            print('Task not found!')
            return
        
        if title == None and assignee == None and priority == None and status == None:
            print('No changes were entered!')
            return
    
        if title != None:
            title = title.strip()
            if title == '':
                print('Title cannot be empty!')
                return
    
        if assignee != None:
            assignee = assignee.strip()
            if assignee == '':
                print('Assignee cannot be empty!')
                return
    
        if priority != None:
            priority = priority.strip().upper()
    
            if priority not in ['LOW', 'MEDIUM', 'HIGH']:
                print('Invalid priority!')
                return
    
        if status != None:
            status = status.strip().upper()
            current_status = self.tasks[id_i]['status']
    
            if status not in ['OPEN', 'IN_PROGRESS', 'DONE']:
                print('Invalid status!')
                return
    
            if status != current_status:
                if not self.is_valid_transition(current_status, status):
                    print('Invalid status transition!')
                    return
    
        if title != None:
            self.tasks[id_i]['title'] = title
    
        if assignee != None:
            self.tasks[id_i]['assignee'] = assignee
    
        if priority != None:
            self.tasks[id_i]['priority'] = priority
    
        if status != None:
            self.tasks[id_i]['status'] = status
    
        print('Task updated successfully!')


    def delete(self, id_i):
        if id_i not in self.tasks:
            print('Task not found!')
            return

        if self.tasks[id_i]['status'] in ['IN_PROGRESS', 'DONE']:
            confirm = input(
                'Are you sure you want to delete? (yes/no): ')

            confirm = confirm.strip().lower()

            if confirm == 'yes':
                del self.tasks[id_i]
                print('Task deleted successfully!')

            elif confirm == 'no':
                print('Deletion cancelled!')

            else:
                print('Invalid input!')

        elif self.tasks[id_i]['status'] == 'OPEN':
            del self.tasks[id_i]
            print('Task deleted successfully!')

    def search_by_assignee(self, assignee):
        found = False

        for task_id in self.tasks:
            if self.tasks[task_id]['assignee'].lower() == assignee.lower():
                found = True
                print('ID:', task_id)
                print('Title:', self.tasks[task_id]['title'])
                print('Assignee:', self.tasks[task_id]['assignee'])
                print('Priority:', self.tasks[task_id]['priority'])
                print('Status:', self.tasks[task_id]['status'])

        if found == False:
            print('No tasks found for this assignee!')

    def search_by_priority(self, priority):
        found = False

        priority = priority.upper()

        if priority not in ['LOW', 'MEDIUM', 'HIGH']:
            print('Invalid priority!')
            return

        for task_id in self.tasks:
            if self.tasks[task_id]['priority'] == priority:
                found = True
                print('ID:', task_id)
                print('Title:', self.tasks[task_id]['title'])
                print('Assignee:', self.tasks[task_id]['assignee'])
                print('Priority:', self.tasks[task_id]['priority'])
                print('Status:', self.tasks[task_id]['status'])

        if found == False:
            print('No tasks found for this priority!')

    def search_by_status(self, status):
        found = False

        status = status.upper()

        if status not in ['OPEN', 'IN_PROGRESS', 'DONE']:
            print('Invalid status!')
            return

        for task_id in self.tasks:
            if self.tasks[task_id]['status'] == status:
                found = True
                print('ID:', task_id)
                print('Title:', self.tasks[task_id]['title'])
                print('Assignee:', self.tasks[task_id]['assignee'])
                print('Priority:', self.tasks[task_id]['priority'])
                print('Status:', self.tasks[task_id]['status'])

        if found == False:
            print('No tasks found for this status!')


    def change_status(self, id_i, new_status):
        if id_i not in self.tasks:
            print('Task not found!')
            return
    
        new_status = new_status.strip().upper()
    
        if new_status not in ['OPEN', 'IN_PROGRESS', 'DONE']:
            print('Invalid status!')
            return
    
        current_status = self.tasks[id_i]['status']
    
        if new_status == current_status:
            print('Status is already the same!')
            return
    
        if self.is_valid_transition(current_status, new_status):
            self.tasks[id_i]['status'] = new_status
            print('Status changed successfully!')
        else:
            print('Invalid status transition!')


    def reports(self):
        total = len(self.tasks)
        completed = 0
        open_tasks = 0

        for task_id in self.tasks:
            if self.tasks[task_id]['status'] == 'DONE':
                completed = completed + 1

            elif self.tasks[task_id]['status'] == 'OPEN':
                open_tasks = open_tasks + 1

        print('Total tasks:', total)
        print('Completed tasks:', completed)
        print('Open tasks:', open_tasks)

    def report_by_assignee(self):
        assignee_count = {}

        for task_id in self.tasks:
            assignee = self.tasks[task_id]['assignee']

            if assignee in assignee_count:
                assignee_count[assignee] = assignee_count[assignee] + 1
            else:
                assignee_count[assignee] = 1

        for assignee in assignee_count:
            print(assignee, ':', assignee_count[assignee])

    def most_open_tasks(self):
        open_count = {}

        for task_id in self.tasks:
            if self.tasks[task_id]['status'] == 'OPEN':
                assignee = self.tasks[task_id]['assignee']

                if assignee in open_count:
                    open_count[assignee] = open_count[assignee] + 1
                else:
                    open_count[assignee] = 1

        if not open_count:
            print('No open tasks found!')
            return

        max_count = max(open_count.values())

        for assignee in open_count:
            if open_count[assignee] == max_count:
                print('Assignee:', assignee)
                print('Open tasks:', max_count)


manager = TaskManager()

while True:
    print('\n========== TASK MANAGER ==========')
    print('1. Create Task')
    print('2. Read Task')
    print('3. Read All Tasks')
    print('4. Update Task')
    print('5. Delete Task')
    print('6. Search by Assignee')
    print('7. Search by Priority')
    print('8. Search by Status')
    print('9. Change Status')
    print('10. Reports')
    print('11. Report by Assignee')
    print('12. Most Open Tasks')
    print('0. Exit')

    choice = input('Choose an option: ')

    if choice == '0':
        print('Goodbye!')
        break

    elif choice == '1':
        try:
            id_i = int(input('Enter ID: '))
        except ValueError:
            print('Please enter a valid number!')
            continue

        title = input('Enter title: ')
        assignee = input('Enter assignee: ')
        priority = input('Enter priority: ')
        status = input('Enter status: ')

        manager.create(id_i, title, assignee, priority, status)

    elif choice == '2':
        try:
            id_i = int(input('Enter ID: '))
        except ValueError:
            print('Please enter a valid number!')
            continue

        manager.read(id_i)

    elif choice == '3':
        manager.read_all()

    elif choice == '4':
        try:
            id_i = int(input('Enter ID: '))
        except ValueError:
            print('Please enter a valid number!')
            continue

        title = input('Enter new title: ')
        assignee = input('Enter new assignee: ')
        priority = input('Enter new priority: ')
        status = input('Enter new status: ')

        manager.update(
            id_i,
            title.strip() if title.strip() else None,
            assignee.strip() if assignee.strip() else None,
            priority.strip() if priority.strip() else None,
            status.strip() if status.strip() else None
        )

    elif choice == '5':
        try:
            id_i = int(input('Enter ID: '))
        except ValueError:
            print('Please enter a valid number!')
            continue

        manager.delete(id_i)

    elif choice == '6':
        assignee = input('Enter assignee: ')
        manager.search_by_assignee(assignee)

    elif choice == '7':
        priority = input('Enter priority: ')
        manager.search_by_priority(priority)

    elif choice == '8':
        status = input('Enter status: ')
        manager.search_by_status(status)

    elif choice == '9':
        try:
            id_i = int(input('Enter ID: '))
        except ValueError:
            print('Please enter a valid number!')
            continue

        new_status = input('Enter new status: ')
        manager.change_status(id_i, new_status)

    elif choice == '10':
        manager.reports()

    elif choice == '11':
        manager.report_by_assignee()

    elif choice == '12':
        manager.most_open_tasks()

    else:
        print('Invalid choice! Please choose 0 to 12.')
