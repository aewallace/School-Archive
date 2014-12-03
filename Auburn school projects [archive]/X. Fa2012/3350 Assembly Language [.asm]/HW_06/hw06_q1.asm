TITLE Triangular Sequence Calculator						(hw05_q4.asm)

; Description: Takes an integer and sums all integers 
; using the formula n + (n-1) + (n-2) + ... + 2 + 1
; Revision date: 2012/10/11

INCLUDE Irvine32.inc
.data
sValA WORD 0
sValB WORD 0
compareTest WORD 0
countTo DWORD 20


.code
main PROC
	call Clrscr  

	mov ecx, countTo			;controls loop decrement; will essentially count to the number defined in countTo
	call fibo					;starts processing of fibonacci sequence

	
	exit
main ENDP

	
fibo PROC

	movzx eax, sValB			;store starting value
	movzx ebx, sValA			;store second starting value
	test ax, compareTest		;test to see if starting value bx = 0 (if so, assume bx = 0 and jump)
	jz plusOne					;jump to display zero then increment bx to help loop iterate properly
	jmp Looper					;if zf not set, carry on with looper as normal

Looper:
	mov dx, ax				;store A
	add ax, bx				;add B to A
	call WriteInt			;display sum
	mov bx, dx				;positions second number for future loop use
	loop Looper				;loop until first 20 numbers are displayed
	jmp endFibo				;exit loop for certain

plusOne:			;called in case initial values of fibo sequence are set to 0 and 0
	call WriteInt	;displays first value of zero
	dec ecx			;1 value displayed; 19 more to go in the loop
	add ax, 1		;manually increments one, since loop would fail to produce results otherwise
	call WriteInt	;displays first 1
	dec ecx			;2 values displaued; 18 more to go in the loop
	jmp Looper		;goes to the loop to finish the remaining 20 (or however many defined) numbers of fibo. sequence

endFibo:			;necessary end of procedure
	ret

fibo ENDP


END main