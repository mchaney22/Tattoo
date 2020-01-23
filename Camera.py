import cv2
import time


class Camera:
    def __init__(self, c_value: int, cool_down=(1/10)):
        self.cap = cv2.VideoCapture(c_value)
        self.cool_down=cool_down #minimum seconds between recorded frames
        self.time_last_frame = 0

    def get_frame(self):
        next_time_min = self.time_last_frame + self.cool_down
        while (next_time_min > time.time()):
            time.sleep(next_time_min-time.time())
        self.time_last_frame = time.time()
        ret, frame = self.cap.read()
        return frame


def test():
    camera = Camera(1)
    for i in range(300):
        filename = "training_B{}.jpg".format(i)
        frame = camera.get_frame()
        cv2.imwrite(filename, frame)

if __name__ == "__main__":
    test()