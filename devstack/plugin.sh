# DevStack Plugin File for a Netmiko-based Switch Configuration

NETMIKO_PLUGIN_DIR=$DEST/netmiko_plugin

function install_netmiko_plugin {
    echo "Installing Netmiko and dependencies"
    pip_install -r $NETMIKO_PLUGIN_DIR/requirements.txt
}

function configure_netmiko_plugin {
    echo "Configuring switch using Netmiko"
    python3 $NETMIKO_PLUGIN_DIR/config_switch.py
}

# Main plugin logic
if [[ "$1" == "stack" && "$2" == "install" ]]; then
    install_netmiko_plugin
elif [[ "$1" == "stack" && "$2" == "post-config" ]]; then
    configure_netmiko_plugin
fi

