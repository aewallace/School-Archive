onerror {resume}
quietly WaveActivateNextPane {} 0
add wave -noupdate /alu/operand1
add wave -noupdate /alu/operand2
add wave -noupdate /alu/operation
add wave -noupdate /alu/signed
add wave -noupdate /alu/result
add wave -noupdate /alu/error
TreeUpdate [SetDefaultTree]
WaveRestoreCursors {{Cursor 1} {2096 ns} 0}
quietly wave cursor active 1
configure wave -namecolwidth 139
configure wave -valuecolwidth 40
configure wave -justifyvalue left
configure wave -signalnamewidth 0
configure wave -snapdistance 10
configure wave -datasetprefix 0
configure wave -rowmargin 4
configure wave -childrowmargin 2
configure wave -gridoffset 0
configure wave -gridperiod 1
configure wave -griddelta 40
configure wave -timeline 0
configure wave -timelineunits ns
update
WaveRestoreZoom {0 ns} {2142 ns}