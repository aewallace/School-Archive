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
  generic(prop_delay: Time := 5 ns); 
  port (
    instruction : in dlx_word;
    regOp1,regOp2,regDest: out register_index;
    alu_func: out func_code; 
    immediate: out half_word;
    opcode: out opcode_type   
  ); 
end mips_decoder;

architecture mips_decoder_behavior of mips_decoder is
begin

  decoder_executable : process (instruction)
    variable opcode_chunk : opcode_type := "111111";
  begin
    opcode_chunk := instruction(31 downto 26);
    opcode <= opcode_chunk after prop_delay;
    case opcode_chunk is
      when "000000" => --this is the catchall for many ALU operations
        alu_func <= instruction(5 downto 0) after prop_delay;
        regOp1 <= instruction(25 downto 21) after prop_delay;
        regOp2 <= instruction(20 downto 16) after prop_delay;
        regDest <= instruction(16 downto 12) after prop_delay;
        immediate <= "0000000000000000" after prop_delay;
        
        
      when "001000" => --when 0x8 do addi
        alu_func <= instruction(5 downto 0) after prop_delay;
        immediate <= instruction(15 downto 0) after prop_delay;
        
      when "001001" => --when 0x9 do addui
        alu_func <= instruction(5 downto 0) after prop_delay;
        immediate <= instruction(15 downto 0) after prop_delay;
        
      when "001010" => --when 10 or 0xa do subi
        alu_func <= instruction(5 downto 0) after prop_delay;
        immediate <= instruction(15 downto 0) after prop_delay;
        
      when "001100" => --when 12 or 0xc do andi
        alu_func <= instruction(5 downto 0) after prop_delay;
        immediate <= instruction(15 downto 0) after prop_delay;
        
      when "100011" => --LW 0x23 or 35
        alu_func <= instruction(5 downto 0) after prop_delay;
        regOp1 <= instruction(25 downto 21) after prop_delay;
        regDest <= instruction(20 downto 16) after prop_delay;
        immediate <= instruction(15 downto 0) after prop_delay;
        
      when "101011" => --SW 0x2b or 43
        alu_func <= instruction(5 downto 0) after prop_delay;
        regOp1 <= instruction(25 downto 21) after prop_delay;
        regDest <= instruction(20 downto 16) after prop_delay;
        immediate <= instruction(15 downto 0) after prop_delay;
        
      when others => null;
    end case;
      
  end process; 
end; --end of mips_decoder architecture


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
         when 1 => --IF stage
         --set the right clocks, do the right logic, then go to state 2
            PC_clock = '1';
            add4_clock = '1';
            NPC_clock = '1';
            instruction_memory = '1';
            instruction_reg = '1';
            
            --Send the program counter (PC) to instruction memory and fetch the
            -- current instruction from instruction memory, storing it in the 
            -- instruction register. Update the NPC to the 
            -- next sequential PC by adding 4 (since each instruction
            -- is 4 bytes) to the current PC value.
            
            
            --IF/ID.IR <- Mem[PC]
            
            --IF/ID.NPC,PC <- ...
            -- --if (EX/MEM.opcode == branch) & EX/MEM.cond == 1
            -- --then <- EX/MEM.ALUOutput 
            -- --else <- {PC+4}
            
            state := 2;
                  
         when 2 => --ID stage
         --set the right clocks, do the right logic, then go to state 3
            clock_registerfile = '1'
            clock_signextend = '1'
            clock_immediate = '1'
            clock_register_a = '1'
            clock_register_b = '1'
            --Decode the instruction from the instruction register
            -- and read the registers corresponding to register source specifiers from the register
            -- file. Do the equality test on the registers as they are read, for a possible branch. Sign-extend the
            -- offset field of the instruction in case it is needed. Store this result in Imm.
            -- Optional: Compute the possible branch target address by adding
            -- the sign-extended offset to the incremented PC. (The branch can be completed at the end of this stage
            -- by storing the branch-target address into the PC, if the condition test yielded true).
            
            --ID/EX.regA <- RegFile[IF/ID.IR[rs]]
            --ID/EX.regB <- RegFile[IF/ID.IR[rs]]
            --ID/EX.NPC <- IF/ID.NPC
            --ID/EX.IR <- IF/ID.IR
            --ID/EX.Imm <- sign-extend(IF/ID.IR[immediate field]
            
            state := 3; 
         when 3 => --EX stage
         --set the right clocks, do the right logic, then go to state 4
            muxa = '1'
            muxb = '1'
            zero = '1'
            alu = '1'
            aluout = '1'
            cond = '1'
            --Memory reference: the ALU adds the base register and the offset to form the effective address.
            
            --ALU Register - Register: the ALU performs the operation specified by the ALU opcode on the
            -- values read from the register file.
            
            --ALU Register-Immediate: The ALU performs the operation specified by the ALU opcode on the
            -- first value read from the register file and the sign-extended immediate
            
            --**if ALU instruction
            
            
            --**if LOAD/STORE
            -- --EX/MEM.ALUOutput <- ID/EX.A + ID/EX.Imm
            -- --EX/MEM.B <- ID/EX.B
            
            --**if BRANCH instruction
            -- --EX/MEM.ALUOutput <- ID/EX.NPC + (ID/EX.Imm << 2)
            -- --EX/MEM.cond <- (ID/EX.A == 0)
            state := 4; 
         when 4 => -- MEM cycle
         --set the right clocks, do the right logic, then go to state 5
         
         --Mem access: If the instruction is a load, the memory does a read using the effective address computed in
         -- the previous cycle. If it is a store, then the memory writes the data from the second register
         -- read from the register file using the effective address.
            case opcode is
              when "100011" => --LW 0x23 or 35
                DM_clock <= '1';
                lmd_clock <= '1';
                DM_readnotwrite <= '1'
              when "101011" => --SW 0x2b or 43
                DM_clock <= '1';
                lmd_clock <= '1';
                DM_readnotwrite <= '0'
              when others => null;
            end case;
         
            state := 5; 
         when 5 => --WB cycle
         --set the right clocks, do the right logic, then start all over
         
         --Write-back cycle: Register-Register ALU instruction or load instruction: Write the result into the register
         -- file, whether it comes from the memory system (for a load) or from the ALU (For an ALU instruction).
            case opcode is
              when "100011" => --LW 0x23 or 35; tell Write Mux to use LMD/DM output
                write_mux <= '1';
              when "000000" => --ALU Register-register operation; tell Write Mux to use ALU result
                write_mux <= '0'
              when others => null;
            end case;
         
         
         --write_mux <= ??? 1 if load/lmd_out is to be used; 0 if ALU instruction is being used for register file
         --cond_out <= ??? [if zero_out = 1, cond = 1; if zero_out = 0, cond = 0
         
            state := 1; 
         when others => null;
       end case;
     else
       if clock'event and clock = '0' then 
		state := state;
       end if;
       
     end if;
  end process behav;                                 

end behaviour;






