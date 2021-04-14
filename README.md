# Ludwig Timer

[Ludwig, a Twitch streamer](https://twitch.tv/ludwig), thought it would be a good idea to start streaming one day and set a timer which increased by 10 seconds for every $5 subscription someone bought. 31 days later, he decided to quit. While he was still live, I wrote a Python script which scans the Twitch stream for this timer overlay, reads the time, and broadcasts out to a custom website in real time with WebSockets.

## YouTube Video

[https://youtu.be/ZYoort5jrUQ](https://youtu.be/ZYoort5jrUQ)

## Python packages to install:

- eventlet
- Flask
- Flask-SocketIO
- greenlet
- Pillow
- numpy
- opencv-python
- py-tesseract

## Install via pip with:

(Windows)
```
py -3.9 -m pip install -r requirements.txt
```
(Linux)
```
python3.9 -m pip install -re requirements.txt
```

You also need tesseract-ocr (on both platforms) and opencv (Linux only)

(Windows)

https://www.youtube.com/watch?v=haHuVAUGY5Y

(Linux)

tesseract-ocr https://www.youtube.com/watch?v=2xrFxHIp\_Fk

opencv https://www.youtube.com/watch?v=cGmGOi2kkJ4

## Credits

This wouldn't have been possible without (obviously) Ludwig's stream, so check him out: https://www.twitch.tv/ludwig

Also inspired by Micael Reeves' "A Robot Shoots Me When I Get Shot in Fortnite" https://www.youtube.com/watch?v=D75ZuaSR8nQ

This uses Flask, SocketIO, Python3, OpenCV, and tesseract-ocr
