
"""
import fast_colorthief

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])
    
    
def rgb_to_hsl(rgb):
    r, g, b = rgb[0] / 255, rgb[1] / 255, rgb[2] / 255
    max_color = max(r, g, b)
    min_color = min(r, g, b)
    delta = max_color - min_color
    lightness = (max_color + min_color) / 2
    saturation = delta / (1 - abs(2 * lightness - 1)) if delta != 0 else 0
    hue = (max_color - r) / delta if delta != 0 else 0
    return hue, saturation, lightness

def extractColors(image):
    
    image_path = image

    dominant_color = rgb_to_hex(fast_colorthief.get_dominant_color(image_path, 1))

    #print(dominant_color)
    color_palette = fast_colorthief.get_palette(image_path)

    #print(color_palette)

    # Convert RGB to HSL and sort by lightness
    hsl_palette = sorted([(rgb_to_hsl(rgb), rgb) for rgb in color_palette], key=lambda x: x[0][2])

    # Select dark color for progressOut
    progressOut_color = hsl_palette[0][1]

    progressIn_color = hsl_palette[-1][1]
    # Select light dominant color for progressIn
    #progressIn_color = max(hsl_palette, key=lambda x: x[0][1])[1]
    
    colors = {"darkest_color": progressOut_color , "lightest_color" : progressIn_color , "dominant_color" : dominant_color}

    return(colors)
"""