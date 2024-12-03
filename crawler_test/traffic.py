import requests
import os
from concurrent.futures import ThreadPoolExecutor, as_completed


class ThreadPool:
    def __init__(self, max_works=os.cpu_count()) -> None:
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


# 200MB
url = "https://dldir1.qq.com/qqfile/qq/PCQQ9.7.17/QQ9.7.17.29225.exe"
# 1000MB
# url = "https://875e1151af8aa9e3b793f51f6049996d.dlied1.cdntips.net/dlied4.myapp.com/myapp/1104466820/cos.release-40109/10040714_com.tencent.tmgp.sgame_a2480356_8.2.1.9_F0BvnI.apk"


def task(i: int):
    print(f"task {i} start ...")
    rsp = requests.get(url)
    print(rsp.status_code)
    print(f"task {i} end ...")


if __name__ == "__main__":
    # task()
    pool = ThreadPool()
    for i in range(20):
        pool.add_task(task, i)

    pool.get_results()
    pool.shutdown()
