# Aapne jo pichle question mein (Question 1) 
# file download kari hai, usko read karke usme number of lines 
# count kar ke print karein. Aapne sirf uss file ki number of lines 
# Count karne ka code likhna hai.

# Hint: Har \n ke baad nayi line 
# shuru hoti hai. Aap yeh use kar ke 
# nayi line ka ko pehchan sakte ho.


f=open("question.4")
count=0
for i in (f):
    count=count+1
print(count)
# f.close()