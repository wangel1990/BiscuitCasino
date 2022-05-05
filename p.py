import csv
csv_columns = ['UID','Name','Balance']
CasinoData = [
{'UID': 1, 'Name': 'Wangel' ,   "Balance":1  },
{'UID': 2, 'Name': 'Carlos' ,   "Balance":1  },
{'UID': 3, 'Name': 'Alex'   ,   "Balance":1  },
{'UID': 4, 'Name': 'CH'     ,   "Balance":1  },
{'UID': 5, 'Name': 'Wotor'  ,   "Balance":2  },
]
csv_file = "Names.csv"
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in CasinoData:
            writer.writerow(data)
except IOError:
    print("db cannot overwrite")
    
def getList(ordered_dict_from_csv):
        return dict.keys()
try:
    a_csv_file = open("Names.csv", "r")
    dict_reader = csv.DictReader(a_csv_file)   

    ordered_dict_from_csv = list(dict_reader)
    n = len(ordered_dict_from_csv)
    getList()
    if 1 in ordered_dict_from_csv:
        print("1 esta ocupado")
        dict_from_csv = dict(ordered_dict_from_csv)
        print(dict_from_csv)

   
    


except IOError:
    print("db cannot be read")