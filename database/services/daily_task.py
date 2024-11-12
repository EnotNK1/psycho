import uuid

from psycopg2 import Error
from sqlalchemy.orm import selectinload

from database.database import session_factory
from database.models.test import *
from database.models.users import *


class DailyTaskServiceDB:

    def change_daily_tasks(self, user_id):
        with session_factory() as session:
            query = (
                session.query(Users)
                .filter(Users.id == user_id)
                .options(
                    selectinload(Users.daily_tasks)
                )
            )
            user = query.one_or_none()
            task_list = []
            all_tasks = []
            last_task_day = 0
            flag = True

            for task in user.daily_tasks:
                all_tasks.append({
                    "id": task.id,
                    "title": task.title,
                    "short_desc": task.short_desc,
                    "destination_id": task.destination_id,
                    "is_complete": task.is_complete,
                    "number": task.number,
                    "day": task.day,
                    "is_current": task.is_current,
                })
            all_tasks = sorted(all_tasks, key=lambda x: x['number'])

            for obj in all_tasks:
                for task in user.daily_tasks:
                    if task.number == obj['number']:
                        task.is_current = False
                obj['is_current'] = False
                if obj['is_complete']:
                    last_task_day = obj['day']
                    if last_task_day == 8:
                        for task in user.daily_tasks:
                            task.is_current = False
                            if task.number in [25, 26, 27]:
                                task.is_current = True
                                task.is_complete = False
                        session.commit()
                        return
                    continue

                if flag:
                    flag = False
                    if last_task_day == 0:
                        stop = 3
                    elif last_task_day != obj['day']:
                        if obj['day'] in [1, 2, 6, 7, 8]:
                            stop = 3
                        elif obj['day'] in [3, 4, 5]:
                            stop = 4
                    else:
                        stop = 4

                if len(task_list) >= stop:
                    break
                task_dict = {
                    "id": obj['id'],
                    "title": obj['title'],
                    "short_description": obj['short_desc'],
                    "destination_id": obj['destination_id'],
                    "is_complete": obj['is_complete'],
                }
                if any(
                        task["title"] == task_dict["title"] and
                        task["short_description"] == task_dict["short_description"] and
                        task["destination_id"] == task_dict["destination_id"] and
                        task["is_complete"] == task_dict["is_complete"]
                        for task in task_list
                ):
                    continue
                for task in user.daily_tasks:
                    if task.number == obj['number']:
                        task.is_current = True
                obj['is_current'] = True
                task_list.append(task_dict)
            session.commit()

    def set_last_day_tasks(self, user_id):
        with session_factory() as session:
            query = (
                session.query(Users)
                .filter(Users.id == user_id)
                .options(
                    selectinload(Users.daily_tasks)
                )
            )
            user = query.one_or_none()

            for task in user.daily_tasks:
                task.is_complete = False
                task.is_current = False
                if task.number in [25, 26, 27]:
                    task.is_current = True
            session.commit()




    def get_daily_tasks(self, user_id):
        with session_factory() as session:
            query = (
                session.query(Users)
                .filter(Users.id == user_id)
                .options(
                    selectinload(Users.daily_tasks)
                )
            )
            user = query.one_or_none()
            task_list = []

            for obj in user.daily_tasks:
                if obj.is_current:
                    task_dict = {
                        "id": obj.id,
                        "title": obj.title,
                        "short_description": obj.short_desc,
                        "destination_id": obj.destination_id,
                        "is_complete": obj.is_complete,
                        "number": obj.number,
                    }
                    task_list.append(task_dict)
            task_list = sorted(task_list, key=lambda x: x['number'])

            for d in task_list:
                d.pop('number', None)

        return task_list

    def complete_daily_task(self, daily_task_id):
        with session_factory() as session:
            task = session.get(Daily_task, daily_task_id)
            if task is None:
                return -1
            task.is_complete = True
            session.commit()
        return 0

    def set_daily_tasks(self):
        with session_factory() as session:
            user = session.query(Users).all()

            for obj in user:
                daily_task_service_db.change_daily_tasks(obj.id)


daily_task_service_db: DailyTaskServiceDB = DailyTaskServiceDB()