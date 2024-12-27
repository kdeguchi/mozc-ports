--- src/main/native/unix_jni_bsd.cc.orig	1979-12-31 15:00:00 UTC
+++ src/main/native/unix_jni_bsd.cc
@@ -67,8 +67,8 @@ uint64_t StatEpochMilliseconds(const portable_stat_str
       return statbuf.st_ctimespec.tv_sec * 1000L +
              statbuf.st_ctimespec.tv_nsec / 1000000;
     case STAT_MTIME:
-      return statbuf.st_mtime.tv_sec * 1000L +
-             statbuf.st_mtimespec.tv_nsec / 1000000;
+      return statbuf.st_mtime * 1000L +
+             statbuf.st_mtimensec / 1000000;
   }
 }
 
