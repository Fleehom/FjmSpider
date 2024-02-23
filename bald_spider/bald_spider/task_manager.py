from typing import Set, Final
from asyncio import Task, Future, Semaphore
import asyncio


class TaskManager:

    def __init__(self, total_concurrency=6):
        self.current_task: Final[Set] = set()
        self.semaphore: Semaphore = Semaphore(total_concurrency)

    def create_task(self, corotine) -> Task:
        task = asyncio.create_task(corotine)
        self.current_task.add(task)

        def done_callback(_funt: Future):
            self.current_task.remove(task)
            self.semaphore.release()

        task.add_done_callback(done_callback)
        return task

    def all_done(self):
        return len(self.current_task) == 0