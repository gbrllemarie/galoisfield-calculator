
def add(x, y, p, disp=True):
	# create a reversed copy of the polynomials
	rx = list(reversed(x))
	ry = list(reversed(y))

	ptr = 0
	out = []
	# loop until everything is processed
	while ptr < len(rx) or ptr < len(ry):
		if disp:
			print "2^" + str(ptr) + ":\t",

		try:
			a = rx[ptr]
		except IndexError as e:
			a = 0

		try:
			b = ry[ptr]
		except IndexError as e:
			b = 0

		if disp:
			print "a = " + str(a) + ";\t",
			print "b = " + str(b) + ";\t",

		s = a^b
		out.insert(0, s)
		if disp:
			print "a^b = " + str(s)

		ptr += 1

	# trim zeros
	z = 0
	for i in out:
		if i > 0:
			break
		z += 1

	if z == len(out):
		z -= 1

	return out[z:]

def subtract(x, y, p, disp=True):
	return add(x, y, p, disp)

def digit_multiply(x, y, p, disp=True):
	if disp:
		print "\t" + str(x) + " * " + str(y),
	if x == 0 or y == 0:
		if disp:
			print " = 0"
		return 0

	sp = 0
	fp = 0
	for i, val in enumerate(p):
		sp = sp << 1
		fp = fp << 1
		if i > 0:
			sp = sp | val
			fp = fp | 1

	out = 0
	while y > 0:
		if y & 1:
			out = out ^ x
		y = y >> 1
		carry = x >> (len(p) - 2)
		x = (x << 1) & fp
		if carry:
			x = x ^ sp

	if disp:
		print "= " + str(out)
	return out

def multiply(x, y, p, divide=False, disp=True):
	rx = list(reversed(x))
	ry = list(reversed(y))

	out = [0]
	depth = 0
	for dy in ry:
		if divide:
			dy = inverse(dy, p)
		if disp:
			print "\n" + str(x) + " * " + str(dy)

		dp = []
		# perform multiplication of coeffient against x
		for dx in rx:
			dp.insert(0, digit_multiply(dx, dy, p, disp))

		for i in xrange(depth):
			dp.append(0)
		depth += 1

		out = add(out, dp, p, False)

		if disp:
			print "product       = " + str(dp)
			print "total product = " + str(out)

	# trim zeros
	z = 0
	for i in out:
		if i > 0:
			break
		z += 1

	if z == len(out):
		z -= 1

	return out[z:]

def inverse(x, p):
	print "Looking for the multiplicative inverse of " + str(x) + "..."
	if x == 0:
		print "Unable to divide by zero."
		return 0

	# brute force inverse search
	for i in xrange(1, 2**(len(p) - 1)):
		if multiply([x], [i], p, False, False) == [1]:
			break

	print str(i) + " is the multiplicative inverse of " + str(x) + "."
	return i

def poly_inverse(x, p):
	print "Looking for the multiplicative inverse of " + str(x) + "..."
	if x == [0]:
		print "Unable to divide by zero."
		return [0]

	# get m (number of bits)
	m = len(p) - 1
	pm = 2 ** m

	s = p
	v = [0]
	r = x
	u = [1]

	# brute force inverse search
	inverse = [0 for n in xrange(pm)]
	found = False
	old2 = 0
	while not found:
		inverse[pm-1] += 1
		ic = pm - 1
		while inverse[ic] == pm:
			inverse[ic-1] += 1
			inverse[ic] = 0
			ic -= 1

		if inverse[1] != old2:
			print "Checking " + str(inverse)
			old2 = inverse[1]
		if multiply(x, inverse, p, False, False) == [1]:
			found = true

	if not found:
		print "Unable to find the multiplicative inverse."
		return [0]

	print str(inverse) + " is the multiplicative inverse of " + str(x) + "."
	return inverse

def divide(x, y, p):
	#	return multiply(x, poly_inverse(y, p), p)
	#	return multiply(x, y, p, True)
	quotient = []

	nextq = 1
	yprod = multiply(y, [nextq], p, False, False)
	while len(yprod) <= len(x):
		while yprod[0] != x[0]:
			nextq += 1
			yprod = multiply(y, [nextq], p, False, False)

		if len(yprod) > len(x):
			break
		else:
			quotient.append(nextq)
			xlen = len(x)
			for z in xrange(xlen - len(yprod)):
				yprod.append(0)
			print "quotient += " + str(nextq)
			print "x     = " + str(x)
			print "yprod = " + str(yprod)
			x = subtract(x, yprod, p, False)
			print "new x = " + str(x)
			print ""
			for z in xrange(xlen - len(x) - 1):
				quotient.append(0)
			nextq = 1
			yprod = multiply(y, [nextq], p, False, False)

	return quotient


