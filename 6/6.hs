sumSquares n = sum $ map (\x -> x*x) $ [1..n]
squareSum n = (\x -> x*x) $ sum [1..n]

main = putStrLn . show $ (squareSum n) - (sumSquares n)
    where
        n = 100
