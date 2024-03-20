import ansible_runner
import yaml
import subprocess

def load_inventory(file_path):
    with open(file_path, 'r') as inventory_file:
        inventory_data = yaml.safe_load(inventory_file)
    return inventory_data

def main():
    inventory_file_path = 'hosts.yml'
    inventory = load_inventory(inventory_file_path)

    # Execute the hello.yml playbook
    r = ansible_runner.run(private_data_dir='.', playbook='hello.yml')

    # Send curl requests to each host
    for _ in range(2):
        for i in range(3):
            cmd = "curl http://0.0.0.0"
            try:
                result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)
                response = result.stdout.strip()
                print(f"Response from {i}: {response}\n")
            except subprocess.CalledProcessError as e:
                print(f"Error executing command for {host}: {e.stderr.strip()}")

if __name__ == "__main__":
    main()
