import sys
for line in sys.stdin:
    parts = line.strip().split(",")
    if parts[0] == "Formatted Date":
        continue  # Skip the header line
    try:
        date = parts[0]
        temperature = float(parts[3])
        year = date.split("-")[0]
        print(f"{year}\t{temperature}")
    except:
        continue  # Skip lines with errors
