# Compute Posterior Probabilities

A command-line tool to compute and record posterior probabilities for a sequence of observed candies (Cherry vs. Lime) under a simple Bayesian model.

---

##  Requirements

* **Python** 3.x (or even version 2.x works fine)
* Standard library only (`sys`)

> **Note:** This script is designed for correct usage and does minimal input validation. Please ensure you provide valid arguments and observation sequences.

---

## ⚙️ Code Structure

1. **Class: `ComputePosterior`**

   * **Public Attributes:**

     * `hypo` – current hypothesis ratio (prior odds of Cherry vs. Lime)
     * `pro_cherry` – current probability of observing a Cherry
     * `pro_lime` – current probability of observing a Lime
   * **Constructor** – initializes priors and computes initial probabilities
   * **Private Methods:**

     * `_get_current_total(obs: str)` – updates `hypo` by multiplying by likelihood of the given observation
     * `_write_to_file(obs: str, out_file: TextIO)` – writes the updated probabilities for a single observation to the open file

2. **Main Function**

   * Parses the command‐line argument (observation sequence, e.g., `CCLLLLLCCCC`)
   * Opens an output file (`posteriors.txt`) for writing
   * Iterates through each character in the observation string:

     * Calls `_get_current_total(...)` to update beliefs
     * Calls `_write_to_file(...)` to record the posterior
   * Closes the output file

---

## 🚀 Usage

```bash
python3 compute_posterior.py <OBSERVATIONS>
```

* `<OBSERVATIONS>` – sequence of candies in uppercase, where:

  * `C` = Cherry
  * `L` = Lime

**Example**

```bash
$ python3 compute_posterior.py CCLLLLLLCCCC
```

This will produce a file named `posteriors.txt` in the same directory, containing one line per observation with the updated posterior probabilities.

---

## 📄 Output Format

Each line in `posteriors.txt` corresponds to one observed candy and contains:

```
<obs_index> <obs_char> P(Cherry|data) P(Lime|data)
```

* `<obs_index>` – 1‑based index of the observation
* `<obs_char>` – `C` or `L`
* `P(Cherry|data)` – posterior probability of Cherry given observations so far
* `P(Lime|data)` – posterior probability of Lime given observations so far

---

## ⚠️ Notes

* The script assumes well-formed input. If invalid characters appear, please retry with a correct sequence.
* Intended to run on CS Omega or any Unix‑like environment with Python 3.10+.
