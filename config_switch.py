from netmiko import ConnectHandler

# Switch connection details
switch = {
    "device_type": "cisco_ios",
    "host": "10.10.1.18",
    "username": "admin1",
    "password": "admin1",
    "secret": "enable123",  # If the device requires an enable password
}

def configure_switch():
    try:
        # Connect to the switch
        net_connect = ConnectHandler(**switch)
        net_connect.enable()  # Enter enable mode if required

        # List of commands to configure the switch
        config_commands = [
            "interface GigabitEthernet 1/4",
            "description Configured by Netmiko",
            "switchport mode trunk",
            "no shutdown",
        ]

        # Send configuration commands
        output = net_connect.send_config_set(config_commands)
        print("Configuration Output:")
        print(output)

        # Save configuration
        save_output = net_connect.save_config('copy running-config startup-config')
        print("Save Output:")
        print(save_output)

        # Disconnect
        net_connect.disconnect()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    configure_switch()

