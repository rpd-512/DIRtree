import os
dir = input("Enter full directory path")
tb = 0
def tree(dir):
    global tb
    try:
        tb += 2
        if(os.path.isdir(dir)):
            #print(" "*(tb-1)+os.path.basename(dir))
            for i in os.listdir(dir):
                print("| "*int(tb/2)+"-> "+i)
                tree(os.path.join(dir,i))
                tb -= 2
        else:
            pass
    except:
        print("!Permission Denied!!")
        pass
print(dir)
tree(dir)
