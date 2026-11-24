# ECLAT Algorithm – Frequent Itemset Mining and Association Rules

## 📌 Project Overview

This project implements the **ECLAT (Equivalence Class Clustering and bottom-up Lattice Traversal)** algorithm using Python to discover frequent itemsets and generate strong association rules from transactional data.

The project takes a dataset in **Horizontal Data Format**, converts it into **Vertical Data Format**, and uses a bitwise representation to efficiently calculate itemset supports.

The main goal is to identify frequently occurring combinations of items and discover relationships between them using association rule mining.

## 🎯 Project Objectives

1. Read transactional data from a CSV file.
2. Extract all unique items from the transactions.
3. Convert the horizontal dataset into vertical format.
4. Represent transaction occurrences using binary numbers (bit representation).
5. Generate all possible itemsets.
6. Calculate the support of each itemset.
7. Identify frequent itemsets based on minimum support.
8. Generate strong association rules based on minimum confidence.
9. Calculate the lift of each association rule to determine the relationship between items.

## ⚙️ Technologies Used

- Python
- Pandas – Data manipulation and CSV handling.
- NumPy – Extracting unique items.
- itertools – Generating combinations.
- Bitwise Operators – Efficient support calculation.

## 🧠 Algorithm Workflow

### 1. Read the Dataset

The project reads transactional data from a CSV file.

Example:

| TiD | Items |
|---|---|
| 1 | M,O,N,K,E,Y |
| 2 | D,O,N,K,E,Y |
| 3 | M,A,K,E |
| 4 | M,U,C,K,Y |
| 5 | C,O,O,K,I,E |

### 2. Extract Unique Items

The `unique1()` function extracts all unique items from the transactions.

### 3. Convert Horizontal to Vertical Format

The `htov()` function converts the dataset into vertical format using a one-hot encoding representation.

### 4. Binary Representation

The `make_b()` function converts each item's transaction occurrences into a binary number.

For example:

```text
Item M = 10110
Item K = 11111
```

Each bit represents whether an item exists in a particular transaction.

### 5. Generate All Possible Itemsets

The `make_pairs()` function uses recursion to generate all possible combinations of items.

### 6. Calculate Support

The `rem_less_m_s()` function calculates the support of each itemset.

It uses the bitwise AND (`&`) operator to find transactions containing all items in the itemset.

The `get_support()` function counts the number of set bits (1s) in the resulting binary number.

### 7. Find Frequent Itemsets

Itemsets are considered frequent when their support is greater than or equal to the minimum support threshold.

### 8. Generate Strong Association Rules

The `strong_rules()` function generates association rules from frequent itemsets.

It calculates:

- **Support:** Frequency of an itemset in all transactions.

  `Support(A → C) = Support(A ∪ C) / Total Transactions`

- **Confidence:** Probability of finding C when A occurs.

  `Confidence(A → C) = Support(A ∪ C) / Support(A)`

- **Lift:** Measures the relationship between the antecedent and consequent.

  `Lift(A → C) = Confidence(A → C) / Support(C)`

#### Lift Interpretation

| Lift Value | Relationship |
|---|---|
| Lift > 1 | Positive dependency |
| Lift < 1 | Negative dependency |
| Lift = 1 | Independent |

## 📂 Project Structure

```text
ECLAT-Project/
│
├── Horizontal_Format.xlsx - Sheet1.csv
│
├── main.py
│
├── output/
│   ├── all possible itemsets.csv
│   ├── frequent_itemsets.csv
│   └── strong_rules.csv
│
└── README.md
```

## 🚀 How to Run the Project

### 1. Install Requirements

Make sure Python is installed, then install the required libraries:

```bash
pip install pandas numpy
```

### 2. Prepare the Dataset

Place your CSV dataset in the project directory.

The dataset should contain:

- `TiD`: Transaction ID.
- `items`: Comma-separated items in each transaction.

### 3. Configure Parameters

Inside `main.py`, modify the minimum support and minimum confidence values:

```python
sup = 3
conf = 0.8
```

- `sup`: Minimum support count.
- `conf`: Minimum confidence threshold.

### 4. Run the Project

```bash
python main.py
```

## 📊 Generated Output Files

The project automatically generates three CSV files inside the `output` directory.

| File | Description |
|---|---|
| `all possible itemsets.csv` | Contains all possible itemsets and their support counts. |
| `frequent_itemsets.csv` | Contains only itemsets satisfying minimum support. |
| `strong_rules.csv` | Contains association rules satisfying minimum confidence, along with support, confidence, lift, and dependency. |

## 📌 Conclusion

This project demonstrates the implementation of the ECLAT algorithm using Python and bitwise operations.

By converting transactional data into binary representations, the project calculates itemset support using efficient bitwise AND operations.

Finally, it generates frequent itemsets and strong association rules, helping discover meaningful relationships and patterns in transactional datasets.

---

**Course Project:** Data Mining  
**Algorithm:** ECLAT  
**Programming Language:** Python
