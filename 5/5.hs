myGCD :: Integral a => a -> a -> a
myGCD x 0 = x
myGCD x y = myGCD y (x `mod` y)

myLCM :: Integral a => a -> a -> a
myLCM x y = (x * y) `div` (myGCD x y)

main = putStrLn . show $ n
     where
        n = foldl myLCM 1 [1..20]
