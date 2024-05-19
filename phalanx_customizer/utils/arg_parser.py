import argparse


def parse_arguments():
    """
    Parse command line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
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
    return parser.parse_args()
