TITLE Triangular Sequence Calculator						(hw05_q4.asm)

; Description: Takes an integer and sums all integers 
; using the formula n + (n-1) + (n-2) + ... + 2 + 1
; Revision date: 2012/09/20

INCLUDE Irvine32.inc
.data
myMessage BYTE "Please input positive integer",0dh,0ah,0
n DWORD 0


.code
main PROC
	call Clrscr  

	mov	 edx,offset myMessage
	call WriteString			; Write prompt to the screen

	call ReadInt				; Allows user to input integer
	mov n, eax					; writes input integer to variable n
	mov ecx, n					; writes variable n to ecx for loop decrement
	dec ecx						; decrements ecx by 1, for initial n-1 addition

L0:								; begin the loop here
	add n, ecx					; add the decremented number to the current position
	loop L0						; jumps back to L0 and ends once zero is reached

	mov eax, n				; copies the calculated value to edx for display
	call writeInt			; displays the calculated data
	

	exit
main ENDP

END main