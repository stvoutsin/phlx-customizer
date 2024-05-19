from dataclasses import dataclass, field
from .environment_config import EnvironmentConfig


@dataclass
class Environment:
    """
    Represents an environment configuration.
    """

    name: str
    base_url: str
    config: EnvironmentConfig = field(default_factory=EnvironmentConfig)
