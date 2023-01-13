import asyncio
import autoagora.query_metrics
import vcr
from autoagora.config import init_config

init_config(["--indexer-agent-mgmt-endpoint", "http://nowhere",
         "--indexer-service-metrics-endpoint", "http://indexer-service.default.svc.cluster.local:7300/metrics"])


class TestQueryMetrics:
    def test_subgraph_query_count(self):
        with vcr.use_cassette('vcr_cassettes/indexer_service_metrics_endpoint.yaml'):
            res = asyncio.run(
                    autoagora.query_metrics.subgraph_query_count("Qmadj8x9km1YEyKmRnJ6EkC2zpJZFCfTyTZpuqC3j6e1QH")
            )
        print(res)
        assert(res == 928)

