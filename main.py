
"""
	CS 153 Project: Galois Field Calculator
	--
	Gabrielle Marie Torres
	2014 06394
"""

# imports
import galois

# -- read input vectors
print "Welcome to the Galois Field Calculator."
print "Please input polynomials as a space-delimited list of values.\n"

va_in = raw_input("Input polynomial A: ").strip()
vb_in = raw_input("Input polynomial B: ").strip()
vp_in = raw_input("Input P(x): ").strip()

# -- convert input string into a list of integers
va = [int(i) for i in va_in.split()]
vb = [int(i) for i in vb_in.split()]
vp = [int(i) for i in vp_in.split()]

op = ""
while op not in ["add", "subtract", "multiply", "divide"]:
	op = raw_input("[add/subtract/multiply/divide]: ").strip().lower()

# get m (number of bits)
m = len(vp) - 1
pm = 2 ** m
print "\nGalois field = GF(" + str(pm) + ") or GF(2^" + str(m) + ")\n"

# -- perform operation
if op == "add":
	print "-- Performing A + B --\n"
	out = galois.add(va, vb, vp)
elif op == "subtract":
	print "-- Performing A - B --\n"
	out = galois.subtract(va, vb, vp)
elif op == "multiply":
	print "-- Performing A * B --\n"
	out = galois.multiply(va, vb, vp)
elif op == "divide":
	print "-- Performing A / B --\n"
	out = galois.divide(va, vb, vp)

# display results
print "\n-- Results --\n"
print "  " + "\t".join([str(i) for i in va])
if op == "add":
	print "+",
if op == "subtract":
	print "-",
if op == "multiply":
	print "*",
if op == "divide":
	print "/",
print "\t".join([str(i) for i in vb])
print "= " + "\t".join([str(i) for i in out])
