(ns pe6.core)

(defn square-sum
  "Returns the square of the sum of the integers from 1 to n."
  [n]
  (Math/pow (/ (* n (+ n 1)) 2) 2))

(defn sum-squares
  "Returns the sum of the squares of the integers from 1 to n."
  [n]
  (/ (reduce * [n (+ n 1) (+ (* 2 n) 1)]) 6))

(defn main
  [n]
  (- (square-sum n) (sum-squares n)))

(main 100)
