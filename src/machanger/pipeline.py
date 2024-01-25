from .argparser import ArgParser
from .argvalidator import ArgValidator
from .changer import change_mac


class Pipeline:
    def __init__(self) -> None:
        self.parser = ArgParser()

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
                f"Changing MAC address for interface: {self.interface} to {self.new_mac}"
            )

            if self.interface:
                print(f"Changing MAC address for interface {self.interface}")
        else:
            print(f"- Something went wrong validating the {self.args=}.")

    def handle_changing_mac(self):
        if self.new_mac and self.interface:
            print("Changing Mac Addressu")
            # change_mac(self.interface, self.new_mac)
