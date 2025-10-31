# 🎨 Cartoonify Image using OpenCV

This project applies a **cartoon effect** to any image (especially portraits) using **OpenCV** and **NumPy**.  
It combines **bilateral filtering**, **edge detection**, and **adaptive thresholding** to create smooth color regions and bold black outlines — just like a hand-drawn cartoon.

---

## 🚀 Features

- Converts any image into a **cartoon-style** version  
- Uses **bilateral filtering** for smooth color areas  
- Detects **edges** with adaptive thresholding  
- Fully customizable with parameters (smoothing, thresholds, etc.)  
- Ideal for portraits and fun photo filters  

---

## 🧠 How It Works

1. **Color Smoothing (Cartoon Colors)**  
   - Applies multiple **bilateral filters** to reduce noise while preserving edges.
   - Produces flat color regions like cartoon shading.

2. **Edge Detection (Bold Lines)**  
   - Converts the image to grayscale.  
   - Applies **median blur** to remove texture noise.  
   - Uses **adaptive thresholding** to highlight edges (black lines).

3. **Combining Both Layers**  
   - Combines the **smoothed color image** with the **edge mask** using `cv2.bitwise_and()`.

---

## 📂 Project Structure

