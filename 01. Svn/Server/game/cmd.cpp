// Ara:
#ifdef ENABLE_WHISPER_OFFLINE_MESSAGE
ACMD(do_anka_offline_msg);
#endif

// Altina ekle:
#ifdef ENABLE_IKASHOP_SEARCH_RENEWAL
ACMD(do_anka_open_shop);
#endif


// Ara:
#ifdef ENABLE_RANKING
ACMD(do_ranking_subcategory);
#endif

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
ACMD(do_offshop_force_close_shop);
#endif


// Ara:
#ifdef ENABLE_WHISPER_OFFLINE_MESSAGE
	{ "anka_offline_msg", do_anka_offline_msg, 0, POS_DEAD, GM_PLAYER },
#endif

// Altina ekle:
#ifdef ENABLE_IKASHOP_SEARCH_RENEWAL
	{ "anka_open_shop", do_anka_open_shop, 0, POS_DEAD, GM_PLAYER },
#endif


// Ara:
#ifdef ENABLE_RANKING
	{"ranking_subcategory", do_ranking_subcategory, 0, POS_DEAD, GM_PLAYER },
#endif

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
	{ "offshop_force_close_shop", do_offshop_force_close_shop, 0,  POS_DEAD, GM_IMPLEMENTOR },
#endif
