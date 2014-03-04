import cPickle as p
import matplotlib.pyplot as plt

f = file("./count")
a, b = p.load(f)
plt.plot(b)
plt.show()
# print len(a)

