import time
import sys
import numpy
import random
import datetime
from SALPY_ATCamera import *

freq = 0.01
mgr = SAL_ATCamera()

mgr.salTelemetryPub("ATCamera_bonnShutter")
mgr.salTelemetryPub("ATCamera_wreb")
mgr.salTelemetryPub("ATCamera_wrebPower")

bonnShutter = ATCamera_bonnShutterC()
wreb = ATCamera_wrebC()
myData = ATCamera_wrebPowerC()

while True:
	#Topic 1
	bonnShutter.shutter5V = random.randint(4,6)
	bonnShutter.shutter36V = random.randint(33,38)
	retval = mgr.putSample_bonnShutter(bonnShutter)

	#Topic 2
	wreb.ckPSH_V = random.randint(4,6)
	wreb.ckPOV = random.randint(4,6)
	wreb.ogoV = random.randint(4,6)
	wreb.temp1 = random.randint(4,6)
	wreb.temp2 = random.randint(4,6)
	wreb.temp3 = random.randint(4,6)
	wreb.temp4 = random.randint(4,6)
	wreb.temp5 = random.randint(4,6)
	wreb.temp6 = random.randint(4,6)
	wreb.atemp0U = random.randint(4,6)
	wreb.atemp0L = random.randint(4,6)
	wreb.ccdTemp0 = random.randint(4,6)
	wreb.rtdTemp = random.randint(4,6)
	wreb.digPS_V = random.randint(4,6)
	wreb.digPS_I = random.randint(4,6)
	wreb.anaPS_V = random.randint(4,6)
	wreb.anaPS_I = random.randint(4,6)
	wreb.clkHPS_V = random.randint(4,6)
	wreb.clkHPS_I = random.randint(4,6)
	wreb.odPS_V = random.randint(4,6)
	wreb.odPS_I = random.randint(4,6)
	wreb.htrPS_V = random.randint(4,6)
	wreb.htrPS_I = random.randint(4,6)
	wreb.power = random.randint(4,6)
	wreb.sckU_V = random.randint(4,6)
	wreb.sckL_V = random.randint(4,6)
	wreb.rgU_V = random.randint(4,6)
	wreb.rgL_V = random.randint(4,6)
	wreb.cks0V = random.randint(4,6)
	wreb.rg0V = random.randint(4,6)
	wreb.od0V = random.randint(4,6)
	wreb.rd0V = random.randint(4,6)
	wreb.gd0V = random.randint(4,6)
	wreb.od0I = random.randint(4,6)
	retval = mgr.putSample_wreb(wreb)

	#Topic 3
	myData.digital_V = random.randint(4,6)
	myData.digital_I = random.randint(4,6)
	myData.analog_V = random.randint(4,6)
	myData.analog_I = random.randint(4,6)
	myData.clkHigh_V = random.randint(4,6)
	myData.clkHigh_I = random.randint(4,6)
	myData.clkLow_V = random.randint(4,6)
	myData.clkLow_I = random.randint(4,6)
	myData.od_V = random.randint(4,6)
	myData.od_I = random.randint(4,6)
	myData.dphi_V = random.randint(4,6)
	myData.dphi_I = random.randint(4,6)
	myData.heater_V = random.randint(4,6)
	myData.heater_I = random.randint(4,6)
	myData.hvbias_V = random.randint(4,6)
	myData.hvbias_I = random.randint(4,6)
	retval = mgr.putSample_wrebPower(myData)

	#Topic 4
	#Topic 5
	#Topic 6
	#Topic 7

	time.sleep(freq)

mgr.salShutdown()
exit()

