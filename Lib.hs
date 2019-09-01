module Lib where

import Control.Monad
import Control.Monad.ST
import Data.Array.ST
import Data.Array.Unboxed
import Data.List -- for nub

-- The most time-efficient, but not memory efficient way to
-- compute primes in Haskell.
-- https://wiki.haskell.org/Prime_numbers
sieveUA :: Int -> UArray Int Bool
sieveUA top = runSTUArray $ do
    let m = (top-1) `div` 2
        r = floor . sqrt $ fromIntegral top + 1
    sieve <- newArray (1,m) True      -- :: ST s (STUArray s Int Bool)
    forM_ [1..r `div` 2] $ \i -> do
      isPrime <- readArray sieve i
      when isPrime $ do               -- ((2*i+1)^2-1)`div`2 == 2*i*(i+1)
        forM_ [2*i*(i+1), 2*i*(i+2)+1..m] $ \j -> do
          writeArray sieve j False
    return sieve
 
primesToUA :: Int -> [Int]
primesToUA top = 2 : [i*2+1 | (i,True) <- assocs $ sieveUA top]

-- 
prime :: Int -> UArray Int Bool 
prime n = runSTUArray $ do
    arr <- newArray ( 2 , n ) True :: ST s ( STUArray s Int Bool ) 
    forM_ ( takeWhile ( \x -> x*x <= n ) [ 2 .. n ] ) $ \i -> do
        ai <- readArray arr i 
        when ( ai  ) $ forM_ [ i^2 , i^2 + i .. n ] $ \j -> do
            writeArray arr j False 
 
    return arr 

-- Optimized divisors, only checking range from [2..sqrt n].
-- https://stackoverflow.com/questions/1480563/making-a-list-of-divisors-in-haskell
divisors' n = (1:) $ nub $ concat [ [x, div n x] | x <- [2..limit], rem n x == 0 ]
     where limit = (floor.sqrt.fromIntegral) n

-- (eq. to) find2km (2^k * n) = (k,n)
find2km :: Integral a => a -> (a,a)
find2km n = f 0 n
    where 
        f k m
            | r == 1 = (k,m)
            | otherwise = f (k+1) q
            where (q,r) = quotRem m 2        

-- n is the number to test; a is the (presumably randomly chosen) witness
millerRabinPrimality :: Integer -> Integer -> Bool
millerRabinPrimality n a
    | a <= 1 || a >= n-1 = 
        error $ "millerRabinPrimality: a out of range (" 
              ++ show a ++ " for "++ show n ++ ")" 
    | n < 2 = False
    | even n = False
    | b0 == 1 || b0 == n' = True
    | otherwise = iter (tail b)
    where
        n' = n-1
        (k,m) = find2km n'
        b0 = powMod n a m
        b = take (fromIntegral k) $ iterate (squareMod n) b0
        iter [] = False
        iter (x:xs)
            | x == 1 = False
            | x == n' = True
            | otherwise = iter xs

-- (eq. to) pow' (*) (^2) n k = n^k
pow' :: (Num a, Integral b) => (a->a->a) -> (a->a) -> a -> b -> a
pow' _ _ _ 0 = 1
pow' mul sq x' n' = f x' n' 1
    where 
        f x n y
            | n == 1 = x `mul` y
            | r == 0 = f x2 q y
            | otherwise = f x2 q (x `mul` y)
            where
                (q,r) = quotRem n 2
                x2 = sq x
 
mulMod :: Integral a => a -> a -> a -> a
mulMod a b c = (b * c) `mod` a
squareMod :: Integral a => a -> a -> a
squareMod a b = (b * b) `rem` a

-- (eq. to) powMod m n k = n^k `mod` m
powMod :: Integral a => a -> a -> a -> a
powMod m = pow' (mulMod m) (squareMod m)
