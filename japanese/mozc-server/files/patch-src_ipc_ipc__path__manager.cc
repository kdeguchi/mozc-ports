--- src/ipc/ipc_path_manager.cc.orig	2025-03-10 03:54:24 UTC
+++ src/ipc/ipc_path_manager.cc
@@ -284,8 +284,10 @@ bool IPCPathManager::GetPathName(std::string *ipc_name
 #endif  // _WIN32
 
 #ifdef __linux__
+#if !defined(__FreeBSD__)
   // On Linux, use abstract namespace which is independent of the file system.
   (*ipc_name)[0] = '\0';
+#endif  // !__FreeBSD__
 #endif  // __linux__
 
   ipc_name->append(ipc_path_info_.key());
