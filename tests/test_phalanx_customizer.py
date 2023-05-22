"""
Tests for Phalanx Customizer module
"""
import os
import unittest
import tempfile
from phalanx_customizer import EnvironmentCustomizer


class TestPhalanxCustomizer(unittest.TestCase):
    """
    Phalanx Customizer unittest test class
    """
    def setUp(self):
        current_dir = os.getcwd()
        parent_dir = os.path.dirname(os.getcwd())
        self.phalanx_repo_path = os.path.join(current_dir, "phalanx_demo")
        self.envs_path = os.path.join(parent_dir, "envs")

    def tearDown(self):
        pass

    def test_parse_environment_yaml(self):
        """
        Test that parsing works correctly
        """
        yaml_data = """
        name: TestEnvironment
        base_url: http://example.com
        loadbalancerip: 192.168.0.1
        vault_path: path/to/vault
        nfs: nfs.example.com
        gcs_bucket: example-bucket
        gcs_bucket_url: http://example-bucket.com
        qserv: qserv.example.com
        github_oauth_client_id: abc123
        """

        customizer = EnvironmentCustomizer(self.phalanx_repo_path)

        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write(yaml_data)
            temp_file_path = temp_file.name

        environment = customizer.parse_environment_yaml(temp_file_path)
        os.remove(temp_file_path)

        self.assertEqual(environment.name, 'TestEnvironment')
        self.assertEqual(environment.base_url, 'http://example.com')
        self.assertEqual(environment.loadbalancerip, '192.168.0.1')
        self.assertEqual(environment.vault_path, 'path/to/vault')
        self.assertEqual(environment.nfs, 'nfs.example.com')
        self.assertEqual(environment.gcs_bucket, 'example-bucket')
        self.assertEqual(environment.gcs_bucket_url, 'http://example-bucket.com')
        self.assertEqual(environment.qserv, 'qserv.example.com')
        self.assertEqual(environment.github_oauth_client_id, 'abc123')

    def test_create_environment_from_yaml(self):
        """
        Assert that the new environment was created
        """
        customizer = EnvironmentCustomizer(self.phalanx_repo_path)
        customizer.create_environment_from_yaml(f"{self.envs_path}/roe.yaml",
                                                f"{self.envs_path}/rsptest.yaml")
        self.assertTrue(os.path.exists(
            f"{self.phalanx_repo_path}/environments/values-rsptest.yaml"))


if __name__ == '__main__':
    unittest.main()
