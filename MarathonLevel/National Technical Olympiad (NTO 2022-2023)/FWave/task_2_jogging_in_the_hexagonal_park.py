
def jogging(x):
    l = ['AHG', 'ABIG', 'ABCJG',
         'GJCBHG', 'AHICJLF', 'FLKEFAHG',
         'ABCDELIBA', 'ABCDEFGIBA', 'ABCDEFGJCBA', 'ABCDEFGKDCBA']
    res = ''
    if x <= 1200:
        x = x // 100
        for i in range(len(l)):
            if x == len(l[i]):
                print(l[i])
    else:
        if x % 100 != 0:
            z = x % 100
            y = 100 - z
            x += y
        x = x // 100
        xa = x % 10
        xb = x - xa
        xxb = x // 10 % 10
        res += str(xxb * l[7])
        for i in range(len(l)):
            if xa == len(l[i]):
                res += l[i]
        return res


print(jogging(1234))


"""
## **Task 1.2. Run in the hexagonal park**
### **[constructive construction; problems for beginners]**

Ivan Ivanovich is jogging in the park, which has the shape of a hexagon. There are 12 alleys in the park, marked with
the symbols of the Latin alphabet from "A" to "L". See the map for the park.
The length of each alley is exactly 100 meters. The park has only one entrance at the intersection of alleys
"A", "F", "G". Ivan Ivanovich wants to start and finish the run at the entrance to the park and run exactly k*k* meters.
At every intersection, Ivan Ivanovich can turn in any direction, but he does not want to turn back.

Write a program that will create any route that meets the specified requirements.

https://ucarecdn.com/ed063b58-1c2d-4d49-9070-b342a4fe6636/   <------- !

### **Input data format**

One natural number k is given as input — the desired length of the route, 300≤*k*≤10000.
The number *k* is divisible by 100 without a remainder.

### **Output data format**

It is required to output a string of k/100 characters containing alley designations in the constructed route.

### **Verification Method**

The program is tested on 21 tests. Passing each test is worth 1 point.
The test from the task condition is not used for verification.

### **Sample Input 1:**
800

### **Sample Output 1:**
FLKEFAHG
"""
