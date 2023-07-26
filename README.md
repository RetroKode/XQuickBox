
#  XQuickBox (Pre-Alpha)

The savior project to **create web sites with native Python** code! Design static landings pages in minutes with **Python**. Use the prebuilt components to **generate common HTML objects** like "navs" with prefabricated structures or design them yourself to create the coolest things that cross your mind.

  

This is an OpenSource project **created with the purpose of facilitating the creation of "generic" websites** easily, quickly and 100% **from Python**. Let's forget about writing HTML.

  

For easier (and more indicated) use **install the Python package using pip** and read the **documentation**, unless you want to collaborate, which is always available!



# Quick started (use to developer and demostration)

To create an app with **XQuickBox**, it is, as the name suggests: ***QUICK***.

1. First, clone this repository.
	```bash
	git clone https://github.com/RetroKode/XQuickBox
	```

2. Build!:
Remember that **XQuickBox** is a **construction of children of children**, so keeping this in mind, instantiate your first app and build it!

	```python
	from XQuickBox.Main.HtmlComponents import * # Importas todos los componentes

	MyQuickWeb = Box(title='funny cats images') # "Box", for practical purposes, it is a web page. A secure and fast environment where you can run it, test it and create it.
	```
	If you read, **"Box"**, for practical purposes, **it is a web page**. A secure and fast environment where you can **run it**, **test it** and **create it**.

	Yes, **you already have an app**. Let's put an image and some titles to test (**let's remember that the limit is your creativity**).
	```python
	MyQuickWeb.content = [

		DivComponent(id='funnyCatsContainer',
		content=[

			TitleComponent(
				content=['See my cats (not are my cats really)']),
				
			ImgComponent(
				imageUrl='https://i.ytimg.com/vi/YSHDBB6id4A/maxresdefault.jpg', 
				altImage = 'a cute cat (with a hat)')

			])
	]

	MyQuickWeb.Generate()
	```
	What would be the result of this? This would be the equivalent of:
	```html
	<!DOCTYPE  html>
	<html  lang="en">
		<head>
		<meta  charset="UTF-8">
		<meta  name="viewport" content="width=device-width, initial-scale=1.0">
		<title>funny cats images</title>
	</head>
	<body  style="margin: 0;padding: 0;">

		<div  id="funnyCatsContainer">

			<h1>
				See my cats (not are my cats really)
			</h1>

			<img  alt="a cute cat (with a hat)" src="https://i.ytimg.com/vi/YSHDBB6id4A/maxresdefault.jpg" width="512px"/>

		</div>

	</body>
	</html>
	```
---
All this, **without having touched a single line of HTML**!

**This can be exploited** when we create the **template system**! It will be much more efficient to build websites from now on with this framework.

In addition to the features you see here, **great things are missing**, such as:
- Development server (to edit and see the changes reflected in real time) support.
- Functionality to export and deploy the web.
- Template system.
- CSS porting to native Python code.
- Documentation
- Other little things!


  

#  Instalation

Coming Soon

  
  

#  Documentation

Coming Soon