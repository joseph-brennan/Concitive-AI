"""
Joey Brennan
"""
import random

class NeuralNet:

    class Neurodes:
        weight = {}
        decay = 0
        activation = 0
        forgetting = 0
        gain = 0
        output = 0

        def __init__(self, decay, act, forget, gain):
            self.decay = decay
            self.activation = act
            self.forgetting = forget
            self.gain = gain

            self.weight = {self}
            self.output = random.random()

        def making_weight(self, neuron):
            for n in neuron:
                self.weight[n].append(random.random())

    def __init__(self, decay, act, forget, gain):
        i = 0
        self.brain = []
        while i < 10:
            neu = self.Neurodes
            self.brain.append(neu(decay, act, forget, gain))

    def printer(self):
        print("tester")
        for p in self.brain:
            print(p)


if __name__ == '__main__':
    print("bullshit")
    work = NeuralNet(.5, .4, .3, .2)
    work.printer()
