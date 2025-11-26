from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional


def setup_logging(log_file: Optional[str] = None, level: int = logging.INFO) -> None:
    """Configure a central logger that writes to a file and the console.

    - Ensures the `logs/` directory exists.
    - Adds a rotating file handler writing to `logs/app.log` by default.
    - Leaves existing handlers for uvicorn intact while ensuring our module
      loggers emit to the file.
    """
    if log_file is None:
        log_file = "logs/app.log"

    log_path = Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Avoid adding duplicate handlers if called multiple times
    for h in list(root_logger.handlers):
        if isinstance(h, RotatingFileHandler) and getattr(
            h, "baseFilename", None
        ) == str(log_path):
            break
    else:
        file_handler = RotatingFileHandler(
            str(log_path), maxBytes=10 * 1024 * 1024, backupCount=3
        )
        file_handler.setLevel(level)
        formatter = logging.Formatter(
            "%(asctime)s %(levelname)-8s %(name)s:%(lineno)d - %(message)s"
        )
        file_handler.setFormatter(formatter)
        root_logger.addHandler(file_handler)

    # Ensure our app logger uses the same level
    logging.getLogger("app").setLevel(level)
