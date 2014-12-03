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

entity dlx_register is
  
  generic(prop_delay: Time := 5 ns);
  port(in_val: in dlx_word; clock: in bit; out_val: out dlx_word); 

end entity dlx_register; 

architecture dlx_register_behavior of dlx_register is --beginning the architecture of the register


begin --this is the code that will actually be run using the procedures declared above
  executable : process (in_val, clock)
  
  begin
    
  if clock = '1' then
    out_val <= in_val after prop_delay; --set the value of the output as the value of the input, basically "storing" it
  end if;
    
  end process;
  
end; --end of the architecture
  
  