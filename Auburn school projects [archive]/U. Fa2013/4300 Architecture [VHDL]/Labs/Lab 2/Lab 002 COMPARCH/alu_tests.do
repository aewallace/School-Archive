#Albert Wallace, aew0024@auburn.edu, COMP4300, 15 Oct 2013

#This test file, companion to the virtual ALU, tests...
#Op 0x2 = logical AND
#Op 0x3 = logical OR
#Op 0x0 = addition
#Op 0x1 = subtraction
#Op 0xE = multiplication
#Op 0x9 = [test of an unused code]
#Op 0xB = set less than...
#in that order.

#some cases causes error to be set to 0001 [overflow]
#otherwise it should be set to 0000

#let the tests begin...NOW

#test AND
add wave -r /*

force -freeze /alu/operation 16#2

force -freeze /alu/operand1 2#00000000000000000000000000000000
force -freeze /alu/operand2 2#11111111111111111111111111111111
force -freeze /alu/signed 1

run 50

force -freeze /alu/operand1 2#01111111111111111111111111111111
force -freeze /alu/operand2 2#00000000000000000000000000000001
force -freeze /alu/signed 1

run 50

force -freeze /alu/operand1 2#11111111111111111111111111111111
force -freeze /alu/operand2 2#11111111111111111111111111111111
force -freeze /alu/signed 1

run 50

force -freeze /alu/operand1 2#00000000000000000000000000000000
force -freeze /alu/operand2 2#00000000000000000000000000000000
force -freeze /alu/signed 1

run 50

#test OR
force -freeze /alu/operation 16#3

force -freeze /alu/operand1 2#00000000000000000000000000000000
force -freeze /alu/operand2 2#11111111111111111111111111111111
force -freeze /alu/signed 1

run 50

force -freeze /alu/operand1 2#01111111111111111111111111111111
force -freeze /alu/operand2 2#00000000000000000000000000000001
force -freeze /alu/signed 1

run 50

force -freeze /alu/operand1 2#11111111111111111111111111111111
force -freeze /alu/operand2 2#11111111111111111111111111111111
force -freeze /alu/signed 1

run 50

force -freeze /alu/operand1 2#00000000000000000000000000000000
force -freeze /alu/operand2 2#00000000000000000000000000000000
force -freeze /alu/signed 1

run 50

#test ADD
force -freeze /alu/operation 16#0

#signed ADD
force -freeze /alu/signed 1

force -freeze /alu/operand1 2#11111111111111111111111111111111
force -freeze /alu/operand2 2#00000000000000000000000000000011
run 50

force -freeze /alu/operand1 2#00000000000000000000000000000001
force -freeze /alu/operand2 2#01111111111111111111111111111111
run 50

force -freeze /alu/operand1 2#11111111111111111111111111111111
force -freeze /alu/operand2 2#11111111111111111111111111111111
run 50

force -freeze /alu/operand1 2#00000000000000000000000000000000
force -freeze /alu/operand2 2#00000000000000000000000000000000
run 50

#unsigned ADD
force -freeze /alu/signed 0

force -freeze /alu/operand1 2#01111111111111111111111111111111
force -freeze /alu/operand2 2#00000000000000000000000000000000
run 50

force -freeze /alu/operand1 2#01111111111111111111111111111111
force -freeze /alu/operand2 2#01111111111111111111111111111111
run 50

force -freeze /alu/operand1 2#01111111111111111111111111111111
force -freeze /alu/operand2 2#01111111111111111111111111111111

run 50

force -freeze /alu/operand1 2#00000000000000000000000000000000
force -freeze /alu/operand2 2#00000000000000000000000000000000
run 50

#run SUB...
force -freeze /alu/operation 1

#signed SUB

force -freeze /alu/operand1 2#10000000000000000000000000000000
force -freeze /alu/operand2 2#10000000000000000000000000000000
run 50

force -freeze /alu/signed 1
force -freeze /alu/operand1 2#11111111111111111111111111111111
force -freeze /alu/operand2 2#00000000000000000000000000000000
run 50

force -freeze /alu/operand1 2#00000000000000000000000000000000
force -freeze /alu/operand2 2#11111111111111111111111111111111
run 50

force -freeze /alu/operand1 2#01111111111111111111111111111111
force -freeze /alu/operand2 2#01111111111111111111111111111111
run 50

force -freeze /alu/operand1 2#11111111111111111111111111111111
force -freeze /alu/operand2 2#00000000000000000000000000000001
run 50



#unsigned SUB
force -freeze /alu/signed 0

force -freeze /alu/operand1 2#01111111111111111111111111111111
force -freeze /alu/operand2 2#00000000000000000000000000000000
run 50

force -freeze /alu/operand1 2#01111111111111111111111111111111
force -freeze /alu/operand2 2#01111111111111111111111111111111
run 50

force -freeze /alu/operand1 2#01111111111111111111111111111111
force -freeze /alu/operand2 2#01111111111111111111111111111111

run 50

force -freeze /alu/operand1 2#11111111111111111111111111111111
force -freeze /alu/operand2 2#00000000000000000000000000000001
run 50

#test the two types of MUL...so set the operation
force -freeze /alu/operation 16#E

#now test signed MUL

force -freeze /alu/signed 1
force -freeze /alu/operand1 2#11111111111111111111111111111111
force -freeze /alu/operand2 2#00000000000000000000000000000000
run 50

force -freeze /alu/operand1 2#00000000000000000000000000000000
force -freeze /alu/operand2 2#11111111111111111111111111111111
run 50

force -freeze /alu/operand1 2#11111111111111111111111111111111
force -freeze /alu/operand2 2#01111111111111111111111111111111
run 50

force -freeze /alu/operand1 2#11111111111111111111111111111111
force -freeze /alu/operand2 2#00000000000000000000000000000001
run 50

#and test unsigned MUL
force -freeze /alu/signed 0

force -freeze /alu/operand1 2#01111111111111111111111111111111
force -freeze /alu/operand2 2#00000000000000000000000000000000
run 50

force -freeze /alu/operand1 2#01111111111111111111111111111111
force -freeze /alu/operand2 2#01111111111111111111111111111111
run 50

force -freeze /alu/operand1 2#01111111111111111111111111111111
force -freeze /alu/operand2 2#01111111111111111111111111111111

run 50

force -freeze /alu/operand1 2#11111111111111111111111111111111
force -freeze /alu/operand2 2#00000000000000000000000000000001
run 50

#run unknown command; default output to 0 (hopefully)
force -freeze /alu/operation 16#9

#signed UNKNOWN

force -freeze /alu/signed 1
force -freeze /alu/operand1 11111111111111111111111111111111
force -freeze /alu/operand2 00000000000000000000000000000000
run 50

#set operation to test SLT
force -freeze /alu/operation 16#B

#signed SLT

force -freeze /alu/signed 1
force -freeze /alu/operand1 2#11111111111111111111111111111111
force -freeze /alu/operand2 2#00000000000000000000000000000000
run 50

force -freeze /alu/operand1 2#00000000000000000000000000000000
force -freeze /alu/operand2 2#11111111111111111111111111111111
run 50

force -freeze /alu/operand1 2#00111111111111111111111111111111
force -freeze /alu/operand2 2#01111111111111111111111111111111
run 50

force -freeze /alu/operand1 2#11111111111111111111111111111111
force -freeze /alu/operand2 2#00000000000000000000000000000001
run 50

#would test unsigned SLT; with Lab 002 implementation, still uses S-SLT
force -freeze /alu/signed 0

force -freeze /alu/operand1 2#01111111111111111111111111111111
force -freeze /alu/operand2 2#00000000000000000000000000000000
run 50

force -freeze /alu/operand1 2#01111111111111111111111111111111
force -freeze /alu/operand2 2#01111111111111111111111111111111
run 50

force -freeze /alu/operand1 2#01111111111111111111111111111111
force -freeze /alu/operand2 2#01111111111111111111111111111111

run 50

force -freeze /alu/operand1 2#11111111111111111111111111111111
force -freeze /alu/operand2 2#00000000000000000000000000000001
run 50