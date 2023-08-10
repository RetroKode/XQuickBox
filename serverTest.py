"""

Las webs hechas con XQuickBox son una estructura de hijos. Todos los hijos son componentes, incluso la aplicación principal. Por tanto, podríamos definir que la estructura de una web XQuickBox es una red de hijos con hijos, una forma un poco más literal de ver los archivos HTML, que incluso su objeto principal (<!DOCTYPE html></html>), que contiene TODAS las webs, se podrían usar como hijos de por ejemplo, un "<div>" cualquiera, aunque no se deba hacer. 

XQuickBox funciona de la misma forma, toda aplicación tiene un componente equivalente al "<!DOCTYPE html></html>", que representa una App (también tiene las mismas propiedades que los demás), y aunque se puede usar como hijo de otros componentes, no se debe hacer.

"""


from Main.HtmlComponents import *


MyQuickWeb = Box(title='funny cats images') # "Box", for practical purposes, it is a web page. A secure and fast environment where you can run it, test it and create it.


MyQuickWeb.content = [

	TextComponent(content=['Text me']),
	LinkComponent(visibleText='here', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'),

	DivComponent(id='funnyCatsContainer',
	content=[

		TitleComponent(
			content=['See my cats (not are my cats really)']),
			
		ImgComponent(
			imageUrl='https://i.ytimg.com/vi/YSHDBB6id4A/maxresdefault.jpg', 
			altImage = 'a cute cat (with a hat)')
		])
]



MyQuickWeb.RunTestMode()