# pyright: reportMissingImports=false
# pylint: disable=E0401,C0116,C0103,W0603,R0913

import datetime
import dbus
import random
from typing import Dict, Optional, Tuple


# Define hex_to_int function
def hex_to_int(hex_color: str) -> int:
    return int(hex_color.lstrip("#"), 16)


from kitty.fast_data_types import Screen, get_options
from kitty.tab_bar import (
    DrawData,
    ExtraData,
    TabBarData,
    as_rgb,
    draw_tab_with_powerline,
    draw_title,
)
from kitty.utils import color_as_int

opts = get_options()

BG_COLOR: Dict[str, str] = {
  "flamingo": "#f2cdcd",
"pink": "#f5c2e7",
"maroon": "#eba0ac",
"peach": "#fab387",
"yellow": "#f9e2af",
"green": "#a6e3a1",
"teal": "#94e2d5",
"sapphire": "#74c7ec",
"blue": "#89b4fa",
"lavender": "#b4befe"
}

FG_COLOR: Dict[str, str] = {
  "crust": "#11111b",
}

chosen_colors_fg = []
chosen_colors_bg = []


def get_color(COLORS: Dict[str, str], chosen_colors: list[str]) -> str:
    # Exclude colors that are in chosen_colors
    suitable_colors: Dict[str, str] = {
        k: v for k, v in COLORS.items() if k not in chosen_colors
    }

    # If all colors are excluded, reset chosen_colors to retry
    if not suitable_colors:
        chosen_colors.clear()
        suitable_colors = COLORS  # Reset to include all colors again

    chosen_color = random.choice(list(suitable_colors.values()))
    chosen_color_name = next((k for k, v in COLORS.items() if v == chosen_color), None)

    # Add chosen color to chosen_colors list
    if chosen_color_name:
        chosen_colors.append(chosen_color_name)

    return chosen_color


# Icon settings
ICON: str = " → "
ICON_LENGTH: int = len(ICON)
ICON_FG: int = as_rgb(hex_to_int(get_color(FG_COLOR, chosen_colors_fg)))
ICON_BG: int = as_rgb(hex_to_int(get_color(BG_COLOR, chosen_colors_bg)))

# Date and time colors
CLOCK_FG: int = as_rgb(hex_to_int(get_color(FG_COLOR, chosen_colors_fg)))
CLOCK_BG: int = as_rgb(hex_to_int(get_color(BG_COLOR, chosen_colors_bg)))
DATE_FG: int = as_rgb(hex_to_int(get_color(FG_COLOR, chosen_colors_fg)))
DATE_BG: int = as_rgb(hex_to_int(get_color(BG_COLOR, chosen_colors_bg)))

# Spotify colors
SPOTIFY_FG: int = as_rgb(hex_to_int(get_color(FG_COLOR, chosen_colors_fg)))
SPOTIFY_BG: int = as_rgb(hex_to_int(get_color(BG_COLOR, chosen_colors_bg)))

current_session: int = 1


def get_spotify_info() -> str:
    status = ""
    try:
        session_bus = dbus.SessionBus()
        spotify_bus = session_bus.get_object(
            "org.mpris.MediaPlayer2.spotify_player", "/org/mpris/MediaPlayer2"
        )
        spotify_properties = dbus.Interface(
            spotify_bus, "org.freedesktop.DBus.Properties"
        )
        metadata = spotify_properties.Get("org.mpris.MediaPlayer2.Player", "Metadata")
        status += f"{metadata.get('xesam:title', '')}"
    except Exception:
        status = ""
    return status


def _draw_icon(screen: Screen, index: int) -> int:
    if index != current_session:
        return screen.cursor.x

    fg, bg, bold, italic = (
        screen.cursor.fg,
        screen.cursor.bg,
        screen.cursor.bold,
        screen.cursor.italic,
    )
    screen.cursor.bold, screen.cursor.italic, screen.cursor.fg, screen.cursor.bg = (
        True,
        False,
        ICON_FG,
        ICON_BG,
    )
    screen.draw(ICON)
    # set cursor position
    screen.cursor.x = ICON_LENGTH
    # restore color style
    screen.cursor.fg, screen.cursor.bg, screen.cursor.bold, screen.cursor.italic = (
        fg,
        bg,
        bold,
        italic,
    )
    return screen.cursor.x


def _draw_left_status(
    draw_data: DrawData,
    screen: Screen,
    tab: TabBarData,
    before: int,
    max_title_length: int,
    index: int,
    is_last: bool,
    extra_data: ExtraData,
    use_kitty_render_function: bool = False,
) -> int:
    if use_kitty_render_function:
        # Use `kitty` function render tab
        end = draw_tab_with_powerline(
            draw_data, screen, tab, before, max_title_length, index, is_last, extra_data
        )
        return end

    if draw_data.leading_spaces:
        screen.draw(" " * draw_data.leading_spaces)

    # draw tab title
    draw_title(draw_data, screen, tab, index)

    trailing_spaces = min(max_title_length - 1, draw_data.trailing_spaces)
    max_title_length -= trailing_spaces
    extra = screen.cursor.x - before - max_title_length
    if extra > 0:
        screen.cursor.x -= extra + 1
        screen.draw("…")
    if trailing_spaces:
        screen.draw(" " * trailing_spaces)

    screen.cursor.bold = screen.cursor.italic = False
    screen.cursor.fg = 0
    if not is_last:
        screen.cursor.bg = as_rgb(color_as_int(draw_data.inactive_bg))
        screen.draw(draw_data.sep)
    screen.cursor.bg = 0
    return screen.cursor.x


def _draw_right_status(screen: Screen, is_last: bool) -> int:
    if not is_last:
        return screen.cursor.x

    cells: Tuple[Tuple[int, int, str], ...] = (
        (SPOTIFY_FG, SPOTIFY_BG, f" {get_spotify_info()} "),
        (CLOCK_FG, CLOCK_BG, datetime.datetime.now().strftime(" %H:%M ")),
        (DATE_FG, DATE_BG, datetime.datetime.now().strftime(" %Y/%m/%d ")),
    )

    right_status_length = 0
    for _, _, cell in cells:
        right_status_length += len(cell)

    draw_spaces = screen.columns - screen.cursor.x - right_status_length
    if draw_spaces > 0:
        screen.draw(" " * draw_spaces)

    for fg, bg, cell in cells:
        screen.cursor.fg = fg
        screen.cursor.bg = bg
        screen.draw(cell)
    screen.cursor.fg = 0
    screen.cursor.bg = 0

    screen.cursor.x = max(screen.cursor.x, screen.columns - right_status_length)
    return screen.cursor.x


def draw_tab(
    draw_data: DrawData,
    screen: Screen,
    tab: TabBarData,
    before: int,
    max_title_length: int,
    index: int,
    is_last: bool,
    extra_data: ExtraData,
) -> int:
    _draw_icon(screen, index)
    end = _draw_left_status(
        draw_data,
        screen,
        tab,
        before,
        max_title_length,
        index,
        is_last,
        extra_data,
        use_kitty_render_function=False,
    )
    _draw_right_status(screen, is_last)
    return end
