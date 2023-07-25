"""
Las webs hechas con XQuickBox son una estructura de hijos. Todos los hijos son componentes, incluso la aplicación principal. Por tanto, podríamos definir que la estructura de una web XQuickBox es una red de hijos con hijos, una forma un poco más literal de ver los archivos HTML, que incluso su objeto principal (<!DOCTYPE html></html>), que contiene TODAS las webs, se podrían usar como hijos de por ejemplo, un "<div>" cualquiera, aunque no se deba hacer. 

XQuickBox funciona de la misma forma, toda aplicación tiene un componente equivalente al "<!DOCTYPE html></html>", que representa una App (también tiene las mismas propiedades que los demás), y aunque se puede usar como hijo de otros componentes, no se debe hacer.


"""


from MainComponents.components import App

test = App(
    title='My quickly web uwu',
    styles=[{'margin': 0}, {'padding': 0}], #? Temporal System.
    metaDescription='A test web with XQuickBox', 
    metaKeywords=['test', 'XQuickBox', 'RetroKode', 'RetroKodeFramework']
    )


# You can use ".append" to enter a new value in case the list already exists (and you want to enter it at the end, as you can assign everything within a single list. 
test.content = ['...']
test.content.append('...')