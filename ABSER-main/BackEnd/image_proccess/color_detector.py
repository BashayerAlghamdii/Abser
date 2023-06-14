
import webcolors
import colorgram as cg

# Function to find the Closest Color for the passed RGB Value


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():  # All the Defined Color Names
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        # Euclidian Distance Formula for finding the Closest Colors in the List
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]  # Returning the Closest Color


def get_colour_name(requested_colour):
    try:
        # Checking if the RGB Value is exactly of a predefined color
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


def color_detector(img):
    img = cg.extract(img, 256)
    colors = []
    for color in img:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        colors.append(get_colour_name((r, g, b))[1])
    return colors

# Python code for Multiple Color Detection


