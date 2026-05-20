import os


class BinaryReader:
    """
    Handles binary payload retrieval for
    validation and transport workflows.

    Purpose:
        Used for:
        - payload replay
        - captured data loading
        - HIL validation flows
        - binary transport analysis
        - validation input retrieval

    Output:
        Raw binary byte stream loaded from disk.
    """

    def __init__(
        self,
        file_path: str
    ):
        """
        Initialize binary reader configuration.

        Args:
            file_path (str):
                Source binary file path.
        """

        if not isinstance(file_path, str):
            raise TypeError(
                "file_path must be a string."
            )

        if len(file_path.strip()) == 0:
            raise ValueError(
                "file_path cannot be empty."
            )

        self.file_path = file_path

    def read(self) -> bytes:
        """
        Read binary payload from disk.

        Returns:
            bytes:
                Binary payload loaded from file.
        """

        if not os.path.exists(
            self.file_path
        ):
            raise FileNotFoundError(
                f"File does not exist: "
                f"{self.file_path}"
            )

        if not os.path.isfile(
            self.file_path
        ):
            raise ValueError(
                f"Path is not a file: "
                f"{self.file_path}"
            )

        with open(
            self.file_path,
            "rb"
        ) as binary_file:

            binary_data = binary_file.read()

        if len(binary_data) == 0:
            raise ValueError(
                "Binary file is empty."
            )

        return binary_data