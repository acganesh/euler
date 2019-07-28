(ns pe3.core
  (:require [clojure.math.numeric-tower :refer [sqrt ceil]]))



(defn greatest-prime-of [number]
  (reduce max (filter #(zero? (mod number %))
                      (take-while #(< % (sqrt number)) primes))))

(defn main [n]
  (let [limit (int (ceil (sqrt n)))] 
    (apply max (filter #(and (= (mod n %) 0) (prime? %)) 
                 (range 2 limit))))
 )
