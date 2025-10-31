import cv2
import numpy as np
import sys

def cartoonify_image(image_path, num_bilateral=7, sigma_color=250, sigma_space=250, median_blur_ksize=7, adaptive_thresh_ksize=9, adaptive_thresh_c=2):
    """
    Applies a cartoon effect to an image, ideal for portraits due to bilateral filtering.

    :param image_path: Path to the input image.
    :param num_bilateral: Number of times to apply the bilateral filter. (Increased for smoother results)
    :param sigma_color: Filter sigma in the color space. (Increased for flatter skin tones)
    :param sigma_space: Filter sigma in the coordinate space. (Increased for preserving large structures)
    :param median_blur_ksize: Kernel size for median blur (must be odd). (Increased for better noise reduction)
    :param adaptive_thresh_ksize: Block size for adaptive thresholding (must be odd).
    :param adaptive_thresh_c: Constant subtracted from the mean or weighted mean.
    :return: The cartoonified image.
    """
    # 1. Read the image
    img_rgb = cv2.imread(image_path)
    if img_rgb is None:
        print(f"Error: Could not read image at {image_path}")
        sys.exit()

    # --- Step 1: Color Quantization/Smoothing (for cartoon 'flat' colors) ---
    # Bilateral filter is applied multiple times to achieve strong smoothing while preserving facial features.
    
    img_color = img_rgb
    for _ in range(num_bilateral):
        # The 'd' parameter (9) is the diameter of the pixel neighborhood
        img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=sigma_color, sigmaSpace=sigma_space)

    # --- Step 2: Edge Detection (for bold outlines) ---

    # Convert to grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # Apply median blur to reduce noise (like skin texture) before edge detection
    img_blur = cv2.medianBlur(img_gray, median_blur_ksize)
    
    # Adaptive thresholding to create a binary edge mask (black lines on white)
    img_edge = cv2.adaptiveThreshold(
        img_blur, 
        255, 
        cv2.ADAPTIVE_THRESH_MEAN_C, 
        cv2.THRESH_BINARY, 
        blockSize=adaptive_thresh_ksize, 
        C=adaptive_thresh_c
    )
    
    # Convert the edge mask back to color (BGR)
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2BGR)

    # --- Step 3: Combine Color and Edges ---
    # Overlay the black edge lines onto the smoothed color image.
    cartoon_image = cv2.bitwise_and(img_color, img_edge)

    return cartoon_image

# -------------------------------------------------------------------------
# --- Main Execution ---
if __name__ == "__main__":
    
# cartoonify_image.py (around line 63)

# cartoonify_image.py (around line 65)

    # 🎨 Set the path to your portrait image
    input_file = "IMAGE_FILE/portrait.jpg"  # <--- Change this line!
    
    # 💾 Set the name for the output cartoon image
    output_file = "cartoonified_portrait.jpg" 
    
    # The default parameters passed to the function are already optimized for a smooth, high-contrast portrait
    # You can customize the effect by passing different arguments here:
    cartoon = cartoonify_image(
        input_file,
        num_bilateral=8,         # More smoothing passes for flawless skin
        sigma_color=300,         # High color smoothing
        sigma_space=300,         # High spatial smoothing
        median_blur_ksize=7,     # Better noise reduction before edge detection
        adaptive_thresh_ksize=9, # Block size for clear edges
        adaptive_thresh_c=2      # Offset for threshold
    )

    if cartoon is not None:
        # Save the output image
        cv2.imwrite(output_file, cartoon)
        
        # Display the output image
        cv2.imshow("Original Image", cv2.imread(input_file))
        cv2.imshow("Cartoonified Portrait", cartoon)
        
        # Wait for a key press and close windows
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print(f"Success! Cartoonified image saved as: {output_file}")
    else:
        print("Cartoonification failed.")