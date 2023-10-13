# Get-Meesho-Product-Details

**Installating**

1. Install Python, add to PATH.
2. Clone this repository.
3. Run 'setup.bat'. (This will install 'selenium' and 'requests')

**How to use?**

1. Edit 'links.txt'. Simply put all the links of products on meesho that you want details of.
2. Run 'run.bat'. (This will run 'main.py' inside your default terminal application)

**What does it do?**

1. This opens Microsoft Edge (not Headless).
2. Gets all the details.
3. Clicks on every preview image and downloads the large version of it.
4. Saves everything in the products directory. For each product it uses the links to generate directory names (takes the part of the url after meesho.com and replaces forward slashes ( / ) with underscores ( \_ )).\
(Already downloaded products are automatically skipped)

**Direcroty Structure:**

    products
        product_name
            images
                image_0.webp
                image_1.webp
                image_2.webp
                image_n.webp
            details.txt

**Format of the details.txt:**

    ID: {name of the product generated form the url}
    Link: {Link of the product}
    Title: {Name of the product}
    Price: {Price in Rupees}
    Sizes:
    {All the available sizes}
    Description: 
    {description of the product}
**Images:**           
![Windows Terminal](<example images/image_2.png>)
![Microsoft Edge](<example images/image_0.png>)
![Directory Structure](<example images/image_1.png>)