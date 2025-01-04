from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from bs4 import BeautifulSoup
import os
import textwrap

# Function to extract text from HTML file
def extract_recipe_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract hRecipe components
    recipe_name = soup.find(class_='fn').text if soup.find(class_='fn') else "Recipe"
    ingredients = [ing.text for ing in soup.find_all(class_='ingredient')]
    
    # Extract instructions by separating paragraphs inside the 'instructions' class
    instructions = [step.get_text() for step in soup.find_all('span', class_='instructions') if step.get_text()]
    # Further split the instructions into individual steps based on paragraph tags <p>
    if instructions:
        instructions = instructions[0].split('\n')
    
    return recipe_name, ingredients, instructions

# Function to wrap text based on a specified width
def wrap_text(text, width):
    return textwrap.fill(text, width)

# Function to create PDF using reportlab
def create_pdf(recipe_name, ingredients, instructions, output_file):
    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter
    
    # Add title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 100, recipe_name)
    
    # Add Ingredients
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, height - 130, "Ingredients:")
    c.setFont("Helvetica", 12)
    y_position = height - 150
    for ingredient in ingredients:
        c.drawString(120, y_position, f"- {ingredient}")
        y_position -= 15
    
    # Add Instructions
    c.setFont("Helvetica-Bold", 12)
    y_position -= 10
    c.drawString(100, y_position, "Instructions:")
    c.setFont("Helvetica", 12)
    y_position -= 20
    
    step_number = 1
    for step in instructions:
        # Wrap the text for instructions
        wrapped_text = wrap_text(step.strip(), 80)  # 80 characters per line
        first_line = True
        for line in wrapped_text.split('\n'):
            if y_position < 50:  # Add a new page if needed
                c.showPage()
                c.setFont("Helvetica", 12)
                y_position = height - 100
            
            if first_line:
                c.drawString(120, y_position, f"{step_number}. {line}")
                first_line = False
            else:
                c.drawString(140, y_position, line)  # Indent further for wrapped lines
            y_position -= 15
        step_number += 1
        y_position -= 10  # Extra space between steps
    
    # Save PDF
    c.save()

# Define source and destination directories
source_dir = r'path/to/source/directory'  # Replace with the directory containing your HTML recipe files
dest_dir = r'path/to/destination/directory'  # Replace with the directory where PDFs will be saved

# Create destination directory if it doesn't exist
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

# Process each HTML file in the source directory
for file_name in os.listdir(source_dir):
    if file_name.endswith('.html'):
        input_file_path = os.path.join(source_dir, file_name)
        output_file_path = os.path.join(dest_dir, file_name.replace('.html', '.pdf'))
        
        # Read HTML content
        with open(input_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        
        # Extract recipe data
        recipe_name, ingredients, instructions = extract_recipe_data(html_content)
        
        # Create PDF
        create_pdf(recipe_name, ingredients, instructions, output_file_path)

print(f"All HTML files have been converted to PDF and stored in {dest_dir}.")
