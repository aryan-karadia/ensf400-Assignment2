import ansible_runner
import yaml

def load_inventory(file_path):
    with open(file_path, 'r') as inventory_file:
        inventory_data = yaml.safe_load(inventory_file)
    return inventory_data

def main():
    inventory_file_path = 'hosts.yml'
    inventory = load_inventory(inventory_file_path)

    # Print host information
    for group_name, group_data in inventory.items():
        if group_name == "ungrouped":
            continue
        print(f"Group: {group_name}")
        for host_name, host_info in group_data.get('hosts', {}).items():
            ansible_host = host_info.get('ansible_host', 'Unknown')
            ansible_user = host_info.get('ansible_user', 'Unknown')
            print(f"  Host: {host_name} ({ansible_host}), User: {ansible_user}")

    print("\n\npinging hosts...")
    # Execute ansible ping command
    r = ansible_runner.run(private_data_dir='.', module='ping', host_pattern='all:localhost')

    # Print ping results
    for result in r.events:
        if result['event'] == 'runner_on_ok':
            host = result['event_data']['host']
            status = result['event_data']['res']['ping']
            print(f"{host} is {'Online' if status else 'Offline'}")

if __name__ == "__main__":
    main()
