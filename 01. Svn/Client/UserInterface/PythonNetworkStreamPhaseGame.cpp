// void CPythonNetworkStream::GamePhase() icinde:
// Ara:
			case HEADER_GC_DRAGON_SOUL_REFINE:
				ret = RecvDragonSoulRefine();
				break;

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
			case HEADER_GC_NEW_OFFLINESHOP:
				ret = RecvOfflineshopPacket();
				break;
#endif


// void CPythonNetworkStream::__LeaveGamePhase() icinde:
// Ara:
	CPythonItem& rkItemMgr=CPythonItem::Instance();
	rkItemMgr.Destroy();

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#ifdef ENABLE_IKASHOP_ENTITIES
	CPythonIkarusShop::instance().DeleteEntities();
#endif
#endif
