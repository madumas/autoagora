import unittest
import asyncio
import autoagora.query_metrics

from autoagora.config import init_config
init_config(["--indexer-agent-mgmt-endpoint", "http://nowhere",
             "--indexer-service-metrics-endpoint", "http://indexer-service.default.svc.cluster.local:7300/metrics"])

class MyTestCase(unittest.TestCase):
    def test_subgraph_query_count(self):
        res = asyncio.run(
            autoagora.query_metrics.subgraph_query_count("Qmadj8x9km1YEyKmRnJ6EkC2zpJZFCfTyTZpuqC3j6e1QH")
        )
        print(res)
        self.assertEqual(res, 928)

if __name__ == '__main__':
    unittest.main()
