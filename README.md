# maya-pagoda-tool
Creates a pagoda based off of To-ji Temple in Kyoto, Japan in Autodesk Maya with a simple UI.


The width parameter controls the width of the pagoda in column widths. A value of 4 will result in a width of 4 columns. Spaces in between columns are fixed.

The height parameter controls the number of stories the pagoda has. The height of the individual stories is fixed. 

The merge geometry checkbox merges geometry. Left unchecked, it will output geometry in the original groupings they were made in to make assigning shaders and textures easier. 


pagoda-tool.py contains the script that makes the pagoda.
sample-render.jpg contains a sample render of the tool. The pagoda was shaded, lit, and rendered with Arnold and then composited in Photoshop.
tool-UI-and-samples.png is a screenshot of the UI (top left) as well as sample configurations of the tool. 
