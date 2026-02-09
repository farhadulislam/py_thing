import csv

# Open the first CSV file
with open('file1.csv', 'r') as file1:
    # Create a CSV reader for the first file
    reader1 = csv.reader(file1)

    # Open the second CSV file
    with open('file2.csv', 'r') as file2:
        # Create a CSV reader for the second file
        reader2 = csv.reader(file2)

        # Open the output CSV file
        with open('output.csv', 'w', newline='') as output:
            # Create a CSV writer for the output file
            writer = csv.writer(output)

            # Write the header row from the first file
            writer.writerow(next(reader1))

            # Iterate over the rows in the first file
            for row in reader1:
                # Write the row to the output file
                writer.writerow(row)

            # Write the header row from the second file
            writer.writerow(next(reader2))

            # Iterate over the rows in the second file
            for row in reader2:
                # Write the row to the output file
                writer.writerow(row)
