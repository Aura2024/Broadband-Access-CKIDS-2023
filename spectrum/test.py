from spectrum_frame_work import *
from threading import *
from multiprocessing.pool import ThreadPool

class App(Thread):
    def __init__(self, full_address):
        Thread.__init__(self)
        self.full_address = full_address
        self.plan = {}


    def run(self):
        self.plan = plan_set(self.full_address)

    def get_plan(self):
        return self.plan



address_book = [["1 62nd Place", "","90803"], ["10 17th Avenue","","90291"],["100 19th Street","","90254"], ["1000 245th Street","","90710"], ["10000 Aldea Avenue", "", "91325"]]

address_one = App(address_book[0])
address_two = App(address_book[1])

address_one.start()
address_two.start()

address_one.join()
address_two.join()

print(address_one.get_plan())
