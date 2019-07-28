(ns pe4.core)
(require '[clojure.string :as s])

(defn is-palindrome [s]
  (= (s/reverse (str s)) (str s)))

(is-palindrome "racecar")
(is-palindrome (str 2))

(defn main [] 
  (let [mults (range 990 99 -11)
       three-digits (range 999 99 -1)] 
  (apply max 
         (filter is-palindrome 
                 (for [a mults b three-digits] (* a b))))) 
  )

(main)
