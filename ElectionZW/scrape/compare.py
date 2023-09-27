import difflib

def compare_text_files(file1_path, file2_path):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()
    
    diff = difflib.unified_diff(file1_lines, file2_lines, fromfile=file1_path, tofile=file2_path)
    diff_text = '\n'.join(diff)
    
    return diff_text

# Provide the paths to the text files to compare
file1_path = "candidate_votes.json"
file2_path = "candidate_votesv2.json"

# Compare the text files
differences = compare_text_files(file1_path, file2_path)

# Specify the output file path
output_file_path = "differences.txt"

# Write the differences to the output file
with open(output_file_path, "w") as output_file:
    output_file.write(differences)

print("Differences exported to", output_file_path)