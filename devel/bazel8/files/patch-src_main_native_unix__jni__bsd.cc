--- src/main/native/unix_jni_bsd.cc.orig	1980-01-01 05:00:00 UTC
+++ src/main/native/unix_jni_bsd.cc
@@ -152,6 +152,12 @@ int portable_cpu_speed() {
 int portable_cpu_speed() {
   // Currently not implemented.
   return -1;
+}
+
+extern "C" JNIEXPORT void JNICALL
+Java_com_google_devtools_build_lib_profiler_SystemNetworkStats_getNetIoCountersNative(
+    JNIEnv *env, jclass clazz, jobject counters_list) {
+  // Currently not implemented.
 }
 
 }  // namespace blaze_jni
