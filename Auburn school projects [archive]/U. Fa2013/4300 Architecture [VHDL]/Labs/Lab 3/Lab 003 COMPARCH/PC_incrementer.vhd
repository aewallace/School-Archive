--Albert Wallace, aew0024, 28 October 2013, COMP4300

use work.dlx_types.all;
use work.bv_arithmetic.all;

entity add4 is

    generic(prop_delay: Time := 5 ns);
    port (input: in dlx_word; output: out dlx_word);

end entity add4;

architecture add4_pc_incrementer of add4 is
  
begin
  
  executable : process (input)
  
  variable extra_4 : dlx_word := "00000000000000000000000000000100";
  begin
    if input = "11111111111111111111111111111111" then
      output <= "00000000000000000000000000000011";

    elsif input = "11111111111111111111111111111110" then
      output <= "00000000000000000000000000000010";

    elsif input = "11111111111111111111111111111101" then
      output <= "00000000000000000000000000000001";

    elsif input = "11111111111111111111111111111100" then
      output <= "00000000000000000000000000000000";

    elsif input = "11111111111111111111111111111011" then
      output <= "11111111111111111111111111111111";

    else
      output <= input + extra_4;

    end if;
  end process;
end; -- end architecture