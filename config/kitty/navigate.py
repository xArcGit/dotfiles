from os import getuid
from pathlib import Path
from re import match

from pynvim import attach

from typing import List
from kitty.boss import Boss

def wincmd(nvim, direction):
    wincmd_direction = {
        "left": "h",
        "bottom": "j",
        "top": "k",
        "right": "l",
    }[direction]

    old_win_id = nvim.command_output("echo win_getid()")
    new_win_id = nvim.command_output(f"wincmd {wincmd_direction} | echo win_getid()")

    return old_win_id != new_win_id


def nvim_runtime_path(boss):
    """
    Grabbing the nvim runtime path using a pynvim child process has perceptible overhead, so we cache the result
    """

    if not hasattr(boss, "_nvim_rtp"):
        Boss._nvim_rtp = None

    if boss._nvim_rtp is None:
        with attach(
            "child", argv=["/bin/env", "nvim", "--embed", "--headless"]
        ) as nvim:
            boss._nvim_rtp = nvim.command_output("echo stdpath('run')")

    return boss._nvim_rtp


def pid_from_socket_path(path) -> str:
    m = match(r"nvim\.(?P<pid>\d+)\.\d+", path.name)
    if m is not None:
        return int(m["pid"])


def this_nvim(window):
    fg_pids = set(proc["pid"] for proc in window.child.foreground_processes)

    uid = getuid()
    nvim_sockets_by_pid = {
        pid: path
        for path in Path(f"/run/user/{uid}").glob("nvim.*")
        if (pid := pid_from_socket_path(path)) is not None
    }

    for pid, socket in nvim_sockets_by_pid.items():
        if pid in fg_pids:
            return attach("socket", path=str(socket))

    return None


def main(args: List[str]) -> str:
    pass


from kittens.tui.handler import result_handler


@result_handler(no_ui=True)
def handle_result(
    args: List[str],
    answer: str,
    target_window_id: int,
    boss: Boss,
    *other_args,
    **kwargs,
) -> None:

    window = boss.window_id_map.get(target_window_id)
    direction = args[1]

    # Remap "up" and "down" to the right edge names
    direction = {"up": "top", "down": "bottom"}.get(direction, direction)

    nvim = this_nvim(window)

    if nvim is not None and wincmd(nvim, direction):
        return

    boss.active_tab.neighboring_window(direction)
