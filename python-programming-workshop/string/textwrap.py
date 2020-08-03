
import textwrap

value = """The image in these opening lines evidently refers to a bird
knocking itself out, in full flight, against the outer surface of a glass
pane in which a mirrored sky, with its slightly darker tint and slightly 
slower cloud, presents the illusion of continued space."""

# Wrap this text.
list = textwrap.wrap(value, width=50)

# Print each line.
for element in list:
    print(element)
