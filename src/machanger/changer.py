import re
import subprocess as sp

MAC_ADDRESS_REGX_PATTERN = "\\w\\w:\\w\\w:\\w\\w:\\w\\w:\\w\\w:\\w\\w"


def ifconfig() -> int:
    return sp.call("ifconfig", shell=True)


def ifconfig_change(interface: str, new_mac: str) -> None:
    sp.call(["ifconfig", interface, "down"])
    sp.call(["ifconfig", interface, "hw ether", new_mac])
    sp.call(["ifconfig", interface, "up"])


def get_current_mac(interface: str) -> str | None:
    """extracts the MAC address of an interface"""
    try:
        ifconfig_res: str = sp.check_output(["ifconfig", interface]).decode()
    except Exception as e:
        print(f"Exception: {e}")
    else:
        mac_address = re.search(rf"{MAC_ADDRESS_REGX_PATTERN}", ifconfig_res)

        if not mac_address:
            print(
                f"- Could not extract current MAC address from interface: {interface}"
            )
            return
        mac: str = mac_address.group(0)
        print(f"- CURRENT MAC address: {mac}")
        return mac


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


def check_new_mac_address_validity(new_mac: str):
    valid_mac_address = re.search(rf"{MAC_ADDRESS_REGX_PATTERN}", new_mac)
    if valid_mac_address:
        return True
    return False


def check_new_mac_against_current(new_mac, current_mac) -> bool:
    if new_mac == current_mac:
        print(
            f"- The current MAC address {current_mac} is the same as the one to be changed too {new_mac}."
        )
        return False
    return True


def validate_mac_change(interface: str, new_mac: str, current_mac: str):
    if new_mac == current_mac:
        print(
            f"- MAC address changed from {current_mac} to {new_mac} for interface: {interface}"
        )
