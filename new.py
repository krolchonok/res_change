import dearpygui.dearpygui as dpg
import sys

dpg.create_context()


class ScreenRes(object):
    @classmethod
    def set(cls, width=None, height=None, freqs=60, depth=32):
        if width and height:
            print(
                "Setting resolution to {}x{} {}hz".format(width, height, freqs, depth)
            )
        else:
            print("Setting resolution to defaults")

        if sys.platform == "win32":
            cls._win32_set(width, height, freqs, depth)

    @staticmethod
    def _win32_set(width=None, height=None, freqs=60, depth=32):
        import win32api

        if width and height and freqs:

            if not depth:
                depth = 32
            if not freqs:
                freqs = 60

            mode = win32api.EnumDisplaySettings()
            mode.PelsWidth = width
            mode.PelsHeight = height
            mode.BitsPerPel = depth
            mode.DisplayFrequency = freqs

            win32api.ChangeDisplaySettings(mode, 0)
        else:
            win32api.ChangeDisplaySettings(None, 0)


def fullscreen():
    ScreenRes.set(2560, 1440, 165)


def gamescreen():
    ScreenRes.set(1920, 1440, 165)


def mouse_drag_callback(_, app_data):
    _, drag_delta_x, drag_delta_y = app_data
    viewport_pos_x, viewport_pos_y = dpg.get_viewport_pos()
    new_pos_x = viewport_pos_x + drag_delta_x
    new_pos_y = max(viewport_pos_y + drag_delta_y, 0)
    dpg.set_viewport_pos([new_pos_x, new_pos_y])


with dpg.handler_registry():
    dpg.add_mouse_drag_handler(button=0, threshold=0, callback=mouse_drag_callback)

with dpg.window() as primary_window:
    dpg.set_global_font_scale(1.5)
    dpg.add_button(label="Full", callback=lambda: fullscreen())
    dpg.add_button(label="Gamming", callback=lambda: gamescreen())
    with dpg.menu_bar():
        dpg.add_text("res_changer")
        dpg.add_spacer(width=40)
        dpg.add_button(label="x", callback=lambda: dpg.destroy_context())

dpg.set_primary_window(primary_window, True)
dpg.create_viewport(width=200, height=100, decorated=False)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
