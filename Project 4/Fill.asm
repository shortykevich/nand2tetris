// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

// Set 'end' to 24575 (last valid screen address)
@24575
D=A
@end
M=D

// If key pressed, go to BLACKEN else goto WHITEN
(LOOP)
    @KBD
    D=M
    @BLACKEN
    D;JNE    
    @WHITEN
    0;JMP

// Initialize ptr to SCREEN
(WHITEN)
    @SCREEN
    D=A
    @ptr
    M=D      

// If ptr > end, exit loop
(WHITEN_LOOP)
    @ptr
    D=M      
    @end
    D=D-M    
    @WHITEN_END
    D;JGT    

    // Set pixel at ptr to white (0)
    @ptr
    A=M
    M=0      

    @ptr
    M=M+1

    // Check keyboard after each pixel
    @KBD
    D=M
    @BLACKEN
    D;JNE

    // Continue whitening
    @WHITEN_LOOP
    0;JMP    

(WHITEN_END)
    @LOOP
    0;JMP

// Blacken the screen
// Initialize ptr to SCREEN
(BLACKEN)
    @SCREEN
    D=A
    @ptr
    M=D      

// If ptr > end, exit loop
(BLACKEN_LOOP)
    @ptr
    D=M      
    @end
    D=D-M    
    @BLACKEN_END
    D;JGT    

    // Set pixel at ptr to black (-1)
    @ptr
    A=M
    M=-1     

    @ptr
    M=M+1

    // Check keyboard after each pixel
    // If key released, switch to WHITEN
    @KBD
    D=M
    @WHITEN
    D;JEQ 

    // Continue blackening
    @BLACKEN_LOOP
    0;JMP    

(BLACKEN_END)
    @LOOP
    0;JMP
