<div align="center">

# 📊 Python Algorithms: Selection Sort
**Implementing the Selection Sort Algorithm**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Algorithms](https://img.shields.io/badge/Focus-Sorting_Algorithms-blueviolet?style=for-the-badge)

</div>

---

## 📝 Description
This assignment covers the implementation of the **Selection Sort** algorithm. This algorithm sorts an array by repeatedly finding the minimum element from the unsorted part of the array and putting it at the beginning.



---

## 🎯 Key Logic
1. **Find Minimum:** Iterate through the unsorted portion of the array to find the smallest element.
2. **Swap:** Swap the found minimum element with the first element of the unsorted portion.
3. **Repeat:** Move the boundary of the unsorted portion one step to the right and repeat until the entire array is sorted.

---

## 🛠️ Key Concepts
* **Efficiency:** Like Insertion Sort, Selection Sort has a time complexity of $O(n^2)$, making it easy to understand but less efficient for very large datasets.
* **In-Place Sorting:** It sorts the array without needing significant extra memory.
* **Min Index Tracking:** Using an index variable (`min_idx`) to keep track of the smallest element found during each pass.
* **Pythonic Swapping:** Utilizing Python’s tuple unpacking `a, b = b, a` for elegant variable swapping.

---

## 🚀 How to Run
1. Ensure [Python](https://www.python.org/) is installed on your machine.
2. Navigate to the directory containing this script.
3. Run the following command in your terminal:

```bash
python selection_sort.py