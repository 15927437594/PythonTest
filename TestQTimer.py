# """
# user: Created by jid on 2023/5/14 11:04
# email: jid@hwtc.com.cn
# description:
# """
import sys
import time

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication


class TestQTimer:

    def __init__(self):
        super().__init__()
        print('12222')
        self.burn_time = 0
        self.aging_time_timer = QTimer()
        self.aging_time_timer.timeout.connect(self.update_burn_time)

    def update_burn_time(self):
        self.burn_time += 1
        print(self.burn_time)
        if self.burn_time == 5:
            self.stop()
            time.sleep(2)
            self.start()

    def start(self):
        self.aging_time_timer.start(1000)

    def stop(self):
        self.aging_time_timer.stop()
        self.burn_time = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer = TestQTimer()
    timer.start()
    sys.exit(app.exec_())

# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtCore import QTimer
# import sys
#
#
# def work():
#     print("hello world")
#
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     t = QTimer()
#     t.start(1000)
#     t.timeout.connect(work)
#     sys.exit(app.exec_())
