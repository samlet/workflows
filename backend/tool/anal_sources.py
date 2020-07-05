from anytree import NodeMixin
from anytree import RenderTree
from anytree.search import findall, findall_by_attr
import ast, gast
from cached_property import cached_property

class AstNode(NodeMixin, object):
    def __init__(self, parent=None, ast_node=None):
        self.name=ast_node.name if 'name' in ast_node._fields else '_'
        self.parent = parent
        self.ast_node=ast_node
        self.ast_type=type(ast_node).__name__
        def as_children(ast_node):
            return [AstNode(parent=self, ast_node=n) for n in ast_node.body]
        self.children = as_children(ast_node) if 'body' in ast_node._fields else []

    @cached_property
    def doc_str(self):
        return gast.get_docstring(self.ast_node)

    def __repr__(self):
        return f"{self.name}"

    @staticmethod
    def load(file):
        tree = parse(file)
        return AstNode(ast_node=tree)

    @property
    def functions(self):
        fn_ls=findall(self, filter_=lambda node: node.ast_type in ("FunctionDef"), maxlevel=2)
        return fn_ls

    @property
    def fn_docs(self):
        return [(fn.name, fn.doc_str) for fn in self.functions]

def tree_vis(tree):
    root=AstNode(ast_node=tree)
    rnd_tree = RenderTree(root)
    for pre, fill, node in rnd_tree:
        print(f"{pre}{node.ast_type}: {node.name}")

def parse(file):
    code = open(file).read()
    tree = ast.parse(code)
    gtree = gast.ast_to_gast(tree)
    return gtree

class AnalSources(object):
    def anal(self, file):
        """
        $ python -m backend.tool.anal_sources anal executors/downloader.py

        :param file:
        :return:
        """
        tree_vis(parse(file))

if __name__ == '__main__':
    import fire
    fire.Fire(AnalSources)

