import Data.Function (fix)

f k n = if n < k
        then n+1
        else sum([f k (i `div` k) | i <- [0..n]])

f2 k n = if n < k
        then n+1
        else f2 k n-1 + f2 k (n `div` k)


k = 2 
-- f2 implemented with open recursion
f3 mf n = if n < k
            then n+1
            else mf n-1 + mf (n `div` k)

f3_list :: [Int]
f3_list = map (f3 faster_f3) [0..]

faster_f3 :: Int -> Int
faster_f3 n = f3_list !! n




