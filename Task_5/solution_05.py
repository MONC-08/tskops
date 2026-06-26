virtual_machine = {
    "id": "vm-101",
    "ip": "192.168.1.10",
    "status": "running",
    "region": "eu-central-1"
}

# update status
virtual_machine["status"] = "stopped"

# add new key
virtual_machine["instance_type"] = "t3.large"

print(virtual_machine)