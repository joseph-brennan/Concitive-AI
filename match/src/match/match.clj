(ns match.match
  (:gen-class))

(defn -main []
  (defn header "returns the frame header" [frame] (first frame))
  
  (defn body "returns the frame body" [frame] (rest frame))
  
  (defn is-var?
   "Determines if parameter is a variable"
   [x]
   (and (symbol? x)
        (re-matches #"^\?.*" (name x))))
  
  (defn name-var
    "Returns the name of a variable"
    [x]
    {:pre [(is-var? x)]}
    (symbol (subs (name x) 1)))
  
  (defn match
    "Determines whether the pattern matches the constant given the binding form;
    returns updated binding form"
    [pattern constant bindings])
  
  (defn map-to-alist
    [x]
    (map #(list (symbol(name (key %))) (val %)) (seq x))))
