import argparse
from phalanx_customizer.core.environment_customizer import (
    EnvironmentCustomizer,
)


def main():
    parser = argparse.ArgumentParser(
        description="Phalanx Environment Customizer"
    )
    parser.add_argument(
        "phalanx_repo_path", help="Path to the Phalanx repository"
    )
    parser.add_argument(
        "base_env_yaml",
        help="Path to the YAML file containing base environment configuration",
    )
    parser.add_argument(
        "new_env_yaml",
        help="Path to the YAML file containing new environment configuration",
    )
    args = parser.parse_args()

    customizer = EnvironmentCustomizer(args.phalanx_repo_path)
    customizer.create_environment_from_yaml(
        args.base_env_yaml, args.new_env_yaml
    )


if __name__ == "__main__":
    main()
