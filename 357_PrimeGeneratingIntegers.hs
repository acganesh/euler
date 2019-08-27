import Lib
import Data.Array.Unboxed

limit :: Int
limit = 10 ^ 8

-- Boolean prime list
pList :: UArray Int Bool
pList = prime $ limit

isPrime :: Int -> Bool
isPrime x = pList ! x

-- Let f(d) = d + n/d.  Note that f(d) = f(n/d),
 {-allowing us to simplify the search.-}

isPrimeGenerating :: Int -> Bool
isPrimeGenerating n = and [n `mod` x /= 0 || (isPrime $ x + n `div` x) | x <- [2..truncate $ sqrt $ fromIntegral n]]

-- Process each entry from 2..limit.
process x
  | isPrime x && isPrimeGenerating (x-1) = x-1
  | otherwise = 0

-- Sum the numbers that satisfy the desired condition.
main = do
  print $ sum $ map process [2..limit]
