from phalanx_customizer.config.environment import Environment
from phalanx_customizer.parsers.yaml_parser import EnvironmentYamlParser
from phalanx_customizer.file_operations.file_finder import FileFinder
from phalanx_customizer.file_operations.file_customizer import FileCustomizer
from phalanx_customizer.file_operations.config_updater import (
    NginxConfigUpdater,
    TapConfigUpdater,
)


class EnvironmentCustomizer:
    """
    A class to customize environment configuration files for the Phalanx project.
    """

    def __init__(self, repo_path: str):
        self.repo_path = repo_path
        self.file_finder = FileFinder(repo_path)
        self.file_customizer = FileCustomizer()
        self.nginx_updater = NginxConfigUpdater(repo_path)
        self.tap_updater = TapConfigUpdater(repo_path)
        self.yaml_parser = EnvironmentYamlParser()

    def create_environment_from_yaml(
        self, base_env_yaml: str, new_env_yaml: str
    ) -> None:
        """
        Customize the environment configuration files using YAML files.

        Args:
            base_env_yaml (str): Path to the YAML file containing base environment configuration.
            new_env_yaml (str): Path to the YAML file containing new environment configuration.
        """
        base_env = self.yaml_parser.parse(base_env_yaml)
        new_env = self.yaml_parser.parse(new_env_yaml)
        self.create_environment(base_env, new_env)

    def create_environment(
        self, base_env: Environment, new_env: Environment
    ) -> None:
        """
        Customize the environment configuration files.

        Args:
            base_env (Environment): The base environment.
            new_env (Environment): The new environment.
        """
        matching_files = self.file_finder.find_matching_files(base_env.name)

        for file_path in matching_files:
            new_file_path = self.file_customizer.create_custom_file(
                file_path, base_env.name, new_env.name
            )

            for param in ("nfs", "github_oauth_client_id"):
                new_config, base_config = new_env.config, base_env.config
                self.file_customizer.replace_string_in_file(
                    new_file_path,
                    getattr(base_config, param),
                    getattr(new_config, param),
                )

            for param in ("name", "base_url"):
                self.file_customizer.replace_string_in_file(
                    new_file_path,
                    getattr(base_env, param),
                    getattr(new_env, param),
                )

        self.nginx_updater.update_nginx_config(new_env)
        self.tap_updater.update_tap_config(new_env)
