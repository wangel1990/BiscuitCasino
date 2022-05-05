import csv
a_csv_file = open("sample.csv", "r")
dict_reader = csv.DictReader(a_csv_file)

ordered_dict_from_csv = list(dict_reader)[0]
dict_from_csv = dict(ordered_dict_from_csv)

print(dict_from_csv)