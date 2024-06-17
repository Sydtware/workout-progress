import matplotlib.pyplot as plt

# Weeks
weeks = list(range(1, 13))

# Example Data
lat_pulldown_weights = [70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
bench_press_weights = [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
cardio_performance = [2, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1]  # Distances in miles
session_ratings = [4, 5, 4, 5, 5, 4, 4, 5, 4, 5, 5, 5]

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Lat Pulldown Progression
axs[0, 0].plot(weeks, lat_pulldown_weights, marker='o', linestyle='-', color='b', label='Lat Pulldown')
axs[0, 0].set_title('Lat Pulldown Progression (March - June)')
axs[0, 0].set_xlabel('Weeks')
axs[0, 0].set_ylabel('Weight (lb)')
axs[0, 0].legend()
axs[0, 0].grid(True)

# Bench Press Progression
axs[0, 1].plot(weeks, bench_press_weights, marker='o', linestyle='-', color='r', label='Bench Press')
axs[0, 1].set_title('Bench Press Progression (March - June)')
axs[0, 1].set_xlabel('Weeks')
axs[0, 1].set_ylabel('Weight (lb)')
axs[0, 1].legend()
axs[0, 1].grid(True)

# Cardio Performance
axs[1, 0].plot(weeks, cardio_performance, marker='o', linestyle='-', color='g', label='Cardio Distance')
axs[1, 0].set_title('Cardio Performance (March - June)')
axs[1, 0].set_xlabel('Weeks')
axs[1, 0].set_ylabel('Distance (miles)')
axs[1, 0].legend()
axs[1, 0].grid(True)

# Session Ratings
axs[1, 1].plot(weeks, session_ratings, marker='o', linestyle='-', color='purple', label='Session Ratings')
axs[1, 1].set_title('Session Ratings (March - June)')
axs[1, 1].set_xlabel('Weeks')
axs[1, 1].set_ylabel('Rating')
axs[1, 1].legend()
axs[1, 1].grid(True)

plt.tight_layout()
plt.show()
