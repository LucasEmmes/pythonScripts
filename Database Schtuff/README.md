# Stuff that makes TDT4145 tests a bit easier #  
  
tables_and_dependencies.py:
- For tasks where you are given a table  
along with functional dependencies.  
You can add your table and dependencies,  
and then easily check for (super)keys,  
candidate keys, or see whether one attribute  
can be derived from another
  
Add tables in the form of "R(A,B,C,D,E,F)",  
and dependencies in the following form  
"F={A -> B; AB -> C; C -> DE}"  
Then use parse_table and parse_dependency  
to make them available  
  
If you wanna check every attribute derived  
from "AB", you use derivate_attributes("AB")
  
  
  
I would like to note that I have not used this  
to *answer* any questions, just test the answers  
that I got by myself