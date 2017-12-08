"""
Joey Brennan
"""
import random


class NeuralNet:
    # ================================================================
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

            self.weight = {self: random.random()}

            self.output = random.random()

        def print_weight(self):
            print(self.weight[self])
            print(self.decay)
            print(self.activation)
            print(self.forgetting)
            print(self.gain)
            print(self.output)

        def change(self, increment, value):
            dy = -self.decay * self.output
            total = 0

            for pair in self.weight:
                n = self.weight[pair]
                
                if pair == self:
                    continue
                new_weight = -self.forgetting * self.output

                potential = (self.output * n * increment - self.activation)

                print(potential)

                if potential > 0:

                    total += (n * potential)

                    new_weight += self.gain * self.output * potential

                    self.weight[self] = new_weight

            dy += value * total

            self.output = dy / (1 + abs(dy))


    # ================================================================

    def __init__(self, decay, act, forget, gain):
        i = 0
        self.brain = []
        self.neu = self.Neurodes

        while i < 10:
            self.brain.append(self.neu(decay, act, forget, gain))

            i += 1

    def printer(self):
        for p in self.brain:
            print(self.neu.print_weight(p))


if __name__ == '__main__':
    print("bullshit?")
    work = NeuralNet(.5, .4, .3, .2)
    work.printer()
