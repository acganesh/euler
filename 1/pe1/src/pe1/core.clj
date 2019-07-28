(ns pe1.core)

(defn -main [n]
  "Solution to Project Euler 1."
  (reduce + (filter #(or (= (mod % 5) 0) (= (mod % 3) 0)) (take n (range))))
  )

(-main 1000)
