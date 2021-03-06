from flask_socketio import SocketIO
from flask import Flask, render_template
from PIL import ImageGrab
from cv2 import cv2
import pytesseract
import numpy as np
import re

cv2.namedWindow("capture", cv2.WINDOW_FREERATIO)

app = Flask(__name__)
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("connect")
def connect():
    print("connected")


class TimeCapture:
    def __init__(self, x: int = 0, y: int = 0, width: int = 0, height: int = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.previous = "99:99:99"
        self.is_processing = True

    def capture(self):
        img = ImageGrab.grab(
            bbox=(
                self.x,
                self.y,
                self.x + self.width,
                self.y + self.height,
            )
        ).convert("L")
        img = np.array(img)
        cv2.imshow("capture", img)
        if not self.is_processing:
            return self.previous, False

        txt = pytesseract.image_to_string(img).strip()
        if (
            match := re.search(r"\d+:\d+:\d+", txt)
        ) is not None and match.group() != self.previous:
            self.previous = match.group()
            return match.group(), True
        return self.previous, False


def handle_keys(tc: TimeCapture):
    key = cv2.waitKey(25) & 0xFF
    if key == ord("q"):
        cv2.destroyAllWindows()
        return True
    elif key == ord(" "):
        tc.is_processing = not tc.is_processing
    elif key == ord("p"):
        print({"x": tc.x, "y": tc.y, "width": tc.width, "height": tc.height})
    elif not tc.is_processing:
        if key == ord("w"):
            tc.y -= 1
        elif key == ord("a"):
            tc.x -= 1
        elif key == ord("s"):
            tc.y += 1
        elif key == ord("d"):
            tc.x += 1
        elif key == ord("i"):
            tc.height -= 1
        elif key == ord("l"):
            tc.width += 1
        elif key == ord("k"):
            tc.height += 1
        elif key == ord("j"):
            tc.width -= 1
    return False


def capturing():
    print("capturing")
    tc = TimeCapture(128, 162, 331, 85)  # predetermined location
    socketio.sleep(2)
    while True:
        socketio.sleep(0.2 if tc.is_processing else 0)
        time, changed = tc.capture()
        if changed:
            print(time)
            hours, minutes, seconds = time.split(":")
            socketio.emit(
                "time",
                {
                    "hours": hours,
                    "minutes": minutes,
                    "seconds": seconds,
                },
            )
        if handle_keys(tc):
            break


def main():
    socketio.start_background_task(capturing)
    socketio.run(app, host="0.0.0.0", port="3600")


if __name__ == "__main__":
    main()
