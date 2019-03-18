import time
import sys
import numpy
import random
import datetime

from SALPY_ATMCS import *
mgr = SAL_ATMCS()

mgr.salTelemetryPub("ATMCS_mountMotorEncoders")
mountMotorEncoders = ATMCS_mountMotorEncodersC()

mgr.salTelemetryPub("ATMCS_mountEncoders")
mountEncoders = ATMCS_mountEncodersC()

mgr.salTelemetryPub("ATMCS_measuredMotorVelocity")
measuredMotorVelocity = ATMCS_measuredMotorVelocityC()

mgr.salTelemetryPub("ATMCS_measuredTorque")
measuredTorque = ATMCS_measuredTorqueC()

mgr.salTelemetryPub("ATMCS_torqueDemand")
torqueDemand = ATMCS_torqueDemandC()

while True:
	time_init = datetime.datetime.now()

	#Topic 1
	mountMotorEncoders.elevationEncoder = random.uniform(0, 100)
	mountMotorEncoders.azimuth1Encoder = random.uniform(0, 100)
	mountMotorEncoders.azimuth2Encoder = random.uniform(0, 100)
	mountMotorEncoders.nasmyth1Encoder = random.uniform(0, 100)
	mountMotorEncoders.nasmyth2Encoder = random.uniform(0, 100)
	mountMotorEncoders.m3Encoder = random.uniform(0, 100)
	mountMotorEncoders.elevationEncoderRaw = random.randint(0,100)
	mountMotorEncoders.azimuth1EncoderRaw = random.randint(0,100)
	mountMotorEncoders.azimuth2EncoderRaw = random.randint(0,100)
	mountMotorEncoders.nasmyth1EncoderRaw = random.randint(0,100)
	mountMotorEncoders.nasmyth2EncoderRaw = random.randint(0,100)
	mountMotorEncoders.m3EncoderRaw = random.randint(0,100)
	retval = mgr.putSample_mountMotorEncoders(mountMotorEncoders)


	#Topic 2
	mountEncoders.elevationCalculatedAngle = random.uniform(0, 100)
	mountEncoders.azimuthCalculatedAngle = random.uniform(0, 100)
	mountEncoders.nasmyth1CalculatedAngle = random.uniform(0, 100)
	mountEncoders.nasmyth2CalculatedAngle = random.uniform(0, 100)
	mountEncoders.elevationEncoder1Raw = random.randint(0,100)
	mountEncoders.elevationEncoder2Raw = random.randint(0,100)
	mountEncoders.elevationEncoder3Raw = random.randint(0,100)
	mountEncoders.azimuthEncoder1Raw = random.randint(0,100)
	mountEncoders.azimuthEncoder2Raw = random.randint(0,100)
	mountEncoders.azimuthEncoder3Raw = random.randint(0,100)
	mountEncoders.nasmyth1Encoder1Raw = random.randint(0,100)
	mountEncoders.nasmyth1Encoder2Raw = random.randint(0,100)
	mountEncoders.nasmyth1Encoder3Raw = random.randint(0,100)
	mountEncoders.nasmyth2Encoder1Raw = random.randint(0,100)
	mountEncoders.nasmyth2Encoder2Raw = random.randint(0,100)
	mountEncoders.nasmyth2Encoder3Raw = random.randint(0,100)
	mountEncoders.trackId = random.randint(0,100)
	retval = mgr.putSample_mountEncoders(mountEncoders)

	#Topic 3
	measuredMotorVelocity.elevationMotorVelocity = random.uniform(0, 100)
	measuredMotorVelocity.azimuthMotor1Velocity = random.uniform(0, 100)
	measuredMotorVelocity.azimuthMotor2Velocity = random.uniform(0, 100)
	measuredMotorVelocity.nasmyth1MotorVelocity = random.uniform(0, 100)
	measuredMotorVelocity.nasmyth2MotorVelocity = random.uniform(0, 100)
	measuredMotorVelocity.m3Velocity = random.uniform(0, 100)
	retval = mgr.putSample_measuredMotorVelocity(measuredMotorVelocity)

	#Topic 4
	measuredTorque.elevationMotorTorque = random.uniform(0, 100)
	measuredTorque.azimuthMotor1Torque = random.uniform(0, 100)
	measuredTorque.azimuthMotor2Torque = random.uniform(0, 100)
	measuredTorque.nasmyth1MotorTorque = random.uniform(0, 100)
	measuredTorque.nasmyth2MotorTorque = random.uniform(0, 100)
	measuredTorque.m3Torque = random.uniform(0, 100)
	retval = mgr.putSample_measuredTorque(measuredTorque)

	#Topic 5
	torqueDemand.elevationMotorTorque = random.uniform(0, 100)
	torqueDemand.azimuthMotor1Torque = random.uniform(0, 100)
	torqueDemand.azimuthMotor2Torque = random.uniform(0, 100)
	torqueDemand.nasmyth1MotorTorque = random.uniform(0, 100)
	torqueDemand.nasmyth2MotorTorque = random.uniform(0, 100)
	retval = mgr.putSample_torqueDemand(torqueDemand)


	time.sleep(0.02) #Print at 50Hz
	print(datetime.datetime.now() - time_init) #Print publish frequency

mgr.salShutdown()
exit()

