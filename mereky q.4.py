sakshi=open("question.4","r")
for i in sakshi:
    if "delhi" in i:
        sakshi=open("delhi.txt","a")
        sakshi.write(i)
    elif "shimla" in i:
        sakshi=open("shimla.txt","a")
        sakshi.write(i)
    else :
        sakshi=open("others.txt","a")
        sakshi.write(i)
sakshi.close()

