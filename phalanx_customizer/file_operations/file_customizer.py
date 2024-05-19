import shutil
import fileinput


class FileCustomizer:
    @staticmethod
    def create_custom_file(
        file_path: str, environment_base: str, new_environment_name: str
    ) -> str:
        """
        Create a customized copy of the configuration file.

        Args:
            file_path (str): Path of the original configuration file.
            environment_base (str): The base environment name.
            new_environment_name (str): The new environment name.

        Returns:
            str: Path of the newly created customized file.
        """
        new_file_path = file_path.replace(
            environment_base, new_environment_name
        )
        shutil.copy2(file_path, new_file_path)
        return new_file_path

    @staticmethod
    def replace_string_in_file(
        file_path: str, old_string: str, new_string: str
    ) -> None:
        """
        Replace a string in a file.

        Args:
            file_path (str): Path of the file.
            old_string (str): String to be replaced.
            new_string (str): Replacement string.
        """
        with fileinput.FileInput(file_path, inplace=True) as file:
            for line in file:
                print(line.replace(old_string, new_string), end="")
