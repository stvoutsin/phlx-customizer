# Phalanx Environment Customizer

This module provides functionality to customize environment configuration files for the Phalanx project. It allows you to create customized environment configurations based on base configurations defined in YAML files.

## Prerequisites

- Python 3.x
- `pyyaml` library (can be installed using `pip install pyyaml`)

## Usage

1. Clone the Phalanx repository:
   ```
   git clone <phalanx_repository_url>
   ```
2. Navigate to the repository directory:

        cd phalanx

4. Execute the customizer script:

        phalanx_customizer <phalanx_repo_path> <base_env_yaml> <new_env_yaml>


The customized environment files will be created based on the provided configurations.

## Class Documentation

### Environment

Represents an environment configuration.

- `name` (str): Name of the environment.
- `base_url` (str): Base URL of the environment.
- `loadbalancerip` (str): Load balancer IP address (optional).
- `vault_path` (str): Vault path (optional).
- `nfs` (str): NFS configuration (optional).
- `gcs_bucket` (str): GCS bucket (optional).
- `gcs_bucket_url` (str): GCS bucket URL (optional).
- `qserv` (str): Qserv configuration (optional).
- `github_oauth_client_id` (str): GitHub OAuth client ID (optional).

### EnvironmentCustomizer

A class to customize environment configuration files for the Phalanx project.

- `phalanx_repo_path` (str): Path to the Phalanx repository.


## License

This project is licensed under the GNU License. See the [LICENSE](LICENSE) file for details.
