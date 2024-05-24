# pyright: reportMissingImports=false
import dbus
import datetime
from kitty.boss import get_boss
from kitty.fast_data_types import Screen, add_timer
from kitty.rgb import Color
from kitty.tab_bar import DrawData, ExtraData, TabBarData, as_rgb, draw_title
from kitty.utils import color_as_int


timer_id = None


def calc_draw_spaces(*args) -> int:
    """Calculate the total width required to draw given items."""
    lengths = [len(str(i)) for i in args]
    return sum(lengths)


def _draw_icon(screen: Screen, index: int) -> int:
    """Draw an icon at the specified index."""
    if index != 1:
        return screen.cursor.x

    fg, bg = screen.cursor.fg, screen.cursor.bg
    screen.cursor.fg = as_rgb(color_as_int(Color(255, 255, 255)))
    screen.cursor.bg = as_rgb(color_as_int(Color(160, 125, 180)))
    screen.draw(" A ")
    screen.cursor.fg, screen.cursor.bg = fg, bg
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
) -> int:
    """Draw the left status."""
    global timer_id
    if draw_data.leading_spaces:
        screen.draw(" " * draw_data.leading_spaces)
    draw_title(draw_data, screen, tab, index)
    trailing_spaces = min(max_title_length - 1, draw_data.trailing_spaces)
    max_title_length -= trailing_spaces
    extra = screen.cursor.x - before - max_title_length
    if extra > 0:
        screen.cursor.x -= extra + 1
        screen.draw("…")
    if trailing_spaces:
        screen.draw(" " * trailing_spaces)
    if timer_id is None:
        timer_id = add_timer(_redraw_tab_bar, 30, True)
    end = screen.cursor.x
    screen.cursor.bold = screen.cursor.italic = False
    screen.cursor.fg = 0
    if not is_last:
        screen.cursor.bg = as_rgb(color_as_int(draw_data.inactive_bg))
        screen.draw(draw_data.sep)
    screen.cursor.bg = 0
    return end


def currently_playing() -> str:
    """Get the currently playing media information."""
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

        status += f" {metadata.get('xesam:title', '')} "

    except Exception:
        status = ""

    return status


def _draw_right_status(screen: Screen, is_last: bool) -> int:
    """Draw the right status."""
    if not is_last:
        return screen.cursor.x

    current_time = datetime.datetime.now().strftime(" %I:%M %p ")
    song_info = currently_playing()

    right_status_items = [song_info, current_time]
    right_status_length = calc_draw_spaces(*right_status_items)

    draw_spaces = screen.columns - screen.cursor.x - right_status_length
    if draw_spaces > 0:
        screen.draw(" " * draw_spaces)

    cells = [
        (Color(6, 7, 9), Color(148, 226, 213), song_info),
        (Color(69, 71, 90), Color(180, 190, 254), current_time),
    ]

    for fg_color, bg_color, status in cells:
        screen.cursor.bg = as_rgb(color_as_int(bg_color))
        screen.cursor.fg = as_rgb(color_as_int(fg_color))
        screen.draw(status)
    screen.cursor.bg = 0

    if screen.columns - screen.cursor.x > right_status_length:
        screen.cursor.x = screen.columns - right_status_length

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
    """Draw a tab with left and right status."""
    _draw_icon(screen, index)
    _draw_left_status(
        draw_data,
        screen,
        tab,
        before,
        max_title_length,
        index,
        is_last,
        extra_data,
    )
    end = screen.cursor.x

    _draw_right_status(screen, is_last)
    return end


def _redraw_tab_bar():
    """Redraw the tab bar."""
    tm = get_boss().active_tab_manager
    if tm is not None:
        tm.mark_tab_bar_dirty()
