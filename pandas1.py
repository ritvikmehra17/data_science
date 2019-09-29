import pandas as pd
import matplotlib.pyplot as plt
fruits=['apples','bananas','oranges','cherries']
quantities=[10,20,55,15]
s=pd.Series(quantities, index=fruits)
s=s.plot(kind="bar")
plt.title("This is my chart")
plt.show()
