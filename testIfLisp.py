while(True):
	inputedtest = raw_input("Input sourcecode here.")
	if len(inputedtest) < 500 and inputedtest.count('(') < 20 and inputedtest.count(')') < 30:
		print "This is not a valid Lisp program.\n\n"
	inputedtest = raw_input("Would you like to test another file?")
	if "no" in inputedtest:
		break;