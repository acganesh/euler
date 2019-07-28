divis k n
    | mod n k == 0 = n
    | otherwise = 0

f n = x + y - z
    where
        x = sum $ map (divis 3) [1..n-1]
        y = sum $ map (divis 5) [1..n-1]
        z = sum $ map (divis 15) [1..n-1]