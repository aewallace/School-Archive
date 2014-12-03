#PC incrementer, add-4 to 32-bit address tests (PC_incrementer)
#Albert Wallace (aew0024@auburn.edu), COMP4300, 29 October 2013

add wave -r /*
force -freeze /add4/input 2#11111111111111111111111111111100

run 50

force -freeze /add4/input 2#00000000000000000000000000000000

run 50

force -freeze /add4/input 2#11111111111111111111111111111010

run 50

force -freeze /add4/input 2#10000000000000001000000000000000

run 50

force -freeze /add4/input 2#00000000000000001111111111111111

run 50

force -freeze /add4/input 2#11111111111111111111111111111111

run 50

force -freeze /add4/input 2#11111111111111111111111111111110

run 50