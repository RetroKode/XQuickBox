# Librerías
from bs4 import BeautifulSoup
from flask import Flask


# La App principal. Equivale a un archivo HTML.
class Box:
    def __init__(self, id: str = None, className: str = None, styles: list = [{'margin': 0}, {'padding': 0}], title: str = 'My XQuickBox! - RetroKode', metaDescription: str = None, metaKeywords: list = [], webIcon: str = None, content: list = []): # Tag basic structure.
        """

            # Instance of a web!

            This class is a new web instance! It is the equivalent of creating an HTML file.

            :param id: HTML identifier. It is the value taken by the "id" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param className: It is the value taken by the "class" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param styles: List of dictionaries with css styles. This feature is under test and will possibly evolve to native Python support with own objects. For now, leave key-value values as they are in CSS. An example would be: ```{"display": "flex"}```

            :param title: Title of the page!
            
            :param metaDescription: The description of the web page. It is the value resulting from assigning the key "content" in the meta key tag "name" with value "desc".

            :param metaKeywords: Keywords of the web page. List of strings. It is the value resulting from assigning the key "content" in the meta key tag "name" with value "keywords".

            :param webIcon: represents the local path (inside your computer) or URL of your web icon.

            :param content: List containing all the children of this container. Here will go all the other components you want inside this container.
        
        """

        #! Metatags y otra info (los demás componentes no tendrán esto, solo la Box principal)!


        self.availableCommonTypes = (Box, DivComponent, TextComponent, NavComponent, FooterComponent, LinkComponent, ImgComponent, TitleComponent, SubtitleComponent, SmallTitleComponent, UnorderedListComponent, OrderedListComponent)
        self.availableHeadTypes = ()
    

        # TODO: Hacer uso de los metadatos.
        self.title = title
        self.metaDescription = metaDescription
        self.metaKeywords = metaKeywords
        self.webIcon = webIcon # Web icon.

        self.closeTagType = True # ¿La etiqueta tiene cierre?
        self.tagName = 'body'
        
        self.id = id # Id de la etiqueta. 
        self.className = className # clase de la etiqueta.
        self.styles = styles # Una lista que contendrá los estilos css. Avanzaré más con este concepto en el futuro.


        self.content = content # Siendo bastante figurativos, este "self.Content" representa las etiquetas HTML.




    def StylesParser(self, styles: list):
        """

            # Get CSS Styles form a list with python dicts.

            This function takes the styles passed in dictionary form and passes them to a string usable as a parameter for an HTML element.
        
        """

        stylesString = ''

        for property in styles:
            stylesString += f'{list(property.keys())[0]}: {list(property.values())[0]};'

        return stylesString

    def CodeParser(self, HtmlCode: str):
        """
        
            # Generate nice html code!

            :param HtmlCode: HTML code to be formatted.

        """


        soup = BeautifulSoup(HtmlCode, features="html.parser")
        formattedCode = soup.prettify()

        return formattedCode


    def RunTestMode(self, port: int = 8080):
        """
        
        # CREATES A REAL-TIME TEST SERVER

        :param port: Port on which your test site will run. The default is 8080. If the port is busy, it will be searched on port + 1.
        
        """

        app = Flask(self.title)

        web_content = self.Generate() # El contenido de la aplicación.

        @app.route('/')
        def main_app():
            return web_content
        


        
        app.run(port = port, debug = True)

        



    #! Si se hereda de Box no usar esta función, use el método Generate() de su propia función, hacerlo podría traer errores irreparables a nivel de código HTML.
    def Generate(self):
        """
        
            # Generate the HTML equivalent.

            If this generates the HTML equivalent that the component represents. If you are not an experienced developer who needs something very concrete, DO NOT TOUCH THIS. XQuickBox generates these equivalents in an automated way.
        
            If you inherit from Box do not use this function, use the Generate() method of your own function, doing so could lead to irreparable errors at the HTML level.
            
            :return: HTML String equivalent.

        """

        head = f"""

            <head>
            
                <title>{self.title if self.title != None else 'Super Girls'}</title>
                <meta name="description" content="{self.metaDescription if self.metaDescription != None else 'Short Description Here. Web made with XQuickBox (https://retrokode.com/projects/frameworks/XQuickBox)'}">

                <meta name="keywords" content="{str(self.metaKeywords).replace('[', '').replace(']', '').replace('"', '').replace("'", '')}">

                <link rel="shortcut icon" href="{self.webIcon if self.webIcon != None else 'https://pbs.twimg.com/profile_images/1607576808660078592/MlagycpF_400x400.jpg'}" type="image/x-icon">

            </head>

        """

        





        # Resultado. Esto devuelve un string HTML.
        stylesString = self.StylesParser(self.styles)

        # Ésta es la primera parte del resultado.
        result = f"""<{self.tagName} {'id="' + self.id + '"' if self.id != None else ''} {'class="' + self.className + '"' if self.className != None else ''} {'style="' + stylesString + '"' if len(self.styles) >= 1 else ''} {'>' if self.closeTagType else '/>'}\n"""

        if self.closeTagType:

            for element in self.content:
                
                if isinstance(element, self.availableCommonTypes):
                    elementResult = element.Generate()
                    result += elementResult

                elif isinstance(element, (str, int, float)):
                    # TODO: Arreglar esto.
                    elementResult = TextComponent(className='basicText', content=[str(element)]).Generate()
                    result += elementResult



            result += f'\n</{self.tagName}>\n'


        result = result.replace('  ', ' ')


        result = self.CodeParser('<!DOCTYPE html><html lang="en">' + head + result + '</html>') 


        return result








#! OBJETOS HTML! EN RESUMEN: ETIQUETAS HTML.
# Usar este componente (div) como base.
class DivComponent(Box):
    def __init__(self, id: str = None, className: str = None, styles: list = [], content: list = []): # Tag basic structure.
        """

            # A "div" component!

            Universal container. It is generally used to put other elements inside. It is equivalent to a "div" in HTML. 

            :param id: HTML identifier. It is the value taken by the "id" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param className: It is the value taken by the "class" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param styles: List of dictionaries with css styles. This feature is under test and will possibly evolve to native Python support with own objects. For now, leave key-value values as they are in CSS. An example would be: ```{"display": "flex"}```

            :param content: List containing all the children of this container. Here will go all the other components you want inside this container.
        
        """

        self.availableCommonTypes = (Box, DivComponent, TextComponent, NavComponent, FooterComponent, LinkComponent, ImgComponent, TitleComponent, SubtitleComponent, SmallTitleComponent, UnorderedListComponent, OrderedListComponent)
        self.availableHeadTypes = ()

        self.closeTagType = True # ¿La etiqueta tiene un cierre aparte?
        self.tagName = 'div' # Etiqueta de entrada.
        
        self.id = id # Id de la etiqueta. 
        self.className = className # clase de la etiqueta.
        self.styles = styles # Una lista que contendrá los estilos css. Avanzaré más con este concepto en el futuro.

        self.content = content # Siendo bastante figurativos, este "self.Content" representa las etiquetas HTML.




    # Función que perite generar el string HTML.
    def Generate(self):
        """
        
            # Generate the HTML equivalent.

            If this generates the HTML equivalent that the component represents. If you are not an experienced developer who needs something very concrete, DO NOT TOUCH THIS. XQuickBox generates these equivalents in an automated way.
        
            
            :return: HTML String equivalent.

        """

        # Resultado. Esto devuelve un string HTML.
        stylesString = self.StylesParser(self.styles)

        # Ésta es la primera parte del resultado.
        result = f"""<{self.tagName} {'id="' + self.id + '"' if self.id != None else ''} {'class="' + self.className + '"' if self.className != None else ''} {'style="' + stylesString + '"' if len(self.styles) >= 1 else ''} {'>' if self.closeTagType else '/>'}\n"""

        if self.closeTagType:
            for element in self.content:
                
                if isinstance(element, self.availableCommonTypes):
                    elementResult = element.Generate()
                    result += elementResult

                elif isinstance(element, (str, int, float)):
                    # TODO: Arreglar esto.
                    elementResult = TextComponent(className='basicText', content=[str(element)]).Generate()
                    result += elementResult



            result += f'\n</{self.tagName}>\n'


        result = result.replace('  ', ' ')

        return result

class TextComponent(Box):
    def __init__(self, id: str = None, className: str = None, styles: list = [], content: list = []): # Tag basic structure.
        """

            # A "p" component.

            Component used to place text. It does not usually contain other elements inside as a "div". It is equivalent to a "p" in HTML.

            :param id: HTML identifier. It is the value taken by the "id" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param className: It is the value taken by the "class" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param styles: List of dictionaries with css styles. This feature is under test and will possibly evolve to native Python support with own objects. For now, leave key-value values as they are in CSS. An example would be: ```{"display": "flex"}```

            :param content: List containing all the children of this container. If you want text as is, just put a string inside the list, if you want components, insert the components themselves.
        
        """
        
        self.availableCommonTypes = (Box, DivComponent, TextComponent, NavComponent, FooterComponent, LinkComponent, ImgComponent, TitleComponent, SubtitleComponent, SmallTitleComponent, UnorderedListComponent, OrderedListComponent)
        self.availableHeadTypes = ()

        self.closeTagType = True # ¿La etiqueta tiene cierre? NO SE CIERRA A SÍ MISMA.
        self.tagName = 'p' # Etiqueta de entrada.
        
        self.id = id # Id de la etiqueta. 
        self.className = className # clase de la etiqueta.
        self.styles = styles # Una lista que contendrá los estilos css. Avanzaré más con este concepto en el futuro.

        self.content = content # Siendo bastante figurativos, este "self.Content" representa las etiquetas HTML.


    # Función que perite generar el string HTML.
    def Generate(self):
        """
        
            # Generate the HTML equivalent.

            If this generates the HTML equivalent that the component represents. If you are not an experienced developer who needs something very concrete, DO NOT TOUCH THIS. XQuickBox generates these equivalents in an automated way.
        
            
            :return: HTML String equivalent.

        """

        # Resultado. Esto devuelve un string HTML.
        stylesString = self.StylesParser(self.styles)

        # Ésta es la primera parte del resultado.
        result = f"""<{self.tagName} {'id="' + self.id + '"' if self.id != None else ''} {'class="' + self.className + '"' if self.className != None else ''} {'style="' + stylesString + '"' if len(self.styles) >= 1 else ''} {'>' if self.closeTagType else '/>'}\n"""

        if self.closeTagType:
            for element in self.content:
                        
                if isinstance(element, self.availableCommonTypes):
                    elementResult = element.Generate()
                    result += elementResult

                elif isinstance(element, (str, int, float)):
                    # TODO: Arreglar esto.
                    elementResult = element
                    result += elementResult



            result += f'\n</{self.tagName}>\n'


        result = result.replace('  ', ' ')

        return result

#! Main Structures.
class NavComponent(Box):
    def __init__(self, id: str = None, className: str = None, styles: list = [], content: list = []): # Tag basic structure.
        """

            # A "nav" component!

            A nav container. That used to make the top bars of web pages. Use it if that is your purpose. It is equivalent to a "nav" in HTML. 

            :param id: HTML identifier. It is the value taken by the "id" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param className: It is the value taken by the "class" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param styles: List of dictionaries with css styles. This feature is under test and will possibly evolve to native Python support with own objects. For now, leave key-value values as they are in CSS. An example would be: ```{"display": "flex"}```

            :param content: List containing all the children of this container. Here will go all the other components you want inside this container.
        
        """

        self.availableCommonTypes = (Box, DivComponent, TextComponent, NavComponent, FooterComponent, LinkComponent, ImgComponent, TitleComponent, SubtitleComponent, SmallTitleComponent, UnorderedListComponent, OrderedListComponent)
        self.availableHeadTypes = ()

        self.closeTagType = True # ¿La etiqueta tiene un cierre aparte?
        self.tagName = 'nav' # Etiqueta de entrada.
        
        self.id = id # Id de la etiqueta. 
        self.className = className # clase de la etiqueta.
        self.styles = styles # Una lista que contendrá los estilos css. Avanzaré más con este concepto en el futuro.

        self.content = content # Siendo bastante figurativos, este "self.Content" representa las etiquetas HTML.




    # Función que perite generar el string HTML.
    def Generate(self):
        """
        
            # Generate the HTML equivalent.

            If this generates the HTML equivalent that the component represents. If you are not an experienced developer who needs something very concrete, DO NOT TOUCH THIS. XQuickBox generates these equivalents in an automated way.
        
            
            :return: HTML String equivalent.

        """

        # Resultado. Esto devuelve un string HTML.
        stylesString = self.StylesParser(self.styles)

        # Ésta es la primera parte del resultado.
        result = f"""<{self.tagName} {'id="' + self.id + '"' if self.id != None else ''} {'class="' + self.className + '"' if self.className != None else ''} {'style="' + stylesString + '"' if len(self.styles) >= 1 else ''} {'>' if self.closeTagType else '/>'}\n"""

        if self.closeTagType:
            for element in self.content:
                
                if isinstance(element, self.availableCommonTypes):
                    elementResult = element.Generate()
                    result += elementResult

                elif isinstance(element, (str, int, float)):
                    # TODO: Arreglar esto.
                    elementResult = TextComponent(className='basicText', content=[str(element)]).Generate()
                    result += elementResult



            result += f'\n</{self.tagName}>\n'


        result = result.replace('  ', ' ')

        return result

class FooterComponent(Box):
    def __init__(self, id: str = None, className: str = None, styles: list = [], content: list = []): # Tag basic structure.
        """

            # A "footer" component!

            A footer container. That used to make the bottom top bars of web pages. Use it if that is your purpose. It is equivalent to a "footer" in HTML. 

            :param id: HTML identifier. It is the value taken by the "id" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param className: It is the value taken by the "class" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param styles: List of dictionaries with css styles. This feature is under test and will possibly evolve to native Python support with own objects. For now, leave key-value values as they are in CSS. An example would be: ```{"display": "flex"}```

            :param content: List containing all the children of this container. Here will go all the other components you want inside this container.
        
        """

        self.availableCommonTypes = (Box, DivComponent, TextComponent, NavComponent, FooterComponent, LinkComponent, ImgComponent, TitleComponent, SubtitleComponent, SmallTitleComponent, UnorderedListComponent, OrderedListComponent)
        self.availableHeadTypes = ()

        self.closeTagType = True # ¿La etiqueta tiene un cierre aparte?
        self.tagName = 'footer' # Etiqueta de entrada.
        
        self.id = id # Id de la etiqueta. 
        self.className = className # clase de la etiqueta.
        self.styles = styles # Una lista que contendrá los estilos css. Avanzaré más con este concepto en el futuro.

        self.content = content # Siendo bastante figurativos, este "self.Content" representa las etiquetas HTML.




    # Función que perite generar el string HTML.
    def Generate(self):
        """
        
            # Generate the HTML equivalent.

            If this generates the HTML equivalent that the component represents. If you are not an experienced developer who needs something very concrete, DO NOT TOUCH THIS. XQuickBox generates these equivalents in an automated way.
        
            
            :return: HTML String equivalent.

        """

        # Resultado. Esto devuelve un string HTML.
        stylesString = self.StylesParser(self.styles)

        # Ésta es la primera parte del resultado.
        result = f"""<{self.tagName} {'id="' + self.id + '"' if self.id != None else ''} {'class="' + self.className + '"' if self.className != None else ''} {'style="' + stylesString + '"' if len(self.styles) >= 1 else ''} {'>' if self.closeTagType else '/>'}\n"""

        if self.closeTagType:
            for element in self.content:
                
                if isinstance(element, self.availableCommonTypes):
                    elementResult = element.Generate()
                    result += elementResult

                elif isinstance(element, (str, int, float)):
                    # TODO: Arreglar esto.
                    elementResult = TextComponent(className='basicText', content=[str(element)]).Generate()
                    result += elementResult



            result += f'\n</{self.tagName}>\n'


        result = result.replace('  ', ' ')

        return result


#! Other Components.
class LinkComponent(Box):
    def __init__(self, id: str = None, className: str = None, styles: list = [], visibleText: str = None, url: str = None, inNewTab: bool = True): # Tag basic structure.
        """

            # A "Link" component!

            Put a link in your web. Use a link component to place hyperlinks within your website! You can make buttons, nice redirects or whatever you can imagine. It is equivalent to a "a" in HTML. 

            :param id: HTML identifier. It is the value taken by the "id" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param className: It is the value taken by the "class" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param styles: List of dictionaries with css styles. This feature is under test and will possibly evolve to native Python support with own objects. For now, leave key-value values as they are in CSS. An example would be: ```{"display": "flex"}```


            :param visibleText: The text that will be visible for the link.

            :param url: The link to which the text will redirect.

            :param inNewTab: Gets a boolean value. If "True", it means that clicking on the link will open a new tab. 
        
        """

        self.availableCommonTypes = (Box, DivComponent, TextComponent, NavComponent, FooterComponent, LinkComponent, ImgComponent, TitleComponent, SubtitleComponent, SmallTitleComponent, UnorderedListComponent, OrderedListComponent)
        self.availableHeadTypes = ()

        self.closeTagType = True # ¿La etiqueta tiene un cierre aparte?
        self.tagName = 'a' # Etiqueta de entrada.
        
        self.id = id # Id de la etiqueta. 
        self.className = className # clase de la etiqueta.
        self.styles = styles # Una lista que contendrá los estilos css. Avanzaré más con este concepto en el futuro.

        self.visibleText = visibleText # El texto que es visible. 
        self.url = url
        self.inNewTab = inNewTab




    # Función que perite generar el string HTML.
    def Generate(self):
        """
        
            # Generate the HTML equivalent.

            If this generates the HTML equivalent that the component represents. If you are not an experienced developer who needs something very concrete, DO NOT TOUCH THIS. XQuickBox generates these equivalents in an automated way.
        
            
            :return: HTML String equivalent.

        """

        # Resultado. Esto devuelve un string HTML.
        stylesString = self.StylesParser(self.styles)

        # Ésta es la primera parte del resultado.
        result = f"""<{self.tagName} {'id="' + self.id + '"' if self.id != None else ''} {'class="' + self.className + '"' if self.className != None else ''} {'style="' + stylesString + '"' if len(self.styles) >= 1 else ''} {'href="' + self.url + '"' if self.url else ''} {'target="_blank"' if self.inNewTab else ''} {'>' if self.closeTagType else '/>'}\n"""

        if self.closeTagType:
            
            result += self.visibleText


            result += f'\n</{self.tagName}>\n'


        result = result.replace('  ', ' ')

        return result

class ImgComponent(Box):
    def __init__(self, id: str = None, className: str = None, styles: list = [], imageUrl: str = None, width: float = 512, height: float = None, altImage: str = None): # Tag basic structure.
        """

            # A "img" component!

            Image route! This can be a local path (found on your computer) or from a website (such as https://retrokode.com/imgs/cute_cat.png, nope, dont exist nigga xd). It is equivalent to a "img" in HTML. 

            :param id: HTML identifier. It is the value taken by the "id" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param className: It is the value taken by the "class" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param styles: List of dictionaries with css styles. This feature is under test and will possibly evolve to native Python support with own objects. For now, leave key-value values as they are in CSS. An example would be: ```{"display": "flex"}```


            :param imageUrl: Image route! This can be a local path (found on your computer) or from a website (such as https://retrokode.com/imgs/logo.png).

            :param width: Image width, set in pixels. It has a default value of 512px. If you set this value, it can be discarded from CSS.

            :param height: Image height, set in pixels. It has a default value of None. If you set this value, it can be discarded from CSS.

            :param altImage: The ALT of an image is a text that describes (neither too long nor too short) the content of the image. Google, for example, makes use of this feature to index your images in the search engine.
        
        """

        self.availableCommonTypes = (Box, DivComponent, TextComponent, NavComponent, FooterComponent, LinkComponent, ImgComponent, TitleComponent, SubtitleComponent, SmallTitleComponent, UnorderedListComponent, OrderedListComponent)
        self.availableHeadTypes = ()

        self.closeTagType = False # ¿La etiqueta tiene un cierre aparte?
        self.tagName = 'img' # Etiqueta de entrada.
        
        self.id = id # Id de la etiqueta. 
        self.className = className # clase de la etiqueta.
        self.styles = styles # Una lista que contendrá los estilos css. Avanzaré más con este concepto en el futuro.

        self.imageUrl = imageUrl # Referencia a la imagen!
        self.width = width
        self.height = height
        self.altImage = altImage



    # Función que perite generar el string HTML.
    def Generate(self):
        """
        
            # Generate the HTML equivalent.

            If this generates the HTML equivalent that the component represents. If you are not an experienced developer who needs something very concrete, DO NOT TOUCH THIS. XQuickBox generates these equivalents in an automated way.
        
            
            :return: HTML String equivalent.

        """

        # Resultado. Esto devuelve un string HTML.
        stylesString = self.StylesParser(self.styles)

        # Ésta es la primera parte del resultado.
        result = f"""<{self.tagName} {'id="' + self.id + '"' if self.id != None else ''} {'class="' + self.className + '"' if self.className != None else ''} {'style="' + stylesString + '"' if len(self.styles) >= 1 else ''} {'src="' + self.imageUrl + '"' if self.imageUrl else ''} {'width="' + str(self.width) + 'px"' if self.width else ''} {'height="' + str(self.height) + 'px"' if self.height else ''} {'alt="' + self.altImage + '"' if self.altImage else ''} {'>' if self.closeTagType else '/>'}\n"""

        if self.closeTagType:
            
            result += self.visibleText


            result += f'\n</{self.tagName}>\n'


        result = result.replace('  ', ' ')

        return result


class TitleComponent(Box):
    def __init__(self, id: str = None, className: str = None, styles: list = [], content: list = []): # Tag basic structure.
        """

            # A "h1" component.

            Component used to place titles. It is used to set the main titles of your Boxlication. As a rule, this component should only be there once, and is often used to put the title of the website in it (inside the nav). It is equivalent to a "h1" in HTML.

            :param id: HTML identifier. It is the value taken by the "id" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param className: It is the value taken by the "class" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param styles: List of dictionaries with css styles. This feature is under test and will possibly evolve to native Python support with own objects. For now, leave key-value values as they are in CSS. An example would be: ```{"display": "flex"}```

            :param content: List containing all the children of this container. If you want title as is, just put a string inside the list, if you want components, insert the components themselves.
        
        """
        
        self.availableCommonTypes = (Box, DivComponent, TextComponent, NavComponent, FooterComponent, LinkComponent, ImgComponent, TitleComponent, SubtitleComponent, SmallTitleComponent, UnorderedListComponent, OrderedListComponent)
        self.availableHeadTypes = ()

        self.closeTagType = True # ¿La etiqueta tiene cierre? NO SE CIERRA A SÍ MISMA.
        self.tagName = 'h1' # Etiqueta de entrada.
        
        self.id = id # Id de la etiqueta. 
        self.className = className # clase de la etiqueta.
        self.styles = styles # Una lista que contendrá los estilos css. Avanzaré más con este concepto en el futuro.

        self.content = content # Siendo bastante figurativos, este "self.Content" representa las etiquetas HTML.


    # Función que perite generar el string HTML.
    def Generate(self):
        """
        
            # Generate the HTML equivalent.

            If this generates the HTML equivalent that the component represents. If you are not an experienced developer who needs something very concrete, DO NOT TOUCH THIS. XQuickBox generates these equivalents in an automated way.
        
            
            :return: HTML String equivalent.

        """

        # Resultado. Esto devuelve un string HTML.
        stylesString = self.StylesParser(self.styles)

        # Ésta es la primera parte del resultado.
        result = f"""<{self.tagName} {'id="' + self.id + '"' if self.id != None else ''} {'class="' + self.className + '"' if self.className != None else ''} {'style="' + stylesString + '"' if len(self.styles) >= 1 else ''} {'>' if self.closeTagType else '/>'}\n"""

        if self.closeTagType:
            for element in self.content:
                        
                if isinstance(element, self.availableCommonTypes):
                    elementResult = element.Generate()
                    result += elementResult

                elif isinstance(element, (str, int, float)):
                    # TODO: Arreglar esto.
                    elementResult = element
                    result += elementResult



            result += f'\n</{self.tagName}>\n'


        result = result.replace('  ', ' ')

        return result

class SubtitleComponent(Box):
    def __init__(self, id: str = None, className: str = None, styles: list = [], content: list = []): # Tag basic structure.
        """

            # A "h2" component.

            Component used to place subtitles. Subtitles are less important for SEO (but still have them), so they are usually used for article titles or similar. It is equivalent to a "h2" in HTML.

            :param id: HTML identifier. It is the value taken by the "id" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param className: It is the value taken by the "class" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param styles: List of dictionaries with css styles. This feature is under test and will possibly evolve to native Python support with own objects. For now, leave key-value values as they are in CSS. An example would be: ```{"display": "flex"}```

            :param content: List containing all the children of this container. If you want subtitle as is, just put a string inside the list, if you want components, insert the components themselves.
        
        """
        
        self.availableCommonTypes = (Box, DivComponent, TextComponent, NavComponent, FooterComponent, LinkComponent, ImgComponent, TitleComponent, SubtitleComponent, SmallTitleComponent, UnorderedListComponent, OrderedListComponent)
        self.availableHeadTypes = ()

        self.closeTagType = True # ¿La etiqueta tiene cierre? NO SE CIERRA A SÍ MISMA.
        self.tagName = 'h2' # Etiqueta de entrada.
        
        self.id = id # Id de la etiqueta. 
        self.className = className # clase de la etiqueta.
        self.styles = styles # Una lista que contendrá los estilos css. Avanzaré más con este concepto en el futuro.

        self.content = content # Siendo bastante figurativos, este "self.Content" representa las etiquetas HTML.


    # Función que perite generar el string HTML.
    def Generate(self):
        """
        
            # Generate the HTML equivalent.

            If this generates the HTML equivalent that the component represents. If you are not an experienced developer who needs something very concrete, DO NOT TOUCH THIS. XQuickBox generates these equivalents in an automated way.
        
            
            :return: HTML String equivalent.

        """

        # Resultado. Esto devuelve un string HTML.
        stylesString = self.StylesParser(self.styles)

        # Ésta es la primera parte del resultado.
        result = f"""<{self.tagName} {'id="' + self.id + '"' if self.id != None else ''} {'class="' + self.className + '"' if self.className != None else ''} {'style="' + stylesString + '"' if len(self.styles) >= 1 else ''} {'>' if self.closeTagType else '/>'}\n"""

        if self.closeTagType:
            for element in self.content:
                        
                if isinstance(element, self.availableCommonTypes):
                    elementResult = element.Generate()
                    result += elementResult

                elif isinstance(element, (str, int, float)):
                    # TODO: Arreglar esto.
                    elementResult = element
                    result += elementResult



            result += f'\n</{self.tagName}>\n'


        result = result.replace('  ', ' ')

        return result

class SmallTitleComponent(Box):
    def __init__(self, id: str = None, className: str = None, styles: list = [], content: list = []): # Tag basic structure.
        """

            # A "h3" component.

            Component used to place subtitles. This component is even less important for SEO than the "SubtitleComponent" component itself, but it is also used to create subtitles!. It is equivalent to a "h3" in HTML.

            :param id: HTML identifier. It is the value taken by the "id" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param className: It is the value taken by the "class" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param styles: List of dictionaries with css styles. This feature is under test and will possibly evolve to native Python support with own objects. For now, leave key-value values as they are in CSS. An example would be: ```{"display": "flex"}```

            :param content: List containing all the children of this container. If you want subtitle as is, just put a string inside the list, if you want components, insert the components themselves.
        
        """
        
        self.availableCommonTypes = (Box, DivComponent, TextComponent, NavComponent, FooterComponent, LinkComponent, ImgComponent, TitleComponent, SubtitleComponent, SmallTitleComponent, UnorderedListComponent, OrderedListComponent)
        self.availableHeadTypes = ()

        self.closeTagType = True # ¿La etiqueta tiene cierre? NO SE CIERRA A SÍ MISMA.
        self.tagName = 'h3' # Etiqueta de entrada.
        
        self.id = id # Id de la etiqueta. 
        self.className = className # clase de la etiqueta.
        self.styles = styles # Una lista que contendrá los estilos css. Avanzaré más con este concepto en el futuro.

        self.content = content # Siendo bastante figurativos, este "self.Content" representa las etiquetas HTML.


    # Función que perite generar el string HTML.
    def Generate(self):
        """
        
            # Generate the HTML equivalent.

            If this generates the HTML equivalent that the component represents. If you are not an experienced developer who needs something very concrete, DO NOT TOUCH THIS. XQuickBox generates these equivalents in an automated way.
        
            
            :return: HTML String equivalent.

        """

        # Resultado. Esto devuelve un string HTML.
        stylesString = self.StylesParser(self.styles)

        # Ésta es la primera parte del resultado.
        result = f"""<{self.tagName} {'id="' + self.id + '"' if self.id != None else ''} {'class="' + self.className + '"' if self.className != None else ''} {'style="' + stylesString + '"' if len(self.styles) >= 1 else ''} {'>' if self.closeTagType else '/>'}\n"""

        if self.closeTagType:
            for element in self.content:
                        
                if isinstance(element, self.availableCommonTypes):
                    elementResult = element.Generate()
                    result += elementResult

                elif isinstance(element, (str, int, float)):
                    # TODO: Arreglar esto.
                    elementResult = element
                    result += elementResult



            result += f'\n</{self.tagName}>\n'


        result = result.replace('  ', ' ')

        return result


class UnorderedListComponent(Box):
    def __init__(self, id: str = None, className: str = None, styles: list = [], content: list = []): # Tag basic structure.
        """

            # A "ul" component!

            A container for creating Unordered lists (this is its purpose). It is equivalent to a "ul" in HTML. 

            :param id: HTML identifier. It is the value taken by the "id" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param className: It is the value taken by the "class" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param styles: List of dictionaries with css styles. This feature is under test and will possibly evolve to native Python support with own objects. For now, leave key-value values as they are in CSS. An example would be: ```{"display": "flex"}```

            :param content: List containing all the children of this container. Unordered lists can take any type of the other components. Insert whatever you want!
        
        """

        self.availableCommonTypes = (Box, DivComponent, TextComponent, NavComponent, FooterComponent, LinkComponent, ImgComponent, TitleComponent, SubtitleComponent, SmallTitleComponent, UnorderedListComponent, OrderedListComponent)
        self.availableHeadTypes = ()

        self.closeTagType = True # ¿La etiqueta tiene un cierre aparte?
        self.tagName = 'ul' # Etiqueta de entrada.
        
        self.id = id # Id de la etiqueta. 
        self.className = className # clase de la etiqueta.
        self.styles = styles # Una lista que contendrá los estilos css. Avanzaré más con este concepto en el futuro.

        self.content = content # Siendo bastante figurativos, este "self.Content" representa las etiquetas HTML.




    # Función que perite generar el string HTML.
    def Generate(self):
        """
        
            # Generate the HTML equivalent.

            If this generates the HTML equivalent that the component represents. If you are not an experienced developer who needs something very concrete, DO NOT TOUCH THIS. XQuickBox generates these equivalents in an automated way.
        
            
            :return: HTML String equivalent.

        """

        # Resultado. Esto devuelve un string HTML.
        stylesString = self.StylesParser(self.styles)

        # Ésta es la primera parte del resultado.
        result = f"""<{self.tagName} {'id="' + self.id + '"' if self.id != None else ''} {'class="' + self.className + '"' if self.className != None else ''} {'style="' + stylesString + '"' if len(self.styles) >= 1 else ''} {'>' if self.closeTagType else '/>'}\n"""

        if self.closeTagType:
            for element in self.content:
                
                if isinstance(element, self.availableCommonTypes):
                    elementResult = element.Generate()
                    result += elementResult

                elif isinstance(element, (str, int, float)):
                    # TODO: Arreglar esto.
                    elementResult = TextComponent(className='basicText', content=[str(element)]).Generate()
                    result += elementResult



            result += f'\n</{self.tagName}>\n'


        result = result.replace('  ', ' ')

        return result


class OrderedListComponent(Box):
    def __init__(self, id: str = None, className: str = None, styles: list = [], content: list = []): # Tag basic structure.
        """

            # A "ol" component!

            A container for creating Ordered lists (this is its purpose). It is equivalent to a "ol" in HTML. 

            :param id: HTML identifier. It is the value taken by the "id" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param className: It is the value taken by the "class" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param styles: List of dictionaries with css styles. This feature is under test and will possibly evolve to native Python support with own objects. For now, leave key-value values as they are in CSS. An example would be: ```{"display": "flex"}```

            :param content: List containing all the children of this container. Ordered lists can take any type of the other components. Insert whatever you want!
        
        """

        self.availableCommonTypes = (Box, DivComponent, TextComponent, NavComponent, FooterComponent, LinkComponent, ImgComponent, TitleComponent, SubtitleComponent, SmallTitleComponent, UnorderedListComponent, OrderedListComponent)
        self.availableHeadTypes = ()

        self.closeTagType = True # ¿La etiqueta tiene un cierre aparte?
        self.tagName = 'ol' # Etiqueta de entrada.
        
        self.id = id # Id de la etiqueta. 
        self.className = className # clase de la etiqueta.
        self.styles = styles # Una lista que contendrá los estilos css. Avanzaré más con este concepto en el futuro.

        self.content = content # Siendo bastante figurativos, este "self.Content" representa las etiquetas HTML.




    # Función que perite generar el string HTML.
    def Generate(self):
        """
        
            # Generate the HTML equivalent.

            If this generates the HTML equivalent that the component represents. If you are not an experienced developer who needs something very concrete, DO NOT TOUCH THIS. XQuickBox generates these equivalents in an automated way.
        
            
            :return: HTML String equivalent.

        """

        # Resultado. Esto devuelve un string HTML.
        stylesString = self.StylesParser(self.styles)

        # Ésta es la primera parte del resultado.
        result = f"""<{self.tagName} {'id="' + self.id + '"' if self.id != None else ''} {'class="' + self.className + '"' if self.className != None else ''} {'style="' + stylesString + '"' if len(self.styles) >= 1 else ''} {'>' if self.closeTagType else '/>'}\n"""

        if self.closeTagType:
            for element in self.content:
                
                if isinstance(element, self.availableCommonTypes):
                    elementResult = element.Generate()
                    result += elementResult

                elif isinstance(element, (str, int, float)):
                    # TODO: Arreglar esto.
                    elementResult = TextComponent(className='basicText', content=[str(element)]).Generate()
                    result += elementResult



            result += f'\n</{self.tagName}>\n'


        result = result.replace('  ', ' ')

        return result

