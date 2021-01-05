# PDF Script
The python script can encrypt a single,multiple files. 
Merge multiple files together and encrypt the merged file as well.
Convert image(s) to PDF as well along with encryption if wanted.

What the program does? 

- Merging creates a new PDF with all PDF files
- Encrypts the file with password provided
- Can convert IMAGE to PDF and can also merge with PDF files
- Conversion of Single IMAGE to PDF and Multiple IMAGES to Multiple PDF file


### Requirements
Python3
> pip install -r requirements.txt

### Usage
```
 pdf.py [-h] [-f FILEPATH] [-a FILEPATHS [FILEPATHS ...]] [-e PASSWORD]
              [-m MERGE [MERGE ...]] [-i IMAGE [IMAGE ...]]
              [-s SEPRATEIMAGE [SEPRATEIMAGE ...]]

MERGE, ENCRYPT PDF FILES. CONVERT IMAGES TO PDF,ENCRYPT THEM

optional arguments:
  -h, --help            show this help message and exit
  -f FILEPATH           Path For Single PDF
  -a FILEPATHS [FILEPATHS ...]
                        Paths For Multiple PDF
  -e PASSWORD           Password To Encrypt The PDF
  -m MERGE [MERGE ...]  Merge Multiple PDF File
  -i IMAGE [IMAGE ...]  Convert Multiple Images To One PDF File
  -s SEPRATEIMAGE [SEPRATEIMAGE ...]
                        Convert Multiple Images To Separate PDF File

```

### Contribution

Any kind of contributions are welcome.

1. Fork the Project
2. Commit your Changes
3. Open a Pull Request


