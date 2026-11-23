// void CPythonPlayer::__OnPressSmart(CInstanceBase& rkInstMain, bool isAuto) icinde:
// Ara:
	{
		__OnPressActor(rkInstMain, dwPickedActorID, isAuto);
	}

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#ifdef ENABLE_IKASHOP_ENTITIES
	else if (CPythonIkarusShop::instance().CheckPickedShopEntity(nullptr))
		return;
#endif
#endif


// void CPythonPlayer::__OnClickSmart(CInstanceBase& rkInstMain, bool isAuto) icinde:
// Ara:
	{
		__OnClickActor(rkInstMain, dwPickedActorID, isAuto);
	}

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#ifdef ENABLE_IKASHOP_ENTITIES
	else if (DWORD dwPickedShopVID = 0; CPythonIkarusShop::instance().CheckPickedShopEntity(&dwPickedShopVID))
		CPythonNetworkStream::instance().SendIkarusShopOnClickShopEntity(dwPickedShopVID);
#endif
#endif
