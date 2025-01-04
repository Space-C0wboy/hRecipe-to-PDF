# hRecipe HTML to PDF Converter

A Python script that converts HTML files formatted with hRecipe microformats into PDF documents. It extracts recipe details such as the name, ingredients, and instructions to create professional and printable PDFs.

## Features

- Extracts recipe name, ingredients, and instructions from hRecipe HTML files.
- Automatically generates a PDF for each recipe.
- Supports multi-page PDFs for long recipes.
- Wraps text for better readability in the PDF.
- Processes all `.html` files in a specified directory.

## Requirements

- Python 3.6+
- Install required dependencies with:
  ```bash
  pip install -r requirements.txt
  ```

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Install dependencies:
   ```bash
   pip install beautifulsoup4 reportlab
   ```

## Usage

1. Place your HTML recipe files in the source directory.
2. Update the script with the correct paths for `source_dir` and `dest_dir`:
   ```python
   source_dir = r'G:\My Drive\Recipies\recipes-for-user-2867020'
   dest_dir = r'G:\My Drive\Recipies\Converted-to-pdf'
   ```

3. Run the script:
   ```bash
   python converter.py
   ```

4. Find the generated PDFs in the destination directory.

## Example

**Input (HTML):**
```html
<div class="fn">Chocolate Chip Cookies</div>
<ul>
  <li class="ingredient">2 cups flour</li>
  <li class="ingredient">1 cup sugar</li>
  <li class="ingredient">1 cup chocolate chips</li>
</ul>
<span class="instructions">
  Mix ingredients.  
  Bake at 350°F for 15 minutes.
</span>
```

**Output (PDF):**
```
Chocolate Chip Cookies

Ingredients:
- 2 cups flour
- 1 cup sugar
- 1 cup chocolate chips

Instructions:
1. Mix ingredients.
2. Bake at 350°F for 15 minutes.
```

## Folder Structure

- **Source Directory:** Contains `.html` files formatted with hRecipe microformats.
- **Destination Directory:** Stores the generated `.pdf` files.

## Known Limitations

- Assumes the HTML structure follows the hRecipe microformat (e.g., `fn`, `ingredient`, `instructions` classes).
- Instructions are expected to be in `<span>` tags with the `instructions` class.
- No validation for malformed HTML files.

## Contributing

If you’d like to contribute:
1. Fork this repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have suggestions, feel free to open an issue in the repository.
