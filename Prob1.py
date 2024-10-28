from pgl import *


# 1a: Create histogram array
def create_histogram_array(data: list[int]) -> list[int]:
    histogram = [0] * 10  
    for value in data:
        histogram[value] += 1  
    return histogram

# 1b: Print the histogram with asterisks
def print_histogram(hist: list[int]) -> None:
    for index, count in enumerate(hist):
        print(f"{index}: {'*' * count}")

# 1c: Graph the histogram using PGL
def graph_histogram(hist: list[int], width: int, height: int) -> None:
    gw = GWindow(width, height)  
    
    # Calculate width of each bar and scaling factor for height
    num_bars = len(hist)
    bar_width = width // num_bars
    max_count = max(hist)
    scaling_factor = height / max_count if max_count > 0 else 0
    
    # Helper function to draw rectangles
    def my_rect(x, y, w, h, color):
        rect = GRect(x, y, w, h)
        rect.set_filled(True)
        rect.set_color(color)
        gw.add(rect)
    
    # Draw each bar in the histogram
    for i, count in enumerate(hist):
        bar_height = count * scaling_factor
        my_rect(i * bar_width, height - bar_height, bar_width - 2, bar_height, "red")

# Some testing printouts for your use!
PI_DIGITS = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 5, 8, 9, 7, 9]
hist = create_histogram_array(PI_DIGITS)
print("Histogram array:", hist)
print_histogram(hist)            # Uncomment to test printing
graph_histogram(hist, 400, 400)  # Uncomment to display graphical histogram
