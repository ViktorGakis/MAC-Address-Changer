import subprocess as sp


def ifconfig() -> int:
    return sp.call("ifconfig", shell=True)


def ifconfig_change(interface: str, new_mac: str) -> None:
    sp.call(["ifconfig", interface, "down"])
    sp.call(["ifconfig", interface, "hw ether", new_mac])
    sp.call(["ifconfig", interface, "up"])


def change_mac(interface: str, new_mac: str) -> bool:
    """
    Changes the MAC address of a given network interface.

    Args:
        interface (str): The name of the network interface (e.g., 'eth0').
        new_mac (str): The new MAC address to set (e.g., '00:11:22:33:44:55').

    Returns:
        bool: True if the MAC address was successfully changed, False otherwise.
    """
    try:
        ifconfig_change(interface, new_mac)
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    else:
        return True
