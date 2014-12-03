TITLE Scanning array		(hw07_q3)
; Description: Compares numbers (entered within code).
; Author: Matthew J Swann
; Version 1.0, 2012-08-02
				
INCLUDE Irvine32.inc
.data
	myValueXA WORD 0h
	myValueXB WORD 0h
	spacing BYTE ", ",0
	val1 WORD 24h

.code

main PROC

	mov ax, 100
	mov bx, 55
	mov cx, 24h
	mov dx, 67

set1:	
	cmp cx, bx						;compare the two
	jge ifSet1Designed				;jump if runs as designed
	mov myValueXA, 2				;set to 2 if condition not met
set2:
	cmp ax, dx						;compare the two
	jl	ifSet2Designed				;jump if first part of OR condition met
	cmp cx, val1					;compare the two
	je	ifSet2Designed				;jump if other part of OR condition met
	mov myValueXB, 4				;set to 4 if condition not met
	jmp endOfCode

ifSet1Designed:
	cmp bx, val1
	jne set1S2
	mov myValueXA, 2
	jmp set2

ifSet2Designed:
	mov myValueXB, 3
	jmp endOfCode

set1S2:
	mov myValueXA, 1
	jmp set2


endOfCode:							;when everything else is done
	movzx eax, myValueXA
	call writeInt					;if 1, then bx = > cx AND bx !=  val1; if 2, conditions not met
	mov edx, offset spacing			;allows printing of a space between numbers
	call writeString				;prints space
	movzx eax, myValueXB
	call writeInt					;if 3, then ax < dx OR cx == val1; if 4, conditions not met
exit								;exit program
main ENDP
END main