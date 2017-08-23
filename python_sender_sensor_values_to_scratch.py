import scratch
from gpiozero import DistanceSensor
from time import sleep
s = scratch.Scratch()
Sensor = DistanceSensor(echo=17, trigger=4)
while True:
	print(Sensor.distance)
	s.sensorupdate({'UltrasonicSensor' : Sensor.distance})
	sleep(0.1)
