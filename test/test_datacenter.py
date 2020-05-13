from data_structures.cluster import Cluster
from data_structures.datacenter import Datacenter
from main import get_data, URL
import unittest


class TestDatacenter(unittest.TestCase):
    data = get_data(URL)
    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    def test_init(self):
        for dc in self.datacenters:
            self.assertIsInstance(dc, Datacenter)
            self.assertIsInstance(dc.name, str)
            self.assertIsInstance(dc.clusters, list)
            self.assertIsInstance(dc.clusters[0], Cluster)

    def test_remove(self):
        for dc in self.datacenters:
            clusters_before = dc.clusters
            dc.remove_invalid_clusters()
            clusters_after = dc.clusters
            self.assertGreaterEqual(len(clusters_before), len(clusters_after))
        for dc in self.datacenters:
            for cluster in dc.clusters:
                self.assertEqual(dc.name[:3].upper(), cluster.name[:3])

    def test_match_name(self):
        d = self.datacenters[0]

        self.assertFalse(d.match_name_pattern("ber-21"))
        self.assertFalse(d.match_name_pattern("br-201"))
        self.assertFalse(d.match_name_pattern("BE-21"))
        self.assertFalse(d.match_name_pattern("BER21"))
        self.assertFalse(d.match_name_pattern("BER-9921"))

        self.assertTrue(d.match_name_pattern("BER-21"))
        self.assertTrue(d.match_name_pattern("BER-91"))
        self.assertTrue(d.match_name_pattern("BER-0"))

        d = self.datacenters[1]

        self.assertTrue(d.match_name_pattern('PAR-123'))
        self.assertTrue(d.match_name_pattern('PAR-0'))
        self.assertTrue(d.match_name_pattern('PAR-15'))
        self.assertTrue(d.match_name_pattern('PAR-99'))
        self.assertTrue(d.match_name_pattern('PAR-1'))

        self.assertFalse(d.match_name_pattern('PAR123'))
        self.assertFalse(d.match_name_pattern('PR-123'))
        self.assertFalse(d.match_name_pattern('PaR-123'))
        self.assertFalse(d.match_name_pattern('PAR-'))
        self.assertFalse(d.match_name_pattern('par-123'))
        self.assertFalse(d.match_name_pattern('par123'))
        self.assertFalse(d.match_name_pattern('P-123'))


if __name__ == "__main__":
    unittest.main()
