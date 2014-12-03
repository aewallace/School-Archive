-- lab4_control_v3.vhd

use work.bv_arithmetic.all;
use work.dlx_types.all;

-- This entity chops up a 32-bit word into the relevant component parts.
-- If a particular output is not used for a particular instruction type
-- that field is set to zero. The input from the decoder is the instruction
-- register. It operates in a purely combinational-logic mode. The controller
-- makes use of its outputs when appropriate, ignores them otherwise.
-- For R-type ALU instruction format in Figure 2.27, 
-- reg0p1 is labelled "rs" in Figure 2.27, regOp2 is labelled "rt", and
-- regDest is labelled "rd".
-- For I-type ALU instruction format in Figure 2.27
-- regOp1 is "rs" and regDest is "rt"

entity mips_decoder is
  
  port (
    instruction : in dlx_word;
    regOp1,regOp2,regDest: out register_index;
    alu_func: out func_code; 
    immediate: out half_word;
    opcode: out opcode_type   
  ); 
end mips_decoder;


use work.bv_arithmetic.all;
use work.dlx_types.all;

-- This entity controls the DLX processor. It is driven by the external
-- clock signal, and takes inputs from the decoder also. It drives the
-- input of every latch on the chip, and the control input to every
-- mux, as well as sending function codes
-- to the ALU and processing ALU error codes

entity mips_controller is
 
  port (
    opcode: in  opcode_type;
    alu_func: in func_code;
    clock: in bit; 
    aluA_mux: out bit;
    aluB_mux: out bit;
    alu_oper: out alu_operation_code;
    alu_signed: out bit; 
    write_mux: out bit;
    ir_clock: out bit;
    IM_clock: out bit; 
    pc_clock: out bit;
    npc_clock: out bit;
    imm_clock: out bit;
    alu_out_clock: out bit; 
    lmd_clock: out bit; 
    regA_clock,regB_clock: out bit;
    DM_clock: out bit;
    DM_readnotwrite: out bit;
    reg_clock: out bit;
    reg_readnotwrite: out bit;
    regA_index_mux: out bit; 
    zero_out: in bit;
    cond_out: out bit 
    );
    
end mips_controller;

architecture behaviour of mips_controller is

begin  -- behaviour

  behav: process(opcode,clock) is
     -- cuurent state of the machine 
     type state_type is range 1 to 5;                                
     variable state: state_type := 1;
                               
  begin                                
     if clock'event and clock = '1' then
       case state is 
         when 1 =>
            state := 2;      
         when 2 =>
            state := 3; 
         when 3 =>
            state := 4; 
         when 4 =>
            state := 5; 
         when 5 =>
            state := 1; 
         when others => null;
       end case;
     else
       if clock'event and clock = '0' then 

       end if;
       
     end if;
  end process behav;                                 

end behaviour;






