import kagglehub

# Download latest version
path = kagglehub.competition_download('home-data-for-ml-course')

print("Path to competition files:", path)