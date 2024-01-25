class Config:
    parser_options = [
        dict(
            args=("-i", "--interface"),
            kwds=dict(
                dest="interface",
                help="Interface to have its MAC address changed",
                required=True,
            ),
        ),
        dict(
            args=("-m", "--mac"),
            kwds=dict(
                dest="new_mac",
                help="New MAC address",
                required=True,
            ),
        ),
    ]
