--- src/base/init_mozc.cc.orig	2025-09-02 11:09:32 UTC
+++ src/base/init_mozc.cc
@@ -30,6 +30,7 @@
 #include "base/init_mozc.h"
 
 #include <string>
+#include <stdlib.h>
 
 #include "absl/flags/flag.h"
 
@@ -112,7 +113,9 @@ void InitMozc(const char* arg0, int* argc, char*** arg
   ParseCommandLineFlags(*argc, *argv);
 
   const std::string program_name = *argc > 0 ? (*argv)[0] : "UNKNOWN";
-  RegisterLogFileSink(GetLogFilePathFromProgramName(program_name));
+  const char *nolog = getenv("MOZC_NOLOG");
+  if (nolog == NULL)
+    RegisterLogFileSink(GetLogFilePathFromProgramName(program_name));
 }
 
 }  // namespace mozc
