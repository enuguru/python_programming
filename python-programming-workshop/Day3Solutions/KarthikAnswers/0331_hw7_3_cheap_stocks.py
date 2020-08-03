
# very nice karthick. this is exactly the method
# i wanted, that is use a custom key to sort
# well done

# pick up top 3 cheap stocks

import datetime

dict_stock = {
              "SBUX":(100, datetime.date(2010, 11, 22)),
              "TSLA":(900, datetime.date(2010, 11, 22)),
              "MSFT":(800, datetime.date(2010, 11, 22)),
              "GOOG":(700, datetime.date(2010, 11, 22)),
              "APPL":(600, datetime.date(2010, 11, 22)),
              "FB":(500, datetime.date(2010, 11, 22)),
              "SNAP":(200, datetime.date(2010, 11, 22)),
              "TNDR":(100, datetime.date(2010, 11, 22)),
              "TWTR":(300, datetime.date(2010, 11, 22)),
              "EVDO":(900, datetime.date(2010, 11, 22)),
              }

print("cheapest 3 stocks are")
# Use a custom comparator to sort by the stock value (first item of the value tuple)
# Refer http://stackoverflow.com/questions/16304112/sort-a-dictionary-by-key-value-tuple
key2 = lambda item: item[1][0]
# print(sorted(dict_stock.items(), key=key2))
sorted_dict_stock = sorted(dict_stock.items(), key=key2)
for i in range(0,3):
    print(sorted_dict_stock[i][0])
