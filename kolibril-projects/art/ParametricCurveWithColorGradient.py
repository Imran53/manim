from manim import *

class DrawScene(Scene):
    def construct(self):
        dot = Dot()

        def func(t):
            return np.array((np.sin(2 * t), np.sin(3 * t), 0))

        func = ParametricFunction(func, t_max=TAU, fill_opacity=0)
        func.scale(2)

        # This Class return a VGroup of pieces of the path
        new_func = CurvesAsSubmobjects(func)
        new_func.set_color_by_gradient(BLUE,RED)
        # It is more efficient to use this method in this case.
        dot.add_updater(lambda m: m.move_to(func.get_end()))

        # What we are doing is creating a new path,
        # and the original make it transparent,
        # so that from the illusion that the original is being drawn.
        func.fade(1)
        self.add(dot)

        self.play(
            ShowCreation(new_func),
            ShowCreation(func),
            run_time=5
        )
        self.wait()

import os ; import sys
from pathlib import Path
if __name__ == "__main__":
    project_path = Path(sys.path[1]).parent
    script_name = f"{Path(__file__).resolve()}"
    os.system(f"manim  -l --custom_folders  --disable_caching -s -p -c 'BLACK' --config_file '{project_path}/manim_settings.cfg' " + script_name)