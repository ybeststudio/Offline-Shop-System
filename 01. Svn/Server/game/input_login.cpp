// Ara:
#include "desc_client.h"
#include "desc_manager.h"
#include "char.h"

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#include "ikarus_shop.h"
#include "ikarus_shop_manager.h"
#endif


// void CInputLogin::Entergame(LPDESC d, const char * data) icinde:
// Ara:
		if (pid != 0 && CHorseNameManager::instance().GetHorseName(pid) == NULL)
			db_clientdesc->DBPacket(HEADER_GD_REQ_HORSE_NAME, 0, &pid, sizeof(DWORD));

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
	if (ch->IsPC())
	{
		auto pkShop= ikashop::GetManager().GetShopByOwnerID(ch->GetPlayerID());
		if(pkShop)
			ch->SetIkarusShop(pkShop);

		auto auction = ikashop::GetManager().GetAuctionByOwnerID(ch->GetPlayerID());
		if(auction)
			ch->SetIkarusAuction(auction);
	}
#endif
