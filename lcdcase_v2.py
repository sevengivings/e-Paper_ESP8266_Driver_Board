from solid import *
from solid.utils import *

# Dimensions in mm
outer_dimensions = [84, 58, 8]  # Length, width, height
wall_thickness = 3  # Reduced to save material
lcd_cover_thickness = 2
lcd_viewing_area_top_left = [17, 10]
lcd_viewing_area_bottom_right = [74, 48]
corner_radius = 2  # Small rounding for edges

# Create the outer box with rounded corners
def create_case():
    outer_box = rounded_cube(outer_dimensions, corner_radius)

    # Subtract the inner box to create the hollow structure
    inner_dimensions = [
        outer_dimensions[0] - 2 * wall_thickness,
        outer_dimensions[1] - 2 * wall_thickness,
        outer_dimensions[2]
    ]

    inner_box = translate([wall_thickness, wall_thickness, 0])(rounded_cube(inner_dimensions, corner_radius))
    hollow_case = outer_box - inner_box

    # Create the LCD cover part (2mm thick)
    lcd_cover = cube([
        outer_dimensions[0],
        outer_dimensions[1],
        lcd_cover_thickness
    ], center=False)

    # Add the viewing area cutout
    lcd_viewing_area = translate([
        lcd_viewing_area_top_left[0],
        lcd_viewing_area_top_left[1],
        0
    ])(cube([
        lcd_viewing_area_bottom_right[0] - lcd_viewing_area_top_left[0],
        lcd_viewing_area_bottom_right[1] - lcd_viewing_area_top_left[1],
        lcd_cover_thickness
    ], center=False))

    lcd_cover_with_cutout = lcd_cover - lcd_viewing_area

    # Combine the hollow case and the LCD cover
    final_case = hollow_case + translate([0, 0, outer_dimensions[2] - lcd_cover_thickness])(lcd_cover_with_cutout)

    return final_case

# Rounded cube function
def rounded_cube(size, radius):
    return minkowski()(cube(size), sphere(radius))

# Generate the 3D model
case_model = create_case()

# Save the model to an STL file
scad_render_to_file(case_model, 'rectangular_case.scad')