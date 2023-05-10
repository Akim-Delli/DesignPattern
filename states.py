from __future__ import annotations

from abc import ABC, abstractmethod
from random import randint
from time import sleep


class State(ABC):
    @property
    def job(self) -> Job:
        return self._job

    @job.setter
    def job(self, job: Job) -> None:
        self._job = job

    @abstractmethod
    def notify(self) -> None:
        pass


class Started(State):
    def notify(self):
        print("Job has started")
        print("Notifying Everybody that Job has started")
        self.job.change_state(Running())


class Running(State):
    def notify(self):
        print("No need to notify anybody that job is running, So far so good!")
        print("Job is running...........")

        sleep(3)

        if randint(0, 10) <= 5:
            self.job.change_state(Succeeded())
        else:
            self.job.change_state(Failed())


class Succeeded(State):
    def notify(self):
        print("Job has succesfully completed")
        print("Emailing Stakeholders!")

        self.job.change_state(Finished())


class Failed(State):
    def notify(self):
        print("Job has miserably Failed")
        print("Emailing Engineering right away!")

        self.job.change_state(Finished())


class Finished(State):
    def notify(self):
        print("Job is Finished")

        self.job.change_state(Finished())
