class ArgValidator:
    @staticmethod
    def validate(args):
        if not args.interface:
            print("- Please specify the interface as -i <interface>")
        elif not args.new_mac:
            print("- Please specify the new mac address as -m <mac_address>")
        return True