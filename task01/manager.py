from transport import Transport


class Manager:
    @staticmethod
    def run(transports):
        for transport in transports:
            transport.go()
