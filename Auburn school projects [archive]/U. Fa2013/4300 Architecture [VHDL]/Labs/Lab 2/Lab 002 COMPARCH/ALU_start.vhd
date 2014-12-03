package dlx_types is
  subtype dlx_word is bit_vector(31 downto 0); 
  subtype half_word is bit_vector(15 downto 0);
  subtype byte is bit_vector(7 downto 0); 

  subtype alu_operation_code is bit_vector(3 downto 0); 
  subtype error_code is bit_vector(3 downto 0); 
  subtype register_index is bit_vector(4 downto 0); 
end package dlx_types; 


use work.dlx_types.all;


entity alu is
  
    generic(prop_delay: Time := 5 ns);

    port(operand1, operand2: in dlx_word; operation: in alu_operation_code;

          signed: in bit;

          result: out dlx_word; error: out error_code);


    --port(operand1, operand2: in bit_vector(31 downto 0); operation: in bit_vector(3 downto 0);

          --signed: in bit;

          --result: out bit_vector(31 downto 0); error: out bit_vector(3 downto 0));

end entity alu; --end of the declaration of the ALU entity



architecture alu_hdw_behavior of alu is --beginning of the full definition of the architecture for the ALU
  
  
--associated functions and procedures

--ADD_SIGNED
-- if the input "signed" bit says the number is signed aka SIGNED = 1
-- from "bva-b.vhd"
  procedure bv_add ( bv1, bv2 : in bit_vector;
      	       	     bv_result : out bit_vector;
		     overflow : out boolean ) is

    alias op1 : bit_vector(bv1'length - 1 downto 0) is bv1;
    alias op2 : bit_vector(bv2'length - 1 downto 0) is bv2;  
    variable result : bit_vector(bv_result'length - 1 downto 0);
    variable carry_in : bit;
    variable carry_out : bit := '0';

  begin
    if bv1'length /= bv2'length or bv1'length /= bv_result'length then
      report "bv_add: operands of different lengths"
      severity failure;
    else
      for index in result'reverse_range loop
        carry_in := carry_out;  -- of previous bit
        result(index) := op1(index) xor op2(index) xor carry_in;
        carry_out := (op1(index) and op2(index))
        	      	   or (carry_in and (op1(index) xor op2(index)));
      end loop;
      bv_result := result;
      overflow := carry_out /= carry_in;
    end if;
  end procedure bv_add;

-- ADD_UNSIGNED
-- if the "signed" input says the number is unsigned aka SIGNED = 0
-- from "bva-b.vhd"
  procedure bv_addu ( bv1, bv2 : in bit_vector;
      	       	      bv_result : out bit_vector;
		      overflow : out boolean ) is

    alias op1 : bit_vector(bv1'length - 1 downto 0) is bv1;
    alias op2 : bit_vector(bv2'length - 1 downto 0) is bv2;  
    variable result : bit_vector(bv_result'length - 1 downto 0);
    variable carry : bit := '0';

  begin
    if bv1'length /= bv2'length or bv1'length /= bv_result'length then
      report "bv_addu: operands of different lengths"
      severity failure;
    else
      for index in result'reverse_range loop
        result(index) := op1(index) xor op2(index) xor carry;
        carry := (op1(index) and op2(index))
                 or (carry and (op1(index) xor op2(index)));
      end loop;
      bv_result := result;
      overflow := carry = '1';
    end if;
  end procedure bv_addu;
  
  -- SUB_SIGNED
  -- if the "signed" input says the number is signed aka SIGNED = 1
  --from "bva-b.vhd"
  procedure bv_sub ( bv1, bv2 : in bit_vector;
      	       	     bv_result : out bit_vector;
		     overflow : out boolean ) is

    -- subtraction implemented by adding ((not bv2) + 1), ie -bv2

    alias op1 : bit_vector(bv1'length - 1 downto 0) is bv1;
    alias op2 : bit_vector(bv2'length - 1 downto 0) is bv2;  
    variable result : bit_vector(bv_result'length - 1 downto 0);
    variable carry_in : bit;
    variable carry_out : bit := '1';

  begin
    if bv1'length /= bv2'length or bv1'length /= bv_result'length then
      report "bv_sub: operands of different lengths"
      severity failure;
    else
      for index in result'reverse_range loop
        carry_in := carry_out;  -- of previous bit
        result(index) := op1(index) xor (not op2(index)) xor carry_in;
        carry_out := (op1(index) and (not op2(index)))
        	      	   or (carry_in and (op1(index) xor (not op2(index))));
      end loop;
      bv_result := result;
      overflow := carry_out /= carry_in;
    end if;
  end procedure bv_sub;
  
  --SUB_UNSIGNED
  --if the "signed" bit says unsigned, i.e. SIGNED = 0
  --code from "bva-b.vhd"
  procedure bv_subu ( bv1, bv2 : in bit_vector;
      	       	      bv_result : out bit_vector;
		      overflow : out boolean ) is

    alias op1 : bit_vector(bv1'length - 1 downto 0) is bv1;
    alias op2 : bit_vector(bv2'length - 1 downto 0) is bv2;  
    variable result : bit_vector(bv_result'length - 1 downto 0);
    variable borrow : bit := '0';

  begin
    if bv1'length /= bv2'length or bv1'length /= bv_result'length then
      report "bv_subu: operands of different lengths"
      severity failure;
    else
      for index in result'reverse_range loop
        result(index) := op1(index) xor op2(index) xor borrow;
        borrow := (not op1(index) and op2(index))
        	      	or (borrow and not (op1(index) xor op2(index)));
      end loop;
      bv_result := result;
      overflow := borrow = '1';
    end if;
  end procedure bv_subu;  
  
  --OR_CUSTOM
  --tweaked from unsigned subtractions
  procedure bv_or ( bv1, bv2 : in bit_vector;
      	       	      bv_result : out bit_vector) is

    alias op1 : bit_vector(bv1'length - 1 downto 0) is bv1;
    alias op2 : bit_vector(bv2'length - 1 downto 0) is bv2;  
    variable result : bit_vector(bv_result'length - 1 downto 0);

  begin
    if bv1'length /= bv2'length or bv1'length /= bv_result'length then
      report "bv_subu: operands of different lengths"
      severity failure;
    else
      for index in result'reverse_range loop
        if (op1(index) = '0') and (op2(index) = '0') then
          result(index) := '0';
        else
          result(index) := '1';
        end if;
        --result(index) := op1(index) xor op2(index) xor borrow;
        --borrow := (not op1(index) and op2(index))
        --	      	or (borrow and not (op1(index) xor op2(index)));
      end loop;
      bv_result := result;
      --overflow := borrow = '1';
    end if;
  end procedure bv_or;
  
  --AND_CUSTOM
  --tweaked from unsigned subtractions
  procedure bv_and ( bv1, bv2 : in bit_vector;
      	       	      bv_result : out bit_vector) is

    alias op1 : bit_vector(bv1'length - 1 downto 0) is bv1;
    alias op2 : bit_vector(bv2'length - 1 downto 0) is bv2;  
    variable result : bit_vector(bv_result'length - 1 downto 0);

  begin
    if bv1'length /= bv2'length or bv1'length /= bv_result'length then
      report "bv_and: operands of different lengths"
      severity failure;
    else
      for index in result'reverse_range loop
        if (op1(index) = '1') and (op2(index) = '1') then
          result(index) := '1';
        else
          result(index) := '0';
        end if;
        -- -- begin delete
        --result(index) := op1(index) xor op2(index) xor borrow;
        --borrow := (not op1(index) and op2(index))
        	--      	or (borrow and not (op1(index) xor op2(index)));
	      	-- --end delete
      end loop;
      bv_result := result;
      --overflow := borrow = '1';
    end if;
  end procedure bv_and;
  
  -- SLT_SIGNED
  --from signed subtraction
 procedure bv_slt ( bv1, bv2 : in bit_vector;
      	       	     bv_result : out bit_vector;
		     overflow : out boolean ) is

    -- subtraction implemented by adding ((not bv2) + 1), ie -bv2

    alias op1 : bit_vector(bv1'length - 1 downto 0) is bv1;
    alias op2 : bit_vector(bv2'length - 1 downto 0) is bv2;  
    variable result : bit_vector(bv_result'length - 1 downto 0);
    variable carry_in : bit;
    variable carry_out : bit := '1';
    variable islessthan : bit_vector(bv_result'length - 1 downto 0);

  begin
    if bv1'length /= bv2'length or bv1'length /= bv_result'length then
      report "bv_sub: operands of different lengths"
      severity failure;
    else
      for index in result'reverse_range loop
        carry_in := carry_out;  -- of previous bit
        result(index) := op1(index) xor (not op2(index)) xor carry_in;
        carry_out := (op1(index) and (not op2(index)))
        	      	   or (carry_in and (op1(index) xor (not op2(index))));
 	      islessthan(index) := '0';
      end loop;
      
      overflow := carry_out /= carry_in;
      
      if result(result'left) = '1' then
        islessthan(islessthan'right) := '1';
      else
        islessthan(islessthan'right) := '0';
        
      end if;
      
      bv_result := islessthan;
      
    end if;
  end procedure bv_slt;
  
  --SLT_UNSIGNED
  --from sub_unsigned
  --not used in current implementation, but made available just for fun
  procedure bv_sltu ( bv1, bv2 : in bit_vector;
      	       	      bv_result : out bit_vector;
		      overflow : out boolean ) is

    alias op1 : bit_vector(bv1'length - 1 downto 0) is bv1;
    alias op2 : bit_vector(bv2'length - 1 downto 0) is bv2;  
    variable result : bit_vector(bv_result'length - 1 downto 0);
    variable borrow : bit := '0';
    variable islessthan : bit_vector(bv_result'length - 1 downto 0);

  begin
    if bv1'length /= bv2'length or bv1'length /= bv_result'length then
      report "bv_subu: operands of different lengths"
      severity failure;
    else
      for index in result'reverse_range loop
        result(index) := op1(index) xor op2(index) xor borrow;
        borrow := (not op1(index) and op2(index))
        	      	or (borrow and not (op1(index) xor op2(index)));
	      islessthan(index) := '0';
      end loop;
      
      overflow := borrow = '1';
      
      if result(result'left) = '1' then
        islessthan(islessthan'right) := '1';
      else
        islessthan(islessthan'right) := '0';
        
      end if;
      
      bv_result := islessthan;
    end if;
  end procedure bv_sltu;
  
  
  --UNSIGNED MULTIPLICATION
  --from bva-b.vhd
  procedure bv_multu ( bv1, bv2 : in bit_vector;
      	       	       bv_result : out bit_vector;
		       overflow : out boolean ) is

    alias op1 : bit_vector(bv1'length - 1 downto 0) is bv1;
    alias op2 : bit_vector(bv2'length - 1 downto 0) is bv2;  
    constant len : natural := bv1'length;
    constant accum_len : natural := len * 2;
    variable accum : bit_vector(accum_len - 1 downto 0) := (others => '0');
    constant zero : bit_vector(accum_len - 1 downto len):= (others => '0');
    variable addu_overflow : boolean;

  begin
    if bv1'length /= bv2'length or bv1'length /= bv_result'length then
      report "bv_multu: operands of different lengths"
      severity failure;
    else
      for count in 0 to len - 1 loop
        if op2(count) = '1' then
          bv_addu( accum(count + len - 1 downto count), op1,
                   accum(count + len - 1 downto count), addu_overflow);
          accum(count + len) := bit'val(boolean'pos(addu_overflow));
        end if;
      end loop;
      bv_result := accum(len - 1 downto 0);
      overflow := accum(accum_len-1 downto len) /= zero;
    end if;
  end procedure bv_multu;
  
  --*****************************************
  --**********************************************
  function "-" ( bv1, bv2 : in bit_vector ) return bit_vector is

    -- subtraction implemented by adding ((not bv2) + 1), ie -bv2

    alias op1 : bit_vector(bv1'length - 1 downto 0) is bv1;
    alias op2 : bit_vector(bv2'length - 1 downto 0) is bv2;  
    variable result : bit_vector(bv1'length - 1 downto 0);
    variable carry_in : bit;
    variable carry_out : bit := '1';

  begin
    if bv1'length /= bv2'length then
      report """-"": operands of different lengths"
      severity failure;
    else
      for index in result'reverse_range loop
        carry_in := carry_out;  -- of previous bit
        result(index) := op1(index) xor (not op2(index)) xor carry_in;
        carry_out := (op1(index) and (not op2(index)))
        	      	   or (carry_in and (op1(index) xor (not op2(index))));
      end loop;
    end if;
    return result;
  end function "-";
  
  
  --*****************************************
  --needed to do negation/subtraction in multiplication, maybe other methods
  --*****************************************
  function "-" ( bv : in bit_vector ) return bit_vector is

    constant zero : bit_vector(bv'range) := (others => '0');

  begin
    return zero - bv;
  end function "-";
  
  
  --SIGNED MULTIPLICATION
  --from bva-b.vhd
  procedure bv_mult ( bv1, bv2 : in bit_vector;
      	       	      bv_result : out bit_vector;
		      overflow : out boolean ) is

    variable negative_result : boolean;
    variable op1 : bit_vector(bv1'range) := bv1;
    variable op2 : bit_vector(bv2'range) := bv2;
    variable multu_result : bit_vector(bv1'range);
    variable multu_overflow : boolean;
    variable abs_min_int : bit_vector(bv1'range) := (others => '0');

  begin
    if bv1'length /= bv2'length or bv1'length /= bv_result'length then
      report "bv_mult: operands of different lengths"
      severity failure;
    else
      abs_min_int(bv1'left) := '1';
      negative_result := (op1(op1'left) = '1') xor (op2(op2'left) = '1');
      if op1(op1'left) = '1' then
        op1 := - bv1;
      end if;
      if op2(op2'left) = '1' then
        op2 := - bv2;
      end if;
      bv_multu(op1, op2, multu_result, multu_overflow);
      if negative_result then
        overflow := multu_overflow or (multu_result > abs_min_int);
        bv_result := - multu_result;
      else
        overflow := multu_overflow or (multu_result(multu_result'left) = '1');
        bv_result := multu_result;
      end if;
    end if;
  end procedure bv_mult;
  
  
  
--*************************************************************  
--continuing with the architecture after procedure declarations
--*************************************************************

begin
  executable : process (operand1, operand2, operation, signed) 
  variable voverflow : boolean;
  variable vresult : bit_vector(31 downto 0);
  variable voperation : bit_vector(3 downto 0) := "0000";
  begin 
  voperation := operation;
  case voperation is
    when "0000" => --add
      if signed = '1' then --add
        bv_add(operand1, operand2, vresult, voverflow);
		  else --addu
		    bv_addu(operand1, operand2, vresult, voverflow);
		  end if;
    when "0001" => --SUB
      if signed = '1' then --sub
        bv_sub(operand1, operand2, vresult, voverflow);
      else
        bv_addu(operand1, operand2, vresult, voverflow);
      end if;
    when "0010" => --AND
      bv_and(operand1, operand2, vresult);
    when "0011" => --OR_
      bv_or(operand1, operand2, vresult);
    when "1011" => --SLT
      --if signed = '1' then --slt
        bv_slt(operand1, operand2, vresult, voverflow);
      --else --sltu; implemented but not used
      --  bv_sltu(operand1, operand2, vresult, voverflow);
      --end if;
    when "1110" => --MUL
      if signed = '1' then --mult
        bv_mult(operand1, operand2, vresult, voverflow);
      else --multu
        bv_multu(operand1, operand2, vresult, voverflow);
      end if;
    --when others
    WHEN OTHERS => 
      vresult := "00000000000000000000000000000000"; --32 bits of 0, hard-coded
    END CASE;
  
    if voverflow = true then
      error <= "0001" after prop_delay; --throw ERROR: overflow code 2#0001
    else
      error <= "0000" after prop_delay; --clear ERROR; aka set to 2#0000
    end if;
  
    result <= vresult after prop_delay; --turn out the result
    
    end process;
    
  end; 