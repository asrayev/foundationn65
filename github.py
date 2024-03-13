# 1-masala

soz=input("Soz kiriting:  ")
ls=[]
a=str()
index=0
while index<len(soz):
      if soz[index-1]!=soz[index]:
            a=a+soz[index]
      if soz[index-1]==soz[index] or index==len(soz)-1:
            ls.append(a)
            a=str()
            a=a+soz[index-1]
    
      index+=1
print(f"Takrorlangan sozlar ->{ls}")
print(f"Eng uzuni Natija->   {max(ls,key=len)}")


# 2-masala

# soz=input(">>>  ")
# if len(soz)%2==0:
#    print(soz[len(soz)//2:]+soz[:len(soz)//2])  
# else:
#    print(soz[len(soz)//2+1:]+soz[:len(soz)//2+1])
   
   
# 3-masala

# f=open("text.txt","w+")
# f.write(input("File ga malumot kiriring:  "))
# f.seek(0)
# satr=f.read().split()
# for i in satr:
#     st=set()
#     st.update(i)
#     if len(i)==len(st):
#         if len(i)%2==0:
#            print(i[len(i)//2:]+i[:len(i)//2])  
#         else:
#            print(i[len(i)//2+1:]+i[:len(i)//2+1])
