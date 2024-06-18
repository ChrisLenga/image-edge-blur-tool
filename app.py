import os
from PIL import Image, ImageFilter

# Edit the values in Line #5 (below) to your desired look
def apply_edge_blur(image_path, output_path, blur_radius=2, border_size=10):
    # Open an image file
    with Image.open(image_path) as img:
        # Check if the image has an alpha channel
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            # Separate the alpha channel
            alpha = img.getchannel('A')
        else:
            alpha = None

        # Apply a Gaussian Blur filter
        blurred_img = img.filter(ImageFilter.GaussianBlur(blur_radius))

        # Get dimensions of the original image
        width, height = img.size

        # Define the area for the center (unblurred)
        left = border_size
        top = border_size
        right = width - border_size
        bottom = height - border_size

        # Crop the unblurred center from the original image
        center = img.crop((left, top, right, bottom))

        # Paste the unblurred center back onto the blurred image
        blurred_img.paste(center, (left, top))

        # If there was an alpha channel, add it back into the image
        if alpha:
            blurred_img.putalpha(alpha)

        # Save the processed image to the output path
        blurred_img.save(output_path)

# Directory containing the input images
input_dir = 'input'
# Directory where output images will be saved
output_dir = 'output'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process each image in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
        image_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        apply_edge_blur(image_path, output_path)  # Using default blur settings
        print(f"Processed {filename}")
