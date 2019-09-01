-- N choose K: http://mattwetmore.me/posts/n-choose-k-the-haskell-way.html
instance Num a => Num [a] where
  fromInteger n = [fromInteger n]
  (x:xs) + (y:ys) = (x + y) : (xs + ys)
  xs + [] = xs
  [] + ys = ys
  (x:xs) * (y:ys) = (x*y) : ([x] * ys + xs * (y:ys))
  _ * _ = []

choose :: Int -> Int -> Int
choose n k = ([1,1]^n) !! k

main = do
  print $ 7.0 * (1.0 - (fromIntegral $ choose 60 20) / (fromIntegral $ choose 70 20))
