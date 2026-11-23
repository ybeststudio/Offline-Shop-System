// Ara:
#endif
#include "../../common/VnumHelper.h"
#include "char.h"

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
#include <numeric>
#include <chrono>
#include "ikarus_shop.h"
#include "ikarus_shop_manager.h"
#endif


// void CHARACTER::Initialize() icinde:
// Ara:
	m_chHorse = NULL;
	m_chRider = NULL;
	m_protection_Time.clear();

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
	m_pkIkarusShop = NULL;
	m_pkIkarusShopSafebox	= NULL;
	m_pkIkarusAuction		= NULL;
	m_pkIkarusAuctionGuest= NULL;
	m_pkIkarusShopGuest = NULL;
	m_bIsLookingIkarusShopOfferList = false;
#endif


// void CHARACTER::Destroy() icinde:
// Ara:
	if (m_bMonsterLog)
		CHARACTER_MANAGER::instance().UnregisterForMonsterLog(this);

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
	SetIkarusShop(nullptr);
	SetIkarusShopGuest(nullptr);
	SetIkarusShopSafebox(nullptr);
	SetIkarusAuction(nullptr);
	SetIkarusAuctionGuest(nullptr);
#endif


// bool CHARACTER::CanWarp() const icinde:
// Ara:
	if ((iPulse - GetMyShopTime()) < limit_time)
	{
		return false;
	}

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
	if (iPulse - GetIkarusShopUseTime() < limit_time)
		return false;

	if (GetIkarusShopGuest() || GetIkarusAuctionGuest())
		return false;
#endif


// BYTE CHARACTER::CanRefineAcceMaterials() icinde:
// Ara:
	if (GetExchange() || GetMyShop() || GetShopOwner() || IsOpenSafebox() || IsCubeOpen())
		return bReturn;

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
	if (GetIkarusShopGuest() || GetIkarusAuctionGuest())
		return bReturn;
#endif


// Ara:
    for (DWORD dwNPCVID : vecToRemove)
    {
        RemoveEnemyNPC(dwNPCVID);
    }
}
#endif

// Altina ekle:
#ifdef ENABLE_IKASHOP_RENEWAL
void CHARACTER::SetIkarusShopSafebox(SAFEBOX_HANDLE pk)
{
	if(m_pkIkarusShopSafebox && pk == nullptr)
		m_pkIkarusShopSafebox->SetOwner(nullptr);

	else if(m_pkIkarusShopSafebox == nullptr && pk)
		pk->SetOwner(this);

	m_pkIkarusShopSafebox  = pk;
}

void CHARACTER::SetIkarusShopGuest(SHOP_HANDLE pkShop)
{
	if(m_pkIkarusShopGuest)
		m_pkIkarusShopGuest->RemoveGuest(this);
	m_pkIkarusShopGuest = pkShop;
	if(pkShop)
		pkShop->AddGuest(this);
}

void CHARACTER::SetIkarusAuctionGuest(AUCTION_HANDLE pk)
{
	if(m_pkIkarusAuctionGuest)
		m_pkIkarusAuctionGuest->RemoveGuest(this);
	m_pkIkarusAuctionGuest = pk;
	if(pk)
		pk->AddGuest(this);
}

bool CHARACTER::CanTakeInventoryItem(LPITEM item, TItemPos* pos)
{
	int emptyPos = -1;

	if (item->IsDragonSoul())
	{
		pos->cell = emptyPos = GetEmptyDragonSoulInventory(item);
		pos->window_type = DRAGON_SOUL_INVENTORY;
	}
	else
	{
		pos->cell = emptyPos = GetEmptyInventory(item->GetSize());
		pos->window_type = INVENTORY;
	}

	return emptyPos != -1;
}

bool CHARACTER::IkarusShopFloodCheck(ShopActionWeight weight)
{
	using namespace std::chrono;
	const auto now = duration<double>(high_resolution_clock::now().time_since_epoch()).count();
	const auto elapsedTime = now - 60.0;

	std::erase_if(m_IkarusShopActionRegister, [&](auto& pair){ return pair.second < elapsedTime; });
	const auto totalWeight = std::accumulate(m_IkarusShopActionRegister.begin(), m_IkarusShopActionRegister.end(), 0UL,
		[](auto total, auto& pair){ return total + pair.first; });

	if(totalWeight + weight > OFFLINESHOP_MAX_WEIGHT_PER_PLAYER){
		ikashop::GetManager().SendPopupMessage(this, "IKASHOP_SERVER_POPUP_MESSAGE_PLEASE_SLOW_DOWN");
		return false;
	}

	m_IkarusShopActionRegister.emplace_back(std::make_pair(weight, now));
	return true;
}
#endif
