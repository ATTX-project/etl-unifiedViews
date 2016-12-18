from wf_api.uv.workflow_metadata import workflow_get_output
from nose.tools import assert_is_instance
import unittest
from rdflib import Graph


class WorkflowGraphTest(unittest.TestCase):
    """Test for Activity Response from API."""

    def setUp(self):
        """Set up test fixtures."""
        self.graph = Graph()

    def tearDown(self):
        """Tear down test fixtures."""
        pass

    def test_workflow_get_output(self):
        """Test Workflow processing output is Graph."""
        data = self.graph.parse(data=str(workflow_get_output()).encode('utf-8'),
                                format='turtle')
        assert_is_instance(data, type(Graph()))


if __name__ == "__main__":
    unittest.main()
