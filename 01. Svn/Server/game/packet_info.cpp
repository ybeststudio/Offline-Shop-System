// CPacketInfoCG::CPacketInfoCG() icinde:
// Ara:
	Set(HEADER_CG_DRAGON_SOUL_REFINE,				sizeof(TPacketCGDragonSoulRefine),			"DragonSoulRefine");
	Set(HEADER_CG_STATE_CHECKER,					sizeof(BYTE),								"ServerStateCheck");

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
	Set(HEADER_CG_NEW_OFFLINESHOP,					sizeof(TPacketCGNewIkarusShop),			"NewIkarusShop");
#endif
