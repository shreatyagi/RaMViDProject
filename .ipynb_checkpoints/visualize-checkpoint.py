import numpy as np
import matplotlib.pyplot as plt
import math

# Load the NPZ file
data = np.load('/home/st888/project/ramvid/1x16x64x64x3-4.npz')

# Get the video data
video_data = data['arr_0']

# Print information about the video structure
print("Video data shape:", video_data.shape)
print(f"Number of frames: {video_data.shape[1]}")

# Calculate the optimal grid layout
# We'll create a square-ish grid that fits all frames
n_frames = video_data.shape[1]
grid_size = math.ceil(math.sqrt(n_frames))  # This gives us an n x n grid that will fit all frames

# Create a figure with subplots
# We'll make it larger to see the frames better
fig, axes = plt.subplots(grid_size, grid_size, figsize=(20, 20))
axes = axes.ravel()  # Convert the 2D array of axes into a 1D array for easier indexing

# Plot each frame
for i in range(n_frames):
    frame = video_data[0, i]  # Get frame i from the first video
    axes[i].imshow(frame)
    axes[i].set_title(f'Frame {i}')
    axes[i].axis('off')

# Turn off any empty subplots
for i in range(n_frames, grid_size * grid_size):
    axes[i].axis('off')
    axes[i].set_visible(False)

# Add a main title to the figure
plt.suptitle('All Frames from Video', fontsize=16, y=0.95)

# Adjust the layout
plt.tight_layout()

# Save the plot as a high-resolution PNG file
plt.savefig('all_video_frames.png', dpi=300, bbox_inches='tight')

# Display the plot if you're running this on a machine with a display
plt.show()

# Print some useful statistics about the video
print("\nVideo Statistics:")
print(f"Total number of frames: {n_frames}")
print(f"Frame resolution: {video_data.shape[3]}x{video_data.shape[2]} pixels")
print(f"Minimum pixel value: {video_data.min()}")
print(f"Maximum pixel value: {video_data.max()}")
print(f"Mean pixel intensity: {video_data.mean():.2f}")

print("\nVisualization has been saved as 'all_video_frames.png'")