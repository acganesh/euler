(ns pe7.core)

(defn prime? [n] 
  (let [limit (int (ceil (sqrt n)))]
    (empty? (filter #(= (mod n %) 0) (range 2 limit))))
  )

(defn primes [n]
  "Return a lazy sequence of primes up to the nth prime."
  )

(defn main [n]
  "Returns the nth prime."
  loop
  )
