from typing import Dict, Any

class Client:
    event_queue: Dict[int, str]

    def __init__(self,id):
        self.local_clock = 1
        self.event_queue = {}
        self.client_id = id

    def get_clock(self):
        return self.local_clock

    def get_events(self):
        return self.event_queue

    def update_events(self,event):
        self.event_queue[self.local_clock] = event

    def update_clock(self, input = 1):
        self.local_clock = max(self.local_clock, input) + 1

    def print_clock(self):
        all_event = [str(i) for i in [*self.event_queue].sort()]
        print(" ".join(all_event))
        return

    def get_pid(self):
        return self.client_id



