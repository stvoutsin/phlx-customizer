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

4. Execute the environment_customizer.py script:

        python phalanx_customizer.py <phalanx_repo_path> <base_env_yaml> <new_env_yaml>


4. The customized environment files will be created based on the provided configurations.

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

#### Methods

- `create_environment_from_yaml(base_env_yaml: str, new_env_yaml: str) -> None`:

Customize the environment configuration files using YAML files.

- `parse_environment_yaml(yaml_file: str) -> Environment`:

Parse the environment configuration from a YAML file.

- `create_environment(base_env: Environment, new_env: Environment) -> None`:

Customize the environment configuration files.

- `find_matching_files(environment_base: str) -> List[str]`:

Find all configuration files that match the base environment name.

- `create_custom_file(file_path: str, environment_base: str, new_environment_name: str) -> str`:

Create a customized copy of the configuration file.

- `replace_string_in_file(file_path: str, old_string: str, new_string: str) -> None`:

Replace a string in a file.

- `update_tap(new_env: Environment) -> None`:

Update the tap config file with new settings.

- `update_nginx_config(new_env: Environment) -> None`:

Update the nginx-ingress config file with new settings.

## License

This project is licensed under the GNU License. See the [LICENSE](LICENSE) file for details.
