import os

path = "/Users/symbat/Documents/pp2-22B030325/draft"


cnt = 0


print("Only files:")
y = []
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):
        
        y.append(name)
        cnt+=1
print(y)
print(cnt)
