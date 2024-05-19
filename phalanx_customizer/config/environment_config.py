from dataclasses import dataclass


@dataclass
class EnvironmentConfig:
    """
    Represents the configuration details of an environment.
    """

    loadbalancerip: str = None
    vault_path: str = None
    nfs: str = None
    gcs_bucket: str = None
    gcs_bucket_url: str = None
    qserv: str = None
    github_oauth_client_id: str = None
