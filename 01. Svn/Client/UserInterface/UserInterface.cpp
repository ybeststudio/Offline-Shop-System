// bool RunMainScript(CPythonLauncher& pyLauncher, const char *lpCmdLine) icinde:
// Ara:
	initquest();
	initBackground();
	initMessenger();

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
	initikashop();
#endif
