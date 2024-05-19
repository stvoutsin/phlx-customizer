import os
from typing import List


class FileFinder:
    def __init__(self, repo_path: str):
        """
        Initialize the FileFinder with the repository path.

        Args:
            repo_path (str): Path to the repository.
        """
        self.repo_path = repo_path

    def find_matching_files(self, environment_base: str) -> List[str]:
        """
        Find all configuration files that match the environment_base name.

        Args:
            environment_base (str): The base environment name.

        Returns:
            List[str]: List of file paths.
        """
        return self._find_subpath(
            "applications", environment_base
        ) + self._find_subpath("environments", environment_base)

    def _find_subpath(
        self, directory: str, environment_base: str
    ) -> List[str]:
        """
        Find files within a subpath of the repository that match the env base
        name.

        Args:
            directory (str): Subdirectory to search within.
            environment_base (str): The base environment name.

        Returns:
            List[str]: List of file paths.
        """
        files = []
        for root, _, filenames in os.walk(f"{self.repo_path}/{directory}"):
            for filename in filenames:
                if environment_base in filename:
                    files.append(os.path.join(root, filename))
        return files
