add_list=[]
count=0
def todo():
    global add_list
    global count
   
    while True:
        print("=== TODO LIST ===")
        print("1. Tapşırıq əlavə et\n2. Tapşırıqları göstər\n3. Tapşırıq sil\n4. Çıxış")
        dyr=input("isdediyiniz reqemi girin")
        if dyr=="1":  
            tsk_write=input("tapsiriqin adini girin")
            add_list.append(tsk_write)
            count+=1
        elif dyr=="2":
            for i,item in enumerate(add_list,start=1):
                print(f"{i}. {item}")
        elif dyr=="3":
            dyrss=int(input("reqemi girin"))
            add_list.pop(dyrss)
        elif dyr=="4":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n✅sistemden cixis edildi Tesekkur")
            break
        else:
            print("1 ile 4 arasinda reqem secin") 
todo()
