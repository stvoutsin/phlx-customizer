"""
Phalanx Customizer class
Used to generate new environments for the Phalanx project

"""
import os
import argparse
import shutil
import fileinput
from typing import List
import re
from dataclasses import dataclass, fields
import yaml


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

@dataclass
class Environment:
    """
    Represents an environment configuration.
    """
    name: str
    base_url: str
    config: EnvironmentConfig = EnvironmentConfig()

@dataclass
class EnvironmentCustomizer:
    """
    A class to customize environment configuration files for the Phalanx project.
    """

    phalanx_repo_path: str

    def create_environment_from_yaml(
            self,
            base_env_yaml: str,
            new_env_yaml: str
    ) -> None:
        """
        Customize the environment configuration files using YAML files.

        Args:
            base_env_yaml (str): Path to the YAML file containing base environment configuration.
            new_env_yaml (str): Path to the YAML file containing new environment configuration.
        """
        base_env = self.parse_environment_yaml(base_env_yaml)
        new_env = self.parse_environment_yaml(new_env_yaml)
        self.create_environment(base_env, new_env)

    @staticmethod
    def parse_environment_yaml(yaml_file: str) -> Environment:
        """
        Parse the environment configuration from a YAML file.

        Args:
            yaml_file (str): Path to the YAML file.

        Returns:
            Environment: Parsed environment configuration.
        """
        with open(yaml_file) as file:
            data = yaml.safe_load(file)
            kwargs = {field.name: data.get(field.name) for field in fields(EnvironmentConfig)}
            config = EnvironmentConfig(**kwargs)
            return Environment(name=data.get("name"), base_url=data.get("base_url"), config=config)
    def create_environment(
            self,
            base_env: Environment,
            new_env: Environment
    ) -> None:
        """
        Customize the environment configuration files.

        Args:
            base_env (Environment): The base environment.
            new_env (Environment): The new environment.
        """
        # Find all files matching the base environment name
        matching_files = self.find_matching_files(base_env.name)

        # Clone and customize the configuration files
        for file_path in matching_files:
            new_file_path = self.create_custom_file(file_path, base_env.name, new_env.name)

            for param in ("nfs", "github_oauth_client_id"):
                new_config, base_config = new_env.config, base_env.config
                self.replace_string_in_file(new_file_path, getattr(base_config, param),
                                            getattr(new_config, param))

            for param in ("name", "base_url"):
                self.replace_string_in_file(new_file_path, getattr(base_env, param),
                                            getattr(new_env, param))
        # Update nginx-ingress config file
        self.update_nginx_config(new_env)
        self.update_tap(new_env)

    def find_matching_files(self, environment_base: str) -> List[str]:
        """
        Find all configuration files that match the environment_base name.

        Args:
            environment_base (str): The base environment name.

        Returns:
            List[str]: List of file paths.
        """
        def _find_subpath(directory: str) -> List[str]:
            files = []
            for root, _, filenames in os.walk(f'{self.phalanx_repo_path}/{directory}'):
                for filename in filenames:
                    if environment_base in filename:
                        files.append(os.path.join(root, filename))
            return files

        return _find_subpath("applications") + _find_subpath("environments")

    @staticmethod
    def create_custom_file(file_path: str, environment_base: str, new_environment_name: str) -> str:
        """
        Create a customized copy of the configuration file.

        Args:
            file_path (str): Path of the original configuration file.
            environment_base (str): The base environment name.
            new_environment_name (str): The new environment name.

        Returns:
            str: Path of the newly created customized file.
        """
        new_file_path = file_path.replace(environment_base, new_environment_name)
        shutil.copy2(file_path, new_file_path)
        return new_file_path

    @staticmethod
    def replace_string_in_file(file_path: str, old_string: str, new_string: str) -> None:
        """
        Replace a string in a file.

        Args:
            file_path (str): Path of the file.
            old_string (str): String to be replaced.
            new_string (str): Replacement string.
        """
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                print(line.replace(old_string, new_string), end='')

    def update_tap(
            self,
            new_env: Environment,
    ) -> None:
        """
        Update the tap config file with new settings.

        Args:
            new_env (Environment): The new environment.
        """
        nginx_config_path = os.path.join(f'{self.phalanx_repo_path}/applications',
                                         'tap', f'values-{new_env.name}.yaml')
        with fileinput.FileInput(nginx_config_path, inplace=True) as file:
            for line in file:
                if 'gcsBucket' in line:
                    line = re.sub(r'gcsBucket: .*',
                                  f'gcsBucket: "{new_env.config.gcs_bucket}"', line)
                if 'gcsBucketUrl:' in line:
                    line = re.sub(r'gcsBucketUrl: .*',
                                  f'gcsBucketUrl: "{new_env.config.gcs_bucket_url}"', line)
                if 'host:' in line:
                    line = re.sub(r'host: .*', f'host: "{new_env.config.qserv}"', line)
                print(line, end='')

    def update_nginx_config(
            self,
            new_env: Environment,
    ) -> None:
        """
        Update the nginx-ingress config file with new settings.

        Args:
            new_env (Environment): The new environment.
        """
        nginx_config_path = os.path.join(f'{self.phalanx_repo_path}/applications',
                                         'ingress-nginx', f'values-{new_env.name}.yaml')
        with fileinput.FileInput(nginx_config_path, inplace=True) as file:
            for line in file:
                if 'loadBalancerIP' in line:
                    line = re.sub(r'loadBalancerIP: .*',
                                  f'loadBalancerIP: "{new_env.config.loadbalancerip}"', line)
                print(line, end='')


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description='Phalanx Environment Customizer')
    PARSER.add_argument('phalanx_repo_path',
                        help='Path to the Phalanx repository')
    PARSER.add_argument('base_env_yaml',
                        help='Path to the YAML file containing base environment configuration')
    PARSER.add_argument('new_env_yaml',
                        help='Path to the YAML file containing new environment configuration')
    ARGS = PARSER.parse_args()

    CUSTOMIZER = EnvironmentCustomizer(ARGS.phalanx_repo_path)
    CUSTOMIZER.create_environment_from_yaml(ARGS.base_env_yaml, ARGS.new_env_yaml)
