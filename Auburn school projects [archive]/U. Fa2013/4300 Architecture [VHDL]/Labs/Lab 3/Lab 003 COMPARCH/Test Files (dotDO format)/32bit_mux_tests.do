#32-bit mux test
#Albert Wallace (aew0024@auburn.edu), COMP4300, 29 October 2013

add wave -r /*

force -freeze /mux/input_0 2#11111100000000001111110000000000
force -freeze /mux/input_1 2#00000000001111110000000000111111
force -freeze /mux/which 2#0

run 75

force -freeze /mux/input_0 2#11111100000000001111110000000000
force -freeze /mux/input_1 2#00000000001111110000000000111111
force -freeze /mux/which 2#1

run 75

force -freeze /mux/input_0 2#00000000000111111111110000000000
force -freeze /mux/input_1 2#11111111111111110000111111111111
force -freeze /mux/which 2#0

run 75

force -freeze /mux/input_0 2#00000000000111111111110000000000
force -freeze /mux/input_1 2#11111111111111110000111111111111
force -freeze /mux/which 2#1

run 75