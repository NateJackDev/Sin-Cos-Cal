#!/usr/bin/env python
import math

# Instructions
print "----------------------------------------------------------"
print "----------------------------------------------------------"
print "----------------------------------------------------------"
print "        _____      _            _       _                 "
print "       / ____|    | |          | |     | |                "
print "      | |     __ _| | ___ _   _| | __ _| |_ ___  _ __     "
print "      | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|    "
print "      | |___| (_| | | (__| |_| | | (_| | || (_) | |       "
print "       \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|       "
print "                                                          "
print "----------------------------------------------------------"
print "This is a calculator finding the value of x in sin and cos"
print "----------------------------------------------------------"
print "-------------------  Example: sin(x)=1  ------------------"
print "----------------------------------------------------------"


# Arguments
print "What is the operation:\n"
print "[1] Sin"
print "[2] Cos\n"

option = int(raw_input("Which option> "))
value = float(raw_input("Please enter the value> "))
print "-----------------------------------------------------------"

# Radian to Degree
def rad2deg(radians):
	pi = math.pi
	degrees = 180 * radians / pi
	return degrees

# Print Sin and Cos Value
def info(trigfunc,input,radian,radian2,degree,degree2):
	print str(trigfunc) + "(x)=" + str(input) + "\n"
	print "Radians -> (" + str(radian) + ") and (" + str(radian2) + ")"
	print "Degrees -> " + str(degree) + " and " + str(degree2)

# Constrain argument
def constrainarg():
	print "Is there a constrain?"
	print "[1] Yes"
	print "[2] No"

# Negative radian to Positive radian
def neg2pos(start,finish):
	print "Converting negitive radians to postive radians..."
	print str(start) + " -> " + str(finish)

# Converting Negitive Radians to Positive Radians
def checkneg2pos(trigfunc,trigfunc2,tricfuncc,trigfunc2c):
	if trigfunc < float(0):
		trigfunc = float((2*math.pi) + trigfunc)
		neg2pos(tricfuncc,trigfunc)
	if trigfunc2 < float(0):
		trigfunc2 = float((2*math.pi) + trigfunc2)
		neg2pos(trigfunc2c,trigfunc2)

# Constrain Calculation
def constraincal(end,trigfunc,trigfunc2,res,res2):
	for x in range(0, end):
		if trigfunc + (x*(2*math.pi)) > res and trigfunc + (x*(2*math.pi)) < res2:
			print trigfunc + (x*(2*math.pi))
		elif trigfunc2 + (x*(2*math.pi)) > res and trigfunc2 + (x*(2*math.pi)) < res2:
			print trigfunc2 + (x*(2*math.pi))

def constrainop():
	print "What type of Constrain:"
	print "[1] Raw Radians"
	print "[2] Pre Radian Conf"

# Choice (Sin or Cos)
if option == 1:
	op = 1
elif option == 2:
	op = 2

# Operation of Sin and Cos
if op == 1:
	# Sin Values
	sin = math.asin(value)
	sinTwo = (-1*math.pi) - math.asin(value)
	sinDeg = rad2deg(sin)
	sinDegTwo = rad2deg(sinTwo)

	# Sin Value in Radian and Degree
	info(str("sin"),value,sin,sinTwo,sinDeg,sinDegTwo)
	print "-----------------------------------------------------------"

	# Constrains Options
	constrainarg()
	sincarg = int(raw_input("Which option> "))

	# Redefining Sin
	sinc = sin
	sinTwoc = sinTwo

	# Constrain Calculation
	if sincarg == 1:
		constrainop()
		constrainoparg = int(raw_input("Which option>"))
		if constrainoparg == 1:
			# Converting Negitive Radians to Positive Radians
			checkneg2pos(sin,sinTwo,sinc,sinTwoc)
			sinres1 = float(raw_input("What is the first constrain in radians> "))
			sinres2 = float(raw_input("What is the second constrain in radians> "))
			constraincal(10,sin,sinTwo,sinres1,sinres2)
		elif constrainoparg ==2:
			# Converting Negitive Radians to Positive Radians
			checkneg2pos(sin,sinTwo,sinc,sinTwoc)
			sinres1arg = float(raw_input("What is the first constrain> "))
			sinres2arg = float(raw_input("What is the second constrain> "))
			sinres1 = float((sinres1arg*math.pi) / 2)
			sinres2 = float((sinres2arg*math.pi) / 2)
			constraincal(10,sin,sinTwo,sinres1,sinres2)
	else:
		print "All done here!"
		quit()
elif op == 2:
	# Cos Values
	cos = math.acos(value)
	cosTwo = -1 * cos
	cosDeg = rad2deg(cos)
	cosDegTwo = rad2deg(cosTwo)

	#Cos Value in Radian and Degrees
	info(str("cos"),value,cos,cosTwo,cosDeg,cosDegTwo)
	print "-----------------------------------------------------------"

	# Constrains Options
	constrainarg()
	coscarg = int(raw_input("Which option> "))

	# Redefining Sin
	cosc = cos
	cosTwoc = cosTwo

	# Constrain Calculation
	if coscarg == 1:
		constrainop()
		constrainoparg = int(raw_input("Which option>"))
		if constrainoparg == 1:
			# Converting Negitive Radians to Positive Radians
			checkneg2pos(cos,cosTwo,cosc,cosTwoc)
			cosres1 = float(raw_input("What is the first constrain in radians> "))
			cosres2 = float(raw_input("What is the second constrain in radians> "))
			constraincal(10,cos,cosTwo,cosres1,cosres2)
		elif constrainoparg ==2:
			# Converting Negitive Radians to Positive Radians
			checkneg2pos(cos,cosTwo,cosc,cosTwoc)
			cosres1arg = float(raw_input("What is the first constrain> "))
			cosres2arg = float(raw_input("What is the second constrain> "))
			cosres1 = float((cosres1arg*math.pi) / 2)
			cosres2 = float((cosres2arg*math.pi) / 2)
			constraincal(10,cos,cosTwo,cosres1,cosres2)
	else:
		print "All done here!"
		quit()
