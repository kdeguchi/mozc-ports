--- src/ipc/ipc_path_manager.cc.orig	2025-05-08 06:09:27 UTC
+++ src/ipc/ipc_path_manager.cc
@@ -283,10 +283,12 @@ bool IPCPathManager::GetPathName(std::string *ipc_name
   *ipc_name = kIPCPrefix;
 #endif  // _WIN32
 
+#if !defined(__FreeBSD__)
 #ifdef __linux__
   // On Linux, use abstract namespace which is independent of the file system.
   (*ipc_name)[0] = '\0';
 #endif  // __linux__
+#endif  // !__FreeBSD__
 
   ipc_name->append(ipc_path_info_.key());
   ipc_name->append(".");
