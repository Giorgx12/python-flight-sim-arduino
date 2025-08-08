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
