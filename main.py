import sys
import time
import logging
import re
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler, FileSystemEvent

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger()


class PyCharmCleanerHandler(PatternMatchingEventHandler):
    def __init__(self, patterns):
        super().__init__(patterns=patterns)

    def on_modified(self, event: FileSystemEvent) -> None:
        logger.info(f"Triggered event for modify file {event.src_path}")
        with open(event.src_path, "r") as f:
            contents = f.read()

        logger.info(contents)

        replaced = re.sub(r"wsl\$/", "wsl$$/", contents)

        if replaced == contents:
            logger.info(f"Nothing was replaced, skipping...")
            return

        logger.info("Replacing wsl\\$/ with wsl\\$/")

        with open(event.src_path, "w") as f:
            f.write(replaced)
            f.flush()


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    event_handler = PyCharmCleanerHandler(patterns=["*.override.*.yml"])
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    logger.info(f"Start watching for changes in {path}")
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
