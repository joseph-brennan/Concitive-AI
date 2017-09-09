(ns sharing.core
  (:gen-class))

(defn -main []
  (println "Hello, World!")
  (run! println (shuffle 
                  ["Hi", "Hello", "Howdy", "Greetings", 
                   "Hey", "G'day", "Good day", "How are you", 
                   "What's up", "How goes it", "How do you do", 
                   "Hi there"])))
  

