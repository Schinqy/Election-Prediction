import json

file_path = "candidate_votesv2.json"
output_file_path = "totals.json"

with open(file_path, "r") as file:
    constituencies_data = json.load(file)

constituencies = []

for constituency, candidates in constituencies_data.items():
    zanu_pf_total = 0
    ccc_total = 0
    other_total = 0
    
    for candidate in candidates:
        party = candidate["Party"]
        votes = int(candidate["Votes"])
        
        party = party.replace("-", "").replace(" ", "").lower()  # Remove hyphens and spaces, convert to lowercase
        
        if party == "zanupf":
            zanu_pf_total += votes
        elif party == "ccc":
            ccc_total += votes
        else:
            other_total += votes
    
    constituency_data = {
        "name": constituency,
        "zanu_pf_total": zanu_pf_total,
        "ccc_total": ccc_total,
        "other_total": other_total
    }
    
    constituencies.append(constituency_data)

result = {
    "constituencies": constituencies
}

with open(output_file_path, "w") as output_file:
    json.dump(result, output_file, indent=4)

print("Results exported to", output_file_path)