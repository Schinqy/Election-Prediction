import json

output_file_path = "totals.json"

with open(output_file_path, "r") as file:
    totals_data = json.load(file)

constituencies = totals_data["constituencies"]

zanu_pf_total = 0
ccc_total = 0
other_total = 0

for constituency_data in constituencies:
    zanu_pf_total += constituency_data["zanu_pf_total"]
    ccc_total += constituency_data["ccc_total"]
    other_total += constituency_data["other_total"]

print("ZANU-PF total votes:", zanu_pf_total)
print("CCC total votes:", ccc_total)
print("Others total votes:", other_total)