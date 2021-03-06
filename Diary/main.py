import sys

from diary import storage

conn = storage.connect()
storage.initialize(conn)

def action_show_menu():
	print(''' 
		Ежедневник. Выберите действие:
1. Вывести список задач
2. Добавить задачу
3. Отдредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
q. Выход''')

def action_exit():
	conn.close()
	sys.exit(0)

def action_all_tasks():
	all_tasks=storage.all_tasks(conn)
	for task in all_tasks:
		print('{task[name]} - task[text]} - {task[planned]} - {task[status]}'.format(task=task))

def action_add_task():
	task_name = input('Название задачи:\n')
	task_date = input('Дата выполнения:\n')
	text = input('Тескт задачи:\n')
	storage.add_task(conn, task_name, task_date, text)
		
actions = {
    '1': action_all_tasks,
    '2': action_add_task,
    '3': action_update_task,
    '4': action_close_task,
    '5': action_re_task,
    'm': action_show_menu,
    'q': action_exit
}

if __name__ == '__main__':
    action_show_menu()

    while True:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)
        if action:
            action()
        else:
print('Неизвестная команда')









