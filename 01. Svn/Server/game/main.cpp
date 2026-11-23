// Ara:
#include "desc_manager.h"
#include "item_manager.h"
#include "char.h"

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#include "ikarus_shop.h"
#include "ikarus_shop_manager.h"
#endif


// int main(int argc, char **argv) icinde:
// Ara:
#ifdef ENABLE_ULTIMATE_REGEN
	 mobTimer.Initialize();
#endif

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
	ikashop::CShopManager offshopManager;
#endif
