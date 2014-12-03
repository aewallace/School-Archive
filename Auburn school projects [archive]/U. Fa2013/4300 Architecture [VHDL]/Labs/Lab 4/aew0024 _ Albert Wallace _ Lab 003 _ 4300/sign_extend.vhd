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

entity sign_extend is

    generic(prop_delay: Time := 5 ns);
    port (input: in half_word; signed: in bit; output: out dlx_word);

end entity sign_extend;

architecture sign_extend_behavior of sign_extend is

begin
  executable : process (input)
  
  variable result : dlx_word := "00000000000000000000000000000000";
  variable source : half_word := "0000000000000000";
    
    
  begin
    source := input;
    if signed = '0' then --and you do not copy the MSB/sign bit; just pad with 0
      for indexa in 0 to 15 loop
        result(indexa) := source(indexa);
      end loop;
      for indexr in 16 to 31 loop
        result(indexr) := '0';
      end loop;
      output <= result after prop_delay;
    else --signed = 1 and you absolutely must copy the sign bit/MSB
      for indexa in 0 to 15 loop
        result(indexa) := source(indexa);
      end loop;
      for indexr in 16 to 31 loop
        result(indexr) := source(15);
      end loop;
      output <= result after prop_delay;
    end if;
  end process;

end; --end architecture