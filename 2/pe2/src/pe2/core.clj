(ns pe2.core)


(defn fib 
  ([] (fib 0 1))
  ([a b] (lazy-seq (cons a (fib b (+ b a))))))

(defn -main [n] 
  "Solution to Project Euler 2."
  (reduce + (filter even? (take-while #(<= % n) (fib)))))
