import pandas as pd
import matplotlib.pyplot as plt
cities={"name": ["London", "Berlin","Madrid","Rome",
                 "Paris","Vienna", "Bucharest","Hamburg"
                 ,"Budapest","Warsaw","Barcelona"],
        "population":[8615246,3562166,3165235,2874038,2273305,
                      1802381,1803425,1760433,1754000,1740119,1740119],
        "area":[1572,891.85,605.77,1285,105.4,
                414.6,228,755,525.2,517,101.9]
        }
city_frame=pd.DataFrame(cities,
                        columns=["population","area"],
                        index=cities["name"])
print(city_frame)
city_frame["area"]*=1000
city_frame=city_frame.plot(kind="bar")

plt.show()
