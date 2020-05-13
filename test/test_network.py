from data_structures.network_collection import NetworkCollection
import unittest


class TestNetworkCollection(unittest.TestCase):
    n = NetworkCollection("", {})

    def test_match_ip(self):
        self.assertTrue(self.n.match_ip_pattern("2.1.1.1"))
        self.assertFalse(self.n.match_ip_pattern("01.1.1"))
        self.assertTrue(self.n.match_ip_pattern("2.1.25.1"))
        self.assertFalse(self.n.match_ip_pattern("225.1.1."))
        self.assertFalse(self.n.match_ip_pattern("256.1.1."))
        self.assertFalse(self.n.match_ip_pattern("256.-1.9,0"))

    def test_ip_in_network(self):
        self.assertTrue(self.n.belong_to_network("10.241.20.12", "10.241.20.0/24"))
        self.assertTrue(self.n.belong_to_network("10.241.15.125", "10.241.15.0/25"))
        self.assertTrue(self.n.belong_to_network("10.241.15.130", "10.241.15.128/25"))

        self.assertTrue(self.n.belong_to_network("10.20.1.0", "10.20.0.0/16"))
        self.assertTrue(self.n.belong_to_network("10.20.1.125", "10.20.0.0/16"))

        self.assertTrue(self.n.belong_to_network("192.168.100.1", "192.168.100.0/24"))
        self.assertTrue(self.n.belong_to_network("192.168.200.8", "192.168.200.0/24"))
        self.assertTrue(self.n.belong_to_network("10.20.1.125", "10.20.0.0/16"))

        self.assertFalse(self.n.belong_to_network("192.168.101.1", "192.168.100.0/24"))
        self.assertFalse(self.n.belong_to_network("193.18.101.1", "192.0.0.0/8"))
        self.assertFalse(self.n.belong_to_network("192.168.101.1", "192.0.0.0/10"))
        self.assertFalse(self.n.belong_to_network("192.168.101.1", "192.168.100.0/32"))

if __name__ == "__main__":
    unittest.main()
