main = putStrLn (show val)
val = sum $ filter even $ takeWhile (<= 4000000) [fib x | x <- [1..]]

fib 1 = 1
fib 2 = 2
fib x = fib (x - 1) + fib (x - 2)