import urllib

from flask import Flask, request
from flask_restful import Resource, Api
from nltk.tree import ParentedTree

app = Flask(__name__)
api = Api()


class NewTreesFinder:
    def __init__(self, tree_str: str, limit: int):
        self.tree_str = tree_str
        self.limit = limit
        self.my_trees = set()
        self.first_node = 'NP'
        self.separators = ('CC', ',')
        self.second_node = 'NP'

        self.find_tree(self.tree_str)

    def find_tree(self, tree_str: str):
        t = ParentedTree.fromstring(tree_str)
        for subtree in t.subtrees(lambda t: t.label() in self.separators):
            if len(self.my_trees) >= self.limit:
                return
            left_sibling = subtree.left_sibling()
            right_sibling = subtree.right_sibling()
            if left_sibling and right_sibling:
                ls_match = False
                rs_match = False

                if left_sibling.subtrees().__next__().label() == self.first_node:
                    ls_match = True
                if right_sibling.subtrees().__next__().label() == self.first_node:
                    rs_match = True

                if ls_match and rs_match:

                    parent = subtree.parent()
                    left_index = parent.index(left_sibling)
                    right_index = parent.index(right_sibling)
                    parent.remove(left_sibling)
                    parent.remove(right_sibling)
                    parent.insert(left_index, right_sibling)
                    parent.insert(right_index, left_sibling)

                    new_tree_str = str(t)
                    if hash(new_tree_str) not in (hash(i) for i in self.my_trees):
                        self.my_trees.add(new_tree_str)
                        self.find_tree(new_tree_str)


class NewTreesApp(Resource):

    def get(self):
        tree_str = urllib.parse.unquote(request.args.get('tree', ''))
        if not tree_str.strip():
            return {'error': 'no tree provided'}, 400
        limit = request.args.get('limit', 20, type=int)

        try:
            ParentedTree.fromstring(tree_str)
        except ValueError:
            return {'error': 'invalid tree format'}, 400

        nt = NewTreesFinder(tree_str, limit)
        result = {'paraphrases': [{'tree': i} for i in nt.my_trees]}
        return result


api.add_resource(NewTreesApp, "/paraphrase")
api.init_app(app)
if __name__ == '__main__':
    app.run(host='localhost', port=5000)
