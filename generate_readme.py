import os

def generate_readme():
    # Configuration
    audio_extension = '.ogg'
    # Name of your single universal icon file (must be in the same folder or provide path)
    universal_icon = 'heir-sys-icon.jpg' 
    
    readme_content = "# Audio Files\n\n| Preview | File Name |\n| :---: | :--- |\n"
    
    found_files = False
    
    # Check if the universal icon exists first
    if not os.path.exists(universal_icon):
        print(f"Warning: {universal_icon} not found! Using emoji fallback.")
        universal_icon = "🎵" # Fallback to emoji if image is missing
        is_image = False
    else:
        is_image = True

    for file in os.listdir('.'):
        if file.endswith(audio_extension):
            found_files = True
            
            if is_image:
                # Use the single image for every file
                readme_content += f"| <img src='{universal_icon}' width='64'> | [{file}]({file}) |\n"
            else:
                # Fallback text
                readme_content += f"| 🎵 | [{file}]({file}) |\n"

    if not found_files:
        readme_content = "# No audio files found in this directory."

    with open('README.md', 'w') as f:
        f.write(readme_content)

if __name__ == "__main__":
    generate_readme()   
