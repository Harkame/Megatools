import logging
import subprocess
import os
import sys

logger = logging.getLogger("megatools")


class Megatools:
    megatools_path = ""

    def __init__(self, executable="megatools"):
        self.executable = executable

    def dl(
        self,
        link,
        path=None,
        no_progress=False,
        print_names=False,
        disable_resume=False,
        username=None,
        password=None,
        reload=False,
        limit_speed=0,
        proxy=None,
        netif=None,
        ip_proto=None,
        config=None,
        ignore_config_file=False,
        debug=None,
        version=False,
    ):
        """
        Usage:
          megatools dl [OPTION?] - download exported files from mega.nz

        Help Options:
          -h, --help                  Show help options

        Application Options:
          --path=PATH                 Local directory or file name, to save data to
          --no-progress               Disable progress bar
          --print-names               Print names of downloaded files
          --choose-files              Choose which files to download when downloading folders (interactive)
          --disable-resume            Disable resume when downloading file
          -u, --username=USERNAME     Account username (email)
          -p, --password=PASSWORD     Account password
          --no-ask-password           Never ask interactively for a password
          --reload                    Reload filesystem cache
          --limit-speed=SPEED         Limit transfer speed (KiB/s)
          --proxy=PROXY               Proxy setup string
          --netif=NAME                Network interface or local IP address used for outgoing connections
          --ip-proto=PROTO            Which protocol to prefer when connecting to mega.nz (v4, v6, or any)
          --config=PATH               Load configuration from a file
          --ignore-config-file        Disable loading mega.ini
          --debug=OPTS                Enable debugging output
          --version                   Show version information
        """

        command = f"{self.executable} dl {link} --no-ask-password"

        if path:
            command += "--path="
            command += path
            command += " "

        if no_progress:
            command += "--no-progress"
            command += " "

        if print_names:
            command += "--print-names"
            command += " "

        if disable_resume:
            command += "--disable-resume"
            command += " "

        if username:
            command += "--username="
            command += username
            command += " "

        if password:
            command += "--password="
            command += password
            command += " "

        if reload:
            command += "--reload"
            command += " "

        if limit_speed:
            command += "--limit-speed="
            command += limit_speed
            command += " "

        if proxy:
            command += "--proxy="
            command += proxy
            command += " "

        if netif:
            command += "--netif="
            command += netif
            command += " "

        if ip_proto:
            command += "--ip_proto="
            command += ip_proto
            command += " "

        if config:
            command += "--config="
            command += config
            command += " "

        if ignore_config_file:
            command += "--ignore-config-file"
            command += " "

        if debug:
            command += "--debug="
            command += debug
            command += " "

        if version:
            command += "--version"
            command += " "

        logger.debug(command)

        exit_code, output = execute_command(command)

        logger.debug(exit_code)

        return output

    def ls(
        self,
        username,
        password,
        folder="",
        names=False,
        recursive=False,
        long=False,
        header=False,
        human=False,
        print0=False,
        export=False,
        limit_speed=0,
        proxy=None,
        netif=None,
        ip_proto=None,
        config=None,
        ignore_config_file=False,
        debug=None,
        version=False,
    ):
        command = f'{self.executable} ls -u {username} -p "{password}" --no-ask-password {folder}'

        if names:
            command += "--names"
            command += " "

        if recursive:
            command += "--recursive"
            command += " "

        if long:
            command += "--long"
            command += " "

        if header:
            command += "--header"
            command += " "

        if human:
            command += "--human"
            command += " "

        if print0:
            command += "--print0"
            command += " "

        if export:
            command += "--export"
            command += " "

        if limit_speed:
            command += "----limit-speed="
            command += limit_speed
            command += " "

        if limit_speed:
            command += "----limit-speed="
            command += limit_speed
            command += " "

        if proxy:
            command += "--proxy="
            command += proxy
            command += " "

        if netif:
            command += "--netif="
            command += netif
            command += " "

        if ip_proto:
            command += "--ip_proto="
            command += ip_proto
            command += " "

        if config:
            command += "--config="
            command += config
            command += " "

        if ignore_config_file:
            command += "--ignore-config-file"
            command += " "

        if debug:
            command += "--debug="
            command += debug
            command += " "

        if version:
            command += "--version"
            command += " "

        logger.debug(command)

        exit_code, output = execute_command(command)

        logger.debug(exit_code)

        return output

    def get_filename(self, link):
        command = f"{self.executable} dl {link} --no-ask-password --print-names --limit-speed=1"

        logger.debug(command)

        process = subprocess.Popen(
            command,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=1,
            universal_newlines=True,
        )

        filename = None

        line_stdout = process.stdout.readline()

        process.terminate()

        logger.debug(line_stdout)

        if "error" in line_stdout.lower():
            filename = os.path.basename(
                line_stdout[line_stdout.index("exists:") + 8 : -1]
            )
        elif "warning" in line_stdout.lower():
            filename = None
        elif line_stdout is not None and len(line_stdout) > 0:
            filename = line_stdout[0 : line_stdout.index(":")]

        logger.debug(filename)

        return filename


def execute_command(command):
    output = ""

    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        bufsize=1,
        universal_newlines=True,
    )

    while True:
        line = process.stdout.readline()
        output += line
        if not line:
            break

    return process.returncode, output


if __name__ == "__main__":
    megatools = Megatools(executable="C:\megatools\megatools.exe")
    """
    megatools.dl(
        "https://mega.nz/#!PpVB0CTZ!bwa51HbeKaVjuCff_lzbH4nQnV27uBxmcF89PnnACvY"
    )
    """
    files = megatools.ls("me@mail.com", "mysuperpassword")
    print(files)
