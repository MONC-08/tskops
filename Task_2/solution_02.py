name = " My Project Bucket"

# strip whitespace and replace spaces with hyphens
clean_name = name.strip().replace(" ", "-")

# convert to lowercase
safe_name = clean_name.lower()
print(safe_name)
