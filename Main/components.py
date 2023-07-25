# Estas clases representan las etiquetas HTML. Aquellas como "div" o "p".

class App:
    def __init__(self, id: str = None, className: str = None, styles: list = [{'margin': 0}, {'padding': 0}], title: str = 'My XQuickBox! - RetroKode', metaDescription: str = None, metaKeywords: list = [], content: list = []): # Tag basic structure.
        """

            # Instance of a web!

            This class is a new web instance! It is the equivalent of creating an HTML file.

            :param id: HTML identifier. It is the value taken by the "id" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param className: It is the value taken by the "class" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param styles: List of dictionaries with css styles. This feature is under test and will possibly evolve to native Python support with own objects. For now, leave key-value values as they are in CSS. An example would be: ```{"display": "flex"}```

            :param title: Title of the page!
            
            :param metaDescription: The description of the web page. It is the value resulting from assigning the key "content" in the meta key tag "name" with value "desc".

            :param metaKeywords: Keywords of the web page. List of strings. It is the value resulting from assigning the key "content" in the meta key tag "name" with value "keywords".

            :param content: List containing all the children of this container. Here will go all the other components you want inside this container.
        
        """

        #! Metatags y otra info (los demás componentes no tendrán esto, solo la app principal)!


        self.availableTypes = (App, DivComponent, TextComponent)
    
        self.title = title
        self.metaDescription = metaDescription
        self.metaKeywords = metaKeywords

        self.closeTagType = True # ¿La etiqueta tiene cierre?
        self.tagName = 'html'
        
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


        # TODO: make this.
        return stylesString


    
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

                if isinstance(element, self.availableTypes):
                    elementResult = element.Generate()
                    result += elementResult

                elif type(element) == type(str) or type(element) == type(int) or type(element) == type(float):
                    elementResult = TextComponent(className='basicText', content=element).Generate()
                    result += elementResult



            result += f'\n</{self.tagName}>\n'


        result = result.replace('  ', '')

        return result








#! OBJETOS HTML! EN RESUMEN: ETIQUETAS HTML.

class DivComponent(App):
    def __init__(self, id: str = None, className: str = None, styles: list = [], content: list = []): # Tag basic structure.
        """

            # A "div" component!

            Universal container. It is generally used to put other elements inside. It is equivalent to a "div" in HTML. 

            :param id: HTML identifier. It is the value taken by the "id" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param className: It is the value taken by the "class" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param styles: List of dictionaries with css styles. This feature is under test and will possibly evolve to native Python support with own objects. For now, leave key-value values as they are in CSS. An example would be: ```{"display": "flex"}```

            :param content: List containing all the children of this container. Here will go all the other components you want inside this container.
        
        """

        self.availableTypes = (App, DivComponent, TextComponent)

        self.closeTagType = True # ¿La etiqueta tiene un cierre aparte?
        self.tagName = 'div' # Etiqueta de entrada.
        
        self.id = id # Id de la etiqueta. 
        self.className = className # clase de la etiqueta.
        self.styles = styles # Una lista que contendrá los estilos css. Avanzaré más con este concepto en el futuro.

        self.content = content # Siendo bastante figurativos, este "self.Content" representa las etiquetas HTML.




    # Función que perite generar el string HTML.
    def Generate(self):
        return super().Generate()





# Un div básico. Representa un "<p></p>"
class TextComponent(App):
    def __init__(self, id: str = None, className: str = None, styles: list = [], content: str = ''): # Tag basic structure.
        """

            # A "p" component.

            Component used to place text. It does not usually contain other elements inside as a "div". It is equivalent to a "p" in HTML.

            :param id: HTML identifier. It is the value taken by the "id" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param className: It is the value taken by the "class" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

            :param styles: List of dictionaries with css styles. This feature is under test and will possibly evolve to native Python support with own objects. For now, leave key-value values as they are in CSS. An example would be: ```{"display": "flex"}```

            :param content: Text to be contained in the label. It is a string.
        
        """
        
        self.availableTypes = (App, DivComponent, TextComponent)

        self.closeTagType = True # ¿La etiqueta tiene cierre?
        self.tagName = 'p' # Etiqueta de entrada.
        
        self.id = id # Id de la etiqueta. 
        self.className = className # clase de la etiqueta.
        self.styles = styles # Una lista que contendrá los estilos css. Avanzaré más con este concepto en el futuro.

        self.content = content # Siendo bastante figurativos, este "self.Content" representa las etiquetas HTML.


    # Función que perite generar el string HTML.
    def Generate(self):
        return super().Generate()