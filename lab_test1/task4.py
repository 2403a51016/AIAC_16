import csv

def calculate_totals_and_averages(csv_filename):
    with open(csv_filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        print(f"{'Name':<10} {'Total':<6} {'Average':<7}")
        print("-" * 25)
        for row in reader:
            # Extract marks and convert to integers
            try:
                maths = int(row['Maths'])
                physics = int(row['Physics'])
                chemistry = int(row['Chemistry'])
            except (ValueError, KeyError):
                continue  # Skip rows with invalid data

            total = maths + physics + chemistry
            average = total / 3
            print(f"{row['Name of the student']:<10} {total:<6} {average:<7.2f}")

if __name__ == "__main__":
    calculate_totals_and_averages('test.csv')
