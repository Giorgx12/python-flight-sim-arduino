from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
import serial

ser = serial.Serial('COM3', 9600, timeout=1)

class FlightSim(ShowBase):
    def init(self):
        ShowBase.init(self)
        self.disableMouse()

        self.plane = self.loader.loadModel("models/airplane.egg")
        self.plane.reparentTo(self.render)
        self.plane.setScale(0.5)
        self.plane.setPos(0, 50, 5)

        self.cam.setPos(0, -100, 20)
        self.cam.lookAt(self.plane)

        self.accept("arrow_left", lambda: self.cam.setH(self.cam.getH() + 5))
        self.accept("arrow_right", lambda: self.cam.setH(self.cam.getH() - 5))
        self.accept("arrow_up", lambda: self.cam.setP(self.cam.getP() - 2))
        self.accept("arrow_down", lambda: self.cam.setP(self.cam.getP() + 2))

        self.taskMgr.add(self.update_from_arduino, "updateTask")

    def update_from_arduino(self, task):
        if ser.in_waiting:
            try:
                data = ser.readline().decode().strip()
                x, y, throttle = map(int, data.split(','))
                self.plane.setH(x / 10 - 50)
                self.plane.setP(y / 10 - 50)
                self.plane.setY(self.plane, (throttle / 1023) * 0.5)
            except:
                pass
        return task.cont

app = FlightSim()
app.run()
