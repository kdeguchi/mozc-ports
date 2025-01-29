--- merge_dictionaries.py.orig	2025-01-28 05:46:28.000000000 +0900
+++ merge_dictionaries.py	2025-01-29 12:32:46.471938000 +0900
@@ -9,9 +9,7 @@
 import os
 import subprocess
 import sys
-import urllib.request
 from unicodedata import normalize
-from zipfile import ZipFile
 
 
 def main():
@@ -50,38 +48,18 @@
 
 
 def get_mozc_dic():
-    # Mozc の最終コミット日を取得
-    url = 'https://github.com/google/mozc/commits/master/'
+    id_def  = open("id.def", "r")
+    id_mozc = id_def.read()
+    id_mozc = id_mozc.split(' 名詞,一般,')[0].split('\n')[-1]
 
-    with urllib.request.urlopen(url) as response:
-        date = response.read().decode()
-        date = date.split('"committedDate":"')[1]
-        date = date[:10]
-        date = date.replace('-', '')
+    # Mozc 公式辞書を取得
+    mozc_dic = []
 
-    # Mozc のアーカイブが古い場合は取得
-    url = 'https://github.com/google/mozc/archive/refs/heads/master.zip'
+    for i in range(10):
+        file = open('%%WRKSRC%%/src/data/dictionary_oss/' +
+            f'dictionary0{i}.txt')
+        mozc_dic += file.read().splitlines()
 
-    if os.path.exists(f'mozc-{date}.zip') is False:
-        urllib.request.urlretrieve(
-                url, f'mozc-{date}.zip')
-
-    with ZipFile(f'mozc-{date}.zip') as zip_ref:
-        # 一般名詞のIDを取得
-        with zip_ref.open(
-                'mozc-master/src/data/dictionary_oss/id.def') as file:
-            id_mozc = file.read().decode()
-            id_mozc = id_mozc.split(' 名詞,一般,')[0].split('\n')[-1]
-
-        # Mozc 公式辞書を取得
-        mozc_dic = []
-
-        for i in range(10):
-            with zip_ref.open(
-                    'mozc-master/src/data/dictionary_oss/' +
-                    f'dictionary0{i}.txt') as file:
-                mozc_dic += file.read().decode().splitlines()
-
     mozc_dic.append(id_mozc)
     return (mozc_dic)
 
@@ -121,10 +99,6 @@
 
 
 def count_word_hits():
-    subprocess.run(
-        ['wget', '-N', 'https://dumps.wikimedia.org/jawiki/latest/' +
-            'jawiki-latest-pages-articles-multistream-index.txt.bz2'],
-        check=True)
 
     with bz2.open(
             'jawiki-latest-pages-articles-multistream-index.txt.bz2',
