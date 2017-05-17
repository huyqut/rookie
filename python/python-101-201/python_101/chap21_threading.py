# "threading" module

import random
import time
import os
from urllib.request import *
from threading import Thread


def default_run():
    """
    Default way to run thread:
    task = Thread(target = ..., args = (...), ...)
    task.start() <= officially start the thread
    task.join() <= wait for the task to merge
    :return: 
    """
    x = Thread(target = add, args = (1, 50))
    y = Thread(target = minus, args = (10, 20))
    x.start()  # Reverse order of lock
    y.start()
    y.join()
    x.join(10)  # Time-out of 10 seconds


def add(a, b):
    for i in range(a, b):
        print(i)


def minus(a, b):
    for i in range(b, a, -1):
        print(i)


class DumpThread(Thread):
    """
    Customized class for threading
    """

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        """
        Thread running
        """
        duration = random.randint(3, 15)
        time.sleep(duration)
        print(f"{self.name} is running")


def custom_thread():
    for i in range(10):
        DumpThread(f"Thread {i}").start()

# custom_thread()


class DownloadGist(Thread):
    """
    This class downloads a gist file given a url
    """

    def __init__(self, url: str, name: str):
        super().__init__()
        self.url = url
        self.name = name

    def run(self):
        """Start download the gist"""
        handle = urlopen(self.url)
        filename = os.path.basename(self.url)
        with open(filename, 'wb') as file:
            while True:
                chunk = handle.read(1024)
                if not chunk:
                    break
                file.write(chunk)
        print(f"Finish downloading. Please check the file {filename}")


def start_download(url: str):
    task = DownloadGist(url, 'Gist Download')
    task.start()
    task.join(10)

start_download('https://gist.githubusercontent.com/huyqut/28aadf0cb56deb01611349ef614ee893/raw/3081c504daae9362e5e670fe55a1c21d77595043/Java%2520Coding%2520Styles.xml')
