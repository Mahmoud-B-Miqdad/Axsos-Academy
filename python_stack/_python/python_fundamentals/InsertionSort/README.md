<div align="center">

# 📊 Python Algorithms: Insertion Sort
**Implementing the Classic Insertion Sort Algorithm**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Algorithms](https://img.shields.io/badge/Focus-Sorting_Algorithms-blueviolet?style=for-the-badge)

</div>

---

## 📝 Description
This assignment demonstrates the implementation of the **Insertion Sort** algorithm in Python. Insertion sort works similarly to the way you sort playing cards in your hands: it iterates through the list, taking one element at a time and "inserting" it into its correct position relative to the previously sorted elements.



---

## 🎯 Key Logic
1. **Iterate:** Starting from the second element, treat each element as the "key" to be inserted.
2. **Compare:** Compare the key with elements in the sorted sub-list (to its left).
3. **Shift:** Shift elements greater than the key to the right to create a space for the key.
4. **Insert:** Place the key into its correct sorted position.

---

## 🛠️ Key Concepts
* **Sorting Algorithms:** Understanding basic algorithmic efficiency.
* **In-Place Sorting:** The algorithm modifies the original list directly without requiring extra space for a second list.
* **Nested Loops:** Using a `while` loop inside a `for` loop to control the comparison and shifting process.
* **Time Complexity:** Recognizing that while simple, this algorithm has a complexity of $O(n^2)$, making it suitable for small datasets.

---

## 🚀 How to Run
1. Ensure [Python](https://www.python.org/) is installed on your machine.
2. Navigate to the directory containing this script.
3. Run the following command in your terminal:

```bash
python insertion_sort.py