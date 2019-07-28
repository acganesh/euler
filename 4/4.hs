head $ reverse $ sort [c | c <- [x*y | x <- [ 11*a | a <- [10..90]], y <- [a | a <- [100..999]]], (show c) == (reverse $ show c)]
