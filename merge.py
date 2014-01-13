#!/usr/bin/python

IN1 = "5_ces.txt"
IN2 = "5_fra.txt"

in1 = open(IN1, "r")
in2 = open(IN2, "r")
out = open('5merge.out', "w")

cze = in1.readlines()
fra = in2.readlines()

instructions = ""
for i, c in enumerate(cze):
    c = c.strip()
    if c.startswith("#!"):
        if len(c) > 2:
            instructions = " (%s)" % c[2:]
        else:
            instructions = ""
    if c.startswith("#"):
        continue
    out.write("%s%s#%s\n" % (c, instructions, fra[i].strip()))


