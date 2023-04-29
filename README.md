# Syntax_tree
## Installing
1. Clone the repository
```
git clone https://github.com/Derafino/Syntax_tree.git
```
2. Create a virtual environment
```
python3 -m venv env
```
3. Activate the virtual environment
```
env\Scripts\activate
```
4. Install requirements
```
pip install -r requirements.txt
```
5. For start type 
```
flask run --host=localhost  --port=<port>
```

To obtain new trees, make a request:
```
localhost:<port>/paraphrase?tree=your_tree&limit=
```
## Example
For url:
```
localhost:5000/paraphrase?tree=(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS restaurants) ) ) ) ) ) ) )
```
Result:
![image](https://user-images.githubusercontent.com/61626827/235297546-ddb74195-c242-4456-a4e8-01f59e566c96.png)
JSON:
```json
{
    "paraphrases": [
        {
            "tree": "(S\n  (NP\n    (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter))\n    (, ,)\n    (CC or)\n    (NP (NNP Barri) (NNP Gòtic)))\n  (, ,)\n  (VP\n    (VBZ has)\n    (NP\n      (NP (JJ narrow) (JJ medieval) (NNS streets))\n      (VP\n        (VBN filled)\n        (PP\n          (IN with)\n          (NP\n            (NP (JJ trendy) (NNS bars))\n            (, ,)\n            (NP (NNS clubs))\n            (CC and)\n            (NP (JJ Catalan) (NNS restaurants))))))))"
        },
        {
            "tree": "(S\n  (NP\n    (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter))\n    (, ,)\n    (CC or)\n    (NP (NNP Barri) (NNP Gòtic)))\n  (, ,)\n  (VP\n    (VBZ has)\n    (NP\n      (NP (JJ narrow) (JJ medieval) (NNS streets))\n      (VP\n        (VBN filled)\n        (PP\n          (IN with)\n          (NP\n            (NP (JJ Catalan) (NNS restaurants))\n            (, ,)\n            (NP (JJ trendy) (NNS bars))\n            (CC and)\n            (NP (NNS clubs))))))))"
        },
        {
            "tree": "(S\n  (NP\n    (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter))\n    (, ,)\n    (CC or)\n    (NP (NNP Barri) (NNP Gòtic)))\n  (, ,)\n  (VP\n    (VBZ has)\n    (NP\n      (NP (JJ narrow) (JJ medieval) (NNS streets))\n      (VP\n        (VBN filled)\n        (PP\n          (IN with)\n          (NP\n            (NP (NNS clubs))\n            (, ,)\n            (NP (JJ trendy) (NNS bars))\n            (CC and)\n            (NP (JJ Catalan) (NNS restaurants))))))))"
        },
        {
            "tree": "(S\n  (NP\n    (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter))\n    (, ,)\n    (CC or)\n    (NP (NNP Barri) (NNP Gòtic)))\n  (, ,)\n  (VP\n    (VBZ has)\n    (NP\n      (NP (JJ narrow) (JJ medieval) (NNS streets))\n      (VP\n        (VBN filled)\n        (PP\n          (IN with)\n          (NP\n            (NP (JJ trendy) (NNS bars))\n            (, ,)\n            (NP (JJ Catalan) (NNS restaurants))\n            (CC and)\n            (NP (NNS clubs))))))))"
        },
        {
            "tree": "(S\n  (NP\n    (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter))\n    (, ,)\n    (CC or)\n    (NP (NNP Barri) (NNP Gòtic)))\n  (, ,)\n  (VP\n    (VBZ has)\n    (NP\n      (NP (JJ narrow) (JJ medieval) (NNS streets))\n      (VP\n        (VBN filled)\n        (PP\n          (IN with)\n          (NP\n            (NP (JJ Catalan) (NNS restaurants))\n            (, ,)\n            (NP (NNS clubs))\n            (CC and)\n            (NP (JJ trendy) (NNS bars))))))))"
        },
        {
            "tree": "(S\n  (NP\n    (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter))\n    (, ,)\n    (CC or)\n    (NP (NNP Barri) (NNP Gòtic)))\n  (, ,)\n  (VP\n    (VBZ has)\n    (NP\n      (NP (JJ narrow) (JJ medieval) (NNS streets))\n      (VP\n        (VBN filled)\n        (PP\n          (IN with)\n          (NP\n            (NP (NNS clubs))\n            (, ,)\n            (NP (JJ Catalan) (NNS restaurants))\n            (CC and)\n            (NP (JJ trendy) (NNS bars))))))))"
        }
    ]
}
```
