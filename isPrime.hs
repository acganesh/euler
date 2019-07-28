import Data.Functor
import Debug.Trace
import Data.List


isPrime 0 = False                                                                                                          
isPrime 1 = False                                                                                                         
isPrime 2 = True                                                                                                         
isPrime x = not $ elem 0 $ (x `mod`) <$> [2..ceiling(sqrt(fromIntegral(x)))]                                              
n_primes n = take n $ [x | x <- [1..], isPrime x]
n_prime n = head $ reverse $ n_primes n
                                                                                                                  
primes = [x | x <- [1..], isPrime x]                                                                                      

recurse sums [] = sums                                                                                                    
recurse sums primes = recurse (insert ((head $ reverse sums) + (sum $ take 2 $ primes)) sums) (drop 2 $ primes)

list n = filter isPrime $ takeWhile (<=1000000) $ recurse [n_prime n] (drop n $ take 5000 $ primes)
maxSum list = head $ reverse list

let mainFunc = 
	let ListOfLists = [list x | x <- [1, 2]]
	let PrimeListOfLists = map filter $ isPrime $ ListOfLists	
--[max $ list n | n <- [1..10]]
