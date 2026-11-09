"""
This problem requires you to calculate compounding interest and final value of a  US treasury deposit based upon
current interest rates (that will be provided). Your analysis should return the final value of the investment
after a 10-year and 20-year period. The final values should be stored in the variables "ten_year_final"
and "twenty_year_final", respectively. Perform all your calculations in this file. Do not perform the calculations by hand
and simply write in the final result.

Prompt: On October 27th, 2022, Elon Musk purchased Twitter for $44B in total, with reportedly $33B of his own money. Since
that time, it appears this investment has not worked out. If Elon has instead bought $33B of US Treasury Bonds, how much
would his investment be worth in 10-year and 20-year bonds? Assume the 10-year bonds pay 3.96%,
the 20-year bonds pay 4.32%, with each compounding annually.
Note that Elon's capital will be $33B.
"""

### all your code below ###

#Elon's starting capital
capital=33000000000

#interest rates
ten_year_rate=0.0396
twenty_year_rate=0.0432

#value after 10 years
ten_year_final=capital*(1+ten_year_rate)**10

#value after 20 years
twenty_year_final=capital*(1+twenty_year_rate)**20

#print
print(f"10 year final:${ten_year_final:,.0f}")
print(f"20 year final:${twenty_year_final:,.0f}")

# final answer for 10-year
ten_year_final = None

# final answer for 20-year
twenty_year_final = None
