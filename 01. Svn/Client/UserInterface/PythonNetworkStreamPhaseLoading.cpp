// void CPythonNetworkStream::LoadingPhase() icinde:
// Ara:
			if (RecvQuickSlotAddPacket())
			{
				return;
			}
			break;

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
		case HEADER_GC_NEW_OFFLINESHOP:
			if (RecvOfflineshopPacket())
				return;
			break;
#endif
