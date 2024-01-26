from .argparser import ArgParser
from .changer import change_mac, get_current_mac
from .validators import ArgValidator


class Pipeline:
    def __init__(self) -> None:
        self.parser = ArgParser()
        self.proceed_mac_change = False
        self.current_mac = ""

    def handle_arg_parsing(self) -> None:
        self.parser.add_options()
        self.args = self.parser.parse_args()

    def handle_arg_validation(self):
        self.interface = None
        self.new_mac = None
        if ArgValidator.validate(self.args):
            self.interface = self.args.interface
            self.new_mac = self.args.new_mac

            print(
                f"- Changing MAC address for interface: {self.interface} to {self.new_mac}"
            )

            if self.interface:
                print(f"- Changing MAC address for interface {self.interface}")
        else:
            print(f"- Something went wrong validating the {self.args=}.")

    def handle_finding_current_mac(self):
        if self.new_mac and self.interface:
            self.current_mac: str | None = get_current_mac(self.interface)

    def pre_change_mac_validation(self):
        if self.current_mac:
            if check_new_mac_against_current(self.new_mac, self.current_mac):
                self.proceed_mac_change = True
                print("- Args are valid, proceeding in changing the MAC address....")

    def handle_changing_mac(self):
        if self.proceed_mac_change:
            print("- Changing MAC Addressu")
            output = change_mac(self.interface, self.new_mac)

    def run(self):
        self.handle_arg_parsing()

        self.handle_arg_validation()

        self.handle_finding_current_mac()

        self.pre_change_mac_validation()

        # pipeline.handle_changing_mac()
