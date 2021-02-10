from SingleInstance import SingleInstance
import numpy as np


class Timer():
    _dict = {}
    finish_list = []

    def trigger(self, who):
        self._dict[who] = who.interval

    def update(self):
        # keys=np.array(list(self._dict.keys()))
        # print(keys)
        # intervals=np.array(list(self._dict.values()))
        # intervals-=3
        # print(2,intervals)
        #
        # end_index = np.argwhere(intervals > 0)
        # print(end_index)
        # self.finish_list=list(self._dict.keys())
        # intervals
        for w in self._dict.keys():
            if self._dict[w] > 0:
                self._dict[w] -= 3
            else:
                self.finish_list.append(w)
        # print(self.finish_list)

    def finish(self, who):
        if who in self._dict.keys():
            if who in self.finish_list:
                self.finish_list.remove(who)
                del self._dict[who]
                return True
            else:
                return self._dict[who]
        else:
            return True


@SingleInstance
class TimerColdDown(Timer):
    pass


class TimerInterval():
    def __init__(self, interval):
        self.interval = interval
        self.ready = 0

    def is_ready(self):
        return self.ready

    def set_ready(self, bool):
        self.ready = bool


class Timer2():
    _dict_line_id = {}
    rest = []
    vec = None

    def __init__(self, length):
        self.vec = np.zeros([length, 1])

    def start(self, who):
        if not self.rest:
            self._dict_line_id[who] = len(self._dict_line_id)
            self.vec.put(len(self._dict_line_id) - 1, who.interval)
        else:
            self.vec.put(self.rest.pop(), who.interval)

    def update(self):
        timer.vec-3


    def caller(self, input, func):
        pass

    def finish(self, who):
        if who in self._dict_line_id.keys():
            self._dict_lineId[who]
