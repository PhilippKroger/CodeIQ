def three_squares(a, b):
    a1 = min(a, b)  # a = 80
    b1 = max(a, b)  # b = 120
    if a <= 1000 and b <= 1000:
        s = a * b
        if b1 - a1 == (a1 // 2):
            k1 = (b1 - a1) * (b1 - a1)
            k2 = (b1 - a1) * (b1 - a1)
            s = s - k1 - k2
            return s, k1, k2


print(three_squares(120, 80))


"""

## **Task 1.1. Three squares**

### **[maths; problems for beginners]**

The farmer owns a piece of land in the shape of a rectangle with side lengths a*a* and b*b*.
Recently, a farmer realized that he could divide his plot into three parts so that each
part would be in the shape of a square, and decided to take advantage of this opportunity.
Write a program that will find the area of ​​each piece after splitting.

https://ucarecdn.com/fdae6562-8a90-414a-ac0e-79696bcc1eed/    <----- !

### **Input data format**

The input is two natural numbers a*a* and b*b* — the lengths of the sides of the rectangle.
Numbers do not exceed 1000. Each number is given on a separate line. It is guaranteed that the
lengths of the sides are such that the rectangle can be divided into three squares.

### **Output data format**

It is required to print three natural numbers separated by a space — the areas of each of the sections
after the partition. Numbers can be displayed in any order.

### **Verification Method**

The program is tested on 15 tests. Passing each test is worth 1 point.
The test from the task condition is not used for verification.

### **Sample Input 1:**

12080

### **Sample Output 1:**

6400 1600 1600

### **Explanation for example**

With the given dimensions, the rectangle can be divided into three squares as shown in the figure below.
Please note that there may be other partitioning options.
"""