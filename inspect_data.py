import csv

def inspect_column(filename, column):
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    values = []
    for row in rows:
        raw = row[column].strip()
        if raw  == "":
            continue
        values.append(float(raw))

    return{
        "smallest":min(values),
        "largest":max(values),
        "count":len(values)
    }

area_result = inspect_column("Ward_Boundaries.csv", "area_km2")
print("Area:", area_result)
uniq_id_result = inspect_column("Ward_Boundaries.csv", "uniq_id")
print("Unique IDs:", uniq_id_result)
