import os
import re
import fileinput
from phalanx_customizer.config.environment import Environment


class NginxConfigUpdater:
    def __init__(self, repo_path: str):
        """
        Initialize the NginxConfigUpdater with the repository path.

        Args:
            repo_path (str): Path to the repository.
        """
        self.repo_path = repo_path

    def update_nginx_config(self, new_env: Environment) -> None:
        """
        Update the nginx-ingress config file with new settings.

        Args:
            new_env (Environment): The new environment.
        """
        nginx_config_path = os.path.join(
            f"{self.repo_path}/applications",
            "ingress-nginx",
            f"values-{new_env.name}.yaml",
        )
        self._update_file(
            nginx_config_path, "loadBalancerIP", new_env.config.loadbalancerip
        )

    def _update_file(self, file_path: str, key: str, new_value: str) -> None:
        """
        Update a specific key in a file with a new value.

        Args:
            file_path (str): Path of the file.
            key (str): Key to be updated.
            new_value (str): New value for the key.
        """
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                if key in line:
                    line = re.sub(f"{key}: .*", f'{key}: "{new_value}"', line)
                print(line, end="")


class TapConfigUpdater:
    def __init__(self, repo_path: str):
        """
        Initialize the TapConfigUpdater with the repository path.

        Args:
            repo_path (str): Path to the repository.
        """
        self.repo_path = repo_path

    def update_tap_config(self, new_env: Environment) -> None:
        """
        Update the tap config file with new settings.

        Args:
            new_env (Environment): The new environment.
        """
        tap_config_path = os.path.join(
            f"{self.repo_path}/applications",
            "tap",
            f"values-{new_env.name}.yaml",
        )
        self._update_file(
            tap_config_path, "gcsBucket", new_env.config.gcs_bucket
        )
        self._update_file(
            tap_config_path, "gcsBucketUrl", new_env.config.gcs_bucket_url
        )
        self._update_file(tap_config_path, "host", new_env.config.qserv)

    def _update_file(self, file_path: str, key: str, new_value: str) -> None:
        """
        Update a specific key in a file with a new value.

        Args:
            file_path (str): Path of the file.
            key (str): Key to be updated.
            new_value (str): New value for the key.
        """
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                if key in line:
                    line = re.sub(f"{key}: .*", f'{key}: "{new_value}"', line)
                print(line, end="")
