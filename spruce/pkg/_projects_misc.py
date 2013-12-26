"""Projects miscellany."""

__copyright__ = "Copyright (C) 2013 Ivan D Vasin and Cogo Labs"
__docformat__ = "restructuredtext"


def normalized_project_name(project):
    try:
        name = project.name
    except AttributeError:
        name = project
    return name.lower()
