# CIS-117 lab3
# Name: Azmaaen Atiq
# Submitting Individually
# This program reads a CSV file containing country data, 
# separates the countries by their respective regions, 
# and creates a new CSV file for each region containing the countries in that region.


import csv
countries = {}
# Read the CSV file and separate countries by region
try:
    with open('country_full.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            region = row['region']
            name = row["name"]

            if region:
                if region not in countries:
                    countries[region] = []

                countries[region].append(name)

except FileNotFoundError as e:
    print("Error: File not found.", e)

except Exception as e:
    print("Error: Could not read the file.", e)
else: 
# Make a new CSV file for each region and write the countries to it
    for region in countries:
        try:
            filename = region + ".csv"

            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)

                writer.writerow(["name", "region"])

                for name in countries[region]:
                    writer.writerow([name, region])

        except FileNotFoundError as e:
            print("Error: File not found.", e)

        except Exception as e:
            print("Error: Could not write to the file.", e)

        
