import PyPDF2
import os
from datetime import datetime

now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def merge_pdfs(file1, file2, output_file):
    # Open the input PDF files
    with open(file1, 'rb') as file1_obj, open(file2, 'rb') as file2_obj:
        # Create PDF reader objects for each file
        file1_reader = PyPDF2.PdfReader(file1_obj)
        file2_reader = PyPDF2.PdfReader(file2_obj)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Iterate over each page in the first file
        for page_num in range(len(file1_reader.pages)):
            # Get the page from the first file
            page = file1_reader.pages[page_num]
            overlay_page = file2_reader.pages[page_num]
         
            # Merge the two pages by overlaying the second page on top of the first
            page.merge_page(overlay_page)

            # Add the merged page to the PDF writer
            pdf_writer.add_page(page)

        # Write the merged PDF to the output file+
        with open(output_file, 'wb') as output:
            pdf_writer.write(output)

    print("")
    print("")
    print(color.BOLD + f'The PDF files have been merged into ' + color.RED + color.UNDERLINE + f'{output_file}'+ color.END + color.BOLD + "+ successfully." + color.END)
    print("")
    print("")


print("")
print("""
 ___  _ __ ___  ___  _    ___  _                  
| . || / // __>| __>| |  / __>|/                  
|   ||  \ \__ \| _> | |_ \__ \                    
|_|_||_\_\<___/|___>|___|<___/              
 __ __  ___  ___   _  ___   ___  ___  ___         
|  \  \| . |/  _> | ||  _> | . \| . \| __>        
|     ||   || <_/\| || <__ |  _/| | || _>         
|_|_|_||_|_|`____/|_|`___/ |_|  |___/|_|          
 ___  ___  __ __  ___  _  _ _  ___  ___  ___  ___ 
|  _>| . ||  \  \| . >| || \ || . ||_ _|| . || . \\
| <__| | ||     || . \| ||   ||   | | | | | ||   /
`___/`___'|_|_|_||___/|_||_\_||_|_| |_| `___'|_\_\                                                
""")
print("")
backgroundFile = input(f'Drop the {color.BLUE}background{color.END} file into the terminal and press ENTER\n')
print(" ")
contentFile = input(f'Drop the {color.BLUE}content{color.END} file into the terminal and press ENTER\n')
backgroundFile = backgroundFile.replace('\\ ', ' ').strip()
contentFile = contentFile.replace('\\ ', ' ').strip()

# Example usage
merge_pdfs(backgroundFile, contentFile, os.getcwd()+'/combined'+dt_string+'.pdf')