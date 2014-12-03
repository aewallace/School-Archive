#32-bit 32-entry register file tests (register_file)
#Albert Wallace (aew0024@auburn.edu), COMP4300, 29 October 2013

add wave -r /*

#read_notwrite
#clock
#regA
#regB
#data_in

force -freeze /regfile/clock 2#1
force -freeze /regfile/read_notwrite 2#0

force -freeze /regfile/regA 2#00000
force -freeze /regfile/data_in 2#00000000000000000000000000000000
run 25

force -freeze /regfile/regA 2#11111
force -freeze /regfile/data_in 2#11111111111111111111111111111111
run 25


force -freeze /regfile/read_notwrite 2#1
force -freeze /regfile/regA 2#11111
force -freeze /regfile/regB 2#00000
run 50

force -freeze /regfile/clock 2#0
force -freeze /regfile/read_notwrite 2#0

force -freeze /regfile/regA 2#00000
force -freeze /regfile/data_in 2#11111111111111111111111111111111
run 25

force -freeze /regfile/regA 2#11111
force -freeze /regfile/data_in 2#00000000000000000000000000000000
run 25


force -freeze /regfile/read_notwrite 2#1
force -freeze /regfile/regA 2#11111
force -freeze /regfile/regB 2#00000
run 50

force -freeze /regfile/clock 2#1
force -freeze /regfile/read_notwrite 2#0

force -freeze /regfile/regA 2#00000
force -freeze /regfile/data_in 2#11111111111111111111111111111111
run 25

force -freeze /regfile/regA 2#11111
force -freeze /regfile/data_in 2#00000000000000000000000000000000
run 25


force -freeze /regfile/read_notwrite 2#1
force -freeze /regfile/regA 2#11111
force -freeze /regfile/regB 2#00000
run 50


force -freeze /regfile/regA 2#00000
force -freeze /regfile/regB 2#11111
run 50

force -freeze /regfile/read_notwrite 2#0
force -freeze /regfile/regA 2#11000
force -freeze /regfile/regB 2#11001
#attempt to save to location dictated by regB should be ignored, but will try
force -freeze /regfile/data_in 2#11011011011000000000000000000000
run 25

#output from B should be anything but the above
force -freeze /regfile/read_notwrite 2#1
run 50

force -freeze /regfile/read_notwrite 2#0
force -freeze /regfile/regA 2#11001
force -freeze /regfile/data_in 2#11011011011000000000000000000000
run 25

#if we read output now, setting A to location 11000 and B to location 11001, should get same on both outputs
force -freeze /regfile/regA 2#11000
force -freeze /regfile/regB 2#11001
force -freeze /regfile/read_notwrite 2#1
run 50

#now we should be able to return to the previously set registers, indexes 0 and 31 (natural: 1 and 32)
#output should be 0x0000 and 0xFFFF
force -freeze /regfile/regA 2#00000
force -freeze /regfile/regB 2#11111
run 50