import ipaddress

class Entry:
    def __init__(self, address, available, last_used):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """

        self.address = address
        self.available = available
        self.last_used = last_used

    def dot_to_decimal(self, ip):
        return int(ipaddress.ip_address(ip))

    def __eq__(self, other):
        return self.dot_to_decimal(self.address) == self.dot_to_decimal(other.address)

    def __ne__(self, other):
        return self.dot_to_decimal(self.address) != self.dot_to_decimal(other.address)

    def __lt__(self,other):
        return self.dot_to_decimal(self.address) < self.dot_to_decimal(other.address)
    #
    # def __le__(self,other):
    #     return self.dot_to_decimal(self.address) <= self.dot_to_decimal(other.address)

    def __gt__(self,other):
        return self.dot_to_decimal(self.address) > self.dot_to_decimal(other.address)
    #
    # def __ge__(self,other):
    #     return self.dot_to_decimal(self.address) <= self.dot_to_decimal(other.address)

