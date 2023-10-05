# Read the text file
with open('scholat_spl.txt', 'r') as file:
    content = file.read()

# Split the content into lines
lines = content.split('\n')

# Initialize variables
mean_values = []
current_mean = None

# Iterate over lines and extract Mean values for the specific function
for line in lines:
    if line.startswith("Function: nx.shortest_path(g, source = node)"):
        current_mean = None
    elif line.startswith("Mean:"):
        current_mean = float(line.split(":")[1].strip())
    elif line.startswith("samples:"):
        if current_mean is not None:
            mean_values.append(current_mean)

# Calculate the overall mean of mean values
overall_mean = sum(mean_values) / len(mean_values)

print(f"Mean values: {mean_values}")
print(f"Overall Mean: {overall_mean:.6f}")
