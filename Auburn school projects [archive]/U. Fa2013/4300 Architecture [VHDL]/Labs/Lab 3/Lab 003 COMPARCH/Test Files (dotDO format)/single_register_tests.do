#32-bit single register test (32_bit_register)
#Albert Wallace (aew0024@auburn.edu), COMP4300, 29 October 2013

add wave -r /*

force -freeze /dlx_register/clock 2#0
force -freeze /dlx_register/in_val 2#00000000000000000000000000000000
run 50



force -freeze /dlx_register/in_val 2#11111111111111111111111111111111
run 50


force -freeze /dlx_register/clock 2#1
force -freeze /dlx_register/in_val 2#11111111111111111111111111111111

run 50

force -freeze /dlx_register/in_val 2#00000000000000000000000000000000
run 50

force -freeze /dlx_register/in_val 2#00000000000000011111111111111111
run 50

force -freeze /dlx_register/in_val 2#11111111111111111000000000000000
run 50

force -freeze /dlx_register/clock 2#0
force -freeze /dlx_register/in_val 2#00000000000000011111111111111111
run 50

force -freeze /dlx_register/in_val 2#11111111111111111000000000000000
run 50
