#@ function abs (n: int) → int = if n ≥ 0 then n else -n
#@ predicate require_max_abs (a:int ,b:int ,c: int ) = 
#@ predicate ensure_max_abs (a:int ,b:int ,c:int , res: int) =
#@ predicate test_max_abs (a:int ,b:int ,c:int , res : int ) = require_max_abs (a,b,c) → ensure_max_abs (a,b,c, res )
