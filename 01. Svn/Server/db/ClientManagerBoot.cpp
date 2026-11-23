// bool CClientManager::InitializeTables() icinde:
// Ara:
		sys_err("InitializeObjectTable FAILED");
		return false;
	}

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
	if (!InitializeIkarusShopTable())
	{
		sys_err("InitializeIkarusShopTable FAILED");
		return false;
	}
#endif
