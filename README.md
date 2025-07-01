# 🧮 Matrix Calculator

This is a Python-based Matrix Calculator that allows users to perform a wide range of matrix operations through a command-line interface and Jupyter notebook demo.

---

## 📂 Project Structure

```
Matrix-Calculator/
├── Class_MtxCalc.py              # Contains the MatrixCalculator class with core logic
├── Program_MtxCalc.py            # CLI program that interacts with the user
├── Matrix_Calculator_Demo.ipynb  # Jupyter notebook demonstrating usage of each method
├── requirements.txt              # Dependencies for pip users
└── environment.yaml              # Conda environment file
```

---

## ⚙️ Features

- Matrix Addition & Multiplication
- Determinant calculation
- Inverse of a matrix
- Eigenvalues and Eigenvectors
- Diagonalization
- Powers of a matrix
- Matrix function operations:  
  `sin`, `cos`, `exp`, `log`, `sinh`, `cosh`

---

## 💻 How to Run

### 🔹 Option 1: Using pip

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the calculator
python Program_MtxCalc.py
```

---

### 🔹 Option 2: Using conda

```bash
# Create environment
conda env create -f environment.yaml

# Activate it
conda activate matrix-calculator

# Run the calculator
python Program_MtxCalc.py
```

---

## 📓 Jupyter Notebook Demo

Open `Matrix_Calculator_Demo.ipynb` in Jupyter to see how each method in the `MatrixCalculator` class works individually.

```bash
jupyter notebook Matrix_Calculator_Demo.ipynb
```

---

## 🧠 Technologies Used

- [NumPy](https://numpy.org/) — for matrix and numerical operations  
- [SymPy](https://www.sympy.org/) — for symbolic mathematics  
- [SciPy](https://www.scipy.org/) — for matrix function evaluations

---

## 📌 Notes

- Only square matrices are supported for operations like determinant, inverse, diagonalization, etc.
- The CLI guides you through entering matrices interactively and supports undoing rows (`u`) or stopping input (`x`).

---

## 🙌 Acknowledgements

Thanks for using the Matrix Calculator!  
Pull requests and suggestions are welcome. 🎉
