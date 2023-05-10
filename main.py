from __future__ import annotations

from states import Started

class Job:
    
    _current_state = None

    def __init__(self, state: State):
        self.change_state(state)

    def change_state(self, new_state: str):
        print(f"Job: Transitioning to {type(new_state).__name__}")
        self._current_state = new_state
        self._current_state.job = self
    
    def notify(self):
        self._current_state.notify()


        
    



if __name__ == '__main__':
    job = Job(Started())
    for _ in range(3):
        job.notify()
