--Albert Wallace, aew0024, 28 October 2013, COMP4300

package dlx_types is
  subtype dlx_word is bit_vector(31 downto 0); 
  subtype half_word is bit_vector(15 downto 0);
  subtype byte is bit_vector(7 downto 0); 

  subtype alu_operation_code is bit_vector(3 downto 0); 
  subtype error_code is bit_vector(3 downto 0); 
  subtype register_index is bit_vector(4 downto 0); 
end package dlx_types; 

use work.dlx_types.all;
--use work.bv_arithmetic.all;

entity add4 is

    generic(prop_delay: Time := 5 ns);
    port (input: in dlx_word; output: out dlx_word);

end entity add4;

architecture add4_pc_incrementer of add4 is
  
  function "+" ( bv1, bv2 : in bit_vector ) return bit_vector is

    alias op1 : bit_vector(bv1'length - 1 downto 0) is bv1;
    alias op2 : bit_vector(bv2'length - 1 downto 0) is bv2;  
    variable result : bit_vector(bv1'length - 1 downto 0);
    variable carry_in : bit;
    variable carry_out : bit := '0';

  begin
    if bv1'length /= bv2'length then
      report """+"": operands of different lengths"
      severity failure;
    else
      for index in result'reverse_range loop
        carry_in := carry_out;  -- of previous bit
        result(index) := op1(index) xor op2(index) xor carry_in;
        carry_out := (op1(index) and op2(index))
        	      	   or (carry_in and (op1(index) xor op2(index)));
      end loop;
    end if;
    return result;
  end function "+";
  
begin
  
  executable : process (input)
  
  variable extra_4 : dlx_word := "00000000000000000000000000000100";
  begin
    if input = "11111111111111111111111111111111" then
      output <= "00000000000000000000000000000011" after prop_delay;

    elsif input = "11111111111111111111111111111110" then
      output <= "00000000000000000000000000000010" after prop_delay;

    elsif input = "11111111111111111111111111111101" then
      output <= "00000000000000000000000000000001" after prop_delay;

    elsif input = "11111111111111111111111111111100" then
      output <= "00000000000000000000000000000000" after prop_delay;

    elsif input = "11111111111111111111111111111011" then
      output <= "11111111111111111111111111111111" after prop_delay;

    else
      output <= input + extra_4 after prop_delay;

    end if;
  end process;
end; -- end architecture