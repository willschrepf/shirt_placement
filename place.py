from PIL import Image

# method 1, assuming we hardcode the shirt text onto the printful image:

# assuming that pixels per inch of 300; may be 72 or another number when you run it yourself
# https://www.adobe.com/uk/creativecloud/photography/discover/pixels-per-inch-ppi-resolution.html
pixels_per_sq_in = 300

def resize_image(input_path, output_path, target_width=(12 * pixels_per_sq_in), target_height=(16 * pixels_per_sq_in)):
    img = Image.open(input_path)
    
    # resize the image to the target dimensions
    img = img.resize((target_width, target_height), Image.ANTIALIAS)
    
    img.save(output_path, "PNG")

# sample use

input_image_name = "death1"
input_image_path = f"input_img/{input_image_name}.png"  # Replace with the path to your input image
resize_image(input_image_path, f"output_img/{input_image_name}_output.png")

# method 2, assuming we just want to generate the whole image to be placed on a blank shirt

def overlay_images(overlay_path, output_path):
    background = Image.open("input_img/default_bg.png")
    overlay = Image.open(overlay_path)
    
    overlay = overlay.resize(((12 * pixels_per_sq_in), (16 * pixels_per_sq_in)), Image.ANTIALIAS)

    # put in center
    position = (
        (background.width - overlay.width) // 2,
        (background.height - overlay.height) // 2
    )

    background.paste(overlay, position, overlay)

    background.save(output_path)

overlay_image_name = "death1"
overlay_image_path = f"input_img/{overlay_image_name}.png"  

overlay_images(overlay_image_path, f"output_img/{overlay_image_name}_output_overlaid.png")

