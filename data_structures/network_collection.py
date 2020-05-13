from data_structures.entry import Entry
import re, ipaddress


class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """
        self.ipv4_network = ipv4_network
        self.entries = [Entry(address=network['address'],
                              available=network['available'],
                              last_used=network['last_used'])
                        for network in raw_entry_list]

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """

        valid_entries = []
        for entry in self.entries:
            if self.match_ip_pattern(entry.address) and self.belong_to_network(entry.address, self.ipv4_network):
                valid_entries.append(entry)
        self.entries = valid_entries

    def match_ip_pattern(self, ip):
        """
        Args:
            ip: ip in dot zecimal notation

        Returns: true if ip is right formatted

        """
        pattern = """^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"""
        c_pattern = re.compile(pattern)
        return c_pattern.match(ip) is not None

    def belong_to_network(self, ip, network):
        """
        Args:
            ip: ip in dot zecimal notation
            network: network in dot zecimal notation

        Returns: true if ip is in network, otherwise returns false

        """
        return ipaddress.ip_address(ip) in ipaddress.ip_network(network)

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
