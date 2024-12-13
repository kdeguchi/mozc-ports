--- merge_dictionaries.py.orig	2024-12-12 16:58:48.000000000 +0900
+++ merge_dictionaries.py	2024-12-13 12:17:37.042962000 +0900
@@ -8,18 +8,14 @@
 import html
 import subprocess
 import sys
-import urllib.request
 from unicodedata import normalize
 
 
 def get_id_mozc():
     # Mozc の一般名詞のIDを取得
-    url = 'https://raw.githubusercontent.com/' + \
-            'google/mozc/master/src/data/dictionary_oss/id.def'
+    id_def = open("id.def", "r")
+    id_mozc = id_def.read()
 
-    with urllib.request.urlopen(url) as response:
-        id_mozc = response.read().decode()
-
     id_mozc = id_mozc.split(' 名詞,一般,')[0].split('\n')[-1]
     return (id_mozc)
 
@@ -62,10 +58,6 @@
 
 
 def count_word_hits():
-    subprocess.run(
-        ['wget', '-N', 'https://dumps.wikimedia.org/jawiki/latest/' +
-            'jawiki-latest-pages-articles-multistream-index.txt.bz2'],
-        check=True)
 
     with bz2.open(
             'jawiki-latest-pages-articles-multistream-index.txt.bz2',
