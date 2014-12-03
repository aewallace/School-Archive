TITLE Array Assignment and Evaluation					(hw06_q2.asm)

; Description: Assigns user input to an array and finds the min value.
; Authors: Matthew J Swann, Albert Wallace
; Version 1.1, 2012-10-11

INCLUDE Irvine32.inc
.data
prompt BYTE "Please input a value:", 0
result BYTE "The minimum value of value inputs is:",0
theArray SDWORD 5 DUP(?) 

.code
main PROC
	
	call Clrscr

	mov		edx, offset prompt		;prepare the prompt to be displayed
	mov		ecx, lengthOf theArray	;number of integers to be read into array
	mov		esi, offset theArray	;prepares the array for writing
	mov		ebx, type theArray		;stores amount by which pointer will be advanced

usIntr:								;user interface loop
	call	WriteString				;display the prompt
	call	readInt					;receive the string
	mov		sdword ptr [esi], eax	;push the newly read integer into the array
	add		esi, ebx				;move the focus of the array for the next iteration
	call	crlf					;help interface readability by going to a new line
	loop	usIntr					;continues looping until five values read in


	mov esi, offset theArray		;go to beginning of array for analysis
	mov eax, sdword ptr [esi]		;moves the first value for comparison

	mov ecx, lengthOf theArray		;setting up for iteration through array for comparisons;
	dec ecx							;...n-1 comparisons will need to be made

findMin:							;loop to find the minimum value
	add esi, ebx					;increments pointer to next array member
	mov	edx, sdword ptr [esi]		;moves second value for comparison; compare eax to edx
					;//try to make eax always store the lesser value
	cmp eax, edx					;compares the two values; if zf =1, both equal; if zf = 0, both different (cf = 1 if ax < dx; cf = 0 if ax > dx)
	jg	greaterThan					;jump if eax > edx or eax = edx
	loop findMin
	jmp minFound					;when done, jump past all other instructions



greaterThan:	;//run if eax > edu
	mov eax, edx					;places the lesser of the two values into eax
	loop findMin					;return to loop and do proper loop procedures; if impossible/unnecessary...
	jmp minfound					;this assumes the min has been found, given no more numbers to process

minFound:
	call crlf
	mov edx, offset result			;prepare the result message to be displayed
	call WriteString				;edx points to the string
	call writeInt					;eax points to the final value
	

	exit
main ENDP

END main