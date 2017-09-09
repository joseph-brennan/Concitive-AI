(ns sharing.sharing
  (:gen-class))

(defn -main []
  (run! println (shuffle 
                  ["Hi", "Hello", "Howdy", "Greetings", 
                   "Hey", "G'day", "Good day", "How are you", 
                   "What's up", "How goes it", "How do you do", 
                   "Hi there"])))
  

