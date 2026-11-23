// Ara:
	CHARACTER_NAME_MAX_LEN = 48,
	COUNTRY_FLAG_MAX_LEN = 2,
	PLAYER_NAME_MAX_LEN = 12,

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
	OFFLINE_SHOP_NAME_MAX_LEN = 15 + CHARACTER_NAME_MAX_LEN +1,
#ifdef ENABLE_CHEQUE_SYSTEM
	YANG_PER_CHEQUE = 100'000'000,
#endif
#ifdef EXTEND_IKASHOP_PRO
	OFFLINESHOP_NOTIFICATION_FORMAT_LEN = 40,
#endif
#endif


// Ara:
void initsafebox();
void initguild();
void initMessenger();

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
void initikashop();
#endif
