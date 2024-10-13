# type: ignore

from manim import *


class ShiftingGrids(Scene):
    def construct(self):
        side_length = 0.7
        lshift = LEFT * (side_length + 0.1)
        rshift = RIGHT * (side_length + 0.1)
        tshift = UP * (side_length + 0.1)
        dshift = DOWN * (side_length + 0.1)

        # Create grid
        grid = VGroup()
        for _ in range(25):
            cell = Square(side_length=side_length, stroke_width=0.9)
            grid.add(cell)
        grid_cells = grid.family_members_with_points()

        grid.arrange_in_grid(buff=0.1)

        self.play(Write(grid))

        # Preset cell numbers for mines
        mines_indices = [6, 8, 12, 18]

        # Generate mines and move them to the preset numbers
        mines = VGroup()
        for mine in mines_indices:
            mine_circ = Circle(
                color=TEAL, fill_color=TEAL, fill_opacity=1, radius=0.25
            ).set_z_index(2)
            mine_circ.move_to(grid_cells[mine])
            mines.add(mine_circ)
        self.play(Write(mines))

        text = (
            MarkupText("Let's imagine the mines as <i>ones</i>")
            .scale(side_length)
            .to_edge(UP)
        )
        self.play(Write(text), run_time=1)
        self.wait(1)

        # Create replacement VGroup for mines
        mines.save_state()
        ones = VGroup()
        for mine in mines.family_members_with_points():
            one = Integer(1, font_size=36, stroke_width=2)
            one.move_to(mine)
            ones.add(one)

        self.play(ReplacementTransform(mines, ones))
        self.play(Unwrite(text), run_time=1)

        # Create the shifted grids
        grid_copy_t = VGroup(grid.copy().set_stroke(color=TEAL), ones.copy())
        grid_copy_b = VGroup(grid.copy().set_stroke(color=RED), ones.copy())

        text = (
            MarkupText("Now if we shift our grid up by one")
            .scale(side_length)
            .to_edge(UP)
        )
        self.play(Write(text), run_time=1)
        self.play(grid_copy_t.animate.shift(tshift, RIGHT * 4.5))

        text2 = MarkupText("and once down..").scale(side_length).to_edge(DOWN)
        self.play(Write(text2), run_time=1)
        self.play(grid_copy_b.animate.shift(dshift, LEFT * 4.5))
        self.wait(1)
        self.play(Unwrite(text), Unwrite(text2), run_time=1)

        text = (
            MarkupText("We can actually add these matrices by cell")
            .scale(side_length)
            .to_edge(UP)
        )
        self.play(Write(text), run_time=1)

        self.wait(1)

        # Merge back the grids
        self.play(
            grid_copy_t.animate.shift(LEFT * 4.5),
            grid_copy_b.animate.shift(RIGHT * 4.5),
        )
        self.wait(1)

        vert_grid = grid.copy().set_stroke(color=BLUE)

        # Hard-code values
        ones2 = VGroup()
        ones_cells = [
            0,
            1,
            0,
            1,
            0,
            0,
            1,
            1,
            1,
            0,
            0,
            1,
            1,
            1,
            0,
            0,
            0,
            1,
            2,
            0,
            0,
            0,
            0,
            1,
            0,
        ]

        # Generate the matching number grid
        for i, v in enumerate(ones_cells):
            if v == 0:
                continue
            one = Integer(v, font_size=36, stroke_width=2)
            one.move_to(grid_cells[i])
            ones2.add(one)

        # Replace the grids seamlessly
        self.play(
            ReplacementTransform(grid, vert_grid),
            FadeIn(ones2),
            FadeOut(
                ones,
                grid_copy_t,
                grid_copy_b,
            ),
        )
        text2 = (
            MarkupText(
                "giving us tiles that represent the\nnumber of mines around them <i>vertically</i>",
                should_center=True,
            )
            .scale(side_length)
            .to_edge(DOWN)
        )
        self.play(Write(text2), run_time=1)

        self.wait(1)
        self.play(Unwrite(text2), run_time=1)

        text2 = (
            MarkupText(
                "The same is true for shifting the original grid horizontally.",
                should_center=True,
            )
            .scale(side_length)
            .to_edge(DOWN)
        )
        self.play(Write(text2), run_time=1)

        # We reuse variables for left and right shifts
        grid_copy_b.center()
        grid_copy_t.center()

        self.play(grid_copy_b.animate.shift(rshift))
        self.play(grid_copy_t.animate.shift(lshift))

        self.wait(1)

        ones_cells = [
            0,
            1,
            0,
            1,
            0,
            1,
            1,
            3,
            1,
            1,
            0,
            2,
            1,
            2,
            0,
            0,
            0,
            2,
            1,
            1,
            0,
            0,
            0,
            1,
            0,
        ]

        ones = VGroup()
        for i, v in enumerate(ones_cells):
            if v == 0:
                continue
            one = Integer(v, font_size=36, stroke_width=2)
            one.move_to(grid_cells[i])
            ones.add(one)

        self.play(
            FadeOut(ones2),
            FadeIn(ones),
            FadeOut(grid_copy_b, grid_copy_t),
        )

        self.play(Unwrite(text), Unwrite(text2), run_time=1)
        self.wait(1)

        text = MarkupText("And lastly, diagonally.").scale(side_length).to_edge(UP)
        self.play(Write(text), run_time=1)
        self.wait(1)

        # We reuse variables for diagonal shifts
        grid_copy_b.center()
        grid_copy_t.center()
        grid_copy_lt = VGroup(grid.copy().set_stroke(color=ORANGE), ones.copy())
        grid_copy_rt = VGroup(grid.copy().set_stroke(color=PURPLE), ones.copy())

        self.play(grid_copy_b.animate.shift(lshift, dshift))
        self.play(grid_copy_t.animate.shift(rshift, dshift))
        self.play(grid_copy_lt.animate.shift(lshift, tshift))
        self.play(grid_copy_rt.animate.shift(rshift, tshift))

        ones_cells = [
            1,
            1,
            2,
            1,
            1,
            1,
            1,
            3,
            1,
            1,
            1,
            2,
            1,
            3,
            2,
            0,
            1,
            2,
            1,
            1,
            0,
            0,
            1,
            1,
            1,
        ]
        ones2 = VGroup()
        # Generate the matching number grid
        for i, v in enumerate(ones_cells):
            if v == 0 or i in mines_indices:
                continue
            one = Integer(v, font_size=36, stroke_width=2)
            one.move_to(grid_cells[i])
            ones2.add(one)

        text2 = (
            MarkupText(
                "Let's place the mines back for visual clarity.",
                should_center=True,
            )
            .scale(side_length)
            .to_edge(DOWN)
        )
        self.play(Write(text2), run_time=1)
        self.wait(1)

        self.play(Restore(mines))
        self.wait(1)

        self.play(
            FadeIn(ones2),
            FadeOut(ones),
            FadeOut(grid_copy_b, grid_copy_t, grid_copy_rt, grid_copy_lt),
        )

        self.wait(1)
        self.play(Unwrite(text), Unwrite(text2), run_time=1)

        text2 = (
            MarkupText(
                "Here's our completed Minesweeper board!",
                should_center=True,
            )
            .scale(side_length)
            .to_edge(DOWN)
        )
        self.play(Write(text2), run_time=1)

        self.play(Indicate(vert_grid, color=GREEN, scale_factor=1.05))
        self.wait(1)
