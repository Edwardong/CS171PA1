from typing import Dict, Any
from collections import OrderedDict

class Client:
    #event_queue: OrderedDict[int, str]

    def __init__(self, id):
        self.local_clock = 0
        self.event_queue = OrderedDict()
        self.client_id = id
        self.started = False

    def get_clock(self):
        return self.local_clock

    def get_events(self):
        return self.event_queue

    def update_events(self, event):
        self.event_queue[self.local_clock] = event
        self.started = True

    def update_clock(self, input_counter=1):
        self.local_clock = max(self.local_clock, input_counter) + 1

    def print_clock(self):
        if not self.started:
            print("0")
        else:
            #all_event = [str(i) for i in [*self.event_queue].sort()]
            print("P{} clock:".format(self.client_id))
            for e in self.event_queue:
                print("[", e, "]", self.event_queue[e])

        return self.event_queue

    def get_pid(self):
        return self.client_id
