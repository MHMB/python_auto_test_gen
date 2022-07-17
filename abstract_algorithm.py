import abc


class Algorithm(abc.ABC):
    @abc.abstractmethod
    def init_data(self, run_info):
        pass

    @abc.abstractmethod
    def run(self, run_info):
        pass
