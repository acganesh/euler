import Data.List

main = putStrLn . show $ xs !! 0
     where
        xs = reverse . sort $ filter isPalindrome prods
        isPalindrome n = (reverseInt n) == n
        reverseInt n = read $ reverse $ show n
        prods = [x*y | x <- [999,998..100], y <- [999,998..100]]