

import picoweb
import camera
import machine
import time
import gc

app = picoweb.WebApp('app')

i2c = machine.I2C(scl=machine.Pin(13), sda=machine.Pin(4))



def myCapture():
    while True:
        buf = camera.capture()
        yield (b'--myBoundary\r\n'
               b'Content-Type: image/jpeg\r\n\r\n'
               + buf + b'\r\n')
        del buf
        gc.collect()





camera.init(0, d0=32, d1=35, d2=34, d3=5, d4=39, d5=18, d6=36, d7=19, format=camera.JPEG, framesize=camera.FRAME_QVGA, xclk_freq=camera.XCLK_10MHz, href=26, vsync=25, reset=15, sioc=23, siod=22, xclk=27, pclk=21)

#buf = camera.capture()


@app.route("/")
def index(req, resp):
    yield from picoweb.start_response(resp, content_type = 'text/html')
    htmlFile = open('webCamera.html', 'r')
    for line in htmlFile:
        yield from resp.awrite(line)




@app.route("/capture.jpg")
def capture(req, resp):
    yield from picoweb.start_response(resp, content_type = "multipart/x-mixed-replace; boundary=myBoundary")
    while True:
        yield from resp.awrite(next(myCapture()))
        gc.collect()
        time.sleep(0.2)







app.run(debug=True, host = '192.168.0.148')
#app.run(debug=True, host = '192.168.0.149')
#app.run(debug=True, host = '192.168.4.1')
