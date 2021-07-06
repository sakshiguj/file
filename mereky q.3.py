banks_list = ["Kotak\n", "HDFC\n", "RBL\n", "SBI\n", "Bank of Baroda"] 
f=open("question.3.txt","a")
for i in banks_list:
    f.write(i)
f.close()