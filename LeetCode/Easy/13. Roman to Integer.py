w = {'I': 1,
     'V': 5,
     'X': 10,
     'L': 50,
     'C': 100,
     'D': 500,
     'M': 1000,
     }

s = "MCMXCIV"
ns = []
for i in range(len(s)-1):
    print(s[i], s[i+1])
    if str(s[i]+s[i+1])=='CM':
        ns.append(900)
    elif s[i]+s[i-1]=='MC':
        continue
    else:
        wd = s[i]
        print(wd, w[wd])
        ns.append(w[wd])

print(s)
print(sum(ns))