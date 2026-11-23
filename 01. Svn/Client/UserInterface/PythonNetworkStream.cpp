// Ara:
			Set(HEADER_GC_BUFFI_USE_SKILL, CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCBuffiUseSkill), STATIC_SIZE_PACKET));
#endif
			Set(HEADER_GC_DRAGON_SOUL_REFINE, CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCDragonSoulRefine), STATIC_SIZE_PACKET));

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
			Set(HEADER_GC_NEW_OFFLINESHOP, CNetworkPacketHeaderMap::TPacketType(sizeof(TPacketGCNewOfflineshop), LARGE_DYNAMIC_SIZE_PACKET));
#endif
