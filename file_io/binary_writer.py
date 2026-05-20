import os


class BinaryWriter:
    """
    Handles binary payload persistence for
    validation and transport workflows.

    Purpose:
        Used for:
        - payload archival
        - HIL transport preparation
        - binary replay generation
        - captured data storage
        - validation logging

    Output:
        Raw binary file written to disk.
    """

    SUPPORTED_MODES = ("wb", "ab")

    def __init__(
        self,
        file_path: str,
        mode: str = "wb"
    ):
        """
        Initialize binary writer configuration.

        Args:
            file_path (str):
                Destination binary file path.

            mode (str):
                File write mode.

                Supported:
                    - "wb" : overwrite mode
                    - "ab" : append mode
        """

        if not isinstance(file_path, str):
            raise TypeError(
                "file_path must be a string."
            )

        if len(file_path.strip()) == 0:
            raise ValueError(
                "file_path cannot be empty."
            )

        if not isinstance(mode, str):
            raise TypeError(
                "mode must be a string."
            )

        if mode not in self.SUPPORTED_MODES:
            raise ValueError(
                f"Unsupported mode: {mode}"
            )

        self.file_path = file_path
        self.mode = mode

    def write(
        self,
        data: bytes
    ) -> dict:
        """
        Write binary payload to disk.

        Args:
            data (bytes):
                Binary payload to persist.

        Returns:
            dict:
                Structured write metadata.
        """

        if not isinstance(data, bytes):
            raise TypeError(
                "data must be of type bytes."
            )

        if len(data) == 0:
            raise ValueError(
                "data cannot be empty."
            )

        directory_path = os.path.dirname(
            self.file_path
        )

        if directory_path:

            os.makedirs(
                directory_path,
                exist_ok=True
            )

        with open(
            self.file_path,
            self.mode
        ) as binary_file:

            bytes_written = binary_file.write(
                data
            )

        return {
            "success": True,
            "bytes_written": bytes_written,
            "file_path": self.file_path,
            "mode": self.mode
        }