import inspect
import pydoc

def print_class_hierarchy(classes=()):
    td = pydoc.TextDoc()
    tree_list_of_lists = inspect.getclasstree(classes)
    print(td.formattree(tree_list_of_lists, 'NameSpaceName'))
