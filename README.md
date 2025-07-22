# 🔢 Huffman Coding for Text Compression

This project applies **Huffman Coding**, a fundamental algorithm in lossless data compression, to analyze and compress the short story *"To Build A Fire"* by **Jack London**. It was developed as part of the **Information and Coding Theory (ENEE5304)** course.

---

## 📘 Project Description

Huffman coding is used to assign shorter binary codes to more frequent characters and longer codes to less frequent ones, minimizing the overall number of bits used to represent the data.

In this project, we:
- Read a `.docx` literary file
- Calculated character frequencies and probabilities
- Built a Huffman Tree
- Generated prefix-free Huffman codes
- Calculated entropy and average code length
- Compared compression performance with ASCII encoding

---

## 🧠 Features

- 📄 Supports `.docx` file input (via `docx2txt`)
- 🔢 Computes:
  - Frequency
  - Probability
  - Huffman Code
  - Code Length
  - Entropy
  - Average bits/character
  - Compression percentage vs. ASCII
- 📊 Saves detailed CSV files:
  - `huffman_result.csv` – character-level results
  - `summary_result.csv` – compression and entropy metrics
- 📈 Command-line outputs for total stats


