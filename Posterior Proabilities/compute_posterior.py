import sys


class compute_posterior:
   
   # Hypothesis and probability bags for cherry and lime
    hypo = [0.1, 0.2, 0.4, 0.2, 0.1]  
    pro_cher = [1.0, 0.75, 0.5, 0.25, 0]  
    pro_lime = [0, 0.25, 0.5, 0.75, 1.0]  
    
    def __init__(self, candy, file):
        
        self.candy = candy
        self.file = file
        self.current_probs = self.hypo.copy()
        self.next_C = 0
        self.next_L = 0
        
        # Finds the initial probabilities
        for i in range(5):
            # Cherry
            if candy == 'C':
                self.current_probs[i] = (self.pro_cher[i] * self.hypo[i]) / self._get_currentTotal()
            else: #Lime
                self.current_probs[i] = (self.pro_cher[i] * self.hypo[i]) / self._get_currentTotal()
        
        self._write_toFile()

    def _get_currentTotal(self):
        total = 0.0
        for i in range(5):
            if self.candy == 'C':
                total += self.pro_cher[i] * self.hypo[i]
            else:
                total += self.pro_lime[i] * self.hypo[i]
        return total

    def _write_toFile(self):
        self.next_C = sum(p * self.pro_cher[i] for i, p in enumerate(self.current_probs))
        self.next_L = sum(p * self.pro_lime[i] for i, p in enumerate(self.current_probs))
        
        self.file.write(f"\nP(h1 | Q) = {self.current_probs[0]}")
        self.file.write(f"\nP(h2 | Q) = {self.current_probs[1]}")
        self.file.write(f"\nP(h3 | Q) = {self.current_probs[2]}")
        self.file.write(f"\nP(h4 | Q) = {self.current_probs[3]}")
        self.file.write(f"\nP(h5 | Q) = {self.current_probs[4]}")

        self.file.write(f"\n\nProbability that the next candy we pick will be C, given Q: {self.next_C}")
        self.file.write(f"\nProbability that the next candy we pick will be L, given Q: {self.next_L}\n")

if __name__ == "__main__":
    arg = sys.argv
    observation = arg[1] if len(arg) > 1 else ""
    
    # Keep the file open while performing task
    with open("result.txt", "w") as file:
        
        file.write(f"Observation sequence Q: {observation}\n")
        file.write(f"Length of Q: {len(observation)}\n\nBefore Observations:\n")
        file.write("\n".join(f"P(h{i+1}) = { compute_posterior.hypo[i] }" for i in range(5)))

        file.write(f"\n\nProbability that the next candy we pick will be C, given Q: {sum(compute_posterior.hypo[i] * compute_posterior.pro_cher[i] for i in range(5))}")
        file.write(f"\nProbability that the next candy we pick will be L, given Q: {sum(compute_posterior.hypo[i] * compute_posterior.pro_lime[i] for i in range(5))}\n\n")
        
        for candy in observation:
            compute_posterior(candy, file)