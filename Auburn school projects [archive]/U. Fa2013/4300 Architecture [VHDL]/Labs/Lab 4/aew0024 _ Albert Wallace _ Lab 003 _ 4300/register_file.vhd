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



entity regfile is
    generic(prop_delay: Time := 5 ns);
    
    port (read_notwrite,clock : in bit; 
           regA,regB: in register_index; --note typo rebB has been altered to regB! 
         data_in: in dlx_word; 
         dataA_out,dataB_out: out dlx_word); --end of port declaration
         
    type register_array is array (31 downto 0) of dlx_word;     
    

end entity regfile; 

          --read is dual-ported -- do when read_notwrite = 1
          --write is single-ported -- do when read_notwrite = 0
architecture regfile_behavior of regfile is 
          --note again: typo rebB has been altered to regB!  
          
function bv_to_natural ( bv : in bit_vector ) return natural is

    variable result : natural := 0;

  begin
    for index in bv'range loop
      result := result * 2 + bit'pos( bv(index) );
    end loop;
    return result;
  end function bv_to_natural;
  
begin --begin architecture
  
  executable : process (read_notwrite, clock, regA, regB, data_in)
    variable regA_asnatural, regB_asnatural : integer;
    variable defined_register_array : register_array; 
  begin
    if clock = '1' then
      
      if read_notwrite = '1' then --do reading, dual-port
        regA_asnatural := bv_to_natural(regA);
        regB_asnatural := bv_to_natural(regB);
        dataA_out <= defined_register_array(regA_asnatural) after prop_delay;
        dataB_out <= defined_register_array(regB_asnatural) after prop_delay;
      elsif read_notwrite = '0' then --do writing, single-port
        regA_asnatural := bv_to_natural(regA);
        defined_register_array(regA_asnatural) := data_in;
      end if;
        
    end if;
  end process;
  
end;  --end architecture