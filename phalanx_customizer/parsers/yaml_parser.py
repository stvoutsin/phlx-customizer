from phalanx_customizer.config.environment import Environment
from phalanx_customizer.config.environment_config import EnvironmentConfig
from typing import Protocol
import yaml
from dataclasses import fields


class YamlParser(Protocol):
    def parse(self, yaml_file: str) -> Environment:
        """
        Parse the environment configuration from a YAML file.

        Args:
            yaml_file (str): Path to the YAML file.

        Returns:
            Environment: Parsed environment configuration.
        """
        ...


class EnvironmentYamlParser(YamlParser):
    def parse(self, yaml_file: str) -> Environment:
        """
        Parse the environment configuration from a YAML file.

        Args:
            yaml_file (str): Path to the YAML file.

        Returns:
            Environment: Parsed environment configuration.
        """
        with open(yaml_file, encoding="utf-8") as file:
            data = yaml.safe_load(file)
            kwargs = {
                field.name: data.get(field.name)
                for field in fields(EnvironmentConfig)
            }
            config = EnvironmentConfig(**kwargs)
            return Environment(
                name=data.get("name"),
                base_url=data.get("base_url"),
                config=config,
            )
