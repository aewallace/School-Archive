TITLE Scanning array		(main.asm)
; Description: Scans an array for a negative value.
; Author: Matthew J Swann
; Version 1.0, 2012-08-02
				
INCLUDE Irvine32.inc
.data
	myArray SWORD 3,6,1,10,-10,-30,-40,-4
	sentinel SWORD 0

.code

main PROC	
	mov ebx, type myArray			;size of each element in the array, for pointer increments
	mov esi, offset myArray			;point to an element of the array
	mov ax, sword ptr [esi]			;copy value to be tested
	cmp ax, 0						;will trigger if negative (less than zero)
	jl soNegative					;jump to appropriate command if negative
	mov ecx, lengthOf myArray		;move the number of iterations
	dec ecx							;...less one number to be compared

toLoop:
	add esi, ebx					;point to the next element of the array
	mov ax, sword ptr [esi]			;copy said next element for comparison
	cmp ax, 0						;will trigger if negative (less than zero)
	jl soNegative					;jump to the appropriate command if negative
	loop toLoop						;resume looping as possible
	jmp toEnd						;if no negative can be found...end
	
soNegative:
	call dumpRegs					;this will happen only if a negative number is found
	jmp toEnd						;jump to the end (just clarification)

toEnd:

exit								;exit program
main ENDP
END main