// Ara:
#define ENABLE_HUMAN_RESIST_PVP						// Yarý insanlara karþý bonusu etkinleþtir;
#define ENABLE_RENEWAL_AFFECT						// Yenileme etkisini etkinleþtir (1 yeni alt tip + etki simgesi);
#define ENABLE_OFFLINE_MESSAGE						// Oyuncu baðlý deðilse çevrimdýþý mesaj býrakma seçeneðini etkinleþtir;

// Altina ekle:
#define ENABLE_IKASHOP_RENEWAL						// Ikarus Shop Ultimate: offline shop NPC, shop safebox, offers, auction, search, notifications
	#ifdef ENABLE_IKASHOP_RENEWAL
		#define EXTEND_IKASHOP_PRO					// notifications, restore duration, move shop
		#define EXTEND_IKASHOP_ULTIMATE				// sale history / price average, decorations (skins), locked cells, search premium
		#define ENABLE_IKASHOP_ENTITIES
		#define IKASHOP_ALLOWED_MAPS				{ 1, 21, 41 }
	#endif


// Ara:
#define ENABLE_PET_EXP_BONUS
#define ENABLE_TIME_BONUS_COSTUME
#define ENABLE_WARDROBE_AUTO_STORE

// Altina ekle:
#define ENABLE_IKASHOP_OFFER_REFUND					// Anka: reddedilen / iptal edilen teklifin parasi kasaya degil karaktere doner
#define ENABLE_IKASHOP_SEARCH_RENEWAL
