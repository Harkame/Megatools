import logging
import subprocess

logger = logging.getLogger("megatools_wrapper")


class MegaToolsWrapper:
    megatools_path = ""

    def __init__(self, megatools_path=""):
        self.megatools_path = megatools_path

    def download(self, mega_link, limit_speed=0, path="./"):
        command = f"{self.megatools_path}megadl {mega_link} --limit-speed={limit_speed} --path={path}"

        logger.debug(command)

        return_code = execute_command(command)

        logger.debug(return_code)


def execute_command(command):
    process = subprocess.Popen(
        command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
    process.wait()
    return process.returncode


if __name__ == "__main__":
    formatter = logging.Formatter(
        "%(asctime)s :: %(module)s :: %(lineno)s :: %(funcName)s :: %(message)s"
    )
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)

    logger.addHandler(stream_handler)

    megatools_wrapper = MegaToolsWrapper(megatools_path="")

    megatools_wrapper.download("", limit_speed=0, path="./toto.txt")
