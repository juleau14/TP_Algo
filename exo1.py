
#@ predicate require_sum (n:int) = (n >= 0)
#@ predicate ensure_sum (n:int , res : int ) = n <= res
#@ predicate test_sum (n:int , res : int ) = require_sum (n) -> ensure_sum (n, res )

#@ assert test_sum (0 , 0)
#@ assert test_sum (1 , 1)
#@ assert test_sum (2 , 3)
#@ assert test_sum (3 , 6)
