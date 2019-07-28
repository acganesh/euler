fibs a b = a : fibs b (a + b)

evenMask n
     | mod n 2 == 0 = n
     | otherwise = 0

main = print $ sum $ map evenMask $ takeWhile (< 4000000) $ fibs 0 1
