'''
Question: There is a row of houses in which each house contains some amount of money. Write an algorithm 
that loots the maximum amount of money.

The only restriction is that you cannot loot two houses that are directly next to each other.
Example: for houses {5,3,2,7} select {5,7} =>12. {9,10,3,1} select {9,3} =>12

       |
{5,3,2,7 }
[5 5 7 12]

  9   
[ 9 9  12  	  18    		]
[	10        16			]
[	10	   21				]

9
pick 10 only if 10 > 9+3
pick 9

3 
pick 3 only if 10 + 11 > (9+3)
[9 9 21]

21 
pick 11 only if 11 > 3 + 6


Formalize:
curr = 9


Running max = 9
prev = 9

Running max = 10
prev 

[5 	  7	 ]
[5    7  ]
[  10   7]
[12	    7]
'''
