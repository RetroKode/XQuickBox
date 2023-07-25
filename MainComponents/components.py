# Estas clases representan las etiquetas HTML. Aquellas como "div" o "p".

class App:
    def __init__(self, id: str = None, className: str = None, styles: list = [], title: str = 'My XQuickBox! - RetroKode', metaDescription: str = None, metaKeywords: list = [], content: list = []): # Tag basic structure.
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
        self.title = title
        self.metaDescription = metaDescription
        self.metaKeywords = metaKeywords

        self.closeTagType = True # ¿La etiqueta tiene cierre?
        self.openTag = '<!DOCTYPE html>' # Etiqueta de entrada.
        self.closeTag = '</html>' # Etiqueta de cierre.
        
        self.id = id # Id de la etiqueta. 
        self.className = className # clase de la etiqueta.
        self.styles = styles # Una lista que contendrá los estilos css. Avanzaré más con este concepto en el futuro.



        self.content = content # Siendo bastante figurativos, este "self.Content" representa las etiquetas HTML.


    # Un div básico. Representa un "<div></div>"
    class BasicDiv:
        def __init__(self, id: str = None, className: str = None, styles: list = [], content: list = []): # Tag basic structure.
            """

                # Instance of a web!

                This class is a new web instance! It is the equivalent of creating an HTML file.

                :param id: HTML identifier. It is the value taken by the "id" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

                :param className: It is the value taken by the "class" key in an HTML tag. All tags can take this value without affecting their output. Use this for CSS styling.

                :param styles: List of dictionaries with css styles. This feature is under test and will possibly evolve to native Python support with own objects. For now, leave key-value values as they are in CSS. An example would be: ```{"display": "flex"}```

                :param content: List containing all the children of this container. Here will go all the other components you want inside this container.
            
            """

            self.closeTagType = True # ¿La etiqueta tiene cierre?
            self.openTag = '<!DOCTYPE html>' # Etiqueta de entrada.
            self.closeTag = '</html>' # Etiqueta de cierre.
            
            self.id = id # Id de la etiqueta. 
            self.className = className # clase de la etiqueta.
            self.styles = styles # Una lista que contendrá los estilos css. Avanzaré más con este concepto en el futuro.

            self.content = content # Siendo bastante figurativos, este "self.Content" representa las etiquetas HTML.