# main.py
from file_operations import read_csv_file, write_csv_file
from imputation import impute_missing_values

def main():
    contents = read_csv_file("setosa.csv")
    header = contents[0]
    data = contents[1:]
    impute_missing_values(data, 3)
    write_csv_file(header, data, "setosa_updated.csv")

if __name__ == "__main__":
    main()

