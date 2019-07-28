import Data.Functor
import Data.List

isPrime :: Integer -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime 2 = True
isPrime x = not $ elem 0 $ (x `mod`) <$> [2..ceiling(sqrt(fromIntegral(x)))]
n_primes n = take n $ [x | x <- [1..], isPrime x]
n_prime n = head $ reverse $ n_primes n

primes = [x | x <- [1..], isPrime x]

primeList = map (\i -> drop i $ take 10000 primes) [1..1000]

maxIndex xs = head $ filter ((== maximum xs) . (xs !!)) [0..]

chainSum sums [] = sums
chainSum sums primes
	| (head $ reverse sums) > 1000000 = sums
	| otherwise = chainSum (insert ((head $ reverse sums) + (sum $ take 1 $ primes)) sums) (drop 1 $ primes)

getMax primes = maximum $ filter isPrime $ filter (< 1000000) $ chainSum [0] primes
results = map (\ps -> [elemIndex (getMax ps) $ chainSum [0] ps, (Just $ fromIntegral $ getMax ps)]) primeList

main = do
	putStrLn $ show $ head $ reverse $ results !! (maxIndex $ map (!! 0) results)