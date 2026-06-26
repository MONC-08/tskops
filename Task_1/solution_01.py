url = "https://api.github.com/v3"

pattern = ["https://", "http://"]

clean_url = url

for p in pattern:
    clean_url = clean_url.replace(p, "")

#get domain name    
domain = clean_url.split("/")[0]

domain_name = domain.split(".")
    
final_domain_name = ".".join(domain_name[-2:])
print(final_domain_name)