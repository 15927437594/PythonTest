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
        if self.aging_time_timer.isActive():
            self.aging_time_timer.stop()
        self.burn_time = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer = TestQTimer()
    timer.start()
    brightness_value = int(0 * 255 / 100)
    print(brightness_value)
    brightness_value = int(1 * 255 / 100)
    print(brightness_value)
    brightness_value = int(2 * 255 / 100)
    print(brightness_value)
    brightness_value = int(3 * 255 / 100)
    print(brightness_value)
    brightness_value = int(4 * 255 / 100)
    print(brightness_value)
    brightness_value = int(5 * 255 / 100)
    print(brightness_value)
    brightness_value = int(90 * 255 / 100)
    print(brightness_value)
    brightness_value = int(91 * 255 / 100)
    print(brightness_value)
    brightness_value = int(92 * 255 / 100)
    print(brightness_value)
    brightness_value = int(93 * 255 / 100)
    print(brightness_value)
    brightness_value = int(94 * 255 / 100)
    print(brightness_value)
    brightness_value = int(95 * 255 / 100)
    print(brightness_value)
    brightness_value = int(100 * 255 / 100)
    print(brightness_value)

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
