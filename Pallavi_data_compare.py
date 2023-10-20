import csv

def compare_datasets(file1, file2):
    differences = []

    with open(file1, 'r') as file1_csv, open(file2, 'r') as file2_csv:
        reader1 = csv.DictReader(file1_csv)
        reader2 = csv.DictReader(file2_csv)

        # Assuming the CSV files have a common key field named 'id'
        key_field = 'id'

        dataset1 = {row[key_field]: row for row in reader1}
        dataset2 = {row[key_field]: row for row in reader2}

        # Compare the datasets based on the key field
        for key in dataset1:
            if key not in dataset2:
                differences.append(f"Record with {key_field} '{key}' is present in Dataset 1 but not in Dataset 2")
            else:
                # Compare other fields if needed
                # Example: if dataset1[key]['name'] != dataset2[key]['name']:
                #            differences.append(f"Name mismatch for {key}: {dataset1[key]['name']} vs {dataset2[key]['name']}")
                pass

        for key in dataset2:
            if key not in dataset1:
                differences.append(f"Record with {key_field} '{key}' is present in Dataset 2 but not in Dataset 1")

    return differences

# Example usage
if __name__ == "__main__":
    file1 = 'dataset1.csv'
    file2 = 'dataset2.csv'
    result = compare_datasets(file1, file2)

    if result:
        for diff in result:
            print(diff)
    else:
        print("Datasets are identical.")
