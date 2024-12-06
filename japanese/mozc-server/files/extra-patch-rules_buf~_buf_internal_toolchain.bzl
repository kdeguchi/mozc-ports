--- buf/internal/toolchain.bzl	2024-12-06 08:22:05.140319000 +0900
+++ buf/internal/toolchain.bzl	2024-12-06 08:31:06.006072000 +0900
@@ -148,7 +148,7 @@
         version = versions[0]["name"]
 
     os, cpu = _detect_host_platform(ctx)
-    if os not in ["linux", "darwin", "windows"] or cpu not in ["arm64", "amd64"]:
+    if os not in ["linux", "freebsd", "darwin", "windows"] or cpu not in ["arm64", "amd64"]:
         fail("Unsupported operating system or cpu architecture ")
     if os == "linux" and cpu == "arm64":
         cpu = "aarch64"
