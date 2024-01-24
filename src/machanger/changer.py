import subprocess as sp


def ifconfig():
    return sp.call("ifconfig", shell=True)

def ifconfig_change(device:str, new_mac_address:str):
    sp.call(["ifconfig", device, 'down'])
    sp.call(["ifconfig", device, 'hw ether', new_mac_address])
    sp.call(["ifconfig", device, 'up'])


def change_mac(interface: str, new_mac: str):
    """
    Changes the MAC address of a given network interface.

    Args:
        interface (str): The name of the network interface (e.g., 'eth0').
        new_mac (str): The new MAC address to set (e.g., '00:11:22:33:44:55').

    Returns:
        bool: True if the MAC address was successfully changed, False otherwise.
    """
    try:
        # implement changing mac address logic
        pass
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    else:
        return True
