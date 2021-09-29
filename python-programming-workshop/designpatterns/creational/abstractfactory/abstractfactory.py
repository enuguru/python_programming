
class Window:
   __toolkit = ""
   __purpose = ""

   def __init__(self, toolkit, purpose):
      self.__toolkit = toolkit
      self.__purpose = purpose
   
   def getToolkit(self):
      return self.__toolkit
   
   def getType(self):
      return self.__purpose

class GtkToolboxWindow(Window):
   def __init__(self):
      Window.__init__(self, "Gtk", "ToolboxWindow")

class GtkLayersWindow(Window):
   def __init__(self):
      Window.__init__(self, "Gtk", "LayersWindow")

class GtkMainWindow(Window):
   def __init__(self):
      Window.__init__(self, "Gtk", "MainWindow")

class QtToolboxWindow(Window):
   def __init__(self):
      Window.__init__(self, "Qt", "ToolboxWindow")

class QtLayersWindow(Window):
   def __init__(self):
      Window.__init__(self, "Qt", "LayersWindow")

class QtMainWindow(Window):
   def __init__(self):
      Window.__init__(self, "Qt", "MainWindow")

# Abstract factory class
class UIFactory:
   def getToolboxWindow(self): pass
   def getLayersWindow(self): pass
   def getMainWindow(self): pass

class GtkUIFactory(UIFactory):
   def getToolboxWindow(self):
      return GtkToolboxWindow()
   def getLayersWindow(self):
      return GtkLayersWindow()
   def getMainWindow(self):
      return GtkMainWindow()

class QtUIFactory(UIFactory):
   def getToolboxWindow(self):
      return QtToolboxWindow()
   def getLayersWindow(self):
      return QtLayersWindow()
   def getMainWindow(self):
      return QtMainWindow()

if __name__ == "__main__":
   gnome = True
   kde = not gnome
   
   if gnome:
      ui = GtkUIFactory()
   elif kde:
      ui = QtUIFactory()
   
   toolbox = ui.getToolboxWindow()
   layers = ui.getLayersWindow()
   main = ui.getMainWindow()
   
   print("%s:%s" % (toolbox.getToolkit(), toolbox.getType()))
   print("%s:%s" % (layers.getToolkit(), layers.getType()))
   print("%s:%s" % (main.getToolkit(), main.getType()))
