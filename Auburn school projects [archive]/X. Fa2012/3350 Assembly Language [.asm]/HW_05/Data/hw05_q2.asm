TITLE Homework 5, Question 1			(hw05_q2.asm)

; Description: Memory reference exercise.
; Author: Matthew J Swann
; Version: 1.0, 2012-08-02

INCLUDE Irvine32.inc
.data
alpha 	DWORD		1h, 2h  
beta 	DWORD		3h, 4h
gamma   DWORD 		5

.code		
main PROC	
	mov eax, 0Ah;			Immediate
	mov ecx, eax;			register to register	
	mov edi, OFFSET beta;	Immediate	
	mov [gamma], eax; 		Indirect	
	mov esi, [gamma];		Direct	
	mov esi, 4;  			Immediate	
	mov eax, beta[esi];		Indirect-offset	
	mov ebx, OFFSET alpha;	Immediate	
	mov eax, [ebx];  		Indirect	
	mov eax, 4[ebx]; 		Indirect-displacement	
	mov eax, 4[ebx][esi];  	Base-Indirect-displacement	
	mov eax, 8[ebx][esi];  	Base-Indirect-displacement	
	mov eax, 12[ebx][esi];  Base-Indirect-displacement

			
	exit
main ENDP

END main