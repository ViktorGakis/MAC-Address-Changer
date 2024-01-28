import re

MAC_ADDRESS_REGX_PATTERN = "\\w\\w:\\w\\w:\\w\\w:\\w\\w:\\w\\w:\\w\\w"


class ArgValidator:
    @staticmethod
    def validate(args):
        if not args.interface:
            print("- Please specify the interface as -i <interface>")
        elif not args.new_mac:
            print("- Please specify the new mac address as -m <mac_address>")
        return True


class MacValidator:
    @staticmethod
    def validator(new_mac: str) -> bool:
        """checks if the MAC address is actually a valid form of a MAC address"""

        valid_mac_address = re.search(rf"{MAC_ADDRESS_REGX_PATTERN}", new_mac)
        if valid_mac_address:
            return True
        return False


class MacComparer:
    @staticmethod
    def compare(new_mac: str, current_mac: str) -> bool:
        """compares two MAC addresses"""
        if new_mac == current_mac:
            print(
                f"- The current MAC address {current_mac} is the same as the one to be changed too {new_mac}."
            )
            return False
        return True
