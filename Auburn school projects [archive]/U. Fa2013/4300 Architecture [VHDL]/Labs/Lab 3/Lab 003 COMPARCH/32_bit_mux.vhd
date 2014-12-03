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
use work.bv_arithmetic.all;

entity mux is
  
    generic(prop_delay: Time := 5 ns);
    
    port (input_1,input_0 : in dlx_word; which: in bit; output: out dlx_word);

end entity mux;

architecture mux_behavior of mux is
begin
  executable : process (input_1, input_0, which)
  begin
  
  if which = '0' then
    output <= input_0 after prop_delay;
  end if;
  
  if which = '1' then 
    output <= input_1 after prop_delay;
  end if;

  end process;
end; --end of the architecture
