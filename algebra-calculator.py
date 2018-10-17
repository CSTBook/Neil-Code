fthing = ""
sthing = ""
var = ""
num = 0
total = 0
stthing = " "
ndthing = " "
varnum = raw_input("Will you enter a variable first, or a number first(v/n)?")
while varnum != 'v' and varnum != 'n':
  varnum = raw_input("Hmm?")
else:
  if varnum == 'v':
    stthing = "Var"
  else:
    stthing = "Num"
if stthing == 'Var':
  stthing = raw_input("Please enter a variable: ")
  ndthing = "Num"
  var = stthing
  fthing + "Var"
else:
  stthing = float(raw_input("Please enter a number: "))
  ndthing = "Var"
  num = stthing
  fthing = "Num"
sign = raw_input("Would you like to add(a), subtract(s), multiply(m), or divide(d)?: ")
if ndthing == 'Var':
  ndthing = raw_input("Please enter a variable: ")
  var = ndthing
  sthing = "Var"
else:
  ndthing = float(raw_input("Please enter a number: "))
  num = ndthing
  sthing = "Num"
end = float(raw_input("Please enter what the equation is equal to: "))
if sign == 'a':
  total = end - num
  sign = "+"
elif sign == 's':
  total = end + num
  sign = "-"
elif sign == 'm':
  total = end / num
  sign = "*"
elif sign == 'd':
  total = end * num
  sign = "/"
else:
  print "Please restart the program "
print var, "is equal to", total
