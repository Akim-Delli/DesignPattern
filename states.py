from __future__ import annotations

from abc import ABC, abstractmethod
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
        print('Job has started')
        print('Notifying Everybody that Job has started')
        self.job.change_state(Running())


class Running(State):

    def notify(self):
        print('Job is running')
        print('No need to notify anybody that job is running, So far so good!')
        
        sleep(3)
        
        self.job.change_state(Succeeded())
       


class Succeeded(State):

    def notify(self):
        print('Job has succefully completed')
        print('Emailing Stakeholders!')