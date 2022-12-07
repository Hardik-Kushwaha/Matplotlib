import matplotlib.pyplot as plt
x = [10,20,30,40,50,60]
y = [13,45,23,34,96,76]
plt.title('GFG Tutorial')
plt.bar(x, y, color='dodgerblue',width=5)
plt.savefig('/home/hardik/myImg.svg')