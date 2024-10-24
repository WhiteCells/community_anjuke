from concurrent.futures import ThreadPoolExecutor, as_completed


class ThreadPool:
    def __init__(self, max_works) -> None:
        self.__max_works = max_works
        self.__exectuor = ThreadPoolExecutor(max_workers=self.__max_works)
        self.__futures = []

    def add_task(self, task, *args, **kwargs) -> None:
        future = self.__exectuor.submit(task, *args, **kwargs)
        self.__futures.append(future)

    def get_results(self) -> list:
        results = []
        for future in as_completed(self.__futures):
            try:
                res = future.result()
                results.append(res)
            except Exception as e:
                print("ThreadPool::get_results Exception: ", e)
        return results

    def shutdown(self) -> None:
        try:
            self.__exectuor.shutdown()
            print("ThreadPool::shutdown")
        except Exception as e:
            print("ThreadPool::shutdown Exception: ", e)


import time


def task(i):
    print(f"Task {i} is starting")
    time.sleep(1)
    print(f"Task {i} is completed")


pool = ThreadPool(2)

pool.add_task(task, 1)
pool.add_task(task, 2)
pool.add_task(task, 3)
