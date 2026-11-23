// Ara:
#define ENABLE_BONUS_COSTUME_SYSTEM							// KostÃ¼mlerde bonus ekleme ve deÄiÅtirme sistemi etkin;
#define ENABLE_RENEWAL_SPECIAL_CHAT							// Yang, eÅya vb. iÃ§in Ã¶zel yenilenmiÅ sohbet sistemi;
	#define ENABLE_PICKUP_ITEM_SOCKET						// toplama paketi soket 0'Ä± da taÅÄ±r (drop listesi: beceri kitabÄ±nÄ±n adÄ± + tooltipi), server ile aynÄ±

// Altina ekle:
#define ENABLE_IKASHOP_RENEWAL								// Ikarus Shop Ultimate: offline shop, shop safebox, offers, auction, search, notifications
#ifdef ENABLE_IKASHOP_RENEWAL
	#define EXTEND_IKASHOP_PRO								// notifications, restore duration, move shop
	#define EXTEND_IKASHOP_ULTIMATE							// price average, decorations (skins), locked cells, search premium
	#define ENABLE_IKASHOP_HIDE_SHOP_NAMES
	#define ENABLE_IKASHOP_ENTITIES
#endif
